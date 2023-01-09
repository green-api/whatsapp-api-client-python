from whatsapp_api_client_python import GreenAPI

greenAPI = GreenAPI("ID_INSTANCE", "API_TOKEN_INSTANCE")


def main():
    response = greenAPI.sending.send_file_by_url(
        chatId="11001234567@c.us",
        urlFile=(
            "https://www.google.com/images/branding/"
            "googlelogo/2x/googlelogo_color_272x92dp.png"
        ),
        fileName="googlelogo_color_272x92dp.png"
    )

    print(response)


if __name__ == "__main__":
    main()
