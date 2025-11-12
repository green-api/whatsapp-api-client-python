from whatsapp_api_client_python import API

greenAPI = API.GreenAPI(
    "1101000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)

def main():
    response = greenAPI.sending.sendInteractiveButtons(
        "79001234567@c.us",
        "This is message with buttons!",
        [{
            "type": "call",
            "buttonId": "1",
            "buttonText": "Call me",
            "phoneNumber": "79001234567"
        },
        {
            "type": "url",
            "buttonId": "2",
            "buttonText": "Green-api",
            "url": "https://green-api.com/en/docs/api/sending/SendInteractiveButtons/"
        }],
        "Check this out",
        "Hope you like it"
    )
    print(response.data)

if __name__ == '__main__':
    main()