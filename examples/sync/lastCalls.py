from whatsapp_api_client_python import API

greenAPI = API.GreenAPI(
    "1101000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)


def main():
    # If no argument, calls for the last 24 hours are returned.

    print("Incoming calls in the last 72 hours:")
    response = greenAPI.journals.lastIncomingCalls(4320)
    print(response.data)

    print("Outgoing calls in the last 72 hours:")
    response = greenAPI.journals.lastOutgoingCalls(4320)
    print(response.data)


if __name__ == '__main__':
    main()
