# whatsapp-api-client-python

![](https://img.shields.io/badge/license-CC%20BY--ND%204.0-green)
![](https://img.shields.io/pypi/status/whatsapp-api-client-python)
![](https://img.shields.io/pypi/pyversions/whatsapp-api-client-python)
![](https://img.shields.io/github/actions/workflow/status/green-api/whatsapp-api-client-python/python-package.yml)
![](https://img.shields.io/pypi/dm/whatsapp-api-client-python)

## Поддержка

[![Support](https://img.shields.io/badge/support@green--api.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:support@green-api.com)
[![Support](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/greenapi_support_ru_bot)
[![Support](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/79993331223)

## Руководства и новости

[![Guides](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)](https://www.youtube.com/@green-api)
[![News](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/green_api)
[![News](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://whatsapp.com/channel/0029VaHUM5TBA1f7cG29nO1C)

whatsapp-api-client-python - библиотека для интеграции с мессенджером WhatsApp через API
сервиса [green-api.com](https://green-api.com/). Чтобы воспользоваться библиотекой, нужно получить регистрационный токен
и ID аккаунта в [личном кабинете](https://console.green-api.com/). Есть бесплатный тариф аккаунта разработчика.

## API

Документация к REST API находится по [ссылке](https://green-api.com/docs/api/). Библиотека является обёрткой к REST API,
поэтому документация по ссылке выше применима и к самой библиотеке.

## Авторизация

Чтобы отправить сообщение или выполнить другие методы GREEN API, аккаунт WhatsApp в приложении телефона должен быть в
авторизованном состоянии. Для авторизации аккаунта перейдите в [личный кабинет](https://console.green-api.com/) и
сканируйте QR-код с использованием приложения WhatsApp.

## Установка

```shell
python -m pip install whatsapp-api-client-python
```

## Импорт

```
from whatsapp_api_client_python import API
```

## Примеры

### Как инициализировать объект

```
greenAPI = API.GreenAPI(
    "1101000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)
```

### Отправка текстового сообщения на номер WhatsApp

Ссылка на пример: [sendTextMessage.py](../examples/sync/sending/sendTextMessage.py).

```
response = greenAPI.sending.sendMessage("11001234567@c.us", "Message text")

print(response.data)
```


### Отправка текстового сообщения асинхронно

Ссылка на пример: [sendMessageAsync.py](../examples/async/sending/sendMessageAsync.py).

```
import asyncio

async def main():
    response = await greenAPI.sending.sendMessageAsync("11001234567@c.us", "Message text")
    print(response.data)

asyncio.run(main())
```

### Отправка картинки по URL

Ссылка на пример: [sendPictureByLink.py](../examples/sync/sending/sendPictureByLink.py).

```
response = greenAPI.sending.sendFileByUrl(
    "11001234567@c.us",
    "https://download.samplelib.com/png/sample-clouds2-400x300.png",
    "sample-clouds2-400x300.png",
    "Sample PNG"
)

print(response.data)
```

### Отправка картинки загрузкой с диска

Ссылка на пример: [sendPictureByUpload.py](../examples/sync/sending/sendPictureByUpload.py).

```
response = greenAPI.sending.sendFileByUpload(
    "11001234567@c.us",
    "data/logo.jpg",
    "logo.jpg",
    "Available rates"
)

print(response.data)
```


### Отправка картинки асинхронно загрузкой с диска

Ссылка на пример: [sendFileByUploadAsync.py](../examples/async/sending/sendFileByUploadAsync.py).

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

### Создание группы и отправка сообщения в эту группу

**Важно**. Если попытаться создать группу с несуществующим номером WhatsApp, то может заблокировать номер отправителя.
Номер в примере не существует.

Ссылка на пример: [createGroupAndSendMessage.py](../examples/sync/createGroupAndSendMessage.py).

```
create_group_response = greenAPI.groups.createGroup(
    "Group Name", ["11001234567@c.us"]
)
if create_group_response.code == 200:
    send_message_response = greenAPI.sending.sendMessage(
        create_group_response.data["chatId"], "Message text"
    )
```

### Получение входящих уведомлений через HTTP API

Ссылка на пример: [receiveNotification.py](../examples/sync/receiveNotification.py).

Общая концепция получения данных в GREEN API описана [здесь](https://green-api.com/docs/api/receiving/). Для старта
получения уведомлений через HTTP API требуется выполнить метод библиотеки:

```
greenAPI.webhooks.startReceivingNotifications(onEvent)
```

onEvent - ваша функция, которая должен содержать параметры:

| Параметр    | Описание                          |
|-------------|-----------------------------------|
| typeWebhook | тип полученного уведомления (str) |
| body        | тело уведомления (dict)           |

Типы и форматы тел уведомлений находятся [здесь](https://green-api.com/docs/api/receiving/notifications-format/).

Эта функция будет вызываться при получении входящего уведомления. Далее обрабатываете уведомления согласно бизнес-логике
вашей системы.


### Асинхронное получение входящих уведомлений через HTTP API

Ссылка на пример: [receiveNotificationAsync.py](../examples/async/receiveNotificationAsync.py).

```
import asyncio

async def main():
    await greenAPI.webhooks.startReceivingNotificationsAsync(onEvent)

asyncio.run(main())
```

### Отправка сообщения с опросом

Ссылка на пример: [sendPoll.py](../examples/sync/sending/sendPoll.py).

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

### Отправка текстового статуса

Ссылка на пример: [sendTextStatus.py](../examples/sync/statusesMethods/sendTextStatus.py).

```
response = greenAPI.statuses.sendTextStatus(
    "I sent this status using Green Api Python SDK!", 
    "#54c774", 
    "NORICAN_REGULAR"
)

print(response.data)
```

### Отправка интерактивных кнопок

Ссылка на пример: [sendInteractiveButtons.py](../examples/sync/sending/sendInteractiveButtons.py).

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

### Асинхронная отправка интерактивных кнопок

Ссылка на пример: [sendInteractiveButtonsAsync.py](../examples/async/sending/sendInteractiveButtonsAsync.py).

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

## Список примеров

| Описание                                               | Модуль                                                                            |
|--------------------------------------------------------|-----------------------------------------------------------------------------------|
| Пример отправки текста                                 | [sendTextMessage.py](../examples/sync/sending/sendTextMessage.py)                 |
| Пример асинхронной отправки текста                     | [sendTextMessageAsync.py](../examples/async/sending/sendMessageAsync.py)          |
| Пример отправки картинки по URL                        | [sendPictureByLink.py](../examples/sync/sending/sendPictureByLink.py)             |
| Пример асинхронной отправки файла по URL               | [sendFileByUrlAsync.py](../examples/async/sending/sendFileByUrlAsync.py)          |
| Пример отправки картинки загрузкой с диска             | [sendPictureByUpload.py](../examples/sync/sending/sendPictureByUpload.py)         |
| Пример асинхронной отправки картинки загрузкой с диска | [sendFileByUploadAsync.py](../examples/async/sending/sendFileByUploadAsync.py)    |
| Пример создания группы и отправки сообщения в группу   | [createGroupAndSendMessage.py](../examples/sync/createGroupAndSendMessage.py)     |
| Пример асинхронных создания группы и отправки сообщения в группу | [createGroupAndSendMessageAsync.py](../examples/async/createGroupAndSendMessageAsync.py)  |
| Пример получения входящих уведомлений                  | [receiveNotification.py](../examples/sync/receiveNotification.py)                 |
| Пример асинхронного получения входящих уведомлений     | [receiveNotificationФынтс.py](../examples/async/receiveNotificationAsync.py)      |
| Пример отправки сообщения с опросом                    | [sendPoll.py](../examples/sync/sending/sendPoll.py)                               |
| Пример асинхронной отправки сообщения с опросом        | [sendPollAsync.py](../examples/async/sending/sendPollAsync.py)                    |
| Пример отправки текстового статуса                     | [sendTextStatus.py](../examples/sync/statusesMethods/sendTextStatus.py)           |
| Пример асинхронной отправки текстового статуса        | [sendTextStatusAsync.py](../examples/async/statusesMethods/sendTextStatusAsync.py) |
| Пример создания инстанса                               | [CreateInstance.py](../examples/sync/partherMethods/CreateInstance.py)            |
| Пример асинхронного создания инстанса                  | [CreateInstanceAsync.py](../examples/async/partnerMethods/CreateInstanceAsync.py) |
| Пример отправки интерактивных кнопок                   | [SendInteractiveButtons.py](../examples/sync/sending/sendInteractiveButtons.py)   |
| Пример асинхронной отправки интерактивных кнопок       | [SendInteractiveButtonsAsync.py](../examples/async/sending/sendInteractiveButtonsAsync.py)   |
| Пример отправки интерактивных кнопок с ответом         | [SendInteractiveButtonsReply.py](../examples/sync/sending/sendInteractiveButtonsReply.py)   |
| Пример асинхронной отправки интерактивных кнопок с ответом | [SendInteractiveButtonsReplyAsync.py](../examples/async/sending/sendInteractiveButtonsReplyAsync.py)   |

## Полный список методов библиотеки

| Метод API                              | Описание                                                                                                                  | Ссылка на документацию                                                                                       |
|----------------------------------------|---------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| `account.getSettings`                  | Метод предназначен для получения текущих настроек аккаунта                                                                | [GetSettings](https://green-api.com/docs/api/account/GetSettings/)                                       |
| `account.getWaSettings`                | Метод предназначен для получения информации о аккаунте WhatsApp                                                           | [GetWaSettings](https://green-api.com/docs/api/account/GetWaSettings/)                                   |
| `account.setSettings`                  | Метод предназначен для установки настроек аккаунта                                                                        | [SetSettings](https://green-api.com/docs/api/account/SetSettings/)                                       |
| `account.getStateInstance`             | Метод предназначен для получения состояния аккаунта                                                                       | [GetStateInstance](https://green-api.com/docs/api/account/GetStateInstance/)                             |
| `account.getStatusInstance`            | Метод предназначен для получения состояния сокета соединения инстанса аккаунта с WhatsApp                                 | [GetStatusInstance](https://green-api.com/docs/api/account/GetStatusInstance/)                           |
| `account.reboot`                       | Метод предназначен для перезапуска аккаунта                                                                               | [Reboot](https://green-api.com/docs/api/account/Reboot/)                                                 |
| `account.logout`                       | Метод предназначен для разлогинивания аккаунта                                                                            | [Logout](https://green-api.com/docs/api/account/Logout/)                                                 |
| `account.qr`                           | Метод предназначен для получения QR-кода                                                                                  | [QR](https://green-api.com/docs/api/account/QR/)                                                         |
| `account.setProfilePicture`            | Метод предназначен для установки аватара аккаунта                                                                         | [SetProfilePicture](https://green-api.com/docs/api/account/SetProfilePicture/)                           |
| `account.getAuthorizationCode`         | Метод предназначен для авторизации инстанса по номеру телефона                                                            | [GetAuthorizationCode](https://green-api.com/docs/api/account/GetAuthorizationCode/)                     |
| `device.getDeviceInfo`                 | Метод предназначен для получения информации об устройстве (телефоне), на котором запущено приложение WhatsApp Business    | [GetDeviceInfo](https://green-api.com/docs/api/phone/GetDeviceInfo/)                                     |
| `groups.createGroup`                   | Метод предназначен для создания группового чата                                                                           | [CreateGroup](https://green-api.com/docs/api/groups/CreateGroup/)                                        |
| `groups.updateGroupName`               | Метод изменяет наименование группового чата                                                                               | [UpdateGroupName](https://green-api.com/docs/api/groups/UpdateGroupName/)                                |
| `groups.getGroupData`                  | Метод получает данные группового чата                                                                                     | [GetGroupData](https://green-api.com/docs/api/groups/GetGroupData/)                                      |
| `groups.addGroupParticipant`           | Метод добавляет участника в групповой чат                                                                                 | [AddGroupParticipant](https://green-api.com/docs/api/groups/AddGroupParticipant/)                        |
| `groups.removeGroupParticipant`        | Метод удаляет участника из группового чата                                                                                | [RemoveGroupParticipant](https://green-api.com/docs/api/groups/RemoveGroupParticipant/)                  |
| `groups.setGroupAdmin`                 | Метод назначает участника группового чата администратором                                                                 | [SetGroupAdmin](https://green-api.com/docs/api/groups/SetGroupAdmin/)                                    |
| `groups.removeAdmin`                   | Метод лишает участника прав администрирования группового чата                                                             | [RemoveAdmin](https://green-api.com/docs/api/groups/RemoveAdmin/)                                        |
| `groups.setGroupPicture`               | Метод устанавливает аватар группы                                                                                         | [SetGroupPicture](https://green-api.com/docs/api/groups/SetGroupPicture/)                                |
| `groups.leaveGroup`                    | Метод производит выход пользователя текущего аккаунта из группового чата                                                  | [LeaveGroup](https://green-api.com/docs/api/groups/LeaveGroup/)                                          |
| `journals.getChatHistory`              | Метод возвращает историю сообщений чата                                                                                   | [GetChatHistory](https://green-api.com/docs/api/journals/GetChatHistory/)                                |
| `journals.getMessage`                  | Метод возвращает сообщение чата                                                                                           | [GetMessage](https://green-api.com/docs/api/journals/GetMessage/)                                        |       
| `journals.lastIncomingMessages`        | Метод возвращает крайние входящие сообщения аккаунта                                                                      | [LastIncomingMessages](https://green-api.com/docs/api/journals/LastIncomingMessages/)                    |
| `journals.lastOutgoingMessages`        | Метод возвращает крайние отправленные сообщения аккаунта                                                                  | [LastOutgoingMessages](https://green-api.com/docs/api/journals/LastOutgoingMessages/)                    |
| `queues.showMessagesQueue`             | Метод предназначен для получения списка сообщений, находящихся в очереди на отправку                                      | [ShowMessagesQueue](https://green-api.com/docs/api/queues/ShowMessagesQueue/)                            |
| `queues.clearMessagesQueue`            | Метод предназначен для очистки очереди сообщений на отправку                                                              | [ClearMessagesQueue](https://green-api.com/docs/api/queues/ClearMessagesQueue/)                          |
| `marking.readChat`                     | Метод предназначен для отметки сообщений в чате прочитанными                                                              | [ReadChat](https://green-api.com/docs/api/marks/ReadChat/)                                               |
| `receiving.receiveNotification`        | Метод предназначен для получения одного входящего уведомления из очереди уведомлений                                      | [ReceiveNotification](https://green-api.com/docs/api/receiving/technology-http-api/ReceiveNotification/) |
| `receiving.deleteNotification`         | Метод предназначен для удаления входящего уведомления из очереди уведомлений                                              | [DeleteNotification](https://green-api.com/docs/api/receiving/technology-http-api/DeleteNotification/)   |
| `receiving.downloadFile`               | Метод предназначен для скачивания принятых и отправленных файлов                                                          | [DownloadFile](https://green-api.com/docs/api/receiving/files/DownloadFile/)                             |
| `sending.sendMessage`                  | Метод предназначен для отправки текстового сообщения в личный или групповой чат                                           | [SendMessage](https://green-api.com/docs/api/sending/SendMessage/)                                       |
| `sending.sendFileByUpload`             | Метод предназначен для отправки файла, загружаемого через форму (form-data)                                               | [SendFileByUpload](https://green-api.com/docs/api/sending/SendFileByUpload/)                             |
| `sending.sendFileByUrl`                | Метод предназначен для отправки файла, загружаемого по ссылке                                                             | [SendFileByUrl](https://green-api.com/docs/api/sending/SendFileByUrl/)                                   |
| `sending.uploadFile`                   | Метод предназначен для загрузки файла в облачное хранилище, который можно отправить методом sendFileByUrl                 | [UploadFile](https://green-api.com/docs/api/sending/UploadFile/)                                         |
| `sending.sendLocation`                 | Метод предназначен для отправки сообщения геолокации                                                                      | [SendLocation](https://green-api.com/docs/api/sending/SendLocation/)                                     |
| `sending.sendContact`                  | Метод предназначен для отправки сообщения с контактом                                                                     | [SendContact](https://green-api.com/docs/api/sending/SendContact/)                                       |
| `sending.forwardMessages`              | Метод предназначен для пересылки сообщений в личный или групповой чат                                                     | [ForwardMessages](https://green-api.com/docs/api/sending/ForwardMessages/)                               |
| `sending.sendPoll`                     | Метод предназначен для отправки сообщения с опросом в личный или групповой чат                                            | [SendPoll](https://green-api.com/docs/api/sending/SendPoll/)                                             |
| `sending.sendInteractiveButtons`       | Метод предназначен для отправки сообщений с интерактивными кнопками                                                       | [sendInteractiveButtons](https://green-api.com/docs/api/sending/SendInteractiveButtons/)  |
| `sending.sendInteractiveButtonsReply`       | Метод предназначен для отправки сообщений с интерактивными кнопками с ответом                                        | [sendInteractiveButtonsReply](https://green-api.com/docs/api/sending/SendInteractiveButtonsReply/)  |
| `serviceMethods.checkWhatsapp`         | Метод проверяет наличие аккаунта WhatsApp на номере телефона                                                              | [CheckWhatsapp](https://green-api.com/docs/api/service/CheckWhatsapp/)                                   |
| `serviceMethods.getAvatar`             | Метод возвращает аватар корреспондента или группового чата                                                                | [GetAvatar](https://green-api.com/docs/api/service/GetAvatar/)                                           |
| `serviceMethods.getContacts`           | Метод предназначен для получения списка контактов текущего аккаунта                                                       | [GetContacts](https://green-api.com/docs/api/service/GetContacts/)                                       |
| `serviceMethods.getContactInfo`        | Метод предназначен для получения информации о контакте                                                                    | [GetContactInfo](https://green-api.com/docs/api/service/GetContactInfo/)                                 |
| `serviceMethods.deleteMessage`         | Метод удаляет сообщение из чата                                                                                           | [DeleteMessage](https://green-api.com/docs/api/service/deleteMessage/)                                   |
| `serviceMethods.editMessage`           | Метод изменяет сообщение в чате                                                                                           | [EditMessage](https://green-api.com/docs/api/service/editMessage/)                                   |
| `serviceMethods.archiveChat`           | Метод архивирует чат                                                                                                      | [ArchiveChat](https://green-api.com/docs/api/service/archiveChat/)                                       |
| `serviceMethods.unarchiveChat`         | Метод разархивирует чат                                                                                                   | [UnarchiveChat](https://green-api.com/docs/api/service/unarchiveChat/)                                   |
| `serviceMethods.setDisappearingChat`   | Метод предназначен для изменения настроек исчезающих сообщений в чатах                                                    | [SetDisappearingChat](https://green-api.com/docs/api/service/SetDisappearingChat/)                       |
| `webhooks.startReceivingNotifications` | Метод предназначен для старта получения новых уведомлений                                                                 |                                                                                                          |
| `webhooks.stopReceivingNotifications`  | Метод предназначен для остановки получения новых уведомлений                                                              |                                                                                                          |
| `partner.GetInstances`   | Метод предназначен для получения всех инстансов аккаунтов созданных партнёром.                                           | [GetInstances](https://green-api.com/docs/partners/getInstances/)                       |
| `partner.CreateInstance`   | Метод предназначен для создания инстанса от имени партнёра.                                           | [CreateInstance](https://green-api.com/docs/partners/createInstance/)                       |
| `partner.DeleteInstanceAccount`   | Метод предназначен для удаления инстанса аккаунта партнёра.                                           | [DeleteInstanceAccount](https://green-api.com/docs/partners/deleteInstanceAccount/)                       |

## Документация по методам сервиса

[https://green-api.com/docs/api/](https://green-api.com/docs/api/).

## Сторонние продукты

- [requests](https://requests.readthedocs.io/en/latest/) - для HTTP запросов.
- [aiohttp](https://docs.aiohttp.org/) - для асинхронных HTTP запросов.

## Лицензия

Лицензировано на условиях [Creative Commons Attribution-NoDerivatives 4.0 International (CC BY-ND 4.0)](https://creativecommons.org/licenses/by-nd/4.0/).
[LICENSE](../LICENSE).
