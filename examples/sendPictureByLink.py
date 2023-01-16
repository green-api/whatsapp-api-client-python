from whatsapp_api_client_python import API as API

ID_INSTANCE = '1101000001'
API_TOKEN_INSTANCE = '3e03ea9ff3324e228ae3dfdf4d48e409bfa1b1ad0b0c46bf8c'

greenAPI = API.GreenApi(ID_INSTANCE, API_TOKEN_INSTANCE)

def main():
    result = greenAPI.sending.sendFileByUrl('11001234567@c.us', 
        'https://www.google.ru/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png', 
        'googlelogo_color_272x92dp.png', 'Google logo')
    print(result.data)

if __name__ == "__main__":
    main()