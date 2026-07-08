from whatsapp_api_client_python import API

greenAPI = API.GreenAPI(
    "1101000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)


def main():
    # Send message with large link preview
    response = greenAPI.sending.sendMessage(
        "79876543210@c.us",
        "Check out our website!",
        typePreview="large"
    )
    print(response.data)

    # Send message with custom link preview
    response = greenAPI.sending.sendMessage(
        "79876543210@c.us",
        "Check out our website!",
        linkPreview=True,
        customPreview={
            "title": "My Website",
            "description": "The best website in the world",
            "link": "example.com"
        }
    )
    print(response.data)

    # Disable link preview
    response = greenAPI.sending.sendMessage(
        "79876543210@c.us",
        "https://example.com — visit us!",
        linkPreview=False
    )
    print(response.data)


if __name__ == '__main__':
    main()
