from whatsapp_api_client_python import GreenAPI

greenAPI = GreenAPI("ID_INSTANCE", "API_TOKEN_INSTANCE")


def main():
    response = greenAPI.sending.send_message(
        chatId="11001234567@c.us",
        message="Any message"
    )

    print(response)


if __name__ == "__main__":
    main()
