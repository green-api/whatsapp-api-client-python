"""Outgoing voice call using a WAV file and decoded audio frames, no audio devices."""

from aiortc.contrib.media import MediaPlayer
from whatsapp_api_client_python.API import GreenAPI
from whatsapp_api_client_python.tools.voip import CallAudio, FrameAudioSink
import asyncio
import os
import sys


async def make_audio() -> CallAudio:
    player = MediaPlayer(sys.argv[2])

    if player.audio is None:
        raise ValueError("The file has no audio stream")

    async def on_frame(frame):
        # Replace this with your application's frame consumer.
        print(f"received {frame.samples} samples")

    sink = FrameAudioSink(on_frame)

    async def close():
        await sink.close()
        player.audio.stop()

    return CallAudio(player.audio, sink.attach, close)


async def main():
    api = GreenAPI(os.environ["GREEN_API_ID"], os.environ["GREEN_API_TOKEN"])
    calls = api.voip.connect(audio_factory=make_audio)
    ended = asyncio.Event()
    calls.on("incoming_call", lambda info: print("Incoming call:", info.wid))

    def on_end(detail):
        print("Call ended:", detail)
        ended.set()

    calls.on("end_call", on_end)
    calls.on("error", lambda detail: print("Call error:", detail))

    try:
        await calls.open(timeout=30)
        await api.voip.dial(sys.argv[1])
        await calls.start_audio()
        await ended.wait()
    finally:
        await calls.close()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("Usage: headless_call.py <phone> <audio.wav>")

    asyncio.run(main())
