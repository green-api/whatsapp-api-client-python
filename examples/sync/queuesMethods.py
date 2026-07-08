from whatsapp_api_client_python import API

greenAPI = API.GreenAPI(
    "1101000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)


def main():
    # Number of messages in the outgoing queue
    response = greenAPI.queues.getMessagesCount()
    print(response.data)

    # Number of notifications in the incoming webhooks queue
    response = greenAPI.queues.getWebhooksCount()
    print(response.data)

    # Clear the incoming webhooks queue (rate-limited to once per minute)
    response = greenAPI.queues.clearWebhooksQueue()
    print(response.data)


if __name__ == '__main__':
    main()
