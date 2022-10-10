from whatsapp_api_client_python.response import Response
from datetime import datetime
from enum import Enum


class TypeWebhook(Enum):
    INCOMING_MESSAGE_RECEIVED = 'incomingMessageReceived'
    OUTGOING_MESSAGE_RECEIVED = 'outgoingMessageReceived'
    OUTGOING_API_MESSAGE_RECEIVED = 'outgoingAPIMessageReceived'
    OUTGOING_MESSAGE_STATUS  = 'outgoingMessageStatus'
    STATE_INSTANCE_CHANGED  = 'stateInstanceChanged'
    STATUS_INSTANCE_CHANGED  = 'statusInstanceChanged'
    DEVICE_INFO  = 'deviceInfo'
    INCOMING_CALL  = 'incomingCall'

class TypeMessage(Enum):
    TEXT_MESSAGE = 'textMessage'
    IMAGE_MESSAGE = 'imageMessage'
    VIDEO_MESSAGE = 'videoMessage'
    DOCUMENT_MESSAGE  = 'documentMessage'
    AUDIO_MESSAGE  = 'audioMessage'
    LOCATION_MESSAGE  = 'locationMessage'
    CONTACT_MESSAGE  = 'contactMessage'
    EXTENDED_TEXT_MESSAGE  = 'extendedTextMessage'
    QUOTED_MESSAGE = 'quotedMessage'

class Webhooks:
    def __init__(self, restApi) -> None:
        self.restApi = restApi
        self.started = False

    def startReceivingNotifications(self) -> bool:
        self.started = True
        self.job()

    def stopReceivingNotifications(self) -> bool:
        self.started = False

    def onIncomingMessageReceived(body):
        idMessage = body['idMessage']
        eventDate = datetime.fromtimestamp(body['timestamp'])
        senderData = body['senderData']
        messageData = body['messageData']
        print(idMessage + ': ' 
            + 'At ' + eventDate + 'Incoming from ' \
            + senderData + ' message = ' + messageData)

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
        print('At ' + eventDate + ': ' + deviceData)

    def onOutgoingMessageReceived(body):
        idMessage = body['idMessage']
        eventDate = datetime.fromtimestamp(body['timestamp'])
        senderData = body['senderData']
        messageData = body['messageData']
        print(idMessage + ': ' 
            + 'At ' + eventDate + 'Outgoing from ' \
            + senderData + ' message = ' + messageData)

    def onOutgoingAPIMessageReceived(body):
        idMessage = body['idMessage']
        eventDate = datetime.fromtimestamp(body['timestamp'])
        senderData = body['senderData']
        messageData = body['messageData']
        print(idMessage + ': ' 
            + 'At ' + eventDate + ' API outgoing from ' + senderData + \
            ' message = ' + messageData)

    def onOutgoingMessageStatus(body):
        idMessage = body['idMessage']
        status = body['status']
        eventDate = datetime.fromtimestamp(body['timestamp'])
        print(idMessage + ': ' 
            + 'At ' + eventDate + ' status = ' + status)

    def onStateInstanceChanged(body):
        eventDate = datetime.fromtimestamp(body['timestamp'])
        stateInstance = body['stateInstance']
        print('At ' + eventDate + ' state instance = ' + stateInstance)

    def onStatusInstanceChanged(body):
        eventDate = datetime.fromtimestamp(body['timestamp'])
        statusInstance = body['statusInstance']
        print('At ' + eventDate + ' status instance = ' + statusInstance)

    def job(self) -> None:
        print('Incoming notifications are being received. '\
        'To interrupt, press Ctrl+C')
        try:
            while self.started == True:
                resultReceive = self.restApi.receiving.receiveNotification()
                if resultReceive.code == 200:
                    if resultReceive.data == None:
                        # There are no incoming notifications, 
                        # we send the request again
                        continue
                    body = resultReceive.data['body']
                    typeWebhook = body['typeWebhook']
                    if typeWebhook == TypeWebhook.INCOMING_MESSAGE_RECEIVED:
                        self.onIncomingMessageReceived(body)      
                    elif typeWebhook == TypeWebhook.DEVICE_INFO:   
                        self.onDeviceInfo(body)              
                    elif typeWebhook == TypeWebhook.INCOMING_CALL:
                        self.onIncomingCall(body)
                    elif typeWebhook == TypeWebhook.INCOMING_MESSAGE_RECEIVED:
                        self.onIncomingMessageReceived(body)
                    elif typeWebhook == TypeWebhook.OUTGOING_API_MESSAGE_RECEIVED:
                        self.onOutgoingAPIMessageReceived(body)
                    elif typeWebhook == TypeWebhook.OUTGOING_MESSAGE_RECEIVED:
                        self.onOutgoingMessageReceived(body)
                    elif typeWebhook == TypeWebhook.OUTGOING_MESSAGE_STATUS:
                        self.onOutgoingMessageStatus(body)
                    elif typeWebhook == TypeWebhook.STATE_INSTANCE_CHANGED:
                        self.onStateInstanceChanged(body)
                    elif typeWebhook == TypeWebhook.STATUS_INSTANCE_CHANGED:
                        self.onStatusInstanceChanged(body)    
                    self.restApi.receiving.deleteNotification(
                        resultReceive.data['receiptId'])
            print('End receiving')
        except KeyboardInterrupt:
            print('End receiving')
            pass
