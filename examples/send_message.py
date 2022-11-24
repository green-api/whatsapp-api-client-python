from os import environ

from whatsapp_api_client_python import GreenAPI

ID_INSTANCE = environ["ID_INSTANCE"]
API_TOKEN_INSTANCE = environ["API_TOKEN_INSTANCE"]

greenAPI = GreenAPI(ID_INSTANCE, API_TOKEN_INSTANCE)


def main():
    response = greenAPI.sending.send_message(
        chatId="79001234567@c.us",
        message="Any message"
    )

    print(response.data)


if __name__ == "__main__":
    main()
