from whatsapp_api_client_python import API

greenAPI = API.GreenAPI(
    "1101000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)


def main():
    response = greenAPI.sending.sendPoll(
        "79876543210@c.us",
        "Please choose a color:",
        [
            {"optionName": "Red"},
            {"optionName": "Green"},
            {"optionName": "Blue"}
        ]
    )

    print(response.data)


if __name__ == '__main__':
    main()
