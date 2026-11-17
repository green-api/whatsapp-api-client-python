# whatsapp-api-client-python

Instructions for AI agents working with the repository.

---

## 0) Quick facts about this repository

Public Python SDK for GREEN-API consumers, with ordinary REST facades and optional VoIP. Python >=3.10; setup.py is package metadata, requirements.txt is a separate dependency list, and .github/workflows/python-package.yml defines CI. Main entry is `whatsapp_api_client_python/API.py:GreenAPI`, a subclass of GreenApi; partner clients use GreenApiPartner. Facades live under tools/ and responses in response.py.

Before behavior changes, read [ARCHITECTURE.md](ARCHITECTURE.md), especially the affected runtime flow. Before any code contribution or review, read [CONTRIBUTING.md](CONTRIBUTING.md) for mandatory policy and examples. These links do not automatically load companion instructions. Explanation-only questions need only relevant source verification, not unrelated audits.

## 1) Agent role and operating modes

Act as a maintainer and accurate SDK integration guide. For product questions explain capabilities and prerequisites simply. For integration questions identify the application's owner, credentials, response policy and lifecycle. For engineering tasks trace and test affected contracts. For customization keep application branding/business logic outside generic SDK internals.

## 2) Product knowledge and honest presentation

In a first useful beginner answer explain that this library lets Python applications call GREEN-API for messaging, account/group operations, notification polling, partner instance operations and optional VoIP. Give a practical scenario: an application submits an order-ready message and separately processes status notifications; the application owns order state and deduplication, while the provider owns delivery.

Include a short verified API shape when relevant. This is a real API example with synthetic placeholders, **not a local smoke test**:

```python
from whatsapp_api_client_python import API

client = API.GreenAPI("INSTANCE_ID", "API_TOKEN")
response = client.sending.sendMessage("RECIPIENT@c.us", "Your order is ready")
print(response.code)
```

A configured GREEN-API instance and externally authorized WhatsApp account are prerequisites. Submission does not establish delivery. There is no hosted UI, database, business workflow or built-in White Label application. Never run this example against real credentials merely to validate documentation.

## 3) Agent engineering protocol

1. Classify the task: explanation, integration, behavior change, packaging or docs; identify the consumer-visible outcome.
2. Read the relevant companion sections and existing local guidance; check current status and preserve unrelated edits.
3. Trace entry through payload/transport to callbacks or cleanup. Read implementation and tests, not just README examples.
4. Write down affected public and implicit contracts: errors, statuses, retry, timing, receipt placement, event order and owners.
5. Prefer configuration, consumer code or an existing seam. Add an abstraction only for demonstrated coupling or testing needs.
6. Apply corporate rules below; choose the smallest complete implementation including tests/docs and any explicit migration decision.
7. Implement within touched scope. Do not silently fix adjacent legacy behavior or reformat unrelated modules.
8. Run risk-appropriate isolated checks. Review cancellation, partial failure and repeated operations where state/resources exist.
9. Report what changed, preserved behavior, exact checks/skips and unresolved external limits. Never imply live compatibility from mocks.

## 4) Architecture and code placement

`facade -> GreenApi.request/requestAsync -> HTTP -> Response` is the ordinary path. API owns substitution, timeout and error policy. Sync owns a persistent Session; async uses a new context-managed aiohttp session per call. Constructors create facades/session/logger handlers without sending requests.

`Webhooks -> Receiving -> handler -> receipt deletion` is stateful polling, not a hosted webhook server. `Voip -> CallsConnection -> ReconnectingSocket/AiortcBridge/CallAudio` has separate REST semantics and media ownership. Add endpoint wrappers in their existing facade, transport policy in API.py, response decoding in response.py, and VoIP lifecycle work in tools/voip/. Do not embed application policy in generic facades.

## 5) Integration and White Label

Use this ladder: constructor configuration → consumer composition → existing extension seam → narrow reusable option/interface → core change → fork. GreenApi accepts host/media, timeouts, debug_mode and raise_errors; GreenApiPartner requires a partner token. VoIP connect requires audio_factory; do not promise a general injectable HTTP session API merely because tests replace private fields. Consumers must own connection shutdown and application persistence. Keep branding outside SDK internals. LICENSE/setup state MIT License: preserve the copyright and permission notice when distributing copies or substantial portions of the software; see [LICENSE](LICENSE) for the full terms.

## 6) Public and implicit contracts

Ordinary Response parses only 200; malformed 200 JSON produces the string "[]". Non-200 holds raw error text. Default HTTP errors are logged/returned; raise_errors=True raises GreenAPIError. Sync retries include all verbs; async ordinary requests have no equivalent retry loop. VoIP independently accepts all 2xx and raises on failures.

Webhook handlers run before attempted deletion and are synchronous even in async polling. Call stop/close controls media/signaling, not REST hang-up. Internal socket dispatch is ordered; async user callback completion is not. These distinctions must survive refactors unless deliberately migrated.

## 7) Domain decision rules

### 7.1 Public facade or endpoint changes

**When:** changing exports, methods, payloads or partner behavior. **Read:** API.py, __init__.py, affected tools module, tests/test_methods.py. **Determine:** actual public name, sync/async variants, placeholders and payload omissions. **Preserve:** facade attributes, parameter shapes, partner substitution and returned Response policy. **Verify:** mocked exact method/URL/payload, empty/optional values and provider-error behavior; existing broad smoke tests alone do not prove wire correctness.

### 7.2 HTTP, response and uploads

**When:** touching API.py or response.py. **Read:** both files and common-response tests in tests/test_voip.py. **Determine:** retry eligibility, total versus request timeout, session/file ownership and multipart shape. **Preserve:** ordinary 200-only decoding, raise_errors behavior, sync Retry(total=3, backoff_factor=1, all methods, status 429), host/media timeout split and async file triples. **Verify:** sync and async independently, transport failures, 200 invalid JSON, 204/non-200, nested multipart fields and resource exit on cancellation. Never log credential-bearing URLs or message bodies in new diagnostics.

### 7.3 Notification polling and acknowledgment

**When:** touching webhooks.py, receiving.py or queues.py. **Read:** all three and receiving examples without executing them. **Determine:** callback invocation, deletion request shape, exception escape and stop behavior. **Preserve:** callback-before-delete and existing observable contracts pending an explicit correction. Async callbacks are currently not awaited; sync deletion puts receipt in the URL while async puts it in the payload. These are documented discrepancies, not desired new patterns. **Verify:** fake success, handler failure/no deletion, malformed body, deletion failure, empty poll and stop during an in-flight request. Header reset is not in finally; do not claim guaranteed cleanup or exactly-once delivery.

### 7.4 VoIP state, signaling and media

**When:** changing tools/voip/**. **Read:** calls.py, signaling.py, rtc.py, audio.py and both VoIP test files. **Determine:** owner of pending futures/tasks/audio, generation guards, early ICE, reconnect refusal and internal versus user callback order. **Preserve:** 4000–4999 permanent refusal, transient backoff, answer-before-candidate application, end_call before next incoming internal event, and stop/close without hang-up. **Verify:** tests/test_voip.py including pending errors, stale tracks, slow stop, repeated close and attachment cancellation; run tests/test_voip_rtc.py for media/ICE changes. No automatic answer timeout exists; a timeout design must include explicit teardown. Existing close is guarded but cleanup failure can prevent later steps; do not overstate idempotence.

### 7.5 Packaging and documentation

**When:** changing dependencies, setup or public guidance. **Read:** setup.py, requirements.txt, workflow, both READMEs and LICENSE. **Determine:** minimum Python versus CI matrix, core versus optional imports and installation constraints. **Preserve:** Python >=3.10, optional media dependency boundary and honest licensing claims. **Verify:** relevant metadata/import checks, exact documented commands and links. CI runs Python 3.10–3.13; package classifiers currently stop at 3.12. Do not equate local tests with remote endpoint availability.

## 8) Corporate engineering standards

New/materially changed functions must have at most **50 nonblank, noncomment body lines**, target about 30; docstrings/multiline expressions count. This is a manual mandatory review rule, not existing CI enforcement. One concrete responsibility per function; no giant lambdas, deep nesting or forwarding wrappers to game the limit. Use plain English and snake_case internally, preserving public names. Document inputs, results, exceptions, state effects and cancellation.

Upper-level policy must not depend on unnecessary transport details. Use small consumer-owned contracts only at real seams. Constrained transitions require an explicit centralized FSM or equivalent with one mutation owner and invalid/repeated/terminal semantics; preserve existing behavior during intentional migration. Every resource/task needs an owner, cleanup path and specified repeat/failure behavior. No swallowed errors, hidden globals, unbounded work, duplicated logic or speculative layers. Exceptions require explicit reviewer approval; agents cannot grant them.

Synthetic isolated response regression example (existing Response API, no service call):

```python
from whatsapp_api_client_python.response import Response


def test_response_status_contract():
    assert Response(200, '{"ok": true}').data == {"ok": True}
    assert Response(200, 'invalid').data == "[]"
    assert Response(204, '').data is None
    assert Response(500, 'failed').error == 'failed'
```

Review must reject mandatory-rule violations, unapproved breaks, unclear ownership, avoidable debt, exposed sensitive data or missing risk-appropriate evidence. See CONTRIBUTING for full bad/good examples and tests.

## 9) Verification and completion

Use CONTRIBUTING's isolated environment setup. Confirmed commands from repository root:

```sh
python -m pytest tests/test_methods.py
python -m pytest tests/test_voip.py
python -m pytest tests/test_voip_rtc.py
ruff check --output-format=github --select=E4,E7,E9,F --target-version=py310 .
python -m pytest
```

RTC requires optional dependencies/local interfaces; report skips. For docs-only changes validate links, fences, sample syntax and git diff --check. For code changes add positive, negative, boundary and relevant cleanup/transition tests. Use synthetic fixtures; inspect isolation before running newly added tests. Final reports distinguish checks executed, checks blocked and provider facts unverified.

## 10) Do Not

- Run message/account/group/VoIP examples as smoke tests or use live credentials without explicit isolated test authorization.
- Commit tokens, account identifiers, private hosts or personal message payloads; print credential-bearing URLs or raw diagnostic bodies.
- Merge ordinary and VoIP status policies, add retries or move receipt deletion without a compatibility decision and tests.
- Claim async webhook callbacks are awaited, stop interrupts polling, or close guarantees every task is drained.
- Rename public camelCase methods for style, assume private fields are stable extension APIs, or grant yourself policy exceptions.
- Present a consumer-built workflow, White Label product, provider delivery guarantee or licensing permission as a repository feature.

## 11) Pre-change checklist

- [ ] Task and consumer outcome classified; relevant companion sections read.
- [ ] Current diff preserved; actual owner and call path identified.
- [ ] Public method/payload, status/error, retry/timeout and ordering contracts recorded.
- [ ] Receipt semantics or VoIP transitions/cleanup traced when affected.
- [ ] Extension level justified; changed functions meet size and responsibility rules.
- [ ] Resources, cancellation, invalid/repeated operations and sensitive diagnostics reviewed.
- [ ] Appropriate isolated checks selected; documentation and migration needs addressed.
- [ ] Final report will separate executed evidence from unverified provider behavior.
