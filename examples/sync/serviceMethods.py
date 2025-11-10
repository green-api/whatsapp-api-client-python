from whatsapp_api_client_python import API

greenAPI = API.GreenAPI(
    "1101000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)


def main():
    # DeleteMessage for sender
    response = greenAPI.serviceMethods.deleteMessage("11001234567@c.us", "BAE52A7F04F452F9", True)

    # DeleteMessage for all (default)
    response = greenAPI.serviceMethods.deleteMessage("11001234567@c.us", "BAE5558FFC7565C2")

    # EditMessage
    response = greenAPI.serviceMethods.editMessage("11001234567@c.us", "BAE5F793F61411D0", "New text")
    print(response.data) # new idMessage

if __name__ == '__main__':
    main()
