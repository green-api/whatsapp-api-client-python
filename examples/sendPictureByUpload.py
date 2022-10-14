from os import environ

from whatsapp_api_client_python import greenAPI as greenAPI

ID_INSTANCE = environ['ID_INSTANCE']
API_TOKEN_INSTANCE = environ['API_TOKEN_INSTANCE']

restApi = greenAPI.RestApi(ID_INSTANCE, API_TOKEN_INSTANCE)

def main():
    result = restApi.sending.sendFileByUpload('77073450985@c.us', 
        'C:\Games\PicFromDisk.png', 
        'PicFromDisk.png', 'Picture from disk')
    print(result.data)

if __name__ == "__main__":
    main()