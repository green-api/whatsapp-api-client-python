"""Answer an incoming voice call using a WAV file, without audio devices."""

import asyncio
import os
import sys

from aiortc.contrib.media import MediaPlayer

from whatsapp_api_client_python.API import GreenAPI
from whatsapp_api_client_python.tools.voip import CallAudio, FrameAudioSink


async def make_audio() -> CallAudio:
    player = MediaPlayer(sys.argv[1])

    if player.audio is None:
        raise ValueError("The file has no audio stream")

    async def on_frame(frame):
        # Replace this with your application's frame consumer.
        print(f"received {frame.samples} samples")

    sink = FrameAudioSink(on_frame)

    async def close():
        await sink.closeAsync()
        player.audio.stop()

    return CallAudio(player.audio, sink.attachAsync, close)


async def main():
    api = GreenAPI(os.environ["GREEN_API_ID"], os.environ["GREEN_API_TOKEN"])
    calls = api.voip.connect(audio_factory=make_audio)
    incoming = asyncio.Queue()
    ended = asyncio.Event()

    calls.on("incoming_call", incoming.put_nowait)
    calls.on("end_call", lambda detail: ended.set())
    calls.on("error", lambda detail: print("Call error:", detail))

    try:
        await calls.openAsync(timeout=30)

        info = await incoming.get()

        print("Incoming call:", info.wid)

        if calls.state is None or calls.state.state != "inc-call":
            return

        await api.voip.acceptAsync()
        await calls.startAudioAsync()
        await ended.wait()
    finally:
        await calls.closeAsync()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: incoming_call.py <audio.wav>")

    asyncio.run(main())
