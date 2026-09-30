"""callsRtc WebSocket with the original retry and ordered dispatch policy."""

from collections import defaultdict
import asyncio
import inspect
import json
import logging

# Constants

INITIAL_BACKOFF_MS = 500

MAX_BACKOFF_MS = 10 * 000

PERMANENT_CLOSE_MIN = 4000

PERMANENT_CLOSE_MAX = 4999


class ReconnectingSocket:
    def __init__(self, url: str, *, socket_factory=None, sleep=None):
        self._url = url
        self._socket_factory = socket_factory
        self._sleep = sleep or asyncio.sleep
        self._socket = None
        self._closed_by_user = False
        self._refused_by_server = False
        self._backoff_ms = INITIAL_BACKOFF_MS
        self._task: asyncio.Task | None = None
        self._connected = asyncio.Event()
        self._listeners = defaultdict(list)

    def on(self, name: str, callback) -> None:
        self._listeners[name].append(callback)

    @property
    def refused(self) -> bool:
        return self._refused_by_server

    async def open(self, *, timeout: float | None = None) -> None:
        if self._closed_by_user:
            raise RuntimeError("ReconnectingSocket is closed")

        if self._task is None:
            self._task = asyncio.create_task(self._connect())

        waiter = asyncio.create_task(self._connected.wait())

        try:
            done, _ = await asyncio.wait((waiter, self._task), timeout=timeout, return_when=asyncio.FIRST_COMPLETED)

            if waiter in done:
                return

            if self._task in done:
                raise RuntimeError("callsRtc connection was refused or closed")

            raise TimeoutError("Timed out connecting to callsRtc")
        finally:
            waiter.cancel()

    async def send(self, data) -> None:
        if self._socket is None:
            raise RuntimeError("ReconnectingSocket is not connected")

        await self._socket.send(json.dumps(data, separators=(",", ":")))

    async def close(self) -> None:
        self._closed_by_user = True
        socket = self._socket
        self._socket = None

        self._connected.clear()

        if socket is not None:
            await socket.close()

        if self._task is not None:
            self._task.cancel()

            try:
                await self._task
            except asyncio.CancelledError:
                pass

    async def _dispatch(self, name: str, detail=None) -> None:
        # Internal handlers must finish before the next frame is read.
        for callback in tuple(self._listeners[name]):
            try:
                result = callback(detail)

                if inspect.isawaitable(result):
                    await result
            except Exception:
                logging.getLogger(__name__).exception("callsRtc %s handler failed", name)

    async def _connect(self) -> None:
        if self._socket_factory is None:
            from websockets.asyncio.client import connect
            self._socket_factory = connect

        while not self._closed_by_user:
            try:
                socket = await self._socket_factory(self._url)

                if self._closed_by_user:
                    await socket.close()
                    return

                self._socket = socket
                self._connected.set()
                self._backoff_ms = INITIAL_BACKOFF_MS

                await self._dispatch("connect")

                while not self._closed_by_user:
                    try:
                        raw = await socket.recv()
                    except Exception as exc:
                        code = getattr(exc, "code", None)

                        if code is None:
                            frame = getattr(exc, "rcvd", None)
                            code = getattr(frame, "code", 1006)
                            reason = getattr(frame, "reason", "")
                        else:
                            reason = getattr(exc, "reason", "")

                        self._socket = None

                        self._connected.clear()

                        if self._closed_by_user:
                            return

                        permanent = PERMANENT_CLOSE_MIN <= code <= PERMANENT_CLOSE_MAX

                        self._refused_by_server |= permanent

                        await self._dispatch("disconnect", {
                            "reason": reason or "connection closed", "code": code,
                            "permanent": permanent,
                        })

                        if permanent:
                            return

                        break
                    try:
                        parsed = json.loads(raw)
                    except (TypeError, ValueError):
                        continue

                    await self._dispatch("message", parsed)
            except asyncio.CancelledError:
                raise
            except Exception as exc:
                if self._closed_by_user:
                    return

                self._socket = None

                self._connected.clear()

                await self._dispatch("disconnect", {
                    # Exception text may contain the URL and its API token.
                    "reason": f"{type(exc).__name__}: connection failed", "code": 1006,
                    "permanent": False,
                })
            if not self._closed_by_user:
                delay = self._backoff_ms
                self._backoff_ms = min(self._backoff_ms * 2, MAX_BACKOFF_MS)
                await self._sleep(delay / 1000)
