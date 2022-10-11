from os import environ

from whatsapp_api_client_python import greenAPI as greenAPI

# First you need to set the environment variables
ID_INSTANCE = environ['ID_INSTANCE']
API_TOKEN_INSTANCE = environ['API_TOKEN_INSTANCE']

restApi = greenAPI.RestApi(ID_INSTANCE, API_TOKEN_INSTANCE)

def main():
    chatIds = [
        "79001234567@c.us"
    ]
    resultCreate = restApi.groups.createGroup('GroupName', 
        chatIds)

    if resultCreate.code == 200:
        print(resultCreate.data)
        resultSend = restApi.sending.sendMessage(resultCreate.data['chatId'], 
            'Message text')
        if resultSend.code == 200:
            print(resultSend.data)
        else:
            print(resultSend.error)    
    else:
        print(resultCreate.error)

if __name__ == "__main__":
    main()