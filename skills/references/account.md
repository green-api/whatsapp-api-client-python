# Account (`greenAPI.account`)

Class: `Account` in `tools/account.py`.  
Index: https://green-api.com/en/docs/api/account/

## `getSettings` / `setSettings`

- Get: https://green-api.com/en/docs/api/account/GetSettings/
- Set: https://green-api.com/en/docs/api/account/SetSettings/

`setSettings(requestBody: dict)` — pass only fields to change. **Reboots instance**;
settings apply within ~5 minutes. Defaults after create: webhooks off.

Important keys (docs):

| Key | Values / notes |
| --- | --- |
| `webhookUrl` | URL or `""` to disable push / enable polling |
| `webhookUrlToken` | optional auth token for your server |
| `delaySendMessagesMilliseconds` | 500–600000; recommend ≤ 300000 |
| `incomingWebhook` | `yes` / `no` |
| `outgoingWebhook` | `yes` / `no` (statuses) |
| `outgoingMessageWebhook` | phone-sent messages |
| `outgoingAPIMessageWebhook` | API-sent messages |
| `stateWebhook` | auth state changes |
| `incomingCallWebhook` | calls |
| `pollMessageWebhook` | polls |
| `editedMessageWebhook` / `deletedMessageWebhook` | edits/deletes |
| `markIncomingMessagesReaded` | `yes` / `no` |
| `keepOnlineStatus` | keep online when phone off |
| `linkPreview` | `yes` / `no` |
| `autoTyping` | 0–10 typing speed preset |
| `enableLidMode` | work with `@lid` chatIds |

```python
greenAPI.account.setSettings({
    "delaySendMessagesMilliseconds": 5000,
    "incomingWebhook": "yes",
    "webhookUrl": "",
})
```

## `getStateInstance`

Docs: https://green-api.com/en/docs/api/account/GetStateInstance/

Returns `{ "stateInstance": "..." }`:

| State | Meaning |
| --- | --- |
| `authorized` | ready |
| `notAuthorized` | scan QR / auth code |
| `blocked` | banned |
| `starting` | booting (wait) |
| `suspended` | temporary restrictions |
| `sleepMode` | outdated status |
| `yellowCard` | deprecated → use `suspended` |

## `getStatusInstance`

Docs: https://green-api.com/en/docs/api/account/GetStatusInstance/  
Socket connection status with WhatsApp (archive section in docs).

## `getWaSettings`

Docs: https://green-api.com/en/docs/api/account/GetWaSettings/  
WhatsApp account information for the linked number.

## `qr`

Docs: https://green-api.com/en/docs/api/account/QR/  
Returns QR payload for authorization.

## `getAuthorizationCode`

Docs: https://green-api.com/en/docs/api/account/GetAuthorizationCode/  
`phoneNumber: int` — link by phone number (international digits).

## `reboot` / `logout`

- https://green-api.com/en/docs/api/account/Reboot/
- https://green-api.com/en/docs/api/account/Logout/

## `setProfilePicture`

Docs: https://green-api.com/en/docs/api/account/SetProfilePicture/  
SDK: `setProfilePicture(path)` local image path.

## `getStateInstanceHistory`

Docs: https://green-api.com/en/docs/api/account/GetStateInstanceHistory/  
Optional query `count`.

## `updateApiToken`

Docs: https://green-api.com/en/docs/api/account/UpdateApiToken/  
Generates a new `apiTokenInstance` — store the new token after success.
