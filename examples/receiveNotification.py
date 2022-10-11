from os import environ
from whatsapp_api_client_python import greenAPI as greenAPI


ID_INSTANCE = environ['ID_INSTANCE']
API_TOKEN_INSTANCE = environ['API_TOKEN_INSTANCE']

restApi = greenAPI.RestApi(ID_INSTANCE, API_TOKEN_INSTANCE)

def main():
   restApi.webhooks.startReceivingNotifications()

if __name__ == "__main__":
    main()