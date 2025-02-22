from whatsapp_api_client_python import API

greenAPI = API.GreenApiPartner(
    "gac.abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrst"
)


def main():
    settings = {
        "name": "Created by Python SDK",
        "webhookUrl": "https://webhook.url",
        "webhookUrlToken": "auth_token",
        "delaySendMessagesMilliseconds": 5000,
        "markIncomingMessagesReaded": "yes",
        "markIncomingMessagesReadedOnReply": "yes",
        "outgoingWebhook": "yes",
        "outgoingMessageWebhook": "yes",
        "outgoingAPIMessageWebhook": "yes",
        "stateWebhook": "yes",
        "incomingWebhook": "yes",
        "deviceWebhook": "yes",
        "keepOnlineStatus": "yes",
        "pollMessageWebhook": "yes",
        "incomingBlockWebhook": "yes",
        "incomingCallWebhook": "yes",
        "editedMessageWebhook": "yes",
        "deletedMessageWebhook": "yes"
    }

    response = greenAPI.partner.createInstance(settings)
    print(response.data)

if __name__ == '__main__':
    main()
