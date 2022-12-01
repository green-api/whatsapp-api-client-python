from os import environ

from whatsapp_api_client_python import GreenAPI

# First you need to set the environment variables.
ID_INSTANCE = environ["ID_INSTANCE"]
API_TOKEN_INSTANCE = environ["API_TOKEN_INSTANCE"]

greenAPI = GreenAPI(ID_INSTANCE, API_TOKEN_INSTANCE)


def main():
    response = greenAPI.sending.send_file_by_upload(
        chatId="79001234567@c.us",
        path="C:\\Games\\PicFromDisk.png"
    )

    print(response.data)


if __name__ == "__main__":
    main()
