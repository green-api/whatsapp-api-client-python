# Service methods (`greenAPI.serviceMethods`)

Class: `ServiceMethods` in `tools/serviceMethods.py`.  
Attribute name is **`serviceMethods`** (camelCase), not `service`.  
Index: https://green-api.com/en/docs/api/service/

## `checkWhatsapp`

Docs: https://green-api.com/en/docs/api/service/CheckWhatsapp/

Pass **either** `chatId` **or** `phoneNumber` (not both). Prefer `chatId`.

| Param | Notes |
| --- | --- |
| `chatId` | e.g. `79001234567@c.us` or `@lid` |
| `phoneNumber` | int, 11–16 digits; deprecated but still in SDK |
| `force` | bool; refresh from WhatsApp, not cache |

Response includes `existsWhatsapp`, `chatId`, `fromCache`.

```python
greenAPI.serviceMethods.checkWhatsapp(chatId="79876543210@c.us")
```

## Contacts list / info / avatar

| Method | Params | Docs |
| --- | --- | --- |
| `getAvatar` | `chatId` | https://green-api.com/en/docs/api/service/GetAvatar/ |
| `getContacts` | optional `group`, `count` (query) | https://green-api.com/en/docs/api/service/GetContacts/ |
| `getContactInfo` | `chatId` | https://green-api.com/en/docs/api/service/GetContactInfo/ |
| `getChats` | optional `count` | https://green-api.com/en/docs/api/service/GetChats/ |

## Messages

| Method | Params | Docs |
| --- | --- | --- |
| `deleteMessage` | `chatId`, `idMessage`, optional `onlySenderDelete` | https://green-api.com/en/docs/api/service/deleteMessage/ |
| `editMessage` | `chatId`, `idMessage`, `message` | https://green-api.com/en/docs/api/service/editMessage/ |

## Chats

| Method | Params | Docs |
| --- | --- | --- |
| `archiveChat` | `chatId` | https://green-api.com/en/docs/api/service/archiveChat/ |
| `unarchiveChat` | `chatId` | https://green-api.com/en/docs/api/service/unarchiveChat/ |
| `setDisappearingChat` | `chatId`, optional `ephemeralExpiration` | https://green-api.com/en/docs/api/service/SetDisappearingChat/ |
| `sendTyping` | `chatId`, optional `typingTime`, `typingType` | https://green-api.com/en/docs/api/service/SendTyping/ |

`typingType`: use `"recording"` for audio recording indicator (per SendTyping docs).
