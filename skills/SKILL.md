---
name: greenapi-client-python
description: >
  Write correct Python code with the official GREEN-API SDK whatsapp-api-client-python
  (package whatsapp_api_client_python). Use when sending/receiving WhatsApp messages,
  files, polls, groups, journals, queues, statuses, contacts, partner instances, polling
  notifications, or configuring a GREEN-API instance in Python. Triggers: GREEN-API,
  green-api, whatsapp-api-client-python, GreenAPI, GreenApi, sendMessage, receiveNotification.
license: MIT
metadata:
  version: "1.0.0"
  sdk: whatsapp-api-client-python
  pypi: whatsapp-api-client-python
  docs: https://green-api.com/en/docs/api/
  github: https://github.com/green-api/whatsapp-api-client-python
---

# GREEN-API Python client (`whatsapp-api-client-python`)

## When to apply

Use this skill whenever the task is to call GREEN-API from **Python** via the official
SDK. Do **not** invent HTTP paths or method names from memory: only methods listed in
[references/inventory.md](references/inventory.md) exist in this SDK. Semantics of
parameters, `chatId` formats, delays, and notification types come from the official docs
linked in each method section — not from other repos.

For **webhook HTTP server** libraries in other languages, use a language-specific
webhook skill if present. This SDK receives notifications via **polling**
(`webhooks.startReceivingNotifications` / `receiving.receiveNotification`) or you can
build your own HTTP endpoint for webhook-endpoint technology.

## Sources of truth (mandatory)

1. **Official API docs** — https://green-api.com/en/docs/api/  
   Parameters, response shapes, limits, `chatId`, delays, notification formats.
2. **This repository / installed package** — method names, class attributes, init
   signatures. Inventory: [references/inventory.md](references/inventory.md).

If a method exists in the docs but **not** in the inventory → do not use it in code.

## Install

```shell
python -m pip install whatsapp-api-client-python
```

Requires Python **>= 3.10**. Credentials: `idInstance` and `apiTokenInstance` from
[console.green-api.com](https://console.green-api.com/).

## Client initialization

```python
from whatsapp_api_client_python import API

greenAPI = API.GreenAPI(
    "1101000001",  # idInstance (string)
    "d75b3a66374942c5b3c019c698abc2067e151558acbd412345",  # apiTokenInstance
)
```

Optional constructor kwargs (from `GreenApi.__init__` in `API.py`):

| Kwarg | Default | Meaning |
| --- | --- | --- |
| `debug_mode` | `False` | Verbose request logging |
| `raise_errors` | `False` | Raise `GreenAPIError` on failures |
| `host` | `https://api.green-api.com` | API host (`apiUrl`) |
| `media` | `https://media.green-api.com` | Media host for uploads |
| `host_timeout` | `180` | Seconds per host request retry |
| `media_timeout` | `10800` | Seconds per media request |

Aliases: `API.GreenAPI` is the same class as `API.GreenApi`.

Partner API (separate client):

```python
partner = API.GreenApiPartner(partnerToken="PARTNER_TOKEN")
# then: partner.partner.getInstances() / createInstance / deleteInstanceAccount
```

### Response object

Every API method returns `whatsapp_api_client_python.response.Response`:

| Attribute | When | Content |
| --- | --- | --- |
| `code` | always | HTTP status, or `None` on transport failure |
| `data` | `code == 200` | Parsed JSON (`dict` / list) |
| `error` | non-200 | Response body text |

Always check `response.code == 200` before reading `response.data`.

### Async

Most groups expose `*Async` twins (`sendMessageAsync`, `receiveNotificationAsync`, …).
Call them with `await` inside `asyncio`.

## chatId and phone format

Docs: https://green-api.com/en/docs/api/chat-id/

| Kind | Format | Example |
| --- | --- | --- |
| Personal chat | `<phone>@c.us` | `79876543210@c.us` |
| Group chat | `...@g.us` | `120363043968066561@g.us` |
| Lid | `...@lid` | returned by API; do not invent |

- Phone: full international number, **digits only**, no `+`, spaces, or leading zeros tricks.
- **Never** hand-craft group IDs — take them from `createGroup`, journals, or notifications.
- Wrong `chatId` → validation 400: must be `phone_number@c.us` or `group_id@g.us`.

## Instance must be authorized

Docs: https://green-api.com/en/docs/api/account/GetStateInstance/

Before sending, verify:

```python
state = greenAPI.account.getStateInstance()
print(state.data)  # expect {"stateInstance": "authorized"}
```

Important states: `authorized`, `notAuthorized`, `blocked`, `starting`, `suspended`.
Authorize via console QR / `account.qr()` / `account.getAuthorizationCode(phoneNumber)`.
Messages sit in the send queue up to **24 hours** until the instance is authorized.

## Message sending delay

Docs: https://green-api.com/en/docs/api/send-messages-delay/

Outgoing messages go through a FIFO queue. Delay is controlled by instance setting
`delaySendMessagesMilliseconds` (min **500** ms, max **600000** ms; recommend ≤ 300000):

```python
greenAPI.account.setSettings({"delaySendMessagesMilliseconds": 5000})
```

Note: `setSettings` reboots the instance; settings apply within ~5 minutes.

## Typical scenarios

### 1. Send a text message

Docs: https://green-api.com/en/docs/api/sending/SendMessage/

```python
from whatsapp_api_client_python import API

greenAPI = API.GreenAPI(id_instance, api_token)

response = greenAPI.sending.sendMessage(
    "79876543210@c.us",
    "Hello from GREEN-API",
    typingTime=3000,  # optional: 1000–20000 ms typing indicator
)

if response.code == 200:
    print(response.data["idMessage"])
else:
    print(response.error)
```

Required: `chatId`, `message` (max 20000 chars). Optional in SDK: `quotedMessageId`,
`archiveChat`, `linkPreview`, `typingTime`, `typePreview`, `customPreview`.
Response: `{ "idMessage": "..." }`.

### 2. Send a file by URL

Docs: https://green-api.com/en/docs/api/sending/SendFileByUrl/

```python
response = greenAPI.sending.sendFileByUrl(
    "79876543210@c.us",
    "https://download.samplelib.com/png/sample-clouds2-400x300.png",
    "sample-clouds2-400x300.png",
    "Caption text",
)
```

Required: `chatId`, `urlFile`, `fileName` (with extension). Max file size **100 MB**.

### 3. Send a file by upload (local path)

Docs: https://green-api.com/en/docs/api/sending/SendFileByUpload/  
Uses **media** host (SDK sets this automatically).

```python
response = greenAPI.sending.sendFileByUpload(
    "79876543210@c.us",
    "data/logo.jpg",
    "logo.jpg",
    "Available rates",
)
# response.data: idMessage, urlFile (link valid 15 days)
```

SDK signature: `sendFileByUpload(chatId, path, fileName=None, caption=None, ...)`.
The local path is the second argument (`path`), not a raw file object.

### 4. Receive notifications — polling (built-in)

Docs: https://green-api.com/en/docs/api/receiving/technology-http-api/ReceiveNotification/

**Requirement:** instance `webhookUrl` must be **empty**. If a custom webhook URL is set,
`receiveNotification` returns an error telling you to clear it.

```python
from whatsapp_api_client_python import API

greenAPI = API.GreenAPI(id_instance, api_token)


def on_event(type_webhook: str, body: dict) -> None:
    if type_webhook == "incomingMessageReceived":
        chat_id = body["senderData"]["chatId"]
        msg = body["messageData"]
        if msg.get("typeMessage") == "textMessage":
            text = msg["textMessageData"]["textMessage"]
            print(chat_id, text)


# Blocks; Ctrl+C to stop. Internally: receiveNotification → handler → deleteNotification
greenAPI.webhooks.startReceivingNotifications(on_event)
```

Handler signature is fixed: `(typeWebhook: str, body: dict)`.
After handling, the SDK deletes the notification by `receiptId` (do not skip this
if you poll manually).

Manual poll loop:

```python
resp = greenAPI.receiving.receiveNotification(receiveTimeout=5)
if resp.code == 200 and resp.data:
    receipt_id = resp.data["receiptId"]
    body = resp.data["body"]
    # ... process body["typeWebhook"] ...
    greenAPI.receiving.deleteNotification(receipt_id)
```

`receiveTimeout`: 5–60 seconds (API default 5). Empty queue → empty body / no data.
Notifications live in the queue **24 hours**, FIFO.

### 5. Receive notifications — webhook endpoint (your HTTP server)

Docs: https://green-api.com/en/docs/api/receiving/technology-webhook-endpoint/

This SDK does **not** ship a webhook HTTP server. Configure the instance, then run your
own endpoint that accepts POST JSON and returns 200:

```python
greenAPI.account.setSettings({
    "webhookUrl": "https://your.public.host/webhook",
    "webhookUrlToken": "Bearer your-secret",  # optional; see docs for Basic/Bearer
    "incomingWebhook": "yes",
    "outgoingWebhook": "yes",
    "outgoingAPIMessageWebhook": "yes",
    "stateWebhook": "yes",
})
```

GREEN-API POSTs notification JSON to `webhookUrl`. Retries every ~1 minute; guaranteed
within 24 hours. While `webhookUrl` is set, **polling will not receive** those notifications.

Common `typeWebhook` values: `incomingMessageReceived`, `outgoingMessageReceived`,
`outgoingAPIMessageReceived`, `outgoingMessageStatus`, `stateInstanceChanged`,
`statusInstanceChanged`, `incomingCall`, `outgoingCall`, `quotaExceeded`, …
Full list: https://green-api.com/en/docs/api/receiving/notifications-format/type-webhook/

### 6. Create a group and message it

Docs: https://green-api.com/en/docs/api/groups/CreateGroup/

```python
created = greenAPI.groups.createGroup("Group Name", ["79876543210@c.us"])
if created.code == 200 and created.data.get("created"):
    chat_id = created.data["chatId"]  # ...@g.us
    greenAPI.sending.sendMessage(chat_id, "Hello group")
```

Do not create groups faster than about **1 per 5 minutes** (anti-spam). Invalid numbers
can get the sender blocked.

## API surface map (SDK attributes)

Access as `greenAPI.<group>.<method>(...)`.

| Attribute | Class | Reference |
| --- | --- | --- |
| `account` | `Account` | [references/account.md](references/account.md) |
| `sending` | `Sending` | [references/sending.md](references/sending.md) |
| `receiving` | `Receiving` | [references/receiving.md](references/receiving.md) |
| `webhooks` | `Webhooks` | [references/receiving.md](references/receiving.md) |
| `groups` | `Groups` | [references/groups.md](references/groups.md) |
| `journals` | `Journals` | [references/journals.md](references/journals.md) |
| `queues` | `Queues` | [references/queues.md](references/queues.md) |
| `serviceMethods` | `ServiceMethods` | [references/service-methods.md](references/service-methods.md) |
| `marking` | `Marking` | [references/marking.md](references/marking.md) |
| `contacts` | `Contacts` | [references/contacts.md](references/contacts.md) |
| `statuses` | `Statuses` | [references/statuses.md](references/statuses.md) |
| `device` | `Device` | [references/device.md](references/device.md) |
| `partner` | `Partner` | only on `GreenApiPartner` — [references/partner.md](references/partner.md) |

Full method list + signatures: [references/inventory.md](references/inventory.md).

## Pitfalls (read before coding)

1. **`chatId` format** — personal `phone@c.us`, group `id@g.us`. No `+` in the phone part.
2. **Authorized instance** — `getStateInstance` must be `authorized` for delivery.
3. **Polling vs webhook** — mutually exclusive for the same traffic: clear `webhookUrl`
   for HTTP API polling; set `webhookUrl` for push.
4. **Always `deleteNotification`** after processing a polled notification, or the same
   event will be returned forever.
5. **Sending delay** — use `delaySendMessagesMilliseconds` ≥ 500 ms; bulk blasts without
   delay risk limits / bans.
6. **File size** — max 100 MB; `sendFileByUpload` goes to `media.green-api.com`.
7. **Response handling** — use `response.data` only when `response.code == 200`.
8. **Deprecated sending APIs** still in SDK but marked deprecated: `sendButtons`,
   `sendTemplateButtons`, `sendListMessage`, `sendLink` — prefer
   `sendInteractiveButtons` / `sendInteractiveButtonsReply` / `sendMessage`.
9. **`serviceMethods` attribute name** — camelCase `serviceMethods`, not `service`.
10. **Partner methods** require `GreenApiPartner`, not `GreenAPI`.
11. **Groups rate limit** — create groups slowly; non-existent numbers are dangerous.
12. **Hosts** — default `api.green-api.com` / `media.green-api.com`; some accounts use
    instance-specific hosts from console — pass `host=` / `media=` if console shows them.

## Agent checklist

When writing code for the user:

- [ ] Import `from whatsapp_api_client_python import API`
- [ ] Init `API.GreenAPI(idInstance, apiTokenInstance)` with real or env credentials
- [ ] Use only methods from [references/inventory.md](references/inventory.md)
- [ ] Format `chatId` as `@c.us` / `@g.us`
- [ ] Check `response.code` before `response.data`
- [ ] For receive: either polling (`startReceivingNotifications` / manual receive+delete)
      or webhook endpoint + `setSettings`, not a fictional SDK method
- [ ] Prefer reading the matching `references/*.md` file for parameters before coding
- [ ] Prefer official docs URL from the method docstring when unsure about edge cases
