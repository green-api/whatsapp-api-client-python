# SDK method inventory

Source of names/signatures: `whatsapp_api_client_python/` in package
`whatsapp-api-client-python`. Every entry below was taken from the Python source.
Async twins (`methodAsync`) exist where noted; signatures match the sync form.

Official semantics: https://green-api.com/en/docs/api/

## Clients (`API.py`)

| Class | Init | Notes |
| --- | --- | --- |
| `GreenApi` / `GreenAPI` | `(idInstance, apiTokenInstance, debug_mode=False, raise_errors=False, host=..., media=..., host_timeout=180, media_timeout=10800)` | Main client |
| `GreenApiPartner` | `(partnerToken, email=None, host=...)` | Partner API; exposes `.partner` |
| `GreenAPIError` | Exception | Raised when `raise_errors=True` |

Response: `response.Response` → `.code`, `.data`, `.error`.

## `account` → `Account`

| Method | Params | Docs |
| --- | --- | --- |
| `getSettings` | — | https://green-api.com/en/docs/api/account/GetSettings/ |
| `getWaSettings` | — | https://green-api.com/en/docs/api/account/GetWaSettings/ |
| `setSettings` | `requestBody: Dict` | https://green-api.com/en/docs/api/account/SetSettings/ |
| `getStateInstance` | — | https://green-api.com/en/docs/api/account/GetStateInstance/ |
| `getStatusInstance` | — | https://green-api.com/en/docs/api/account/GetStatusInstance/ |
| `reboot` | — | https://green-api.com/en/docs/api/account/Reboot/ |
| `logout` | — | https://green-api.com/en/docs/api/account/Logout/ |
| `qr` | — | https://green-api.com/en/docs/api/account/QR/ |
| `setProfilePicture` | `path: str` | https://green-api.com/en/docs/api/account/SetProfilePicture/ |
| `getAuthorizationCode` | `phoneNumber: int` | https://green-api.com/en/docs/api/account/GetAuthorizationCode/ |
| `getStateInstanceHistory` | `count: Optional[int]=None` | https://green-api.com/en/docs/api/account/GetStateInstanceHistory/ |
| `updateApiToken` | — | https://green-api.com/en/docs/api/account/UpdateApiToken/ |

Async: `getSettingsAsync`, `getWaSettingsAsync`, `setSettingsAsync`, `getStateInstanceAsync`, `rebootAsync`, `logoutAsync`, `qrAsync`, `setProfilePictureAsync`, `getAuthorizationCodeAsync`, `getStateInstanceHistoryAsync`, `updateApiTokenAsync`.  
No async for `getStatusInstance` in current source.

## `sending` → `Sending`

| Method | Params | Docs | Notes |
| --- | --- | --- | --- |
| `sendMessage` | `chatId, message, quotedMessageId=None, archiveChat=None, linkPreview=None, typingTime=None, typePreview=None, customPreview=None` | https://green-api.com/en/docs/api/sending/SendMessage/ | |
| `sendButtons` | `chatId, message, buttons, footer=None, quotedMessageId=None, archiveChat=None` | https://green-api.com/en/docs/api/sending/SendButtons/ | **Deprecated** → interactive buttons |
| `sendTemplateButtons` | `chatId, message, templateButtons, footer=None, quotedMessageId=None, archiveChat=None` | https://green-api.com/en/docs/api/sending/SendTemplateButtons/ | **Deprecated** |
| `sendListMessage` | `chatId, message, buttonText, sections, title=None, footer=None, quotedMessageId=None, archiveChat=None` | https://green-api.com/en/docs/api/sending/SendListMessage/ | **Deprecated** |
| `sendFileByUpload` | `chatId, path, fileName=None, caption=None, quotedMessageId=None, typingTime=None, typingType=None` | https://green-api.com/en/docs/api/sending/SendFileByUpload/ | media host |
| `sendFileByUrl` | `chatId, urlFile, fileName, caption=None, quotedMessageId=None, archiveChat=None, typingTime=None, typingType=None` | https://green-api.com/en/docs/api/sending/SendFileByUrl/ | |
| `uploadFile` | `path: str` | https://green-api.com/en/docs/api/sending/UploadFile/ | media host |
| `sendLocation` | `chatId, latitude, longitude, nameLocation=None, address=None, quotedMessageId=None, typingTime=None` | https://green-api.com/en/docs/api/sending/SendLocation/ | |
| `sendContact` | `chatId, contact: Dict, quotedMessageId=None, typingTime=None` | https://green-api.com/en/docs/api/sending/SendContact/ | |
| `sendLink` | `chatId, urlLink, quotedMessageId=None` | https://green-api.com/en/docs/api/sending/SendLink/ | **Deprecated** → `sendMessage` |
| `forwardMessages` | `chatId, chatIdFrom, messages: List[str], typingTime=None` | https://green-api.com/en/docs/api/sending/ForwardMessages/ | |
| `sendPoll` | `chatId, message, options: List[Dict], multipleAnswers=None, quotedMessageId=None, typingTime=None` | https://green-api.com/en/docs/api/sending/SendPoll/ | |
| `sendInteractiveButtons` | `chatId, body, buttons, header=None, footer=None, typingTime=None` | https://green-api.com/en/docs/api/sending/SendInteractiveButtons/ | |
| `sendInteractiveButtonsReply` | `chatId, body, buttons, header=None, footer=None, typingTime=None` | https://green-api.com/en/docs/api/sending/SendInteractiveButtonsReply/ | |

Async for non-deprecated (and most others): `sendMessageAsync`, `sendFileByUploadAsync`, `sendFileByUrlAsync`, `uploadFileAsync`, `sendLocationAsync`, `sendContactAsync`, `forwardMessagesAsync`, `sendPollAsync`, `sendInteractiveButtonsAsync`, `sendInteractiveButtonsReplyAsync`.  
No async variants for `sendButtons`, `sendTemplateButtons`, `sendListMessage`, `sendLink` in current source.

## `receiving` → `Receiving`

| Method | Params | Docs |
| --- | --- | --- |
| `receiveNotification` | `receiveTimeout: Optional[int]=None` | https://green-api.com/en/docs/api/receiving/technology-http-api/ReceiveNotification/ |
| `deleteNotification` | `receiptId: int` | https://green-api.com/en/docs/api/receiving/technology-http-api/DeleteNotification/ |
| `downloadFile` | `chatId, idMessage` | https://green-api.com/en/docs/api/receiving/files/DownloadFile/ |

Async: `receiveNotificationAsync`, `deleteNotificationAsync`, `downloadFileAsync`.

## `webhooks` → `Webhooks`

| Method | Params | Notes |
| --- | --- | --- |
| `startReceivingNotifications` | `onEvent: Callable[[str, dict], Any]` | Polling loop; blocks |
| `startReceivingNotificationsAsync` | `onEvent` | Async polling |
| `stopReceivingNotifications` | — | Stop loop |
| `stopReceivingNotificationsAsync` | — | |
| `started` (property) | — | **Deprecated** |
| `job` | `onEvent` | **Deprecated** |

## `groups` → `Groups`

| Method | Params | Docs |
| --- | --- | --- |
| `createGroup` | `groupName, chatIds: List[str]` | https://green-api.com/en/docs/api/groups/CreateGroup/ |
| `updateGroupName` | `groupId, groupName` | https://green-api.com/en/docs/api/groups/UpdateGroupName/ |
| `getGroupData` | `groupId` | https://green-api.com/en/docs/api/groups/GetGroupData/ |
| `addGroupParticipant` | `groupId, participantChatId` | https://green-api.com/en/docs/api/groups/AddGroupParticipant/ |
| `removeGroupParticipant` | `groupId, participantChatId` | https://green-api.com/en/docs/api/groups/RemoveGroupParticipant/ |
| `setGroupAdmin` | `groupId, participantChatId` | https://green-api.com/en/docs/api/groups/SetGroupAdmin/ |
| `removeAdmin` | `groupId, participantChatId` | https://green-api.com/en/docs/api/groups/RemoveAdmin/ |
| `setGroupPicture` | `groupId, path` | https://green-api.com/en/docs/api/groups/SetGroupPicture/ |
| `leaveGroup` | `groupId` | https://green-api.com/en/docs/api/groups/LeaveGroup/ |
| `updateGroupSettings` | `groupId, allowParticipantsEditGroupSettings=None, allowParticipantsSendMessages=None` | https://green-api.com/en/docs/api/groups/UpdateGroupSettings/ |

All have `*Async` twins.

## `journals` → `Journals`

| Method | Params | Docs |
| --- | --- | --- |
| `getChatHistory` | `chatId, count=None` | https://green-api.com/en/docs/api/journals/GetChatHistory/ |
| `getMessage` | `chatId, idMessage` | https://green-api.com/en/docs/api/journals/GetMessage/ |
| `lastIncomingMessages` | `minutes=None` | https://green-api.com/en/docs/api/journals/LastIncomingMessages/ |
| `lastOutgoingMessages` | `minutes=None` | https://green-api.com/en/docs/api/journals/LastOutgoingMessages/ |
| `lastIncomingCalls` | `minutes=None` | https://green-api.com/en/docs/api/journals/LastIncomingCalls/ |
| `lastOutgoingCalls` | `minutes=None` | https://green-api.com/en/docs/api/journals/LastOutgoingCalls/ |

All have `*Async` twins.

## `queues` → `Queues`

| Method | Params | Docs |
| --- | --- | --- |
| `showMessagesQueue` | — | https://green-api.com/en/docs/api/queues/ShowMessagesQueue/ |
| `clearMessagesQueue` | — | https://green-api.com/en/docs/api/queues/ClearMessagesQueue/ |
| `getMessagesCount` | — | https://green-api.com/en/docs/api/queues/GetMessagesCount/ |
| `getWebhooksCount` | — | https://green-api.com/en/docs/api/queues/GetWebhooksCount/ |
| `clearWebhooksQueue` | — | https://green-api.com/en/docs/api/queues/ClearWebhooksQueue/ |

All have `*Async` twins.

## `serviceMethods` → `ServiceMethods`

| Method | Params | Docs |
| --- | --- | --- |
| `checkWhatsapp` | `phoneNumber=None, chatId=None, force=None` | https://green-api.com/en/docs/api/service/CheckWhatsapp/ |
| `getAvatar` | `chatId` | https://green-api.com/en/docs/api/service/GetAvatar/ |
| `getContacts` | `group=None, count=None` | https://green-api.com/en/docs/api/service/GetContacts/ |
| `getContactInfo` | `chatId` | https://green-api.com/en/docs/api/service/GetContactInfo/ |
| `deleteMessage` | `chatId, idMessage, onlySenderDelete=None` | https://green-api.com/en/docs/api/service/deleteMessage/ |
| `editMessage` | `chatId, idMessage, message` | https://green-api.com/en/docs/api/service/editMessage/ |
| `archiveChat` | `chatId` | https://green-api.com/en/docs/api/service/archiveChat/ |
| `unarchiveChat` | `chatId` | https://green-api.com/en/docs/api/service/unarchiveChat/ |
| `setDisappearingChat` | `chatId, ephemeralExpiration=None` | https://green-api.com/en/docs/api/service/SetDisappearingChat/ |
| `sendTyping` | `chatId, typingTime=None, typingType=None` | https://green-api.com/en/docs/api/service/SendTyping/ |
| `getChats` | `count=None` | https://green-api.com/en/docs/api/service/GetChats/ |

All have `*Async` twins.

## `marking` → `Marking`

| Method | Params | Docs |
| --- | --- | --- |
| `readChat` | `chatId, idMessage=None` | https://green-api.com/en/docs/api/marks/ReadChat/ |

Async: `readChatAsync`.

## `contacts` → `Contacts`

| Method | Params | Docs |
| --- | --- | --- |
| `addContact` | `chatId, firstName, lastName=None, saveInAddressbook=True` | https://green-api.com/en/docs/api/contacts/AddContact/ |
| `editContact` | `chatId, firstName, lastName=None, saveInAddressbook=True` | https://green-api.com/en/docs/api/contacts/EditContact/ |
| `deleteContact` | `chatId` | https://green-api.com/en/docs/api/contacts/DeleteContact/ |

All have `*Async` twins.

## `statuses` → `Statuses`

| Method | Params | Docs |
| --- | --- | --- |
| `sendTextStatus` | `message, backgroundColor=None, font=None, participants=None` | https://green-api.com/en/docs/api/statuses/SendTextStatus/ |
| `sendVoiceStatus` | `urlFile, fileName, backgroundColor=None, participants=None` | https://green-api.com/en/docs/api/statuses/SendVoiceStatus/ |
| `sendMediaStatus` | `urlFile, fileName, caption=None, participants=None` | https://green-api.com/en/docs/api/statuses/SendMediaStatus/ |
| `deleteStatus` | `idMessage` | https://green-api.com/en/docs/api/statuses/DeleteStatus/ |
| `getStatusStatistic` | `idMessage` | https://green-api.com/en/docs/api/statuses/GetStatusStatistic/ |
| `getIncomingStatuses` | `minutes=None` | https://green-api.com/en/docs/api/statuses/GetIncomingStatuses/ |
| `getOutgoingStatuses` | `minutes=None` | https://green-api.com/en/docs/api/statuses/GetOutgoingStatuses/ |

All have `*Async` twins.

## `device` → `Device`

| Method | Params | Docs | Notes |
| --- | --- | --- | --- |
| `getDeviceInfo` | — | https://green-api.com/en/docs/api/phone/GetDeviceInfo/ | **Deprecated** |

No async twin in current source.

## `partner` → `Partner` (on `GreenApiPartner` only)

| Method | Params | Docs |
| --- | --- | --- |
| `getInstances` | — | https://green-api.com/en/docs/partners/getInstances/ |
| `createInstance` | `requestBody: Dict` | https://green-api.com/en/docs/partners/createInstance/ |
| `deleteInstanceAccount` | `idInstance: int` | https://green-api.com/en/docs/partners/deleteInstanceAccount/ |

All have `*Async` twins.

## Not in this SDK (do not invent)

Examples of API areas that may exist in docs but are **not** wrapped here unless listed above: catalogs product methods, websocket QR scan, etc. Check inventory before coding.
