from os import environ

from whatsapp_api_client_python import API as API

ID_INSTANCE = environ['ID_INSTANCE']
API_TOKEN_INSTANCE = environ['API_TOKEN_INSTANCE']

greenAPI = API.GreenAPI(ID_INSTANCE, API_TOKEN_INSTANCE)

def main():
    result = greenAPI.sending.sendFileByUrl('79001234567@c.us', 
        'https://www.google.ru/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png', 
        'googlelogo_color_272x92dp.png', 'Google logo')
    print(result.data)

if __name__ == "__main__":
    main()