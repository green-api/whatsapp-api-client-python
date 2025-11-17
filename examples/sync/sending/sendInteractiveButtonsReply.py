from whatsapp_api_client_python import API

greenAPI = API.GreenAPI(
    "1101000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)

def main():
    response = greenAPI.sending.sendInteractiveButtonsReply(
        "79876543210@c.us",
        "This is message with buttons!",
        [{
            "buttonId": "1",
            "buttonText": "First Button"
        },
        {
            "buttonId": "2",
            "buttonText": "Second Button"
        }],
        "Check this out",
        "Hope you like it"
    )
    print(response.data)

if __name__ == '__main__':
    main()