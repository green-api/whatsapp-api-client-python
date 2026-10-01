"""Local media and ICE checks without an account or audio hardware."""

import asyncio
from fractions import Fraction

import pytest
from aiortc import AudioStreamTrack
from aiortc.mediastreams import MediaStreamError
from av import AudioFrame

from whatsapp_api_client_python.tools.voip import FrameAudioSink
from whatsapp_api_client_python.tools.voip.rtc import (
    AiortcBridge,
    candidate_from_json,
    candidate_to_json,
)


class OneFrameTrack(AudioStreamTrack):
    def __init__(self):
        super().__init__()
        self.sent = False

    async def recv(self):
        if self.sent:
            raise MediaStreamError
        self.sent = True
        frame = AudioFrame(format="s16", layout="mono", samples=960)
        frame.planes[0].update(bytes(1920))
        frame.sample_rate = 48_000
        frame.time_base = Fraction(1, 48_000)
        frame.pts = 0
        return frame


@pytest.mark.asyncio
async def test_frame_sink_delivers_async_callback_and_closes():
    frames = []

    async def on_frame(frame):
        frames.append(frame)

    sink = FrameAudioSink(on_frame)
    await sink.attachAsync(OneFrameTrack())
    for _ in range(30):
        if frames:
            break
        await asyncio.sleep(0)
    assert len(frames) == 1 and isinstance(frames[0], AudioFrame)
    await sink.closeAsync()


def test_candidate_wire_round_trip():
    value = {
        "candidate": "candidate:1 1 udp 2122260223 192.0.2.1 54000 typ host",
        "sdpMid": "0", "sdpMLineIndex": 0,
    }
    assert candidate_to_json(candidate_from_json(value)) == value


@pytest.mark.asyncio
async def test_two_real_peers_exchange_offer_answer_and_audio():
    caller, callee = AiortcBridge([]), AiortcBridge([])
    caller.add_track(AudioStreamTrack())
    callee.add_track(AudioStreamTrack())
    try:
        offer = await caller.create_offer()
        try:
            await caller.set_local_description(offer)
        except PermissionError:
            pytest.skip("Network interfaces are unavailable in this sandbox")
        assert caller.local_description["type"] == "offer"
        assert caller.local_candidates()
        await callee.set_remote_description(caller.local_description)
        answer = await callee._peer.createAnswer()
        await callee._peer.setLocalDescription(answer)
        await caller.set_remote_description(callee.local_description)

        async def connected():
            while caller._peer.connectionState != "connected" or callee._peer.connectionState != "connected":
                await asyncio.sleep(0.05)

        await asyncio.wait_for(connected(), timeout=10)
    finally:
        await caller.close()
        await callee.close()
