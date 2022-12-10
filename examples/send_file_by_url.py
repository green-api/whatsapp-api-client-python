from os import environ

from whatsapp_api_client_python import GreenAPI

# First you need to set the environment variables.
ID_INSTANCE = environ["ID_INSTANCE"]
API_TOKEN_INSTANCE = environ["API_TOKEN_INSTANCE"]

greenAPI = GreenAPI(ID_INSTANCE, API_TOKEN_INSTANCE)


def main():
    response = greenAPI.sending.send_file_by_url(
        chatId="79001234567@c.us",
        urlFile=(
            "https://www.google.com/images/branding/"
            "googlelogo/2x/googlelogo_color_272x92dp.png"
        ),
        fileName="googlelogo_color_272x92dp.png"
    )

    print(response)


if __name__ == "__main__":
    main()
