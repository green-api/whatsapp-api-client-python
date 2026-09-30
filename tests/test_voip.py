"""Call scenarios adapted from the standalone WA VoIP client."""

from whatsapp_api_client_python.API import GreenAPI, GreenAPIError
from whatsapp_api_client_python.response import Response
from whatsapp_api_client_python.tools.voip import CallAudio, CallsConnection
from whatsapp_api_client_python.tools.voip.signaling import ReconnectingSocket
import asyncio
import httpx
import json
import pytest


async def until(predicate, turns=60):
    for _ in range(turns):
        if predicate():
            return
        await asyncio.sleep(0)
    raise AssertionError("Expected async progress")


class FakeSocket:
    def __init__(self):
        self.listeners = {}
        self.sent = []
        self.closed = False

    def on(self, name, callback):
        self.listeners.setdefault(name, []).append(callback)

    async def open(self, **kwargs):
        pass

    async def send(self, value):
        self.sent.append(value)

    async def close(self):
        self.closed = True

    async def emit(self, name, detail=None):
        for callback in self.listeners.get(name, ()):
            value = callback(detail)
            if asyncio.iscoroutine(value):
                await value


class FakeTrack:
    kind = "audio"


class FakeAudioFactory:
    def __init__(self):
        self.sessions = []

    async def __call__(self):
        track = FakeTrack()
        remote = []
        closed = []

        async def attach(value):
            remote.append(value)

        async def close():
            closed.append(True)

        session = CallAudio(track, attach, close)
        session.remote = remote
        session.closed = closed
        self.sessions.append(session)
        return session


class FakeBridge:
    def __init__(self, ice_servers):
        self.ice_servers = ice_servers
        self.calls = []
        self.closed = False
        self.track_callback = None
        self.local_description = {"type": "offer", "sdp": "v=0"}

    def add_track(self, track):
        self.calls.append(("track", track))

    def on_track(self, callback):
        self.track_callback = callback

    async def create_offer(self):
        return self.local_description

    async def set_local_description(self, offer):
        self.calls.append(("local", offer))

    def local_candidates(self):
        return []

    async def set_remote_description(self, answer):
        self.calls.append(("remote", answer))

    async def add_ice_candidate(self, candidate):
        self.calls.append(("candidate", candidate))

    async def close(self):
        self.closed = True


class FakeVoip:
    def __init__(self):
        self.calls = []

    async def get_ice_servers(self):
        self.calls.append("ice")
        return [{"urls": "stun:example.test"}]


@pytest.fixture
def harness():
    socket, voip, audio = FakeSocket(), FakeVoip(), FakeAudioFactory()
    bridges = []

    def make_bridge(servers):
        bridge = FakeBridge(servers)
        bridges.append(bridge)
        return bridge

    calls = CallsConnection(voip, socket=socket, bridge_factory=make_bridge, audio_factory=audio)
    return calls, socket, voip, audio, bridges


async def start(calls, socket):
    sent = len(socket.sent)
    task = asyncio.create_task(calls.start_audio())
    await until(lambda: len(socket.sent) > sent)
    return task


@pytest.mark.asyncio
async def test_rest_dial_and_accept_precede_offer(harness, monkeypatch):
    calls, socket, _, _, _ = harness
    api = GreenAPI("123", "secret")
    timeline = []

    class Transport:
        async def request(self, method, url, **kwargs):
            endpoint = url.split("/")[-2]

            timeline.append(("REST", endpoint))

            if endpoint == "callsGetIceServers":
                return httpx.Response(200, json=[])

            return httpx.Response(204)

    async def unexpected_request(*args, **kwargs):
        raise AssertionError("VoIP must not use the common requestAsync policy")

    monkeypatch.setattr(api, "requestAsync", unexpected_request)

    api.voip._transport = Transport()
    calls._voip = api.voip
    original_send = socket.send

    async def send(frame):
        timeline.append(("WS", frame["type"]))
        await original_send(frame)

    socket.send = send
    await api.voip.dial("79991234567")
    task = await start(calls, socket)
    assert timeline[:3] == [("REST", "callsDial"), ("REST", "callsGetIceServers"), ("WS", "offer")]
    await socket.emit("message", {"type": "answer", "answer": {"type": "answer", "sdp": "v=0"}})
    await task
    await calls.stop_audio()
    socket.sent.clear()
    timeline.clear()
    await api.voip.accept()
    task = await start(calls, socket)
    assert timeline[:3] == [("REST", "callsAccept"), ("REST", "callsGetIceServers"), ("WS", "offer")]
    await socket.emit("message", {"type": "answer", "answer": {"type": "answer", "sdp": "v=0"}})
    await task
    await calls.close()


@pytest.mark.asyncio
async def test_early_candidate_is_applied_after_answer(harness):
    calls, socket, _, _, bridges = harness
    task = await start(calls, socket)
    candidate = {"candidate": "candidate:test", "sdpMid": "0"}
    await socket.emit("message", {"type": "ice-candidate", "candidate": candidate})
    assert ("candidate", candidate) not in bridges[0].calls
    await socket.emit("message", {"type": "answer", "answer": {"type": "answer", "sdp": "v=0"}})
    await task
    assert bridges[0].calls[-2:] == [("remote", {"type": "answer", "sdp": "v=0"}), ("candidate", candidate)]
    await calls.close()


@pytest.mark.asyncio
async def test_stop_and_close_do_not_hang_up(harness):
    calls, socket, _, audio, bridges = harness
    await socket.emit("message", {"type": "state", "state": {"state": "on-call"}})
    task = await start(calls, socket)
    await socket.emit("message", {"type": "answer", "answer": {"type": "answer", "sdp": "v=0"}})
    await task
    await calls.stop_audio()
    assert calls.state.state == "on-call"
    assert socket.sent[-1] == {"type": "stop"}
    assert bridges[0].closed and audio.sessions[0].closed == [True]
    await calls.close()
    assert socket.closed
    assert socket.sent.count({"type": "stop"}) == 1


@pytest.mark.asyncio
async def test_reconnect_creates_fresh_audio_and_ignores_old_track(harness):
    calls, socket, _, audio, bridges = harness
    await socket.emit("message", {"type": "state", "state": {"state": "on-call"}})
    task = await start(calls, socket)
    await socket.emit("message", {"type": "answer", "answer": {"type": "answer", "sdp": "v=0"}})
    await task
    await socket.emit("disconnect", {"reason": "lost", "code": 1006, "permanent": False})
    assert audio.sessions[0].closed == [True]
    await socket.emit("message", {"type": "state", "state": {"state": "on-call"}})
    await until(lambda: len(bridges) == 2 and len(socket.sent) == 2)
    assert audio.sessions[1].local_track is not audio.sessions[0].local_track
    bridges[0].track_callback(FakeTrack())
    await asyncio.sleep(0)
    assert audio.sessions[1].remote == []
    await socket.emit("message", {"type": "answer", "answer": {"type": "answer", "sdp": "v=0"}})
    await calls.close()


@pytest.mark.asyncio
async def test_pending_error_closes_bridge_but_error_after_answer_keeps_it(harness):
    calls, socket, _, audio, bridges = harness
    errors = []

    calls.on("error", errors.append)

    task = await start(calls, socket)
    await socket.emit("message", {"type": "error", "message": "no active call"})
    with pytest.raises(RuntimeError, match="no active call"):
        await task
    assert bridges[0].closed and audio.sessions[0].closed == [True]
    await socket.emit("message", {"type": "state", "state": {"state": "on-call"}})
    task = await start(calls, socket)
    await socket.emit("message", {"type": "answer", "answer": {"type": "answer", "sdp": "v=0"}})
    await task
    await socket.emit("message", {"type": "error", "message": "calls unavailable"})
    assert errors == [{"message": "calls unavailable"}]
    assert calls.has_audio_bridge
    assert not bridges[1].closed and audio.sessions[1].closed == []
    await socket.emit("message", {"type": "state", "state": {"state": "idle"}})
    assert bridges[1].closed and audio.sessions[1].closed == [True]
    await calls.close()


@pytest.mark.asyncio
async def test_idle_reports_end_even_when_stop_send_fails(harness):
    calls, socket, _, audio, bridges = harness
    ended = []
    calls.on("end_call", ended.append)
    await socket.emit("message", {"type": "state", "state": {"state": "on-call"}})
    task = await start(calls, socket)
    await socket.emit("message", {"type": "answer", "answer": {"type": "answer", "sdp": "v=0"}})
    await task

    async def failed_send(frame):
        if frame["type"] == "stop":
            raise ConnectionError("socket closed")

    socket.send = failed_send
    await socket.emit("message", {"type": "state", "state": {"state": "idle", "reason": "hangup"}})
    assert ended == [{"reason": "call-ended", "cause": "hangup"}]
    assert bridges[0].closed and audio.sessions[0].closed == [True]
    await calls.close()


@pytest.mark.asyncio
async def test_permanent_refusal_does_not_resume(harness):
    calls, socket, _, _, bridges = harness
    errors, ended = [], []
    calls.on("error", errors.append)
    calls.on("end_call", ended.append)
    await socket.emit("message", {"type": "state", "state": {"state": "out-call"}})
    task = await start(calls, socket)
    await socket.emit("message", {"type": "answer", "answer": {"type": "answer", "sdp": "v=0"}})
    await task
    await socket.emit("message", {"type": "error", "message": "calls disabled"})
    await socket.emit("disconnect", {"reason": "calls disabled", "code": 4001, "permanent": True})
    await socket.emit("message", {"type": "state", "state": {"state": "out-call"}})
    assert errors == [{"message": "calls disabled"}]
    assert ended == [{"reason": "connection-lost"}]
    assert len(bridges) == 1
    await calls.close()


@pytest.mark.asyncio
async def test_pending_negotiation_fails_on_disconnect(harness):
    calls, socket, _, audio, bridges = harness
    await socket.emit("message", {"type": "state", "state": {"state": "out-call"}})
    task = await start(calls, socket)
    await socket.emit("disconnect", {"reason": "lost", "code": 1006, "permanent": False})
    with pytest.raises(RuntimeError, match="Socket disconnected"):
        await task
    assert bridges[0].closed and audio.sessions[0].closed == [True]
    await calls.close()


@pytest.mark.asyncio
async def test_bad_candidate_after_answer_closes_bridge(harness):
    calls, socket, _, audio, bridges = harness
    errors = []
    calls.on("error", errors.append)
    task = await start(calls, socket)
    await socket.emit("message", {"type": "answer", "answer": {"type": "answer", "sdp": "v=0"}})
    await task

    async def bad_candidate(value):
        raise ValueError("invalid candidate")

    bridges[0].add_ice_candidate = bad_candidate
    await socket.emit("message", {"type": "ice-candidate", "candidate": {"candidate": "broken"}})
    assert errors == [{"message": "invalid candidate"}]
    assert bridges[0].closed and audio.sessions[0].closed == [True]
    await calls.close()


@pytest.mark.asyncio
async def test_close_cancels_pending_remote_attachment(harness):
    calls, socket, _, audio, bridges = harness
    entered = asyncio.Event()
    cancelled = asyncio.Event()

    async def attach(track):
        entered.set()
        try:
            await asyncio.Event().wait()
        except asyncio.CancelledError:
            cancelled.set()
            raise

    task = await start(calls, socket)
    audio.sessions[0].on_remote_track = attach
    bridges[0].track_callback(FakeTrack())
    await entered.wait()
    await calls.close()
    with pytest.raises(RuntimeError, match="closed"):
        await task
    assert cancelled.is_set()
    assert audio.sessions[0].closed == [True]


@pytest.mark.asyncio
async def test_close_while_audio_factory_pending(harness):
    calls, socket, _, _, _ = harness
    waiting = asyncio.Event()
    release = asyncio.Event()
    audio = FakeAudioFactory()

    async def delayed():
        waiting.set()
        await release.wait()
        return await audio()

    calls._audio_factory = delayed
    task = asyncio.create_task(calls.start_audio())
    await waiting.wait()
    await calls.close()
    release.set()
    with pytest.raises(RuntimeError, match="closed"):
        await task
    assert audio.sessions[0].closed == [True]


@pytest.mark.asyncio
async def test_websocket_url_and_rest_error():
    api = GreenAPI("123", "secret", host="https://example.test/base/")
    assert api.voip.websocket_url() == "wss://example.test/base/waInstance123/callsRtc/secret"

    api.voip._transport = StaticTransport(403, "denied")

    with pytest.raises(RuntimeError, match="callsDial failed"):
        await api.voip.dial("79991234567")


class StaticTransport:
    def __init__(self, status, body=""):
        self.status = status
        self.body = body
        self.requests = []

    async def request(self, method, url, **kwargs):
        self.requests.append((method, url, kwargs))
        return httpx.Response(self.status, text=self.body)


@pytest.mark.parametrize("raise_errors", [False, True])
@pytest.mark.asyncio
async def test_voip_rest_accepts_200_and_204_independently_of_sdk_policy(raise_errors):
    api = GreenAPI("123", "secret", raise_errors=raise_errors, host="https://example.test")
    transport = StaticTransport(200, '{"state":"idle"}')
    api.voip._transport = transport

    assert (await api.voip.get_state()).state == "idle"

    assert transport.requests[0] == (
        "GET", "https://example.test/waInstance123/callsState/secret", {},
    )

    transport.status, transport.body = 204, ""

    await api.voip.dial("79991234567")

    assert transport.requests[-1] == (
        "POST", "https://example.test/waInstance123/callsDial/secret",
        {"headers": {"Content-Type": "application/json"}, "json": {"chatId": "79991234567@c.us"}},
    )

    for command in (api.voip.accept, api.voip.reject, api.voip.hang_up):
        await command()
        assert transport.requests[-1][0] == "POST"
        assert transport.requests[-1][2] == {}


@pytest.mark.parametrize("raise_errors", [False, True])
@pytest.mark.asyncio
async def test_voip_rest_rejects_http_error_and_invalid_json(raise_errors):
    api = GreenAPI("123", "secret", raise_errors=raise_errors)
    transport = StaticTransport(403, "denied")
    api.voip._transport = transport

    with pytest.raises(RuntimeError, match="callsAccept failed: 403 denied"):
        await api.voip.accept()

    transport.status, transport.body = 200, "not json"

    with pytest.raises(json.JSONDecodeError):
        await api.voip.get_ice_servers()


def test_common_response_keeps_original_200_only_contract():
    assert Response(200, "{}").data == {}

    for code in (201, 204):
        response = Response(code, "{}")
        assert response.data is None
        assert response.error == "{}"


def test_common_http_handler_still_rejects_204(caplog):
    api = GreenAPI("123", "secret", raise_errors=True)

    with pytest.raises(GreenAPIError, match="status code: 204"):
        api._GreenApi__handle_response_async(204, "")

    api.raise_errors = False

    with caplog.at_level("ERROR"):
        api._GreenApi__handle_response_async(204, "")

    assert "status code: 204" in caplog.text


@pytest.mark.asyncio
async def test_voip_uses_httpx_transport_for_204_without_post_body(monkeypatch):
    api = GreenAPI("123", "secret", raise_errors=True, host="https://example.test")
    requests = []

    def handle(request):
        requests.append(request)
        return httpx.Response(204)

    real_client = httpx.AsyncClient

    monkeypatch.setattr(
        httpx, "AsyncClient",
        lambda: real_client(transport=httpx.MockTransport(handle)),
    )

    await api.voip.accept()
    await api.voip.dial("79991234567")

    assert requests[0].url.path == "/waInstance123/callsAccept/secret"
    assert requests[0].content == b""

    assert "content-type" not in requests[0].headers

    assert requests[1].url.path == "/waInstance123/callsDial/secret"
    assert requests[1].headers["content-type"] == "application/json"
    assert json.loads(requests[1].content) == {"chatId": "79991234567@c.us"}


@pytest.mark.asyncio
async def test_no_automatic_answer_timeout(harness):
    calls, socket, _, audio, bridges = harness
    task = await start(calls, socket)

    with pytest.raises(asyncio.TimeoutError):
        await asyncio.wait_for(asyncio.shield(task), timeout=0.02)

    assert not task.done() and calls.has_audio_bridge
    await calls.close()

    with pytest.raises(RuntimeError, match="closed"):
        await task

    assert bridges[0].closed and audio.sessions[0].closed == [True]


class RawSocket:
    def __init__(self):
        self.incoming = asyncio.Queue()
        self.sent = []
        self.closed = False

    async def recv(self):
        value = await self.incoming.get()
        if isinstance(value, Exception):
            raise value
        return value

    async def send(self, text):
        self.sent.append(text)

    async def close(self):
        self.closed = True


class Closed(Exception):
    def __init__(self, code):
        self.code = code
        self.reason = "closed"


@pytest.mark.asyncio
async def test_socket_reconnect_policy_and_permanent_refusal():
    sockets, delays = [], []

    async def factory(url):
        raw = RawSocket()
        sockets.append(raw)
        return raw

    async def sleep(seconds):
        delays.append(seconds)
        await asyncio.sleep(0)

    socket = ReconnectingSocket("wss://example.test", socket_factory=factory, sleep=sleep)
    await socket.open()
    sockets[0].incoming.put_nowait(Closed(1006))
    await until(lambda: len(sockets) == 2)
    assert delays == [0.5]
    sockets[1].incoming.put_nowait(Closed(4001))
    await until(lambda: socket.refused)
    assert delays == [0.5]
    await socket.close()


@pytest.mark.asyncio
async def test_ordered_frames_wait_for_slow_stop(harness):
    calls, _, _, _, _ = harness
    raw = RawSocket()
    socket = ReconnectingSocket("wss://example.test", socket_factory=lambda url: asyncio.sleep(0, result=raw))
    calls._socket = socket
    socket.on("message", calls._on_message)
    socket.on("disconnect", calls._on_socket_disconnect)
    events = []
    calls.on("state", lambda state: events.append(("state", state.state)))
    calls.on("end_call", lambda detail: events.append(("end", detail["reason"])))
    calls.on("incoming_call", lambda info: events.append(("incoming", info.wid)))
    await socket.open()
    raw.incoming.put_nowait(json.dumps({"type": "state", "state": {"state": "on-call"}}))
    await until(lambda: calls.state is not None)
    task = asyncio.create_task(calls.start_audio())
    await until(lambda: bool(raw.sent))
    raw.incoming.put_nowait(json.dumps({"type": "answer", "answer": {"type": "answer", "sdp": "v=0"}}))
    await task
    entered, release = asyncio.Event(), asyncio.Event()
    original = raw.send

    async def slow_send(text):
        if json.loads(text).get("type") == "stop":
            entered.set()
            await release.wait()
        await original(text)

    raw.send = slow_send
    raw.incoming.put_nowait(json.dumps({"type": "state", "state": {"state": "idle"}}))
    raw.incoming.put_nowait(json.dumps({"type": "state", "state": {"state": "inc-call", "info": {"id": "next", "wid": "200@lid", "name": "Next"}}}))
    await entered.wait()
    assert events == [("state", "on-call"), ("state", "idle")]
    release.set()
    await until(lambda: len(events) == 5)
    assert events[-3:] == [("end", "call-ended"), ("state", "inc-call"), ("incoming", "200@lid")]
    await calls.close()
