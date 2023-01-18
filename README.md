# whatsapp-api-client-python

[![Python application](https://github.com/green-api/whatsapp-api-client-python/actions/workflows/python-app.yml/badge.svg)](https://github.com/green-api/whatsapp-api-client-python/actions/workflows/python-app.yml)
[![Upload Python Package](https://github.com/green-api/whatsapp-api-client-python/actions/workflows/python-publish.yml/badge.svg)](https://github.com/green-api/whatsapp-api-client-python/actions/workflows/python-publish.yml)

- [Документация на русском языке](README_RUS.md)

Python library for intagration with WhatsAPP messanger via API of [green-api.com](https://green-api.com) service. To use the library you have to get a registration token and an account id in the [personal area](https://console.green-api.com). There is a free developer account tariff plan.

## API

You can find REST API documentation by [url](https://green-api.com/docs/api/). The library is a wrapper for REST API, so the documentation at the above url applies to the library as well.

## Installation

```shell
pip install whatsapp-api-client-python
```

## Import 

```
from whatsapp_api_client_python import API
```
## Authorization

To send a message or to exacute some other Green-API method, you have to have the WhatsApp account in the phone application to be authorized. To authorize your account please go to the [personal area](https://console.green-api.com) and scan a QR-code using the WhatsApp application.

## Examples

### How to initialize an object

```python
greenAPI = API.GreenApi(ID_INSTANCE, API_TOKEN_INSTANCE)
```

### Sending a text message to a WhatsApp number

```python
result = greenAPI.sending.sendMessage('79001234567@g.us', 'Message text')
```

Example url: [sendTextMessage.py](https://github.com/green-api/whatsapp-api-client-python/blob/master/examples/sendTextMessage.py)

Please note that keys can be obtained from environment variables:
```python
from os import environ

ID_INSTANCE = environ['ID_INSTANCE']
API_TOKEN_INSTANCE = environ['API_TOKEN_INSTANCE']
```

### Sending an image via URL

```python
result = greenAPI.sending.sendFileByUrl('120363025955348359@g.us', 
        'https://www.google.ru/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png', 
        'googlelogo_color_272x92dp.png', 'Google logo')
```

Example url: [sendPictureByLink.py](https://github.com/green-api/whatsapp-api-client-python/blob/master/examples/sendPictureByLink.py)

### Sending an image by uploading from the disk

```python
result = greenAPI.sending.sendFileByUpload('120363025955348359@g.us', 
        'C:\Games\PicFromDisk.png', 
        'PicFromDisk.png', 'Picture from disk')
```

Example url: [sendPictureByUpload.py](https://github.com/green-api/whatsapp-api-client-python/blob/master/examples/sendPictureByUpload.py)

### Group creation and sending a message to the group

```python
chatIds = [
    "79001234567@c.us"
]
resultCreate = greenAPI.groups.createGroup('GroupName', 
    chatIds)

if resultCreate.code == 200:
    resultSend = greenAPI.sending.sendMessage(resultCreate.data['chatId'], 
        'Message text')
```

IMPORTANT: If one tries to create a group with a non-existent number, WhatsApp 
may block the sender's number. The number in the example is non-existent.

Example url: [createGroupAndSendMessage.py](https://github.com/green-api/whatsapp-api-client-python/blob/master/examples/createGroupAndSendMessage.py)

### Receive incoming messages by HTTP API

The general concept of receiving data in the Green API is described [here](https://green-api.com/en/docs/api/receiving/)
To start receiving messages by the HTTP API you need to execute the library method:

```python
greenAPI.webhooks.startReceivingNotifications(onEvent)
```

onEvent - your method which should contain parameters:
Parameter | Description
----- | -----
typewebhook | received message type (string)
body | message body (json)

Message body types and formats [here](https://green-api.com/en/docs/api/receiving/notifications-format/)

This method will be called when an incoming message is received. Next, process messages according to the business logic of your system.

## Examples list

Description |  Module
----- | ----- 
Example of sending text | [sendTextMessage.py](https://github.com/green-api/whatsapp-api-client-python/blob/master/examples/sendTextMessage.py)
Example of sending a picture by URL | [sendPictureByLink.py](https://github.com/green-api/whatsapp-api-client-python/blob/master/examples/sendPictureByLink.py)
Example of sending a picture by uploading from the disk | [sendPictureByUpload.py](https://github.com/green-api/whatsapp-api-client-python/blob/master/examples/sendPictureByUpload.py)
Example of a group creation and sending a message to the group | [createGroupAndSendMessage.py](https://github.com/green-api/whatsapp-api-client-python/blob/master/examples/createGroupAndSendMessage.py)
Example of incoming webhooks receiving | [receiveNotification.py](https://github.com/green-api/whatsapp-api-client-python/blob/master/examples/receiveNotification.py)


## The full list of the library methods

| Method                                 | Description                                                                                                                                                                                         | Documentation                                                                                                                            |
|----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `account.getSettings`                  | The method is aimed for getting the current settings of the account                                                                                                                                 | [GetSettings.md](https://github.com/green-api/docs/blob/master/ru/docs/api/account/GetSettings.md)                                       |
| `account.getStateInstance`             | The method is aimed for getting the account state                                                                                                                                                   | [GetStateInstance.md](https://github.com/green-api/docs/blob/master/ru/docs/api/account/GetStateInstance.md)                             |
| `account.getStatusInstance`            | The method is aimed for getting the status of the account instance socket connection with WhatsApp                                                                                                  | [GetStatusInstance.md](https://github.com/green-api/docs/blob/master/ru/docs/api/account/GetStatusInstance.md)                           |
| `account.logout`                       | The method is aimed for logging out an account                                                                                                                                                      | [Logout.md](https://github.com/green-api/docs/blob/master/ru/docs/api/account/Logout.md)                                                 |
| `account.qr`                           | The method is aimed for getting QR code                                                                                                                                                             | [QR.md](https://github.com/green-api/docs/blob/master/ru/docs/api/account/QR.md)                                                         |
| `account.reboot`                       | The method is aimed for rebooting an account                                                                                                                                                        | [Reboot.md](https://github.com/green-api/docs/blob/master/ru/docs/api/account/Reboot.md)                                                 |
| `account.setProfilePicture`            | The method is aimed for setting an account picture                                                                                                                                                  | [SetProfilePicture.md](https://github.com/green-api/docs/blob/master/ru/docs/api/account/SetProfilePicture.md)                           |
| `account.setSettings`                  | The method is aimed for setting an account settings                                                                                                                                                 | [SetSettings.md](https://github.com/green-api/docs/blob/master/ru/docs/api/account/SetSettings.md)                                       |
| `account.setSystemProxy`               | The method is aimed for setting a system proxy. Use the method when you need to reset custom proxy settings to system ones                                                                          | [SetSystemProxy.md](https://github.com/green-api/docs/blob/master/ru/docs/api/account/SetSystemProxy.md)                                 |
| `groups.addGroupParticipant`           | Метод добавляет участника в групповой чат                                                                                                                                                           | [AddGroupParticipant.md](https://github.com/green-api/docs/blob/master/ru/docs/api/groups/AddGroupParticipant.md)                        |
| `groups.createGroup`                   | The method adds a participant to a group chat. IMPORTANT: If one tries to create a group with a non-existent number, WhatsApp may block the sender's number.                                        | [CreateGroup.md](https://github.com/green-api/docs/blob/master/ru/docs/api/groups/CreateGroup.md)                                        |
| `groups.getGroupData`                  | The method gets group chat data                                                                                                                                                                     | [GetGroupData.md](https://github.com/green-api/docs/blob/master/ru/docs/api/account/GetGroupData.md)                                     |
| `groups.leaveGroup`                    | The method makes the current account user leave the group chat                                                                                                                                      | [LeaveGroup.md](https://github.com/green-api/docs/blob/master/ru/docs/api/groups/LeaveGroup.md)                                          |
| `groups.removeAdmin`                   | he method removes a participant from group chat administration rights                                                                                                                               | [RemoveAdmin.md](https://github.com/green-api/docs/blob/master/ru/docs/api/groups/RemoveAdmin.md)                                        |
| `groups.removeGroupParticipant`        | The method removes a participant from a group chat                                                                                                                                                  | [RemoveGroupParticipant.md](https://github.com/green-api/docs/blob/master/ru/docs/api/groups/RemoveGroupParticipant.md)                  |
| `groups.setGroupAdmin`                 | The method sets a group chat participant as an administrator                                                                                                                                        | [SetGroupAdmin.md](https://github.com/green-api/docs/blob/master/ru/docs/api/groups/SetGroupAdmin.md)                                    |
| `groups.setGroupPicture`               | The method sets a group picture                                                                                                                                                                     | [SetGroupPicture.md](https://github.com/green-api/docs/blob/master/ru/docs/api/groups/SetGroupPicture.md)                                |
| `groups.updateGroupName`               | The method changes a group chat name                                                                                                                                                                | [UpdateGroupName.md](https://github.com/green-api/docs/blob/master/ru/docs/api/groups/UpdateGroupName.md)                                |
| `journals.getChatHistory`              | The method returns the chat message history                                                                                                                                                         | [GetChatHistory.md](https://github.com/green-api/docs/blob/master/ru/docs/api/journals/GetChatHistory.md)                                |
| `journals.lastIncomingMessages`        | The method returns the last incoming messages of the account. In the default mode the incoming messages for 24 hours are returned                                                                   | [GetChatHistory.md](https://github.com/green-api/docs/blob/master/ru/docs/api/journals/LastIncomingMessages.md)                          |
| `journals.lastOutgoingMessages`        | The method returns the last outgoing messages of the account. In the default mode the last messages for 24 hours are returned                                                                       | [LastOutgoingMessages.md](https://github.com/green-api/docs/blob/master/ru/docs/api/journals/LastOutgoingMessages.md)                    |
| `marking.readChat`                     | The method is aimed for marking messages in a chat as read. Either all messages or a specified message in a chat can be marked as read                                                              | [ReadChat.md](https://github.com/green-api/docs/blob/master/ru/docs/api/marks/ReadChat.md)                                               |
| `device.getDeviceInfo`                 | The method is aimed for getting information about the device (phone) running WhatsApp Business application                                                                                          | [GetDeviceInfo.md](https://github.com/green-api/docs/blob/master/ru/docs/api/phone/GetDeviceInfo.md)                                     |
| `queues.clearMessagesQueue`            | The method is aimed for clearing the queue of messages to be sent                                                                                                                                   | [ClearMessagesQueue.md](https://github.com/green-api/docs/blob/master/ru/docs/api/queues/ClearMessagesQueue.md)                          |
| `queues.showMessagesQueue`             | The method is aimed for getting a list of messages in the queue to be sent                                                                                                                          | [ShowMessagesQueue.md](https://github.com/green-api/docs/blob/master/ru/docs/api/queues/ShowMessagesQueue.md)                            |
| `receiving.deleteNotification`         | The method is aimed for deleting an incoming notification from the notification queue                                                                                                               | [DeleteNotification.md](https://github.com/green-api/docs/blob/master/ru/docs/api/receiving/technology-http-api/DeleteNotification.md)   |
| `receiving.receiveNotification`        | The method is aimed for receiving one incoming notification from the notifications queue                                                                                                            | [ReceiveNotification.md](https://github.com/green-api/docs/blob/master/ru/docs/api/receiving/technology-http-api/ReceiveNotification.md) |
| `sending.sendButtons`                  | The method is aimed for sending a button message to a personal or a group chat                                                                                                                      | [SendButtons.md](https://github.com/green-api/docs/blob/master/ru/docs/api/sending/SendButtons.md)                                       |
| `sending.sendContact`                  | The method is aimed for sending a contact message                                                                                                                                                   | [SendContact.md](https://github.com/green-api/docs/blob/master/ru/docs/api/sending/SendContact.md)                                       |
| `sending.sendFileByUpload`             | The method is aimed for sending a file uploaded by form                                                                                                                                             | [SendFileByUpload.md](https://github.com/green-api/docs/blob/master/ru/docs/api/sending/SendFileByUpload.md)                             |
| `sending.sendFileByUrl`                | The method is aimed for sending a file uploaded by Url                                                                                                                                              | [SendFileByUrl.md](https://github.com/green-api/docs/blob/master/ru/docs/api/sending/SendFileByUrl.md)                                   |
| `sending.sendLink`                     | The method is aimed for sending a message with a link, by which an image preview, title and description will be added                                                                               | [SendLink.md](https://github.com/green-api/docs/blob/master/ru/docs/api/sending/SendLink.md)                                             |
| `sending.sendListMessage`              | The method is aimed for sending a message with a select button from a list of values to a personal or a group chat                                                                                  | [SendListMessage.md](https://github.com/green-api/docs/blob/master/ru/docs/api/sending/SendListMessage.md)                               |
| `sending.sendLocation`                 | The method is aimed for sending a location message                                                                                                                                                  | [SendLocation.md](https://github.com/green-api/docs/blob/master/ru/docs/api/sending/SendLocation.md)                                     |
| `sending.sendMessage`                  | The method is aimed for sending a text message to a personal or a group chat                                                                                                                        | [SendMessage.md](https://github.com/green-api/docs/blob/master/ru/docs/api/sending/SendMessage.md)                                       |
| `sending.sendTemplateButtons`          | The method is aimed for sending a message with template list interactive buttons to a personal or a group chat                                                                                      | [SendTemplateButtons.md](https://github.com/green-api/docs/blob/master/ru/docs/api/sending/SendTemplateButtons.md)                       |
| `sending.forwardMessages`              | The method is intended for forwarding messages to a personal or group chat                                                                                                                          | [ForwardMessages.md](https://github.com/green-api/docs/blob/master/ru/docs/api/sending/ForwardMessages.md)                               |
| `serviceMethods.checkWhatsapp`         | The method checks WhatsApp account availability on a phone number                                                                                                                                   | [CheckWhatsapp.md](https://github.com/green-api/docs/blob/master/ru/docs/api/service/CheckWhatsapp.md)                                   |
| `serviceMethods.getAvatar`             | The method returns a user or a group chat avatar                                                                                                                                                    | [GetAvatar.md](https://github.com/green-api/docs/blob/master/ru/docs/api/service/GetAvatar.md)                                           |
| `serviceMethods.getContactInfo`        | The method is aimed for getting information on a contact                                                                                                                                            | [GetContactInfo.md](https://github.com/green-api/docs/blob/master/ru/docs/api/service/GetContactInfo.md)                                 |
| `serviceMethods.getContacts`           | The method is aimed for getting a list of the current account contacts                                                                                                                              | [GetContacts.md](https://github.com/green-api/docs/blob/master/ru/docs/api/service/GetContacts.md)                                       |
| `serviceMethods.setDisappearingChat`   | The method is aimed for changing settings of disappearing messages in chats. The standard settings of the application are to be used: 0 (off), 86400 (24 hours), 604800 (7 days), 7776000 (90 days) | [SetDisappearingChat.md](https://github.com/green-api/docs/blob/master/ru/docs/api/service/SetDisappearingChat.md)                       |
| `serviceMethods.archiveChat`           | The method archives a chat. One can archive chats that have at least one incoming message                                                                                                           | [ArchiveChat.md](https://github.com/green-api/docs/blob/master/ru/docs/api/service/ArchiveChat.md)                                       |
| `serviceMethods.deleteMessage`         | The method deletes a message from a chat                                                                                                                                                            | [DeleteMessage.md](https://github.com/green-api/docs/blob/master/ru/docs/api/service/deleteMessage.md)                                   |
| `serviceMethods.unarchiveChat`         | The method unarchives a chat                                                                                                                                                                        | [UnarchiveChat.md](https://github.com/green-api/docs/blob/master/ru/docs/api/service/UnarchiveChat.md)                                   |
| `serviceMethods.setDisappearingChat`   | The method is aimed for changing settings of disappearing messages in chats                                                                                                                         | [SetDisappearingChat.md](https://github.com/green-api/docs/blob/master/ru/docs/api/service/SetDisappearingChat.md)                       |
| `webhooks.startReceivingNotifications` | The method is aimed for starting to receive webhooks                                                                                                                                                | <library method>                                                                                                                         |
| `webhooks.stopReceivingNotifications`  | The method is aimed for stopping to receive webhooks                                                                                                                                                | <library method>                                                                                                                         |

## Service methods documentation

[https://green-api.com/en/docs/api/](https://green-api.com/en/docs/api/)

## External products

* [requests](https://requests.readthedocs.io) - for http requests

## License

Licensed under MIT terms. Please see file [LICENSE](LICENSE)
