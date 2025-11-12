# whatsapp-api-client-python

![](https://img.shields.io/badge/license-CC%20BY--ND%204.0-green)
![](https://img.shields.io/pypi/status/whatsapp-api-client-python)
![](https://img.shields.io/pypi/pyversions/whatsapp-api-client-python)
![](https://img.shields.io/github/actions/workflow/status/green-api/whatsapp-api-client-python/python-package.yml)
![](https://img.shields.io/pypi/dm/whatsapp-api-client-python)

## Support links

[![Support](https://img.shields.io/badge/support@green--api.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:support@greenapi.com)
[![Support](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/greenapi_support_eng_bot)
[![Support](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/77273122366)

## Guides & News

[![Guides](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)](https://www.youtube.com/@greenapi-en)
[![News](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/green_api)
[![News](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://whatsapp.com/channel/0029VaLj6J4LNSa2B5Jx6s3h)

- [Документация на русском языке](https://github.com/green-api/whatsapp-api-client-python/blob/master/docs/README.md).

whatsapp-api-client-python is a library for integration with WhatsApp messenger using the API
service [green-api.com](https://green-api.com/en/). You should get a registration token and an account ID in
your [personal cabinet](https://console.green-api.com/) to use the library. There is a free developer account tariff.

## API

The documentation for the REST API can be found at the [link](https://green-api.com/en/docs/). The library is a wrapper
for the REST API, so the documentation at the link above also applies.

## Authorization

To send a message or perform other GREEN API methods, the WhatsApp account in the phone app must be authorized. To
authorize the account, go to your [cabinet](https://console.green-api.com/) and scan the QR code using the WhatsApp app.

## Installation

```shell
python -m pip install whatsapp-api-client-python
```

## Import

```
from whatsapp_api_client_python import API
```

## Examples

### How to initialize an object

```
greenAPI = API.GreenAPI(
    "1101000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)
```

### Sending a text message to a WhatsApp number

Link to example: [sendTextMessage.py](./examples/sync/sending/sendTextMessage.py).

```
response = greenAPI.sending.sendMessage("11001234567@c.us", "Message text")

print(response.data)
```

### Sending a text message asynchronously

Link to example: [sendMessageAsync.py](./examples/async/sending/sendMessageAsync.py).

```
import asyncio

async def main():
    response = await greenAPI.sending.sendMessageAsync("11001234567@c.us", "Message text")
    print(response.data)

asyncio.run(main())
```

### Sending an image via URL

Link to example: [sendPictureByLink.py](./examples/sync/sending/sendPictureByLink.py).

```
response = greenAPI.sending.sendFileByUrl(
    "11001234567@c.us",
    "https://download.samplelib.com/png/sample-clouds2-400x300.png",
    "sample-clouds2-400x300.png",
    "Sample PNG"
)

print(response.data)
```

### Sending an image by uploading from the disk

Link to example: [sendPictureByUpload.py](./examples/sync/sending/sendPictureByUpload.py).

```
response = greenAPI.sending.sendFileByUpload(
    "11001234567@c.us",
    "data/logo.jpg",
    "logo.jpg",
    "Available rates"
)

print(response.data)
```

### Sending an image asynchronously by uploading from the disk

Link to example: [sendFileByUploadAsync.py](./examples/async/sending/sendFileByUploadAsync.py).

```
import asyncio

async def main():
    response = await greenAPI.sending.sendFileByUploadAsync(
        "11001234567@c.us",
        "data/logo.jpg",
        "logo.jpg",
        "Available rates"
    )
    print(response.data)

asyncio.run(main())
```

### Group creation and sending a message to the group

**Attention**. If one tries to create a group with a non-existent number, WhatsApp may block the sender's number. The
number in the example is non-existent.

Link to example: [createGroupAndSendMessage.py](./examples/sync/createGroupAndSendMessage.py).

```
create_group_response = greenAPI.groups.createGroup(
    "Group Name", ["11001234567@c.us"]
)
if create_group_response.code == 200:
    send_message_response = greenAPI.sending.sendMessage(
        create_group_response.data["chatId"], "Message text"
    )
```

### Receive incoming messages by HTTP API

Link to example: [receiveNotification.py](./examples/sync/receiveNotification.py).

The general concept of receiving data in the GREEN API is described [here](
https://green-api.com/en/docs/api/receiving/
). To start receiving notifications by the HTTP API you need to execute the library method:

```
greenAPI.webhooks.startReceivingNotifications(onEvent)
```

onEvent - your function which should contain parameters:

| Parameter   | Description                      |
|-------------|----------------------------------|
| typeWebhook | received notification type (str) |
| body        | notification body (dict)         |

Notification body types and formats can be found [here](https://green-api.com/en/docs/api/receiving/notifications-format/).

This method will be called when an incoming notification is received. Next, process notifications according to the
business logic of your system.

### Receive incoming messages asynchronously by HTTP API

Link to example: [receiveNotificationAsync.py](./examples/async/receiveNotificationAsync.py).

```
import asyncio

async def main():
    await greenAPI.webhooks.startReceivingNotificationsAsync(onEvent)

asyncio.run(main())
```

### Sending a polling message

Link to example: [sendPoll.py](./examples/sync/sending/sendPoll.py).

```
response = greenAPI.sending.sendPoll(
    "11001234567@c.us",
    "Please choose a color:",
    [
        {"optionName": "Red"},
        {"optionName": "Green"},
        {"optionName": "Blue"}
    ]
)

print(response.data)
```

### Sending a text status

Link to example: [sendTextStatus.py](./examples/sync/statusesMethods/sendTextStatus.py).

```
response = greenAPI.statuses.sendTextStatus(
    "I sent this status using Green Api Python SDK!", 
    "#54c774", 
    "NORICAN_REGULAR"
)

print(response.data)
```

### Sending interactive buttons

Link to example: [sendInteractiveButtons.py](../examples/sync/sending/sendInteractiveButtons.py).

```
response = greenAPI.sending.sendInteractiveButtons(
    "79001234567@c.us",
    "This is message with buttons!",
    [{
        "type": "call",
        "buttonId": "1",
        "buttonText": "Call me",
        "phoneNumber": "79001234567"
    },
    {
        "type": "url",
        "buttonId": "2",
        "buttonText": "Green-api",
        "url": "https://green-api.com/en/docs/api/sending/SendInteractiveButtons/"
    }],
    "Check this out",
    "Hope you like it"
)

print(response.data)
```

### Sending interactive buttons async

Link to example: [sendInteractiveButtonsAsync.py](../examples/async/sending/sendInteractiveButtonsAsync.py).

```
import asyncio

async def main():
    response = await greenAPI.sending.sendInteractiveButtonsAsync(
        "79001234567@c.us",
        "This is message with buttons!",
        [{
            "type": "call",
            "buttonId": "1",
            "buttonText": "Call me",
            "phoneNumber": "79001234567"
        },
        {
            "type": "url",
            "buttonId": "2",
            "buttonText": "Green-api",
            "url": "https://green-api.com/en/docs/api/sending/SendInteractiveButtons/"
        }],
        "Check this out",
        "Hope you like it"
    )
    print(response.data)
asyncio.run(main())
```

## Examples list

| Description                                                    | Module                                                                                                                                         |
|----------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Example of sending text                                        | [sendTextMessage.py](./examples/sync/sending/sendTextMessage.pyy)                     |
| Example of sending text asynchronously                         | [sendTextMessageAsync.py](./examples/async/sendMessageAsync.py)              |
| Example of sending a picture by URL                            | [sendPictureByLink.py](./examples/sync/sending/sendPictureByLink.py)                 |
| Example of sending a file by URL asynchronously                | [sendFileByUrlAsync.py](./examples/async/sending/sendFileByUrlAsync.py)      |
| Example of sending a picture by uploading from the disk        | [sendPictureByUpload.py](./examples/sync/sending/sendPictureByUpload.py)             |
| Example of sending file by uploading from the disk asynchronously  | [sendFileByUploadAsync.py](./examples/async/sending/sendFileByUploadAsync.py) |
| Example of a group creation and sending a message to the group | [createGroupAndSendMessage.py](./examples/sync/sending/createGroupAndSendMessage.py) |
| Example of a group creation and sending a message to the group asynchronously | [createGroupAndSendMessageAsync.py](./examples/async/createGroupAndSendMessageAsync.py) |
| Example of incoming webhooks receiving                         | [receiveNotification.py](./examples/sync/receiveNotification.py)             |
| Example of incoming webhooks receiving asynchronously          | [receiveNotificationAsync.py](./examples/async/receiveNotificationAsync.py)  |
| Example of sending a polling message                           | [sendPoll.py](./examples/sync/sending/sendPoll.py)                                   |
| Example of sending a polling message asynchronously            | [sendPollAsync.py](./examples/async/sending/sendPollasync.py)                |
| Example of sending a text status                               | [sendTextStatus.py](./examples/sync/statusesMethods/sendTextStatus.py)       |
| Example of sending a text status asynchronously                | [sendTextStatusAsync.py](./examples/async/statusesMethods/sendTextStatusAsync.py) |
| Example of creating instance                                   | [CreateInstance.py](./examples/sync/partherMethods/CreateInstance.py)        |
| Example of creating instance asynchronously                    | [CreateInstanceAsync.py](./examples/async/partherMethods/CreateInstanceAsync.py)  |
| Example of sending interactive buttons | [SendInteractiveButtons.py](../examples/sync/sending/sendInteractiveButtons.py) |
| Example of sending interactive buttons asynchronously | [SendInteractiveButtonsAsync.py](../examples/async/sending/sendInteractiveButtonsAsync.py) |
| Example of sending interactive buttons with a reply | [SendInteractiveButtonsReply.py](../examples/sync/sending/sendInteractiveButtonsReply.py) |
| Example of sending interactive buttons asynchronously with a reply | [SendInteractiveButtonsReplyAsync.py](../examples/async/sending/sendInteractiveButtonsReplyAsync.py) |

## The full list of the library methods

| API method                             | Description                                                                                                              | Documentation link                                                                                          |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| `account.getSettings`                  | The method is designed to get the current settings of the account                                                        | [GetSettings](https://green-api.com/en/docs/api/account/GetSettings/)                                       |
| `account.getWaSettings`                | The method is designed to get information about the WhatsApp account                                                     | [GetWaSettings](https://green-api.com/en/docs/api/account/GetWaSettings/)                                   |
| `account.setSettings`                  | The method is designed to set the account settings                                                                       | [SetSettings](https://green-api.com/en/docs/api/account/SetSettings/)                                       |
| `account.getStateInstance`             | The method is designed to get the state of the account                                                                   | [GetStateInstance](https://green-api.com/en/docs/api/account/GetStateInstance/)                             |
| `account.getStatusInstance`            | The method is designed to get the socket connection state of the account instance with WhatsApp                          | [GetStatusInstance](https://green-api.com/en/docs/api/account/GetStatusInstance/)                           |
| `account.reboot`                       | The method is designed to restart the account                                                                            | [Reboot](https://green-api.com/en/docs/api/account/Reboot/)                                                 |
| `account.logout`                       | The method is designed to unlogin the account                                                                            | [Logout](https://green-api.com/en/docs/api/account/Logout/)                                                 |
| `account.qr`                           | The method is designed to get a QR code                                                                                  | [QR](https://green-api.com/en/docs/api/account/QR/)                                                         |
| `account.setProfilePicture`            | The method is designed to set the avatar of the account                                                                  | [SetProfilePicture](https://green-api.com/en/docs/api/account/SetProfilePicture/)                           |
| `account.getAuthorizationCode`         | The method is designed to authorize an instance by phone number                                                          | [GetAuthorizationCode](https://green-api.com/en/docs/api/account/GetAuthorizationCode/)                     |
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
| `statuses.sendTextStatus`                    | The method is aimed for sending a text status                                                    | [SendTextStatus](https://green-api.com/en/docs/api/statuses/SendTextStatus/)                                          |
| `statuses.sendVoiceStatus`                    | The method is aimed for sending a voice status                                                    | [SendVoiceStatus](https://green-api.com/en/docs/api/statuses/SendVoiceStatus/)                                          |
| `statuses.sendMediaStatus`                    | The method is aimed for sending a pictures or video status                                                    | [SendMediaStatus](https://green-api.com/en/docs/api/statuses/SendMediaStatus/)                                          |
| `statuses.deleteStatus`                    | The method is aimed for deleting a certain status                                                    | [DeleteStatus](https://green-api.com/en/docs/api/statuses/DeleteStatus/)                                          |
| `statuses.getStatusStatistic`                    | The method returns an array of recipients marked sent/delivered/read for a given status                                                    | [GetStatusStatistic](https://green-api.com/en/docs/api/statuses/GetStatusStatistic/)                                          |
| `statuses.getOutgoingStatuses`                    | The method returns the outgoing statuses of the account                                                    | [GetOutgoingStatuses](https://green-api.com/en/docs/api/statuses/GetOutgoingStatuses/)                                          |
| `statuses.getIncomingStatuses`                    | The method returns the incoming statuses of the account                                                    | [GetIncomingStatuses](https://green-api.com/en/docs/api/statuses/GetIncomingStatuses/)                                          |
| `journals.getChatHistory`              | The method returns the chat message history                                                                              | [GetChatHistory](https://green-api.com/en/docs/api/journals/GetChatHistory/)                                |
| `journals.getMessage`                  | The method returns a chat message                                                                                        | [GetMessage](https://green-api.com/en/docs/api/journals/GetMessage/)                                        |
| `journals.lastIncomingMessages`        | The method returns the most recent incoming messages of the account                                                      | [LastIncomingMessages](https://green-api.com/en/docs/api/journals/LastIncomingMessages/)                    |
| `journals.lastOutgoingMessages`        | The method returns the last sent messages of the account                                                                 | [LastOutgoingMessages](https://green-api.com/en/docs/api/journals/LastOutgoingMessages/)                    |
| `queues.showMessagesQueue`             | The method is designed to get the list of messages that are in the queue to be sent                                      | [ShowMessagesQueue](https://green-api.com/en/docs/api/queues/ShowMessagesQueue/)                            |
| `queues.clearMessagesQueue`            | The method is designed to clear the queue of messages to be sent                                                         | [ClearMessagesQueue](https://green-api.com/en/docs/api/queues/ClearMessagesQueue/)                          |
| `marking.readChat`                     | The method is designed to mark chat messages as read                                                                     | [ReadChat](https://green-api.com/en/docs/api/marks/ReadChat/)                                               |
| `receiving.receiveNotification`        | The method is designed to receive a single incoming notification from the notification queue                             | [ReceiveNotification](https://green-api.com/en/docs/api/receiving/technology-http-api/ReceiveNotification/) |
| `receiving.deleteNotification`         | The method is designed to remove an incoming notification from the notification queue                                    | [DeleteNotification](https://green-api.com/en/docs/api/receiving/technology-http-api/DeleteNotification/)   |
| `receiving.downloadFile`               | The method is for downloading received and sent files                                                                    | [DownloadFile](https://green-api.com/en/docs/api/receiving/files/DownloadFile/)                             |
| `sending.sendMessage`                  | The method is designed to send a text message to a personal or group chat                                                | [SendMessage](https://green-api.com/en/docs/api/sending/SendMessage/)                                       |
| `sending.sendFileByUpload`             | The method is designed to send a file loaded through a form (form-data)                                                  | [SendFileByUpload](https://green-api.com/en/docs/api/sending/SendFileByUpload/)                             |
| `sending.sendFileByUrl`                | The method is designed to send a file downloaded via a link                                                              | [SendFileByUrl](https://green-api.com/en/docs/api/sending/SendFileByUrl/)                                   |
| `sending.uploadFile`                   | The method is designed to upload a file to the cloud storage, which can be sent using the sendFileByUrl method           | [UploadFile](https://green-api.com/en/docs/api/sending/UploadFile/)                                         |
| `sending.sendLocation`                 | The method is designed to send a geolocation message                                                                     | [SendLocation](https://green-api.com/en/docs/api/sending/SendLocation/)                                     |
| `sending.sendContact`                  | The method is for sending a message with a contact                                                                       | [SendContact](https://green-api.com/en/docs/api/sending/SendContact/)                                       |
| `sending.forwardMessages`              | The method is designed for forwarding messages to a personal or group chat                                               | [ForwardMessages](https://green-api.com/en/docs/api/sending/ForwardMessages/)                               |
| `sending.sendPoll`                     | The method is designed for sending messages with a poll to a private or group chat                                       | [SendPoll](https://green-api.com/en/docs/api/sending/SendPoll/)                                             |
| `sending.sendInteractiveButtons`       | This method is used to send messages with interactive buttons                                                            | [sendInteractiveButtons](https://green-api.com/en/docs/api/sending/SendInteractiveButtons/)                |
| `sending.sendInteractiveButtonsReply`  | This method is used to send messages with interactive buttons with a reply                                               | [sendInteractiveButtonsReply](https://green-api.com/en/docs/api/sending/SendInteractiveButtonsReply/)       |
| `serviceMethods.checkWhatsapp`         | The method checks if there is a WhatsApp account on the phone number                                                     | [CheckWhatsapp](https://green-api.com/en/docs/api/service/CheckWhatsapp/)                                   |
| `serviceMethods.getAvatar`             | The method returns the avatar of the correspondent or group chat                                                         | [GetAvatar](https://green-api.com/en/docs/api/service/GetAvatar/)                                           |
| `serviceMethods.getContacts`           | The method is designed to get a list of contacts of the current account                                                  | [GetContacts](https://green-api.com/en/docs/api/service/GetContacts/)                                       |
| `serviceMethods.getContactInfo`        | The method is designed to obtain information about the contact                                                           | [GetContactInfo](https://green-api.com/en/docs/api/service/GetContactInfo/)                                 |
| `serviceMethods.deleteMessage`         | The method deletes the message from chat                                                                                 | [DeleteMessage](https://green-api.com/en/docs/api/service/deleteMessage/)                                   |
| `serviceMethods.editMessage`           | The method edits the message in chat                                                                                     | [EditMessage](https://green-api.com/en/docs/api/service/editMessage/)                                   |
| `serviceMethods.archiveChat`           | The method archives the chat                                                                                             | [ArchiveChat](https://green-api.com/en/docs/api/service/archiveChat/)                                       |
| `serviceMethods.unarchiveChat`         | The method unarchives the chat                                                                                           | [UnarchiveChat](https://green-api.com/en/docs/api/service/unarchiveChat/)                                   |
| `serviceMethods.setDisappearingChat`   | The method is designed to change the settings of disappearing messages in chats                                          | [SetDisappearingChat](https://green-api.com/en/docs/api/service/SetDisappearingChat/)                       |
| `webhooks.startReceivingNotifications` | The method is designed to start receiving new notifications                                                              |                                                                                                             |
| `webhooks.stopReceivingNotifications`  | The method is designed to stop receiving new notifications                                                               |                                                                                                             |
| `partner.GetInstances`   | The method is for getting all the account instances created by the partner.                                           | [GetInstances](https://green-api.com/en/docs/partners/getInstances/)                       |
| `partner.CreateInstance`   | The method is for creating an instance.                                           | [CreateInstance](https://green-api.com/en/docs/partners/createInstance/)                       |
| `partner.DeleteInstanceAccount`   | The method is for deleting an instance.                                           | [DeleteInstanceAccount](https://green-api.com/en/docs/partners/deleteInstanceAccount/)                       |


## Service methods documentation

[https://green-api.com/en/docs/api/](https://green-api.com/en/docs/api/).

## External products

- [requests](https://requests.readthedocs.io/en/latest/) - for HTTP requests.
- [aiohttp](https://docs.aiohttp.org/) - for async HTTP requests.

## License

Licensed under [Creative Commons Attribution-NoDerivatives 4.0 International (CC BY-ND 4.0)](https://creativecommons.org/licenses/by-nd/4.0/) terms.
Please see file [LICENSE](https://github.com/green-api/whatsapp-api-client-python/blob/master/LICENSE).
