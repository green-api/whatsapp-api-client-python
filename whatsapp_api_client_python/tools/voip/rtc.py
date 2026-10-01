"""Thin aiortc boundary; retain the existing SDP and ICE wire behavior."""

from aiortc import RTCConfiguration, RTCIceServer, RTCPeerConnection, RTCSessionDescription
from aiortc.sdp import candidate_from_sdp, candidate_to_sdp


def candidate_from_json(value: dict):
    text = value["candidate"]

    if text.startswith("candidate:"):
        text = text[len("candidate:"):]

    candidate = candidate_from_sdp(text)
    candidate.sdpMid = value.get("sdpMid")
    candidate.sdpMLineIndex = value.get("sdpMLineIndex")

    if candidate.sdpMid is None and candidate.sdpMLineIndex is None:
        raise ValueError("ICE candidate needs sdpMid or sdpMLineIndex")

    return candidate


def candidate_to_json(candidate) -> dict:
    return {
        "candidate": "candidate:" + candidate_to_sdp(candidate),
        "sdpMid": candidate.sdpMid,
        "sdpMLineIndex": candidate.sdpMLineIndex,
    }


class AiortcBridge:
    def __init__(self, ice_servers, *, peer_factory=None):
        servers = [RTCIceServer(
            urls=entry["urls"],
            username=entry.get("username"),
            credential=entry.get("credential"),
        ) for entry in ice_servers]

        factory = peer_factory or RTCPeerConnection
        self._peer = factory(RTCConfiguration(iceServers=servers))

        self._on_track = None

        if hasattr(self._peer, "on"):
            self._peer.on("track", self._handle_track)

    @property
    def local_description(self) -> dict | None:
        description = getattr(self._peer, "localDescription", None)

        if description is None:
            return None

        return {"type": description.type, "sdp": description.sdp}

    def add_track(self, track) -> None:
        self._peer.addTrack(track)

    def on_track(self, callback) -> None:
        self._on_track = callback

    def _handle_track(self, track) -> None:
        if self._on_track is not None:
            self._on_track(track)

    def local_candidates(self) -> list[dict]:
        """Also send gathered SDP candidates as separate signaling frames."""

        description = self.local_description

        if description is None:
            return []

        result = []
        mid = None
        index = -1
        candidates = []

        def flush():
            for text in candidates:
                result.append({"candidate": text, "sdpMid": mid, "sdpMLineIndex": index})

        for line in description["sdp"].splitlines():
            if line.startswith("m="):
                if index >= 0:
                    flush()

                index += 1
                mid = None
                candidates = []
            elif line.startswith("a=mid:"):
                mid = line[len("a=mid:"):]
            elif line.startswith("a=candidate:"):
                candidates.append(line[len("a="):])

        if index >= 0:
            flush()

        return result

    async def create_offer(self) -> dict:
        offer = await self._peer.createOffer()
        return {"type": offer.type, "sdp": offer.sdp}

    async def set_local_description(self, offer: dict) -> None:
        await self._peer.setLocalDescription(RTCSessionDescription(**offer))

    async def set_remote_description(self, answer: dict) -> None:
        await self._peer.setRemoteDescription(RTCSessionDescription(**answer))

    async def add_ice_candidate(self, value: dict) -> None:
        if value is None or not value.get("candidate"):
            await self._peer.addIceCandidate(None)
        else:
            await self._peer.addIceCandidate(candidate_from_json(value))

    async def close(self) -> None:
        await self._peer.close()

    async def get_stats(self):
        return await self._peer.getStats()
