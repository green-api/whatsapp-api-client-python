"""REST commands, call state and media bridge lifecycle."""

from dataclasses import dataclass
from typing import Literal, Mapping
from urllib.parse import urlsplit, urlunsplit
from .audio import AudioFactory, CallAudio
from .signaling import ReconnectingSocket
import asyncio
import inspect
import json
import logging

# Types

CallStateKind = Literal["idle", "inc-call", "out-call", "on-call"]


# Constants

CALL_STATE_KINDS = frozenset(("inc-call", "out-call", "on-call"))

_MISSING = object()


@dataclass(frozen=True)
class CallInfo:
    id: str
    wid: str
    name: str


@dataclass(frozen=True)
class CallState:
    state: CallStateKind
    info: CallInfo | None = None
    reason: str | None = None


def call_state_from_json(value: Mapping) -> CallState:
    info = value.get("info")

    if isinstance(info, dict):
        info = CallInfo(id=info["id"], wid=info["wid"], name=info["name"])

    else:
        info = None

    return CallState(state=value["state"], info=info, reason=value.get("reason"))


class Voip:
    def __init__(self, api, *, transport=None):
        self._api = api
        self._transport = transport

    def _url(self, method: str) -> str:
        return (
            f"{self._api.host.rstrip('/')}/waInstance{self._api.idInstance}"
            f"/{method}/{self._api.apiTokenInstance}"
        )

    def websocket_url(self) -> str:
        host = urlsplit(self._api.host.rstrip("/"))

        if host.scheme not in ("http", "https"):
            raise ValueError("VoIP host must use http or https")

        scheme = "wss" if host.scheme == "https" else "ws"
        path = host.path.rstrip("/") + f"/waInstance{self._api.idInstance}/callsRtc/{self._api.apiTokenInstance}"

        return urlunsplit((scheme, host.netloc, path, "", ""))

    async def _request(self, method: str, endpoint: str, payload=_MISSING):
        kwargs = {}

        if payload is not _MISSING:
            kwargs = {"headers": {"Content-Type": "application/json"}, "json": payload}

        if self._transport is None:
            import httpx

            async with httpx.AsyncClient() as transport:
                response = await transport.request(method, self._url(endpoint), **kwargs)
        else:
            response = await self._transport.request(method, self._url(endpoint), **kwargs)

        if not 200 <= response.status_code < 300:
            raise RuntimeError(f"{endpoint} failed: {response.status_code} {response.text}")

        if response.status_code == 204 or not response.text:
            return None

        return json.loads(response.text)

    async def get_state(self) -> CallState:
        return call_state_from_json(await self._request("GET", "callsState"))

    async def get_ice_servers(self):
        return await self._request("GET", "callsGetIceServers")

    async def dial(self, target: str) -> None:
        chat_id = target if "@" in target else f"{target}@c.us"
        await self._request("POST", "callsDial", {"chatId": chat_id})

    async def accept(self) -> None:
        await self._request("POST", "callsAccept")

    async def reject(self) -> None:
        await self._request("POST", "callsReject")

    async def hang_up(self) -> None:
        await self._request("POST", "callsHangUp")

    def connect(self, *, audio_factory: AudioFactory, **callbacks) -> "CallsConnection":
        connection = CallsConnection(self, audio_factory=audio_factory)

        for name, callback in callbacks.items():
            if not name.startswith("on_"):
                raise TypeError(f"Unknown callback: {name}")

            connection.on(name[3:], callback)

        return connection


class CallsConnection:
    """One callsRtc connection and its current media bridge."""

    def __init__(
        self,
        voip: Voip,
        *,
        audio_factory: AudioFactory,
        socket=None,
        bridge_factory=None,
    ):
        self._voip = voip
        self._socket = socket if socket is not None else ReconnectingSocket(voip.websocket_url())
        self._bridge_factory = bridge_factory
        self._audio_factory = audio_factory
        self._state: CallState | None = None
        self._peer_connection = None
        self._audio: CallAudio | None = None
        self._pending_remote_candidates: list[dict] = []
        self._remote_description_set = False
        self._pending_bridge: asyncio.Future | None = None
        self._resume_pending = False
        self._refusal_reported = False
        self._closed = False
        self._resume_task: asyncio.Task | None = None
        self._bridge_generation = 0
        self._callbacks: dict[str, list] = {}
        self._callback_tasks: set[asyncio.Task] = set()
        self._remote_tasks: set[asyncio.Task] = set()
        self._socket.on("connect", lambda _: self._emit("connect"))
        self._socket.on("disconnect", self._on_socket_disconnect)
        self._socket.on("message", self._on_message)

    def on(self, name: str, callback) -> None:
        """Register a callback. Async callbacks run separately from frame dispatch."""
        self._callbacks.setdefault(name, []).append(callback)

    def off(self, name: str, callback) -> None:
        if callback in self._callbacks.get(name, ()):
            self._callbacks[name].remove(callback)

    def _emit(self, name: str, detail=None) -> None:
        for callback in tuple(self._callbacks.get(name, ())):
            try:
                result = callback(detail)

                if inspect.isawaitable(result):
                    task = asyncio.create_task(result)
                    self._callback_tasks.add(task)
                    task.add_done_callback(self._callback_tasks.discard)
                    task.add_done_callback(self._log_callback_error)
            except Exception:
                logging.getLogger(__name__).exception("VoIP %s callback failed", name)

    @staticmethod
    def _log_callback_error(task: asyncio.Task) -> None:
        if not task.cancelled():
            exc = task.exception()

            if exc is not None:
                logging.getLogger(__name__).error(
                    "VoIP callback failed", exc_info=(type(exc), exc, exc.__traceback__)
                )

    @property
    def state(self) -> CallState | None:
        return self._state

    @property
    def has_audio_bridge(self) -> bool:
        return self._peer_connection is not None

    async def open(self, *, timeout: float | None = None) -> None:
        if self._closed:
            raise RuntimeError("CallsConnection is closed")

        await self._socket.open(timeout=timeout)

    async def start_audio(self) -> None:
        if self._peer_connection is not None or self._pending_bridge is not None:
            raise RuntimeError("Audio bridge already starting or active")

        if self._closed:
            raise RuntimeError("CallsConnection is closed")

        self._pending_bridge = asyncio.get_running_loop().create_future()
        pending = self._pending_bridge

        try:
            await self._start_audio_internal(self._bridge_generation)
        except BaseException as exc:
            if self._pending_bridge is pending:
                self._pending_bridge = None

            await self._teardown_bridge(False)

            if not pending.done():
                pending.set_exception(exc)

            elif pending.exception() is None:
                raise
        try:
            await pending
        except BaseException:
            if self._pending_bridge is pending:
                self._pending_bridge = None
                await self._teardown_bridge(False)

            raise

    async def stop_audio(self) -> None:
        self._resume_pending = False
        self._reject_pending(RuntimeError("Audio bridge stopped"))
        await self._teardown_bridge(True)

    async def close(self) -> None:
        if self._closed:
            return

        self._closed = True
        self._resume_pending = False

        self._reject_pending(RuntimeError("CallsConnection closed"))
        await self._teardown_bridge(False)
        if self._resume_task is not None:
            self._resume_task.cancel()

        await self._socket.close()

    async def _start_audio_internal(self, generation: int) -> None:
        audio = await self._audio_factory()

        if generation != self._bridge_generation:
            await audio.close()
            return

        self._audio = audio
        ice_servers = await self._voip.get_ice_servers()

        if generation != self._bridge_generation:
            return

        if self._bridge_factory is None:
            from .rtc import AiortcBridge
            peer = AiortcBridge(ice_servers)
        else:
            peer = self._bridge_factory(ice_servers)

        self._peer_connection = peer
        self._remote_description_set = False
        self._pending_remote_candidates = []

        peer.add_track(audio.local_track)
        peer.on_track(lambda track: self._on_remote_track(track, generation, peer))

        offer = await peer.create_offer()

        if generation != self._bridge_generation:
            return

        await peer.set_local_description(offer)

        if generation != self._bridge_generation:
            return

        offer = peer.local_description or offer

        await self._socket.send({"type": "offer", "offer": offer})

        for candidate in peer.local_candidates():
            if generation != self._bridge_generation:
                return

            await self._socket.send({"type": "ice-candidate", "candidate": candidate})

    def _on_remote_track(self, track, generation: int, peer) -> None:
        if generation != self._bridge_generation or peer is not self._peer_connection:
            return

        audio = self._audio

        self._emit("remote_track", track)

        if audio is not None:
            async def attach():
                if generation == self._bridge_generation and peer is self._peer_connection:
                    await audio.on_remote_track(track)

            task = asyncio.create_task(attach())

            self._remote_tasks.add(task)
            task.add_done_callback(self._remote_tasks.discard)
            task.add_done_callback(self._log_callback_error)

    async def _teardown_bridge(self, notify_server: bool) -> None:
        self._bridge_generation += 1
        peer, audio = self._peer_connection, self._audio
        self._peer_connection = None
        self._audio = None
        self._pending_remote_candidates = []
        self._remote_description_set = False
        remote_tasks = tuple(self._remote_tasks)

        for task in remote_tasks:
            task.cancel()

        if remote_tasks:
            await asyncio.gather(*remote_tasks, return_exceptions=True)

        try:
            if notify_server and peer is not None:
                await self._socket.send({"type": "stop"})
        finally:
            try:
                if peer is not None:
                    await peer.close()
            finally:
                if audio is not None:
                    await audio.close()

    def _reject_pending(self, exc: Exception) -> None:
        pending = self._pending_bridge
        self._pending_bridge = None

        if pending is not None and not pending.done():
            pending.set_exception(exc)

    async def _on_message(self, message: dict) -> None:
        kind = message.get("type") if isinstance(message, dict) else None

        if kind == "state":
            await self._on_state(call_state_from_json(message["state"]))
        elif kind == "answer":
            peer = self._peer_connection

            if peer is None:
                return

            try:
                await peer.set_remote_description(message["answer"])
                self._remote_description_set = True

                for candidate in self._pending_remote_candidates:
                    await peer.add_ice_candidate(candidate)

                self._pending_remote_candidates = []
            except Exception as exc:
                self._reject_pending(exc)
                await self._teardown_bridge(False)
                return

            pending = self._pending_bridge
            self._pending_bridge = None

            if pending is not None and not pending.done():
                pending.set_result(None)
        elif kind == "ice-candidate":
            if self._remote_description_set:
                if self._peer_connection is not None:
                    try:
                        await self._peer_connection.add_ice_candidate(message["candidate"])
                    except Exception as exc:
                        self._reject_pending(exc)
                        await self._teardown_bridge(False)
                        self._emit("error", {"message": str(exc)})
            else:
                self._pending_remote_candidates.append(message["candidate"])
        elif kind == "error":
            if self._pending_bridge is not None:
                self._reject_pending(RuntimeError(message["message"]))
                await self._teardown_bridge(False)
            else:
                self._refusal_reported = True
                self._emit("error", {"message": message["message"]})

    async def _on_state(self, state: CallState) -> None:
        previous = self._state.state if self._state else None
        self._state = state

        self._emit("state", state)

        if state.state == "inc-call" and previous != "inc-call" and state.info is not None:
            self._emit("incoming_call", state.info)
            return

        if previous in CALL_STATE_KINDS and state.state not in CALL_STATE_KINDS:
            self._resume_pending = False
            self._reject_pending(RuntimeError("Call ended during negotiation"))

            try:
                await self._teardown_bridge(True)
            except Exception:
                logging.getLogger(__name__).exception("Could not send callsRtc stop")

            detail = {"reason": "call-ended"}

            if state.reason:
                detail["cause"] = state.reason

            self._emit("end_call", detail)

            return

        if self._resume_pending and state.state in CALL_STATE_KINDS and not self._peer_connection and not self._pending_bridge:
            self._resume_pending = False
            self._resume_task = asyncio.create_task(self._resume_audio())

    async def _resume_audio(self) -> None:
        try:
            await self.start_audio()
        except Exception as exc:
            self._emit("error", {"message": str(exc)})

    async def _on_socket_disconnect(self, detail: dict) -> None:
        previous = self._state.state if self._state else None
        permanent = detail.get("permanent", False)

        if previous in CALL_STATE_KINDS:
            self._resume_pending = self._peer_connection is not None

            self._reject_pending(RuntimeError("Socket disconnected during negotiation"))
            await self._teardown_bridge(False)

            if permanent:
                self._resume_pending = False

            if not self._resume_pending:
                self._state = None
                self._emit("end_call", {"reason": "connection-lost"})
        else:
            self._state = None

        if permanent and not self._refusal_reported:
            self._emit("error", {"message": detail["reason"]})

        self._refusal_reported = False

        self._emit("disconnect", detail)
