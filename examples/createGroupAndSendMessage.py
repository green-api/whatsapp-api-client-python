from os import environ

from whatsapp_api_client_python import greenAPI as greenAPI

# First you need to set the environment variables
ID_INSTANCE = environ['ID_INSTANCE']
API_TOKEN_INSTANCE = environ['API_TOKEN_INSTANCE']

greenAPI = greenAPI.greenAPI('https://api.green-api.com', 
                        ID_INSTANCE, 
                        API_TOKEN_INSTANCE)

def main():
    chatIds = [
        "79001234567@c.us"
    ]
    resultCreate = greenAPI.groups.createGroup('GroupName', 
        chatIds)

    if resultCreate.code == 200:
        resultSend = greenAPI.sending.sendMessage(resultCreate.data['chatId'], 
            'Message text')
        print(resultSend)

if __name__ == "__main__":
    main()