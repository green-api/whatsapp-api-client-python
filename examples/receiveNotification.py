from os import environ
from whatsapp_api_client_python import API as API
from datetime import datetime


ID_INSTANCE = environ['ID_INSTANCE']
API_TOKEN_INSTANCE = environ['API_TOKEN_INSTANCE']

restApi = API.RestApi('https://api.green-api.com', 
                        ID_INSTANCE, 
                        API_TOKEN_INSTANCE)

def main():
    try:
        while True:
            resultReceive = restApi.receiving.receiveNotification()
            if resultReceive.code == 200:
                if resultReceive.data == None:
                    continue
                body = resultReceive.data['body']
                idMessage = body['idMessage']
                if body['typeWebhook'] == 'incomingMessageReceived':
                    senderData = body['senderData']
                    messageData = body['messageData']
                    if messageData['typeMessage'] == 'textMessage':
                        message = messageData['textMessageData']['textMessage']
                    elif messageData['typeMessage'] == 'extendedTextMessage':
                        message = messageData['extendedTextMessageData']['text']
                    elif messageData['typeMessage'] in ('imageMessage', 
                            'videoMessage', 'documentMessage', 'audioMessage'):
                        message = messageData['fileMessageData']['downloadUrl']
                    elif messageData['typeMessage'] == 'locationMessage':
                        message = str(messageData['locationMessageData']\
                            ['latitude']) + ', ' \
                            + str(messageData['locationMessageData']\
                            ['longitude'])
                    elif messageData['typeMessage'] == 'contactMessage':
                        message = messageData['contactMessageData']['vcard']
                    elif messageData['typeMessage'] == 'quotedMessage':
                        message = messageData['extendedTextMessageData']['text']
                    print(idMessage + ': ' 
                        + 'from ' + senderData['sender'] 
                        + ' (' + senderData['senderName'] + ') - ' + message)
                elif body['typeWebhook'] == 'incomingCall':
                    fromWho = body['from']
                    callDate = datetime.fromtimestamp(body['timestamp'])
                    print(idMessage + ': ' 
                        + 'Call from ' + fromWho 
                        + ' at ' + str(callDate))
                restApi.receiving.deleteNotification(
                    resultReceive.data['receiptId'])    
    except KeyboardInterrupt:
        print('End receiving')
        pass

if __name__ == "__main__":
    main()