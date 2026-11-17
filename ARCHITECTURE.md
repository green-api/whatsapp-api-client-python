# Architecture

See [AGENTS.md](AGENTS.md) for agent workflow and [CONTRIBUTING.md](CONTRIBUTING.md) for mandatory rules for changes. This document describes existing behavior; it does not assert compliance with those future-code rules.

## 1) Scope and entry points

This is a public Python SDK for GREEN-API REST operations and optional VoIP signaling/media. Consumers own credentials, business logic, persistence and process management. The remote service owns account authorization and delivery. There is no hosted application, database, campaign scheduler or branding layer here.

`setup.py` declares version 0.0.55, Python >=3.10, requests==2.34.2, aiofiles>=24.1.0, aiogram>=3.28.2 and aiohttp>=3.13.5. `requirements.txt` uses a lower bound for requests instead of the package's exact pin. The voip extra adds aiortc>=1.15,<2 and websockets>=16,<17. CI also tests Python 3.13 despite classifiers ending at 3.12. Check these files before changing compatibility claims.

## 2) Ownership map

Paths below are under `whatsapp_api_client_python/` unless stated otherwise.

| Location | Owner, callers and change implications |
| --- | --- |
| `API.py:GreenApi`, `GreenAPI` | Consumer entry point; constructs all facades, a requests Session and a logger handler. Construction does not send an API request. Repeated clients add handlers to the same named logger. |
| `API.py:GreenApiPartner` | Calls the base constructor with empty instance credentials, stores partner token/email and adds Partner. Overrides request substitution for the partner token. |
| `tools/sending.py` and other REST facades | Translate consumer arguments into endpoint/payload calls to the API owner. A payload edit affects provider compatibility even if wrapper tests pass. |
| `response.py:Response` | Decodes HTTP results for ordinary facades. Its semantics affect every ordinary method. |
| `tools/receiving.py`, `webhooks.py`, `queues.py` | Receiving supplies polling/deletion calls; Webhooks controls dispatch and deletion sequence; Queues wraps queue operations. There is no durable local receipt store. |
| `tools/voip/calls.py:Voip` | Separate async REST transport and connection factory; does not use the ordinary Response policy. |
| `tools/voip/calls.py:CallsConnection` | Owns current state, pending negotiation, audio, bridge, generation guards and remote attachment tasks. |
| `tools/voip/signaling.py:ReconnectingSocket` | Owns WebSocket, reconnect task, backoff and ordered internal dispatch. |
| `tools/voip/rtc.py`, `audio.py` | AiortcBridge adapts peer negotiation/ICE; CallAudio supplies local track, remote-track callback and close; FrameAudioSink consumes frames. |

## 3) Synchronous REST flow

`Sending.sendMessage -> GreenApi.request -> Session.request -> __handle_response -> Response`.

The facade constructs the endpoint and payload. API substitutes host, media, instance and token placeholders and adds `GREEN-API_SDK_PY/1.0`. Without files it sends JSON with host_timeout=180 seconds; files use data/files and media_timeout=10800 seconds. These are request timeouts, not a whole-operation deadline. The persistent session mounts Retry(total=3, backoff_factor=1.0, allowed_methods=None, status_forcelist=[429]). Thus retries are not restricted to safe HTTP verbs; changing them changes possible repeated side effects.

Transport exceptions become Response(None, message), or GreenAPIError with raise_errors=True. Non-200 HTTP results are logged and returned, or raised under that option. Debug logging can include response bodies. Never assume logging is safe for real message data. The Session belongs to the client; there is no dedicated public client close method in API.py. Consumers managing its lifetime can close the session, but a general injectable transport contract is not provided.

Response parses JSON only at status 200; invalid JSON yields the string `"[]"`, not a list. Other statuses populate error with raw text. JSON values are not restricted to dictionaries despite annotations. `raw_request` bypasses template building but still uses session/error handling. Changing Response to accept all 2xx would alter ordinary callers and must not be inferred from VoIP behavior.

Evidence: `tests/test_methods.py` patches Session.request and checks method results/counts; it is not exhaustive payload coverage. `tests/test_voip.py` includes common-response and HTTP-204 regression checks. New transport changes need explicit payload, exception and retry assertions.

## 4) Asynchronous REST flow

Async facades call requestAsync, which substitutes the same placeholders but opens a new context-managed aiohttp ClientSession per request. Total timeout uses host_timeout or media_timeout. There is no corresponding retry loop. JSON is passed directly for ordinary calls. Multipart payload dict/list values are JSON-stringified; other values become strings. Files unpack as `(filename, file_obj, content_type)`.

The response is read fully, the session exits, then status handling and Response decoding run. Exception policy matches the synchronous wrapper; asyncio cancellation is not converted by the Exception handler on supported Python versions. Context management closes the session, but does not establish ownership of caller-provided file objects. raw_request_async consumes timeout/headers separately and injects the User-Agent.

A shared helper refactor can accidentally introduce retries, change multipart field types or change session lifetime. Test sync and async independently with fakes; passing synchronous method tests does not demonstrate async parity.

## 5) Notification dispatch and receipt lifecycle

`Webhooks.startReceivingNotifications[Async] -> _start_polling[Async] -> Receiving.receiveNotification[Async] -> handler(typeWebhook, body) -> deleteNotification[Async]`.

Start sets `_running=True`; stop only sets it False. Stop does not interrupt an in-flight poll. A 200 with data extracts body/typeWebhook and invokes the handler before attempting deletion. Both variants invoke the handler synchronously: the async variant does **not** await an async callback. Passing a coroutine function can therefore attempt deletion before its processing executes.

Only KeyboardInterrupt is caught in the loops. A callback error or malformed event escapes before deletion. A deletion response is ignored; raised deletion failures escape. There is no local acknowledgment retry or exactly-once guarantee. Empty successful async polls sleep 0.1 seconds; synchronous empty polls continue immediately. Non-200 results loop without a dedicated delay (underlying transport policy still applies).

Polling changes the persistent sync Session Connection header to keep-alive and resets it to close after normal loop exit. Reset/logging is not in finally, so exceptions or cancellation can bypass it; the async polling path changes this same sync Session even though async requests use separate sessions. `_running` is not reset on every exceptional exit.

**Existing wire discrepancy:** sync deleteNotification appends receiptId to the DELETE URL. Async deleteNotificationAsync uses the trailing-slash URL and passes receiptId as the request payload. This is source behavior, not a verified provider contract or a recommendation. A correction requires a focused compatibility decision and mock assertions; do not silently normalize it during unrelated edits.

Moving deletion before processing changes failure recovery. Awaiting callbacks changes ordering and must be deliberate. Existing method smoke tests do not prove callback/ack semantics. Changes need fake receiving tests for successful processing, handler exception, malformed body, empty poll, failed deletion, stop during poll, and sync versus async receipt placement. External redelivery timing remains unverified.

## 6) VoIP lifecycle

### REST admission and signaling

Voip._request uses its own aiohttp session with connect/sock_read timeouts of 5 seconds, total=None, trust_env=True and redirects disabled. It accepts all 2xx, returns None for 204/empty bodies, otherwise parses JSON; non-2xx raises RuntimeError and malformed JSON propagates. These rules are independent of raise_errors. dialAsync appends @c.us only when the target contains no @. accept/reject/hang-up are explicit REST operations; stopping audio or closing a connection does not hang up.

connect requires audio_factory and returns a CallsConnection; openAsync opens signaling. websocketUrl accepts http/https and maps to ws/wss while preserving the host path and adding callsRtc credentials. Never log that URL. ReconnectingSocket awaits internal listeners before reading the next frame. Malformed JSON is ignored, listener failures are logged. Transient disconnections retry starting at 0.5 seconds, doubling to 10 seconds; connection success resets backoff. Close codes 4000–4999 permanently stop reconnection. User close clears connection state, closes socket and cancels/awaits the reconnect task. An open timeout cancels its waiter, not necessarily the connection task: the owner still needs close.

### Negotiation and media ownership

startAudioAsync rejects duplicate active/pending starts and closed connections. It acquires audio from the factory, fetches ICE servers, creates the bridge, adds the local track, installs a remote-track callback, creates/sets an offer and sends offer plus candidates. The pending future resolves after the answer and buffered early candidates are applied. There is no automatic answer timeout. Generation checks discard stale acquisition/track work after teardown.

Answer errors reject pending negotiation and tear down. Candidate failures after the answer also tear down and emit error. A signaling error during negotiation rejects and tears down; after negotiation it emits error without immediate teardown. stopAudioAsync rejects pending work and sends stop during teardown, preserving call state. Teardown clears references/candidate state, increments generation, cancels and gathers remote attachment tasks, then closes peer and audio in nested finally blocks even if sending stop fails.

closeAsync marks closed, rejects pending work, tears down, cancels a resume task and closes the socket. A repeated close returns immediately. This is not a guarantee that cleanup failures can be retried: an earlier failure can prevent later steps after closed is set. User async event callback tasks are tracked and logged but are not drained by closeAsync. Do not claim universal task cleanup or immunity to repeated cancellation.

### State and event ordering

State is distributed event-driven logic, not a validated transition-table FSM. `_on_state` stores the received state and emits state. Entering inc-call from another state with info emits incoming_call; repeated inc-call does not emit another incoming event. Leaving inc-call/out-call/on-call rejects pending negotiation, tears down and emits end_call, including a cause when provided. Internal dispatch waits for this before the next frame; async user callbacks run independently and their completion order is not guaranteed.

On disconnect during an active call, an existing bridge permits transient resume; pending negotiation is rejected and media torn down. Permanent refusal disables resume. Without resume the state clears and end_call is emitted. A later active state can trigger fresh audio. Changing dispatch to fire-and-forget can reorder end_call and incoming_call or attach old tracks to a new bridge.

Evidence: `tests/test_voip.py` covers early ICE, stop/close without hang-up, fresh audio on reconnect, pending errors, refusal, slow-stop ordering and attachment cleanup. `tests/test_voip_rtc.py` covers candidate wire fields candidate/sdpMid/sdpMLineIndex, sink cleanup and local aiortc negotiation. Local peers require interfaces and may skip when unavailable; neither suite proves GREEN-API/WhatsApp interoperability or physical audio behavior.

## 7) Integration and verification boundaries

Use constructor host/media/timeouts/error policy first, then consumer composition. VoIP exposes audio_factory and CallsConnection factory seams; underscore transport replacement in tests is not a general stable SDK transport API. Keep branding, business decisions and persistence in the consumer. No White Label packaging layer ships here. LICENSE and setup metadata state MIT License. Preserve the copyright and permission notice when distributing copies or substantial portions of the software; see [LICENSE](LICENSE) for the full terms.

`.github/workflows/python-package.yml` installs ruff, pytest, pytest-asyncio and `.[voip]` on Ubuntu 24.04 with Python 3.10–3.13, runs Ruff E4/E7/E9/F targeting py310, then pytest. There is no function-length enforcement in that command. See [CONTRIBUTING.md](CONTRIBUTING.md) for exact commands and risk-specific tests. Live provider behavior, account delivery and device interoperability remain unverified by repository-local checks.
