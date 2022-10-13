# whatsapp-api-client-python

[![Python application](https://github.com/green-api/whatsapp-api-client-python/actions/workflows/python-app.yml/badge.svg)](https://github.com/green-api/whatsapp-api-client-python/actions/workflows/python-app.yml)
[![Upload Python Package](https://github.com/green-api/whatsapp-api-client-python/actions/workflows/python-publish.yml/badge.svg)](https://github.com/green-api/whatsapp-api-client-python/actions/workflows/python-publish.yml)

Python библиотека для интеграции с мессенджером WhatsAPP через API сервиса [green-api.com](https://green-api.com). Чтобы воспользоваться библиотекой нужно получить регистрационный токен и id аккаунта в [личном кабинете](https://console.green-api.com). Есть бесплатный тариф аккаунта разработчика.

## API

Документация к REST API находится по [ссылке](https://green-api.com/docs/api/). Библиотека является оберткой к REST API, поэтому документация по ссылке выше применима и к самой библиотеке.

## Установка

```
pip install whatsapp-api-client-python
```

## Import 

```
from whatsapp_api_client_python import API
```
## Авторизация 

Чтобы отправить сообщение или выполнить другой метод Green-API, аккаунт WhatsApp в приложении телефона должен быть в авторизованном состоянии. Для авторизации аккаунта перейдите в [личный кабинет](https://console.green-api.com) и сканируйте QR-код с использованием приложения WhatsApp.

## Примеры

### Как инициализировать объект

```
restApi = API.RestApi('https://api.green-api.com', 
                        ID_INSTANCE, 
                        API_TOKEN_INSTANCE)
```

### Отправка текстового сообщения на номер WhatsApp

```
result = restApi.sending.sendMessage('79001234567@g.us', 'Message text')
```

Ссылка на пример: [sendText.py](https://github.com/green-api/whatsapp-api-client-python/blob/master/examples/sendText.py)

Обратите внимание, что ключи можно получать из переменных среды:
```
from os import environ

ID_INSTANCE = environ['ID_INSTANCE']
API_TOKEN_INSTANCE = environ['API_TOKEN_INSTANCE']
```

### Отправка картинки по URL

```
result = restApi.sending.sendFileByUrl('120363025955348359@g.us', 
        'https://www.google.ru/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png', 
        'googlelogo_color_272x92dp.png', 'Google logo')
```

Ссылка на пример: [sendPictureByLink.py](https://github.com/green-api/whatsapp-api-client-python/blob/master/examples/sendPictureByLink.py)

### Отправка картинки загрузкой с диска

```
result = restApi.sending.sendFileByUpload('120363025955348359@g.us', 
        'C:\Games\PicFromDisk.png', 
        'PicFromDisk.png', 'Picture from disk')
```

Ссылка на пример: [sendPictureByUpload.py](https://github.com/green-api/whatsapp-api-client-python/blob/master/examples/sendPictureByUpload.py)

### Создание группы и отправка сообщения в эту группу

```
chatIds = [
    "79001234567@c.us"
]
resultCreate = restApi.groups.createGroup('GroupName', 
    chatIds)

if resultCreate.code == 200:
    resultSend = restApi.sending.sendMessage(resultCreate.data['chatId'], 
        'Message text')
```

ВАЖНО: Если попытаться создать группу с несуществующим номером WhatsApp 
может заблокировать номер отправителя. Номер в примере не существует.

Ссылка на пример: [createGroupAndSendMessage.py](https://github.com/green-api/whatsapp-api-client-python/blob/master/examples/createGroupAndSendMessage.py)

### Получить входящие уведомления

```
resultReceive = restApi.receiving.receiveNotification()
```

## Список примеров

Описание |  Модуль
----- | ----- 
Пример отправки текста | [sendText.py](https://github.com/green-api/whatsapp-api-client-python/blob/master/examples/sendText.py)
Пример отправки картинки по URL | [sendPictureByLink.py](https://github.com/green-api/whatsapp-api-client-python/blob/master/examples/sendPictureByLink.py)
Пример отправки картинки загрузкой с диска | [sendPictureByUpload.py](https://github.com/green-api/whatsapp-api-client-python/blob/master/examples/sendPictureByUpload.py)
Пример создание группы и отправка сообщения в группу | [createGroupAndSendMessage.py](https://github.com/green-api/whatsapp-api-client-python/blob/master/examples/createGroupAndSendMessage.py)
Пример получения входящих уведомлений | [receiveNotification.py](https://github.com/green-api/whatsapp-api-client-python/blob/master/examples/receiveNotification.py)


## Полный список методов библиотеки

Метод | Описание |  Документация
----- | ----- | ----- 
`account.getSettings` | Метод предназначен для получения текущих настроек аккаунта | [GetSettings.md](https://github.com/green-api/docs/blob/master/ru/docs/api/account/GetSettings.md)
`account.getStateInstance` | Метод предназначен для получения состояния аккаунта | [GetStateInstance.md](https://github.com/green-api/docs/blob/master/ru/docs/api/account/GetStateInstance.md)
`account.getStatusInstance` | Метод предназначен для получения состояния сокета соединения инстанса аккаунта с WhatsApp | [GetStatusInstance.md](https://github.com/green-api/docs/blob/master/ru/docs/api/account/GetStatusInstance.md)
`account.logout` | Метод предназначен для разлогинивания аккаунта | [Logout.md](https://github.com/green-api/docs/blob/master/ru/docs/api/account/Logout.md)
`account.qr` | Метод предназначен для получения QR-кода | [QR.md](https://github.com/green-api/docs/blob/master/ru/docs/api/account/QR.md)
`account.reboot` | Метод предназначен для перезапуска аккаунта | [Reboot.md](https://github.com/green-api/docs/blob/master/ru/docs/api/account/Reboot.md)
`account.setProfilePicture` | Метод предназначен для установки аватара аккаунта | [SetProfilePicture.md](https://github.com/green-api/docs/blob/master/ru/docs/api/account/SetProfilePicture.md)
`account.setSettings` | Метод предназначен для установки настроек аккаунта | [SetSettings.md](https://github.com/green-api/docs/blob/master/ru/docs/api/account/SetSettings.md)
`account.setSystemProxy` | Метод предназначен для установки системного прокси. Нужно используйте метод, когда требуется сбросить пользовательские настройки прокси на системные | [SetSystemProxy.md](https://github.com/green-api/docs/blob/master/ru/docs/api/account/SetSystemProxy.md)
`groups.addGroupParticipant` | Метод добавляет участника в групповой чат | [AddGroupParticipant.md](https://github.com/green-api/docs/blob/master/ru/docs/api/groups/AddGroupParticipant.md)
`groups.createGroup` | Метод добавляет участника в групповой чат. ВАЖНО: Если попытаться создать группу с несуществующим номером WhatsApp может заблокировать номер отправителя. | [CreateGroup.md](https://github.com/green-api/docs/blob/master/ru/docs/api/groups/CreateGroup.md)
`groups.getGroupData` | Метод получает данные группового чата | [GetGroupData.md](https://github.com/green-api/docs/blob/master/ru/docs/api/account/GetGroupData.md)
`groups.leaveGroup` | Метод производит выход пользователя текущего аккаунта из группового чата | [LeaveGroup.md](https://github.com/green-api/docs/blob/master/ru/docs/api/groups/LeaveGroup.md)
`groups.removeAdmin` | Метод лишает участника прав администрирования группового чата | [RemoveAdmin.md](https://github.com/green-api/docs/blob/master/ru/docs/api/groups/RemoveAdmin.md)
`groups.removeGroupParticipant` | Метод удаляет участника из группового чата | [RemoveGroupParticipant.md](https://github.com/green-api/docs/blob/master/ru/docs/api/groups/RemoveGroupParticipant.md)
`groups.setGroupAdmin` | Метод назначает участника группового чата администратором | [SetGroupAdmin.md](https://github.com/green-api/docs/blob/master/ru/docs/api/groups/SetGroupAdmin.md)
`groups.setGroupPicture` | Метод устанавливает аватар группы | [SetGroupPicture.md](https://github.com/green-api/docs/blob/master/ru/docs/api/groups/SetGroupPicture.md)
`groups.updateGroupName` | Метод изменяет наименование группового чата | [UpdateGroupName.md](https://github.com/green-api/docs/blob/master/ru/docs/api/groups/UpdateGroupName.md)
`journals.getChatHistory` | Метод возвращает историю сообщений чата | [GetChatHistory.md](https://github.com/green-api/docs/blob/master/ru/docs/api/journals/GetChatHistory.md)
`journals.lastIncomingMessages` | Метод возвращает крайние входящие сообщения аккаунта. По умолчанию возвращаются последние сообщения за 24 часа | [GetChatHistory.md](https://github.com/green-api/docs/blob/master/ru/docs/api/journals/LastIncomingMessages.md)
`journals.lastOutgoingMessages` | Метод возвращает крайние отправленные сообщения аккаунта. По умолчанию возвращаются последние сообщения за 24 часа | [LastOutgoingMessages.md](https://github.com/green-api/docs/blob/master/ru/docs/api/journals/LastOutgoingMessages.md)
`marking.readChat` | Метод предназначен для отметки сообщений в чате прочитанными. Могут быть отмечены прочитанными все сообщения в чате или только одно заданное сообщение | [ReadChat.md](https://github.com/green-api/docs/blob/master/ru/docs/api/marks/ReadChat.md)
`device.getDeviceInfo` | Метод предназначен для получения информации об устройстве (телефоне), на котором запущено приложение WhatsApp Business | [GetDeviceInfo.md](https://github.com/green-api/docs/blob/master/ru/docs/api/phone/GetDeviceInfo.md)
`queues.clearMessagesQueue` | Метод предназначен для очистки очереди сообщений на отправку | [ClearMessagesQueue.md](https://github.com/green-api/docs/blob/master/ru/docs/api/queues/ClearMessagesQueue.md)
`queues.showMessagesQueue` | Метод предназначен для получения списка сообщений, находящихся в очереди на отправку | [ShowMessagesQueue.md](https://github.com/green-api/docs/blob/master/ru/docs/api/queues/ShowMessagesQueue.md)
`receiving.deleteNotification` | Метод предназначен для удаления входящего уведомления из очереди уведомлений | [DeleteNotification.md](https://github.com/green-api/docs/blob/master/ru/docs/api/receiving/technology-http-api/DeleteNotification.md)
`receiving.receiveNotification` | Метод предназначен для получения одного входящего уведомления из очереди уведомлений | [ReceiveNotification.md](https://github.com/green-api/docs/blob/master/ru/docs/api/receiving/technology-http-api/ReceiveNotification.md)
`sending.sendButtons` | Метод предназначен для отправки сообщения с кнопками в личный или групповой чат | [SendButtons.md](https://github.com/green-api/docs/blob/master/ru/docs/api/sending/SendButtons.md)
`sending.sendContact` | Метод предназначен для отправки сообщения с контактом | [SendContact.md](https://github.com/green-api/docs/blob/master/ru/docs/api/sending/SendContact.md)
`sending.sendFileByUpload` | Метод предназначен для отправки файла, загружаемого через форму | [SendFileByUpload.md](https://github.com/green-api/docs/blob/master/ru/docs/api/sending/SendFileByUpload.md)
`sending.sendFileByUrl` | Метод предназначен для отправки файла, загружаемого по ссылке | [SendFileByUrl.md](https://github.com/green-api/docs/blob/master/ru/docs/api/sending/SendFileByUrl.md)
`sending.sendLink` | Метод предназначен для отправки сообщения со ссылкой, по которой будут добавлены превью изображения, заголовок и описание | [SendLink.md](https://github.com/green-api/docs/blob/master/ru/docs/api/sending/SendLink.md)
`sending.sendListMessage` | Метод предназначен для отправки сообщения с кнопкой выбора из списка значений в личный или групповой чат | [SendListMessage.md](https://github.com/green-api/docs/blob/master/ru/docs/api/sending/SendListMessage.md)
`sending.sendLocation` | Метод предназначен для отправки сообщения геолокации | [SendLocation.md](https://github.com/green-api/docs/blob/master/ru/docs/api/sending/SendLocation.md)
`sending.sendMessage` | Метод предназначен для отправки текстового сообщения в личный или групповой чат | [SendMessage.md](https://github.com/green-api/docs/blob/master/ru/docs/api/sending/SendMessage.md)
`sending.sendTemplateButtons` | Метод предназначен для отправки сообщения с интерактивными кнопками из перечня шаблонов в личный или групповой чат | [SendTemplateButtons.md](https://github.com/green-api/docs/blob/master/ru/docs/api/sending/SendTemplateButtons.md)
`serviceMethods.checkWhatsapp` | Метод проверяет наличие аккаунта WhatsApp на номере телефона | [CheckWhatsapp.md](https://github.com/green-api/docs/blob/master/ru/docs/api/service/CheckWhatsapp.md)
`serviceMethods.getAvatar` | Метод возвращает аватар корреспондента или группового чата | [GetAvatar.md](https://github.com/green-api/docs/blob/master/ru/docs/api/service/GetAvatar.md)
`serviceMethods.getContactInfo` | Метод предназначен для получения информации о контакте | [GetContactInfo.md](https://github.com/green-api/docs/blob/master/ru/docs/api/service/GetContactInfo.md)
`serviceMethods.getContacts` | Метод предназначен для получения списка контактов текущего аккаунта | [GetContacts.md](https://github.com/green-api/docs/blob/master/ru/docs/api/service/GetContacts.md)
`serviceMethods.setDisappearingChat` | Метод предназначен для изменения настроек исчезающих сообщений в чатах. Нужно использовать стандартные настройки приложения: 0 (выключено), 86400 (24 часа), 604800 (7 дней), 7776000 (90 дней) | [SetDisappearingChat.md](https://github.com/green-api/docs/blob/master/ru/docs/api/service/SetDisappearingChat.md)
`serviceMethods.archiveChat` | Метод архивирует чат. Архивировать можно чаты, в которых есть хотя бы одно входящее сообщение | [ArchiveChat.md](https://github.com/green-api/docs/blob/master/ru/docs/api/service/ArchiveChat.md)
`serviceMethods.deleteMessage` | Метод удаляет сообщение из чата | [DeleteMessage.md](https://github.com/green-api/docs/blob/master/ru/docs/api/service/deleteMessage.md)
`serviceMethods.unarchiveChat` | Метод разархивирует чат | [UnarchiveChat.md](https://github.com/green-api/docs/blob/master/ru/docs/api/service/UnarchiveChat.md)
`serviceMethods.setDisappearingChat` | Метод предназначен для изменения настроек исчезающих сообщений в чатах | [SetDisappearingChat.md](https://github.com/green-api/docs/blob/master/ru/docs/api/service/SetDisappearingChat.md)
`webhooks.startReceivingNotifications` | Метод предназначен для запуска получения вебхуков | <библиотечный метод>
`webhooks.stopReceivingNotifications` | Метод предназначен для остановки получения вебхуков | <библиотечный метод>

## Документация по методам сервиса

[https://green-api.com/docs/api/](https://green-api.com/docs/api/)

## Сторонние продукты

* [requests](https://requests.readthedocs.io) - для http запросов

## Лицензия

Лицензировано на условиях MIT. Смотрите файл [LICENSE](LICENSE)
