# whatsapp-api-client-python

[![Python application](https://github.com/green-api/whatsapp-api-client-python/actions/workflows/python-app.yml/badge.svg)](https://github.com/green-api/whatsapp-api-client-python/actions/workflows/python-app.yml)
[![Upload Python Package](https://github.com/green-api/whatsapp-api-client-python/actions/workflows/python-publish.yml/badge.svg)](https://github.com/green-api/whatsapp-api-client-python/actions/workflows/python-publish.yml)

Python библиотека для интеграции с мессенджером WhatsAPP через API сервиса [green-api.com](https://green-api.com). Чтобы воспользоваться библиотекой нужно получить регистрационный токен и id аккаунта в [личном кабинете](https://cabinet.green-api.com). Есть бесплатный тариф аккаунта разработчика.

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

Чтобы отправить сообщение или выполнить другой метод Green-API, аккаунт WhatsApp в приложении телефона должен быть в авторизованном состоянии. Для авторизации аккаунта перейдите в [личный кабинет](https://cabinet.green-api.com) и сканируйте QR-код с использованием прилоения WhatsApp.

## Примеры

### Инициализация

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

Ссылка на пример: [createGroupAndSendMessage.py](https://github.com/green-api/whatsapp-api-client-python/blob/master/examples/createGroupAndSendMessage.py)

### Получить входящие уведомления

```
resultReceive = restApi.receiving.receiveNotification()
```

Ссылка на пример: [receiveNotification.py](https://github.com/green-api/whatsapp-api-client-python/blob/master/examples/receiveNotification.py)

## Документация по методам сервиса

[https://github.com/green-api/docs](https://github.com/green-api/docs)

## Сторонние продукты

* [requests](https://requests.readthedocs.io) - для http запросов

## Лицензия

Лицензировано на условиях MIT. Смотрите файл [LICENSE](LICENSE)