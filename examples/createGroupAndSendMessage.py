from whatsapp_api_client_python import API as API

ID_INSTANCE = '1101000001'
API_TOKEN_INSTANCE = '3e03ea9ff3324e228ae3dfdf4d48e409bfa1b1ad0b0c46bf8c'

greenAPI = API.GreenApi(ID_INSTANCE, API_TOKEN_INSTANCE)

def main():
    chatIds = [
        "11001234567@c.us"
    ]
    resultCreate = greenAPI.groups.createGroup('GroupName', 
        chatIds)

    if resultCreate.code == 200:
        print(resultCreate.data)
        resultSend = greenAPI.sending.sendMessage(resultCreate.data['chatId'], 
            'Message text')
        if resultSend.code == 200:
            print(resultSend.data)
        else:
            print(resultSend.error)    
    else:
        print(resultCreate.error)

if __name__ == "__main__":
    main()