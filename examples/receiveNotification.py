from os import environ

from whatsapp_api_client_python import API as API

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
                body = resultReceive['body']
                idMessage = body['idMessage']
                senderData = body['senderData']
                messageData = body['messageData']
                if messageData['typeMessage'] == 'textMessage':
                    print(idMessage + ': ' 
                        + 'from ' + senderData['sender'] 
                        + ' (' + senderData['senderName'] + ') - '
                        + messageData['textMessageData']['textMessage'])
                restApi.receiving.deleteNotification(
                    resultReceive.data['receiptId'])    
    except KeyboardInterrupt:
        print('End receiving')
        pass

if __name__ == "__main__":
    main()