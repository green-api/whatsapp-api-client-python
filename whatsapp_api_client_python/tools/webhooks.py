from whatsapp_api_client_python.response import Response
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

    def startReceivingNotifications(self, onEvent) -> bool:
        self.started = True
        self.job(onEvent)

    def stopReceivingNotifications(self) -> bool:
        self.started = False

    
    def job(self, onEvent) -> None:
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
                    onEvent(typeWebhook, body)    
                    self.restApi.receiving.deleteNotification(
                        resultReceive.data['receiptId'])
            print('End receiving')
        except KeyboardInterrupt:
            print('End receiving')
            pass