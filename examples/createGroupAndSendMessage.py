from os import environ

from whatsapp_api_client_python import API as API

ID_INSTANCE = environ['ID_INSTANCE']
API_TOKEN_INSTANCE = environ['API_TOKEN_INSTANCE']

restApi = API.RestApi('https://api.green-api.com', 
                        ID_INSTANCE, 
                        API_TOKEN_INSTANCE)

def main():
    chatIds = [
        "79001234567@c.us"
    ]
    resultCreate = restApi.groups.createGroup('GroupName', 
        chatIds)

    if resultCreate.code == 200:
        resultSend = restApi.sending.sendMessage(resultCreate.data['chatId'], 
            'Message text')
        print(resultSend)

if __name__ == "__main__":
    main()