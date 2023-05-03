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

| API method                             | Description                                                                                                              | Documentation link                                                                                          |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| `account.getSettings`                  | The method is designed to get the current settings of the account                                                        | [GetSettings](https://green-api.com/en/docs/api/account/GetSettings/)                                       |
| `account.setSettings`                  | The method is designed to set the account settings                                                                       | [SetSettings](https://green-api.com/en/docs/api/account/SetSettings/)                                          |
| `account.getStateInstance`             | The method is designed to get the state of the account                                                                   | [GetStateInstance](https://green-api.com/en/docs/api/account/GetStateInstance/)                             |
| `account.getStatusInstance`            | The method is designed to get the socket connection state of the account instance with WhatsApp                          | [GetStatusInstance](https://green-api.com/en/docs/api/account/GetStatusInstance/)                           |
| `account.reboot`                       | The method is designed to restart the account                                                                            | [Reboot](https://green-api.com/en/docs/api/account/Reboot/)                                                 |
| `account.logout`                       | The method is designed to unlogin the account                                                                            | [Logout](https://green-api.com/en/docs/api/account/Logout/)                                                 |
| `account.qr`                           | The method is designed to get a QR code                                                                                  | [QR](https://green-api.com/en/docs/api/account/QR/)                                                         |
| `account.setProfilePicture`            | The method is designed to set the avatar of the account                                                                  | [SetProfilePicture](https://green-api.com/en/docs/api/account/SetProfilePicture/)                           |
| `device.getDeviceInfo`                 | The method is designed to get information about the device (phone) on which the WhatsApp Business application is running | [GetDeviceInfo](https://green-api.com/en/docs/api/phone/GetDeviceInfo/)                                     |
| `groups.createGroup`                   | The method is designed to create a group chat                                                                            | [CreateGroup](https://green-api.com/en/docs/api/groups/CreateGroup/)                                        |
| `groups.updateGroupName`               | The method changes the name of the group chat                                                                            | [UpdateGroupName](https://green-api.com/en/docs/api/groups/UpdateGroupName/)                                |
| `groups.getGroupData`                  | The method gets group chat data                                                                                          | [GetGroupData](https://green-api.com/en/docs/api/groups/GetGroupData/)                                      |
| `groups.addGroupParticipant`           | The method adds a participant to the group chat                                                                          | [AddGroupParticipant](https://green-api.com/en/docs/api/groups/AddGroupParticipant/)                        |
| `groups.removeGroupParticipant`        | The method removes the participant from the group chat                                                                   | [RemoveGroupParticipant](https://green-api.com/en/docs/api/groups/RemoveGroupParticipant/)                  |
| `groups.setGroupAdmin`                 | The method designates a member of a group chat as an administrator                                                       | [SetGroupAdmin](https://green-api.com/en/docs/api/groups/SetGroupAdmin/)                                    |
| `groups.removeAdmin`                   | The method deprives the participant of group chat administration rights                                                  | [RemoveAdmin](https://green-api.com/en/docs/api/groups/RemoveAdmin/)                                        |
| `groups.setGroupPicture`               | The method sets the avatar of the group                                                                                  | [SetGroupPicture](https://green-api.com/en/docs/api/groups/SetGroupPicture/)                                |
| `groups.leaveGroup`                    | The method logs the user of the current account out of the group chat                                                    | [LeaveGroup](https://green-api.com/en/docs/api/groups/LeaveGroup/)                                          |
| `journals.getChatHistory`              | The method returns the chat message history                                                                              | [GetChatHistory](https://green-api.com/en/docs/api/journals/GetChatHistory/)                                |
| `journals.lastIncomingMessages`        | The method returns the most recent incoming messages of the account                                                      | [LastIncomingMessages](https://green-api.com/en/docs/api/journals/LastIncomingMessages/)                    |
| `journals.lastOutgoingMessages`        | The method returns the last sent messages of the account                                                                 | [LastOutgoingMessages](https://green-api.com/en/docs/api/journals/LastOutgoingMessages/)                    |
| `queues.showMessagesQueue`             | The method is designed to get the list of messages that are in the queue to be sent                                      | [ShowMessagesQueue](https://green-api.com/en/docs/api/queues/ShowMessagesQueue/)                            |
| `queues.clearMessagesQueue`            | The method is designed to clear the queue of messages to be sent                                                         | [ClearMessagesQueue](https://green-api.com/en/docs/api/queues/ClearMessagesQueue/)                          |
| `marking.readChat`                     | The method is designed to mark chat messages as read                                                                     | [ReadChat](https://green-api.com/en/docs/api/marks/ReadChat/)                                               |
| `receiving.receiveNotification`        | The method is designed to receive a single incoming notification from the notification queue                             | [ReceiveNotification](https://green-api.com/en/docs/api/receiving/technology-http-api/ReceiveNotification/) |
| `receiving.deleteNotification`         | The method is designed to remove an incoming notification from the notification queue                                    | [DeleteNotification](https://green-api.com/en/docs/api/receiving/technology-http-api/DeleteNotification/)   |
| `receiving.downloadFile`               | The method is for downloading received and sent files                                                                    | [DownloadFile](https://green-api.com/en/docs/api/receiving/files/DownloadFile/)                             |
| `sending.sendMessage`                  | The method is designed to send a text message to a personal or group chat                                                | [SendMessage](https://green-api.com/en/docs/api/sending/SendMessage/)                                       |
| `sending.sendButtons`                  | The method is designed to send a message with buttons to a personal or group chat                                        | [SendButtons](https://green-api.com/en/docs/api/sending/SendButtons/)                                       |
| `sending.sendTemplateButtons`          | The method is designed to send a message with interactive buttons from the list of templates in a personal or group chat | [SendTemplateButtons](https://green-api.com/en/docs/api/sending/SendTemplateButtons/)                       |
| `sending.sendListMessage`              | The method is designed to send a message with a selection button from a list of values to a personal or group chat       | [SendListMessage](https://green-api.com/en/docs/api/sending/SendListMessage/)                               |
| `sending.sendFileByUpload`             | The method is designed to send a file loaded through a form (form-data)                                                  | [SendFileByUpload](https://green-api.com/en/docs/api/sending/SendFileByUpload/)                             |
| `sending.sendFileByUrl`                | The method is designed to send a file downloaded via a link                                                              | [SendFileByUrl](https://green-api.com/en/docs/api/sending/SendFileByUrl/)                                   |
| `sending.sendLocation`                 | The method is designed to send a geolocation message                                                                     | [SendLocation](https://green-api.com/en/docs/api/sending/SendLocation/)                                     |
| `sending.sendContact`                  | The method is for sending a message with a contact                                                                       | [SendContact](https://green-api.com/en/docs/api/sending/SendContact/)                                       |
| `sending.sendLink`                     | The method is designed to send a message with a link that will add an image preview, title and description               | [SendLink](https://green-api.com/en/docs/api/sending/SendLink/)                                             |
| `sending.forwardMessages`              | The method is designed for forwarding messages to a personal or group chat                                               | [ForwardMessages](https://green-api.com/en/docs/api/sending/ForwardMessages/)                               |
| `serviceMethods.checkWhatsapp`         | The method checks if there is a WhatsApp account on the phone number                                                     | [CheckWhatsapp](https://green-api.com/en/docs/api/service/CheckWhatsapp/)                                   |
| `serviceMethods.getAvatar`             | The method returns the avatar of the correspondent or group chat                                                         | [GetAvatar](https://green-api.com/en/docs/api/service/GetAvatar/)                                           |
| `serviceMethods.getContacts`           | The method is designed to get a list of contacts of the current account                                                  | [GetContacts](https://green-api.com/en/docs/api/service/GetContacts/)                                       |
| `serviceMethods.getContactInfo`        | The method is designed to obtain information about the contact                                                           | [GetContactInfo](https://green-api.com/en/docs/api/service/GetContactInfo/)                                 |
| `serviceMethods.deleteMessage`         | The method deletes the message from chat                                                                                 | [DeleteMessage](https://green-api.com/en/docs/api/service/deleteMessage/)                                   |
| `serviceMethods.archiveChat`           | The method archives the chat                                                                                             | [ArchiveChat](https://green-api.com/en/docs/api/service/archiveChat/)                                       |
| `serviceMethods.unarchiveChat`         | The method unarchives the chat                                                                                           | [UnarchiveChat](https://green-api.com/en/docs/api/service/unarchiveChat/)                                   |
| `serviceMethods.setDisappearingChat`   | The method is designed to change the settings of disappearing messages in chats                                          | [SetDisappearingChat](https://green-api.com/en/docs/api/service/SetDisappearingChat/)                       |
| `webhooks.startReceivingNotifications` | The method is designed to start receiving new notifications                                                              |                                                                                                             |
| `webhooks.stopReceivingNotifications`  | The method is designed to stop receiving new notifications                                                               |                                                                                                             |

## Service methods documentation

[https://green-api.com/en/docs/api/](https://green-api.com/en/docs/api/)

## External products

* [requests](https://requests.readthedocs.io) - for http requests

## License

[![CC BY-ND 4.0][cc-by-nd-shield]][cc-by-nd]

This work is licensed under a
[Creative Commons Attribution-NoDerivatives 4.0 International License][cc-by-nd].

[cc-by-nd]: https://creativecommons.org/licenses/by-nd/4.0/
[cc-by-nd-shield]: https://img.shields.io/badge/License-CC%20BY--ND%204.0-lightgrey.svg

Please see file [LICENSE](LICENSE)