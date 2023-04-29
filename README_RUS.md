# whatsapp-api-client-python

[![Python application](https://github.com/green-api/whatsapp-api-client-python/actions/workflows/python-app.yml/badge.svg)](https://github.com/green-api/whatsapp-api-client-python/actions/workflows/python-app.yml)
[![Upload Python Package](https://github.com/green-api/whatsapp-api-client-python/actions/workflows/python-publish.yml/badge.svg)](https://github.com/green-api/whatsapp-api-client-python/actions/workflows/python-publish.yml)

- [English documentation](README.md)

Python библиотека для интеграции с мессенджером WhatsAPP через API сервиса [green-api.com](https://green-api.com). Чтобы воспользоваться библиотекой нужно получить регистрационный токен и id аккаунта в [личном кабинете](https://console.green-api.com). Есть бесплатный тариф аккаунта разработчика.

## API

Документация к REST API находится по [ссылке](https://green-api.com/docs/api/). Библиотека является оберткой к REST API, поэтому документация по ссылке выше применима и к самой библиотеке.

## Установка

```shell
pip install whatsapp-api-client-python
```

## Авторизация 

Чтобы отправить сообщение или выполнить другой метод Green-API, аккаунт WhatsApp в приложении телефона должен быть в авторизованном состоянии. Для авторизации аккаунта перейдите в [личный кабинет](https://console.green-api.com) и сканируйте QR-код с использованием приложения WhatsApp.

## Примеры

### Как инициализировать объект

```python
greenAPI = API.GreenApi(ID_INSTANCE, API_TOKEN_INSTANCE)
```

### Отправка текстового сообщения на номер WhatsApp

```python
result = greenAPI.sending.sendMessage('79001234567@g.us', 'Message text')
```

Ссылка на пример: [sendTextMessage.py](https://github.com/green-api/whatsapp-api-client-python/blob/master/examples/sendTextMessage.py)

Обратите внимание, что ключи можно получать из переменных среды:
```python
from os import environ

ID_INSTANCE = environ['ID_INSTANCE']
API_TOKEN_INSTANCE = environ['API_TOKEN_INSTANCE']
```

### Отправка картинки по URL

```python
result = greenAPI.sending.sendFileByUrl('120363025955348359@g.us', 
        'https://www.google.ru/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png', 
        'googlelogo_color_272x92dp.png', 'Google logo')
```

Ссылка на пример: [sendPictureByLink.py](https://github.com/green-api/whatsapp-api-client-python/blob/master/examples/sendPictureByLink.py)

### Отправка картинки загрузкой с диска

```python
result = greenAPI.sending.sendFileByUpload('120363025955348359@g.us', 
        'C:\\Games\\PicFromDisk.png', 
        'PicFromDisk.png', 'Picture from disk')
```

Ссылка на пример: [sendPictureByUpload.py](https://github.com/green-api/whatsapp-api-client-python/blob/master/examples/sendPictureByUpload.py)

### Создание группы и отправка сообщения в эту группу

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

ВАЖНО: Если попытаться создать группу с несуществующим номером WhatsApp 
может заблокировать номер отправителя. Номер в примере не существует.

Ссылка на пример: [createGroupAndSendMessage.py](https://github.com/green-api/whatsapp-api-client-python/blob/master/examples/createGroupAndSendMessage.py)

### Получение входящих сообщений через HTTP API

Общая концепция получения данных в Green API описана [здесь](https://green-api.com/docs/api/receiving/)
Для старта получения сообщений через HTTP API требуется выполнить метод библиотеки:

```python
greenAPI.webhooks.startReceivingNotifications(onEvent)
```

onEvent - ваш метод, который должен содержать параметры:
Параметр |  Описание
----- | -----
typeWebhook | тип полученного сообщения (строка)
body | тело сообщения (json)

Типы и форматы тел сообщений [здесь](https://green-api.com/docs/api/receiving/notifications-format/)

Этот метод будет вызываться при получении входящего сообщения. Далее обрабатываете сообщения согласно бизнес-логике вашей системы.

## Список примеров

Описание |  Модуль
----- | ----- 
Пример отправки текста | [sendTextMessage.py](https://github.com/green-api/whatsapp-api-client-python/blob/master/examples/sendTextMessage.py)
Пример отправки картинки по URL | [sendPictureByLink.py](https://github.com/green-api/whatsapp-api-client-python/blob/master/examples/sendPictureByLink.py)
Пример отправки картинки загрузкой с диска | [sendPictureByUpload.py](https://github.com/green-api/whatsapp-api-client-python/blob/master/examples/sendPictureByUpload.py)
Пример создание группы и отправка сообщения в группу | [createGroupAndSendMessage.py](https://github.com/green-api/whatsapp-api-client-python/blob/master/examples/createGroupAndSendMessage.py)
Пример получения входящих уведомлений | [receiveNotification.py](https://github.com/green-api/whatsapp-api-client-python/blob/master/examples/receiveNotification.py)


## Полный список методов библиотеки

| Метод API                              | Описание                                                                                                                  | Documentation link                                                                                       |
|----------------------------------------|---------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| `account.getSettings`                  | Метод предназначен для получения текущих настроек аккаунта                                                                | [GetSettings](https://green-api.com/docs/api/account/GetSettings/)                                       |
| `account.setSettings`                  | Метод предназначен для установки настроек аккаунта                                                                        | [SetSettings](https://green-api.com/docs/api/account/SetSettings/)                                       |
| `account.getStateInstance`             | Метод предназначен для получения состояния аккаунта                                                                       | [GetStateInstance](https://green-api.com/docs/api/account/GetStateInstance/)                             |
| `account.getStatusInstance`            | Метод предназначен для получения состояния сокета соединения инстанса аккаунта с WhatsApp                                 | [GetStatusInstance](https://green-api.com/docs/api/account/GetStatusInstance/)                           |
| `account.reboot`                       | Метод предназначен для перезапуска аккаунта                                                                               | [Reboot](https://green-api.com/docs/api/account/Reboot/)                                                 |
| `account.logout`                       | Метод предназначен для разлогинивания аккаунта                                                                            | [Logout](https://green-api.com/docs/api/account/Logout/)                                                 |
| `account.qr`                           | Метод предназначен для получения QR-кода                                                                                  | [QR](https://green-api.com/docs/api/account/QR/)                                                         |
| `account.setProfilePicture`            | Метод предназначен для установки аватара аккаунта                                                                         | [SetProfilePicture](https://green-api.com/docs/api/account/SetProfilePicture/)                           |
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
| `journals.get_chat_history`            | Метод возвращает историю сообщений чата                                                                                   | [GetChatHistory](https://green-api.com/docs/api/journals/GetChatHistory/)                                |
| `journals.get_message`                 | Метод возвращает сообщение чата                                                                                           | [GetMessage](https://green-api.com/docs/api/journals/GetMessage/)                                        |       
| `journals.last_incoming_messages`      | Метод возвращает крайние входящие сообщения аккаунта                                                                      | [LastIncomingMessages](https://green-api.com/docs/api/journals/LastIncomingMessages/)                    |
| `journals.last_outgoing_messages`      | Метод возвращает крайние отправленные сообщения аккаунта                                                                  | [LastOutgoingMessages](https://green-api.com/docs/api/journals/LastOutgoingMessages/)                    |
| `queues.showMessagesQueue`             | Метод предназначен для получения списка сообщений, находящихся в очереди на отправку                                      | [ShowMessagesQueue](https://green-api.com/docs/api/queues/ShowMessagesQueue/)                            |
| `queues.clearMessagesQueue`            | Метод предназначен для очистки очереди сообщений на отправку                                                              | [ClearMessagesQueue](https://green-api.com/docs/api/queues/ClearMessagesQueue/)                          |
| `marking.readChat`                     | Метод предназначен для отметки сообщений в чате прочитанными                                                              | [ReadChat](https://green-api.com/docs/api/marks/ReadChat/)                                               |
| `receiving.receiveNotification`        | Метод предназначен для получения одного входящего уведомления из очереди уведомлений                                      | [ReceiveNotification](https://green-api.com/docs/api/receiving/technology-http-api/ReceiveNotification/) |
| `receiving.deleteNotification`         | Метод предназначен для удаления входящего уведомления из очереди уведомлений                                              | [DeleteNotification](https://green-api.com/docs/api/receiving/technology-http-api/DeleteNotification/)   |
| `receiving.downloadFile`               | Метод предназначен для скачивания принятых и отправленных файлов                                                          | [DownloadFile](https://green-api.com/docs/api/receiving/files/DownloadFile/)                             |
| `sending.sendMessage`                  | Метод предназначен для отправки текстового сообщения в личный или групповой чат                                           | [SendMessage](https://green-api.com/docs/api/sending/SendMessage/)                                       |
| `sending.sendButtons`                  | Метод предназначен для отправки сообщения с кнопками в личный или групповой чат                                           | [SendButtons](https://green-api.com/docs/api/sending/SendButtons/)                                       |
| `sending.sendTemplateButtons`          | Метод предназначен для отправки сообщения с интерактивными кнопками из перечня шаблонов в личный или групповой чат        | [SendTemplateButtons](https://green-api.com/docs/api/sending/SendTemplateButtons/)                       |
| `sending.sendListMessage`              | Метод предназначен для отправки сообщения с кнопкой выбора из списка значений в личный или групповой чат                  | [SendListMessage](https://green-api.com/docs/api/sending/SendListMessage/)                               |
| `sending.sendFileByUpload`             | Метод предназначен для отправки файла, загружаемого через форму (form-data)                                               | [SendFileByUpload](https://green-api.com/docs/api/sending/SendFileByUpload/)                             |
| `sending.sendFileByUrl`                | Метод предназначен для отправки файла, загружаемого по ссылке                                                             | [SendFileByUrl](https://green-api.com/docs/api/sending/SendFileByUrl/)                                   |
| `sending.sendLocation`                 | Метод предназначен для отправки сообщения геолокации                                                                      | [SendLocation](https://green-api.com/docs/api/sending/SendLocation/)                                     |
| `sending.sendContact`                  | Метод предназначен для отправки сообщения с контактом                                                                     | [SendContact](https://green-api.com/docs/api/sending/SendContact/)                                       |
| `sending.sendLink`                     | Метод предназначен для отправки сообщения со ссылкой, по которой будут добавлены превью изображения, заголовок и описание | [SendLink](https://green-api.com/docs/api/sending/SendLink/)                                             |
| `sending.forwardMessages`              | Метод предназначен для пересылки сообщений в личный или групповой чат                                                     | [ForwardMessages](https://green-api.com/docs/api/sending/ForwardMessages/)                               |
| `serviceMethods.checkWhatsapp`         | Метод проверяет наличие аккаунта WhatsApp на номере телефона                                                              | [CheckWhatsapp](https://green-api.com/docs/api/service/CheckWhatsapp/)                                   |
| `serviceMethods.getAvatar`             | Метод возвращает аватар корреспондента или группового чата                                                                | [GetAvatar](https://green-api.com/docs/api/service/GetAvatar/)                                           |
| `serviceMethods.getContacts`           | Метод предназначен для получения списка контактов текущего аккаунта                                                       | [GetContacts](https://green-api.com/docs/api/service/GetContacts/)                                       |
| `serviceMethods.getContactInfo`        | Метод предназначен для получения информации о контакте                                                                    | [GetContactInfo](https://green-api.com/docs/api/service/GetContactInfo/)                                 |
| `serviceMethods.deleteMessage`         | Метод удаляет сообщение из чата                                                                                           | [DeleteMessage](https://green-api.com/docs/api/service/deleteMessage/)                                   |
| `serviceMethods.archiveChat`           | Метод архивирует чат                                                                                                      | [ArchiveChat](https://green-api.com/docs/api/service/archiveChat/)                                       |
| `serviceMethods.unarchiveChat`         | Метод разархивирует чат                                                                                                   | [UnarchiveChat](https://green-api.com/docs/api/service/unarchiveChat/)                                   |
| `serviceMethods.setDisappearingChat`   | Метод предназначен для изменения настроек исчезающих сообщений в чатах                                                    | [SetDisappearingChat](https://green-api.com/docs/api/service/SetDisappearingChat/)                       |
| `webhooks.startReceivingNotifications` | Метод предназначен для старта получения новых уведомлений                                                                 |                                                                                                          |
| `webhooks.stopReceivingNotifications`  | Метод предназначен для остановки получения новых уведомлений                                                              |                                                                                                          |

## Документация по методам сервиса

[https://green-api.com/docs/api/](https://green-api.com/docs/api/)

## Сторонние продукты

* [requests](https://requests.readthedocs.io) - для http запросов

## Лицензия

Лицензировано на условиях MIT. Смотрите файл [LICENSE](LICENSE)

[![CC BY-ND 4.0][cc-by-nd-shield]][cc-by-nd]

Эта работа распространяется под лицензией
[Creative Commons Attribution-NoDerivatives 4.0 International License][cc-by-nd].

[cc-by-nd]: https://creativecommons.org/licenses/by-nd/4.0/
[cc-by-nd-shield]: https://img.shields.io/badge/License-CC%20BY--ND%204.0-lightgrey.svg

Пожалуйста, смотрите файл [LICENSE](LICENSE)
