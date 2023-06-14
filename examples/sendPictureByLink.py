from whatsapp_api_client_python import API

greenAPI = API.GreenApi(
    "1101000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)


def main():
    response = greenAPI.sending.sendFileByUrl(
        "11001234567@c.us",
        "https://green-api.com/green-api-logo_2.png",
        "green-api-logo_2.png",
        "GREEN API logo"
    )

    print(response.data)


if __name__ == '__main__':
    main()
