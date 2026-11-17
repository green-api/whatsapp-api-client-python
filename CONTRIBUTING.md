# Contributing

Mandatory policy for human and AI contributions. Read [AGENTS.md](AGENTS.md) for workflow and [ARCHITECTURE.md](ARCHITECTURE.md) for existing behavior. These requirements apply to new and materially changed code; they do not claim that historical code already complies.

## 1) Engineering goal and workflow

Deliver the smallest complete, safe and maintainable change, including necessary tests and documentation.

1. State the consumer problem, affected public methods and intended observable outcome.
2. Trace the facade, transport and lifecycle owners before editing. Record status, payload, retry, ordering and cleanup contracts that must survive.
3. Choose configuration or existing composition before introducing an abstraction. Explain any intentional compatibility break and migration path.
4. Implement the scoped change and improve materially touched legacy functions to these standards. Avoid unrelated formatting sweeps.
5. Test success, failure and relevant boundaries using isolated fakes; review cancellation and ownership for async work.
6. Review the diff for credentials and behavior changes. Report exact checks and remaining limitations. Reviewers, not agents acting alone, approve narrowly described exceptions.

## 2) Mandatory function and contract rules

New and materially changed functions must have **at most 50 nonblank, noncomment body lines**, targeting about 30. Count physical body lines, excluding the signature, blank lines and comment-only lines; docstrings and multiline expressions count. Nested function bodies count within their enclosing body. Review manually: existing CI does not enforce this rule. Giant lambdas, meaningless forwarding wrappers and deep nesting cannot be used to evade it.

Each function has one concrete responsibility. A newcomer should understand inputs, output/effect, errors, state and owner within roughly five minutes. Use ordinary English, Python snake_case for new internal names, and precise domain terms. Preserve published camelCase API names. Predicates return booleans; validate_* functions raise documented errors. Types and docstrings must expose meaningful side effects, cancellation and failure contracts, not narrate syntax.

### Pattern A — naming and decomposition (synthetic consumer code)

Bad: ambiguous name, mixed validation/transport and unexplained return semantics.

```python
def process(x, api):
    if not x:
        return False
    return api.sending.sendMessage(x, "Ready")
```

Good: validation and transport have separate responsibilities; callers own response policy.

```python
def validate_chat_id(chat_id: str) -> None:
    """Reject missing identifiers before any transport work."""
    if not chat_id.strip():
        raise ValueError("chat_id is required")


def send_ready_notice(api, chat_id: str):
    """Submit a notice; return the SDK Response without implying delivery."""
    validate_chat_id(chat_id)
    return api.sending.sendMessage(chat_id, "Ready")
```

**Why:** invalid input cannot masquerade as a transport response, and submission is not described as delivery. **Tests:** valid ID calls once and returns the fake response; empty and whitespace IDs raise before calling; a transport exception propagates. **Review:** reject vague naming, mixed boolean/Response results and public renames solely for style.

## 3) Dependency direction and extension design

High-level policy must not know unnecessary HTTP/provider/storage details. At a real seam, define the smallest contract near its consumer and inject the adapter. Keep fixed local implementation concrete. Every new interface needs an actual consumer and a demonstrated coupling/testing problem; no speculative factories or interface-per-class designs.

### Pattern B — consumer contract, adapter and fake (synthetic)

Bad: a welcome policy constructs SDK URLs and HTTP payloads itself, tying policy tests to network internals.

```python
def welcome_bad(session, url, chat_id):
    return session.post(url, json={"chatId": chat_id, "message": "Welcome"})
```

Good: the consumer needs text submission, with an explicit failure contract.

```python
from typing import Protocol


class TextSender(Protocol):
    def send_text(self, chat_id: str, text: str) -> None:
        """Submit text or raise RuntimeError; does not guarantee delivery."""
        ...


class SdkTextSender:
    def __init__(self, api):
        self.api = api

    def send_text(self, chat_id: str, text: str) -> None:
        response = self.api.sending.sendMessage(chat_id, text)
        if response.code != 200:
            raise RuntimeError("Text submission failed")


class FakeTextSender:
    def __init__(self, fail=False):
        self.fail = fail
        self.sent = []

    def send_text(self, chat_id: str, text: str) -> None:
        if self.fail:
            raise RuntimeError("Text submission failed")
        self.sent.append((chat_id, text))


def welcome(sender: TextSender, chat_id: str) -> None:
    sender.send_text(chat_id, "Welcome")
```

The adapter assumes an SDK client with default raise_errors=False; other configured exceptions propagate and must be documented by a real integration. **Why:** business text can be tested without URLs or credentials; HTTP interpretation stays in the adapter. **Tests:** fake records exactly one welcome; fake failure propagates; adapter returns on 200, rejects 204/500 and does not include response bodies in errors. **Review:** reject provider internals in welcome and abstractions without a real consumer.

## 4) State transition discipline

When correctness depends on allowed states/events, new or materially changed transition logic must use a centralized explicit FSM or equivalent model with one mutation owner. Specify invalid, repeated and terminal cases; separate decisions from I/O where feasible. Do not force an FSM onto trivial flags or silently migrate CallsConnection's current distributed semantics.

### Pattern C — transitions (synthetic, not the SDK call protocol)

Bad: handlers directly overwrite arbitrary states.

```python
def handle_bad(session, event):
    session.state = event
```

Good: one owner commits a pure transition decision.

```python
def next_state(state: str, event: str) -> str:
    transitions = {("new", "start"): "running", ("running", "finish"): "done"}
    if state == "done" and event == "finish":
        return "done"  # Repeated completion is explicitly harmless.
    try:
        return transitions[state, event]
    except KeyError:
        raise ValueError(f"Invalid transition: {state}/{event}") from None


class RunState:
    def __init__(self):
        self.state = "new"

    def apply(self, event: str) -> None:
        self.state = next_state(self.state, event)
```

**Why:** illegal events cannot partially mutate state. **Tests:** new/start/running/finish/done; finish before start; duplicate start; repeated finish; start after done; unknown event leaves state unchanged. **Review:** reject scattered mutation and missing terminal semantics. Actual VoIP changes must also preserve incoming/end event order, early ICE and resume behavior.

## 5) Ownership, cancellation and cleanup

Every connection, task, timer, queue, file and stream must have a named owner, bounded lifetime and end-of-life path. Higher layers invoke a simple lifecycle method instead of closing internals piecemeal. Specify partial acquisition, repeated close, cleanup errors and cancellation. No unowned background work or hidden infinite queues.

### Pattern D — partial acquisition and cancellation (synthetic)

Bad: exceptions and cancellation bypass cleanup.

```python
async def run_bad(open_connection, open_sink, consume):
    connection = await open_connection()
    sink = await open_sink()
    await consume(connection, sink)
    await sink.close()
    await connection.close()
```

Good: the operation scope owns both resources, and each cleanup is registered immediately.

```python
from contextlib import AsyncExitStack


async def run_owned(open_connection, open_sink, consume):
    """Acquire, consume and close in reverse order; propagate failures."""
    async with AsyncExitStack() as resources:
        connection = await open_connection()
        resources.push_async_callback(connection.close)
        sink = await open_sink()
        resources.push_async_callback(sink.close)
        await consume(connection, sink)
```

**Why:** sink acquisition failure still closes the connection; consume failure or ordinary cancellation enters cleanup. Callbacks are attempted in reverse order even when one raises. Cleanup exceptions propagate and can replace an active exception with chaining. Each acquisition function must clean its own partially acquired resources before raising. This scoped API has no repeatable close method: callbacks run once per acquired resource per invocation; it promises neither resource close idempotence nor immunity to repeated cancellation during awaited cleanup. A long-lived owner must document those separately and retain responsibility for supervised cleanup tasks.

**Tests:** normal operation closes sink then connection; sink acquisition failure closes connection only; connection acquisition failure registers nothing; consume exception and cancellation close both; sink close failure still attempts connection close and propagates; two invocations acquire independent resources. **Review:** reject lost tasks, undocumented failure precedence and claims that finally alone guarantees cleanup under repeated cancellation.

## 6) Errors, retries, concurrency and debt

Preserve exception versus returned-error behavior, timeouts, payloads, ordering and observability unless a break has an explicit migration plan. Do not swallow errors, leak credential-bearing URLs into diagnostics, introduce hidden globals, duplicate logic, unbounded concurrency or workaround branches without scope, reason and removal conditions. Retries of sends may repeat side effects: document eligible failures and tests before changing policy. Async callbacks and internal ordered handlers have different scheduling contracts; do not conflate them.

Reuse standard library, current dependencies and existing code first. Minimal diff includes all required tests/docs, not simply the fewest changed lines. Consumers own branding and business workflows. Use configuration, consumer composition, existing seams, then a narrow reusable option, core change, and only lastly a separately reviewed fork. Verify constructor/lifecycle constraints and follow the [MIT License](LICENSE), including its copyright and permission notice requirements for distribution.

## 7) Safe verification

From the repository root, in a disposable virtual environment:

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install ruff pytest pytest-asyncio ".[voip]"
ruff check --output-format=github --select=E4,E7,E9,F --target-version=py310 .
python -m pytest
```

These reproduce CI's lint selection and test invocation (CI uses `pytest`). Installation requires package-index access. No live credentials are needed. For focused checks:

```sh
python -m pytest tests/test_methods.py
python -m pytest tests/test_voip.py
python -m pytest tests/test_voip_rtc.py
```

Ordinary facade changes require mocked URL/method/payload assertions, not just Response equality. HTTP changes require both sync and async exceptions, status handling, multipart boundaries and timeout checks. Webhook changes require callback-before-delete, callback failure/no deletion, malformed event, deletion failure, empty poll and stop tests; add focused tests because existing smoke coverage is insufficient. VoIP changes require the mock suite plus local RTC tests when media/ICE changes. Test invalid/repeated transitions and cancellation at acquisition, negotiation and attachment boundaries. RTC tests require optional dependencies and local network interfaces; report skips rather than treating them as passing interoperability tests.

Examples under examples/ can send messages or mutate accounts/groups; do not run them as smoke tests. Use explicit isolated fixtures and synthetic credentials. Live provider verification requires an explicitly authorized isolated account/scenario; local passing tests never establish real delivery. Documentation-only edits need links, fences, Python snippet syntax and diff checks; do not claim application tests were executed if they were not.

## 8) Review acceptance and rejection

Reviewers must reject mandatory policy violations, unapproved compatibility breaks, avoidable debt, unclear ownership, secret exposure, unverifiable correctness or missing risk-appropriate tests. In particular reject functions over the body limit, arbitrary state mutation for constrained transitions, unbounded callback work, premature receipt deletion, merged ordinary/VoIP status semantics, and retry changes without repeated-side-effect analysis.

Accept only when the diff has a concrete consumer benefit, traceable contracts, clear failure/cleanup behavior, relevant passing checks and truthful limitations. Exceptions require explicit reviewer approval with scope, reason, risk and follow-up/removal condition; AI agents may not grant themselves exceptions. Improve touched legacy scope without demanding an unrelated repository-wide refactor.
