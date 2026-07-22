# Sending (`greenAPI.sending`)

Class: `Sending` in `tools/sending.py`.  
Index: https://green-api.com/en/docs/api/sending/

All send methods enqueue messages. Queue retention **24 hours**. Rate controlled by
`delaySendMessagesMilliseconds` — https://green-api.com/en/docs/api/send-messages-delay/

Typical success body: `{ "idMessage": "..." }` (upload also returns `urlFile`).

## `sendMessage`

Docs: https://green-api.com/en/docs/api/sending/SendMessage/

| Param | Required | Notes |
| --- | --- | --- |
| `chatId` | yes | `@c.us` / `@g.us` |
| `message` | yes | max 20000 chars, UTF-8 |
| `quotedMessageId` | no | same chat only |
| `linkPreview` | no | bool; default on server |
| `typePreview` | no | `large` / `small` |
| `customPreview` | no | object: title, description, link, urlFile, jpegThumbnail |
| `typingTime` | no | 1000–20000 ms |
| `archiveChat` | no | SDK optional (if supported by account) |

```python
greenAPI.sending.sendMessage("79876543210@c.us", "Hello")
await greenAPI.sending.sendMessageAsync("79876543210@c.us", "Hello")
```

## `sendFileByUrl`

Docs: https://green-api.com/en/docs/api/sending/SendFileByUrl/

| Param | Required | Notes |
| --- | --- | --- |
| `chatId` | yes | |
| `urlFile` | yes | direct file URL, `http(s)://` |
| `fileName` | yes | **with extension** |
| `caption` | no | max 1024 |
| `quotedMessageId` | no | |
| `typingTime` / `typingType` | no | `typingType="recording"` for audio |
| `archiveChat` | no | |

Max file size **100 MB**. One file per request.

## `sendFileByUpload`

Docs: https://green-api.com/en/docs/api/sending/SendFileByUpload/

Uses **media** host. SDK: second arg is filesystem `path`.

| Param | Required | Notes |
| --- | --- | --- |
| `chatId` | yes | |
| `path` | yes | local file path (SDK-only name; becomes form file) |
| `fileName` | no | with extension |
| `caption` | no | max 1024 |
| `quotedMessageId`, `typingTime`, `typingType` | no | |

Response: `idMessage`, `urlFile` (link ~15 days).

## `uploadFile`

Docs: https://green-api.com/en/docs/api/sending/UploadFile/

Upload to cloud storage; then send with `sendFileByUrl` using returned URL.

```python
up = greenAPI.sending.uploadFile("data/logo.jpg")
# then sendFileByUrl(..., urlFile=up.data["urlFile"], fileName="logo.jpg")
```

## `sendLocation`

Docs: https://green-api.com/en/docs/api/sending/SendLocation/

Required: `chatId`, `latitude`, `longitude`. Optional: `nameLocation`, `address`,
`quotedMessageId`, `typingTime`.

## `sendContact`

Docs: https://green-api.com/en/docs/api/sending/SendContact/

Required: `chatId`, `contact` dict (fields per docs: phoneContact, firstName, …).

## `forwardMessages`

Docs: https://green-api.com/en/docs/api/sending/ForwardMessages/

Required: `chatId` (destination), `chatIdFrom` (source), `messages` (list of idMessage).

## `sendPoll`

Docs: https://green-api.com/en/docs/api/sending/SendPoll/

```python
greenAPI.sending.sendPoll(
    "79876543210@c.us",
    "Choose a color:",
    [{"optionName": "Red"}, {"optionName": "Green"}, {"optionName": "Blue"}],
    multipleAnswers=False,
)
```

## `sendInteractiveButtons` / `sendInteractiveButtonsReply`

Docs:

- https://green-api.com/en/docs/api/sending/SendInteractiveButtons/
- https://green-api.com/en/docs/api/sending/SendInteractiveButtonsReply/

SDK params: `chatId`, `body`, `buttons`, optional `header`, `footer`, `typingTime`.
Prefer these over deprecated `sendButtons` / `sendTemplateButtons` / `sendListMessage`.

## Deprecated (still in SDK)

Do not use in new code unless the user explicitly asks:

- `sendButtons` → use `sendInteractiveButtons`
- `sendTemplateButtons` → use `sendInteractiveButtonsReply`
- `sendListMessage` → use `sendMessage` / interactive methods
- `sendLink` → use `sendMessage` with `linkPreview`
