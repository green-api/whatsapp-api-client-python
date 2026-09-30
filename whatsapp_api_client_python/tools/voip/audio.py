"""Application-owned audio for one media bridge."""

from __future__ import annotations
from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from typing import TYPE_CHECKING
import asyncio
import inspect
import logging

if TYPE_CHECKING:
    from aiortc import MediaStreamTrack


@dataclass
class CallAudio:
    local_track: MediaStreamTrack
    on_remote_track: Callable[[MediaStreamTrack], Awaitable[None]]
    close: Callable[[], Awaitable[None]]


AudioFactory = Callable[[], Awaitable[CallAudio]]


class FrameAudioSink:
    """Deliver decoded remote frames to a synchronous or async callback."""

    def __init__(self, on_frame: Callable):
        self._on_frame = on_frame
        self._tasks: set[asyncio.Task] = set()
        self._closed = False

    async def attach(self, track: MediaStreamTrack) -> None:
        if self._closed:
            raise RuntimeError("Audio sink is closed")

        if getattr(track, "kind", None) != "audio":
            raise ValueError("Expected a remote audio track")

        task = asyncio.create_task(self._consume(track))

        self._tasks.add(task)
        task.add_done_callback(self._tasks.discard)

    async def _consume(self, track: MediaStreamTrack) -> None:
        from aiortc.mediastreams import MediaStreamError

        try:
            while True:
                frame = await track.recv()
                result = self._on_frame(frame)

                if inspect.isawaitable(result):
                    await result

        except MediaStreamError:
            pass
        except asyncio.CancelledError:
            raise
        except Exception:
            logging.getLogger(__name__).exception("Remote audio frame consumer failed")

    async def close(self) -> None:
        if self._closed:
            return

        self._closed = True
        tasks = tuple(self._tasks)

        for task in tasks:
            task.cancel()

        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)

        self._tasks.clear()
