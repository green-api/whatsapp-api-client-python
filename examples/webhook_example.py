from os import environ
from typing import Union

from whatsapp_api_client_python import GreenAPI
from whatsapp_api_client_python.tools import Webhook

# First you need to set the environment variables.
ID_INSTANCE = environ["ID_INSTANCE"]
API_TOKEN_INSTANCE = environ["API_TOKEN_INSTANCE"]

greenAPI = GreenAPI(ID_INSTANCE, API_TOKEN_INSTANCE)


def main():
    webhook = Webhook(greenAPI)

    webhook.run_forever(handler)


def handler(type_webhook: str, body: Union[dict, list]):
    if type_webhook == "incomingMessageReceived":
        sender_data = body["senderData"]
        message_data = body["messageData"]

        type_message = message_data["typeMessage"]
        if type_message == "textMessage":
            text_message = message_data["textMessageData"]["textMessage"]

            greenAPI.sending.send_message(
                chatId="",
                message=f"You wrote: {text_message}."
            )

if __name__ == "__main__":
    main()

from os import environ
from datetime import datetime
import json
from whatsapp_api_client_python import GreenAPI

ID_INSTANCE = environ['ID_INSTANCE']
API_TOKEN_INSTANCE = environ['API_TOKEN_INSTANCE']

greenAPI = GreenAPI(ID_INSTANCE, API_TOKEN_INSTANCE)


def main():
    greenAPI.webhooks.startReceivingNotifications(onEvent)


def onEvent(typeWebhook, body):
    if typeWebhook == 'incomingMessageReceived':
        onIncomingMessageReceived(body)
    elif typeWebhook == 'deviceInfo':
        onDeviceInfo(body)
    elif typeWebhook == 'incomingCall':
        onIncomingCall(body)
    elif typeWebhook == 'outgoingAPIMessageReceived':
        onOutgoingAPIMessageReceived(body)
    elif typeWebhook == 'outgoingMessageReceived':
        onOutgoingMessageReceived(body)
    elif typeWebhook == 'outgoingMessageStatus':
        onOutgoingMessageStatus(body)
    elif typeWebhook == 'stateInstanceChanged':
        onStateInstanceChanged(body)
    elif typeWebhook == 'statusInstanceChanged':
        onStatusInstanceChanged(body)


def onIncomingMessageReceived(body):
    idMessage = body['idMessage']
    eventDate = datetime.fromtimestamp(body['timestamp'])
    senderData = body['senderData']
    messageData = body['messageData']
    print(idMessage + ': '
          + 'At ' + str(eventDate) + ' Incoming from ' \
          + json.dumps(senderData, ensure_ascii=False) \
          + ' message = ' + json.dumps(messageData, ensure_ascii=False))


def onIncomingCall(body):
    idMessage = body['idMessage']
    eventDate = datetime.fromtimestamp(body['timestamp'])
    fromWho = body['from']
    print(idMessage + ': '
          + 'Call from ' + fromWho
          + ' at ' + str(eventDate))


def onDeviceInfo(body):
    eventDate = datetime.fromtimestamp(body['timestamp'])
    deviceData = body['deviceData']
    print('At ' + str(eventDate) + ': ' \
          + json.dumps(deviceData, ensure_ascii=False))


def onOutgoingMessageReceived(body):
    idMessage = body['idMessage']
    eventDate = datetime.fromtimestamp(body['timestamp'])
    senderData = body['senderData']
    messageData = body['messageData']
    print(idMessage + ': '
          + 'At ' + str(eventDate) + ' Outgoing from ' \
          + json.dumps(senderData, ensure_ascii=False) \
          + ' message = ' + json.dumps(messageData, ensure_ascii=False))


def onOutgoingAPIMessageReceived(body):
    idMessage = body['idMessage']
    eventDate = datetime.fromtimestamp(body['timestamp'])
    senderData = body['senderData']
    messageData = body['messageData']
    print(idMessage + ': '
          + 'At ' + str(eventDate) + ' API outgoing from ' \
          + json.dumps(senderData, ensure_ascii=False) + \
          ' message = ' + json.dumps(messageData, ensure_ascii=False))


def onOutgoingMessageStatus(body):
    idMessage = body['idMessage']
    status = body['status']
    eventDate = datetime.fromtimestamp(body['timestamp'])
    print(idMessage + ': '
          + 'At ' + str(eventDate) + ' status = ' + status)


def onStateInstanceChanged(body):
    eventDate = datetime.fromtimestamp(body['timestamp'])
    stateInstance = body['stateInstance']
    print('At ' + str(eventDate) + ' state instance = ' \
          + json.dumps(stateInstance, ensure_ascii=False))


def onStatusInstanceChanged(body):
    eventDate = datetime.fromtimestamp(body['timestamp'])
    statusInstance = body['statusInstance']
    print('At ' + str(eventDate) + ' status instance = ' \
          + json.dumps(statusInstance, ensure_ascii=False))


if __name__ == "__main__":
    main()
