# Receiving notifications

Index: https://green-api.com/en/docs/api/receiving/

Two technologies:

1. **HTTP API polling** — `receiveNotification` + `deleteNotification` (this SDK helps).
2. **Webhook Endpoint** — GREEN-API POSTs to your public URL (configure via `setSettings`;
   implement the HTTP server yourself).

They are alternatives for the same instance: if `webhookUrl` is set, polling returns an
error that a custom webhook URL is configured.

## `receiving.receiveNotification`

Docs: https://green-api.com/en/docs/api/receiving/technology-http-api/ReceiveNotification/

| Param | Required | Notes |
| --- | --- | --- |
| `receiveTimeout` | no | 5–60 seconds; default 5 |

Waits up to timeout for one notification. Empty queue → empty/`null` body.

Success shape:

```json
{
  "receiptId": 1234567,
  "body": {
    "typeWebhook": "incomingMessageReceived",
    "instanceData": {},
    "timestamp": 1588091580,
    "idMessage": "...",
    "senderData": { "chatId": "...", "sender": "...", "senderName": "..." },
    "messageData": { "typeMessage": "textMessage", "textMessageData": { "textMessage": "..." } }
  }
}
```

## `receiving.deleteNotification`

Docs: https://green-api.com/en/docs/api/receiving/technology-http-api/DeleteNotification/

Required: `receiptId` (int) from the previous receive. **Must** call after processing,
or the queue will not advance.

## `receiving.downloadFile`

Docs: https://green-api.com/en/docs/api/receiving/files/DownloadFile/

Required: `chatId`, `idMessage`. Downloads media for a message the system knows about.

## `webhooks.startReceivingNotifications`

SDK helper (not a REST method). Implements the recommended poll loop:

1. `receiveNotification`
2. if data: call `onEvent(typeWebhook, body)`
3. `deleteNotification(receiptId)`
4. repeat until `stopReceivingNotifications` or Ctrl+C

```python
def on_event(type_webhook: str, body: dict) -> None:
    if type_webhook == "incomingMessageReceived":
        ...

greenAPI.webhooks.startReceivingNotifications(on_event)
```

Async: `await greenAPI.webhooks.startReceivingNotificationsAsync(on_event)`.

Deprecated: `webhooks.started`, `webhooks.job`.

## Webhook endpoint (no SDK server)

Docs: https://green-api.com/en/docs/api/receiving/technology-webhook-endpoint/

```python
greenAPI.account.setSettings({
    "webhookUrl": "https://example.com/green-api/webhook",
    "webhookUrlToken": "Bearer secret",
    "incomingWebhook": "yes",
    "outgoingWebhook": "yes",
    "outgoingAPIMessageWebhook": "yes",
    "stateWebhook": "yes",
    "incomingCallWebhook": "yes",
})
```

- Endpoint must be public and answer **200**.
- Retries ~every 1 minute; delivery guaranteed **24 hours**.
- If `webhookUrlToken` set, expect `Authorization` header (`Bearer` default, or `Basic`).
- To go back to polling: set `webhookUrl` to `""`.

## Notification types (`typeWebhook`)

Docs: https://green-api.com/en/docs/api/receiving/notifications-format/type-webhook/

| typeWebhook | Meaning |
| --- | --- |
| `incomingMessageReceived` | Incoming message/file |
| `outgoingMessageReceived` | Message sent from phone |
| `outgoingAPIMessageReceived` | Message sent via API |
| `outgoingMessageStatus` | Delivery/read status |
| `stateInstanceChanged` | Auth state change |
| `statusInstanceChanged` | Socket status |
| `deviceInfo` | Device/battery (archive / may be off) |
| `incomingCall` / `outgoingCall` | Calls |
| `incomingBlock` | Block events |
| `quotaExceeded` | Developer plan limits |

Enable categories via `setSettings` flags: `incomingWebhook`, `outgoingWebhook`,
`outgoingMessageWebhook`, `outgoingAPIMessageWebhook`, `stateWebhook`,
`incomingCallWebhook`, `pollMessageWebhook`, `editedMessageWebhook`,
`deletedMessageWebhook`, etc.  
Docs: https://green-api.com/en/docs/api/account/SetSettings/

Message payload formats: https://green-api.com/en/docs/api/receiving/notifications-format/

### Extracting text from `incomingMessageReceived`

```python
md = body["messageData"]
t = md.get("typeMessage")
if t == "textMessage":
    text = md["textMessageData"]["textMessage"]
elif t == "extendedTextMessage":
    text = md["extendedTextMessageData"]["text"]
# media types: imageMessage, videoMessage, documentMessage, ... see docs
```
