from os import environ

from whatsapp_api_client_python import GreenAPI

# First you need to set the environment variables.
ID_INSTANCE = environ["ID_INSTANCE"]
API_TOKEN_INSTANCE = environ["API_TOKEN_INSTANCE"]

greenAPI = GreenAPI(ID_INSTANCE, API_TOKEN_INSTANCE)


def main():
    response = greenAPI.sending.send_file_by_url(
        chatId="",
        urlFile="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png",
        fileName="googlelogo_color_272x92dp.png",
        caption="Google "
    )

    print(response.data)


if __name__ == "__main__":
    main()

def main():
    result = greenAPI.sending.sendFileByUrl('79001234567@c.us', 
        'https://www.google.ru/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png', 
        'googlelogo_color_272x92dp.png', 'Google logo')
    print(result.data)

if __name__ == "__main__":
    main()