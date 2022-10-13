from os import environ
from datetime import datetime
import json
from whatsapp_api_client_python import greenAPI as greenAPI
from whatsapp_api_client_python.tools.webhooks import TypeWebhook as TypeWebhook


ID_INSTANCE = environ['ID_INSTANCE']
API_TOKEN_INSTANCE = environ['API_TOKEN_INSTANCE']

restApi = greenAPI.RestApi(ID_INSTANCE, API_TOKEN_INSTANCE)

def main():
   restApi.webhooks.startReceivingNotifications(onEvent)

def onEvent(typeWebhook, body):
   if typeWebhook == TypeWebhook.INCOMING_MESSAGE_RECEIVED.value:
      onIncomingMessageReceived(body)      
   elif typeWebhook == TypeWebhook.DEVICE_INFO.value:   
      onDeviceInfo(body)              
   elif typeWebhook == TypeWebhook.INCOMING_CALL.value:
      onIncomingCall(body)
   elif typeWebhook == TypeWebhook.INCOMING_MESSAGE_RECEIVED.value:
      onIncomingMessageReceived(body)
   elif typeWebhook == TypeWebhook.OUTGOING_API_MESSAGE_RECEIVED.value:
      onOutgoingAPIMessageReceived(body)
   elif typeWebhook == TypeWebhook.OUTGOING_MESSAGE_RECEIVED.value:
      onOutgoingMessageReceived(body)
   elif typeWebhook == TypeWebhook.OUTGOING_MESSAGE_STATUS.value:
      onOutgoingMessageStatus(body)
   elif typeWebhook == TypeWebhook.STATE_INSTANCE_CHANGED.value:
      onStateInstanceChanged(body)
   elif typeWebhook == TypeWebhook.STATUS_INSTANCE_CHANGED.value:
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