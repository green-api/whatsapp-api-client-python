import asyncio
from whatsapp_api_client_python import API

greenAPI = API.GreenApiPartner(
    "gac.abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrst"
)

async def main():
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
        "keepOnlineStatus": "yes",
        "pollMessageWebhook": "yes",
        "incomingCallWebhook": "yes",
        "editedMessageWebhook": "yes",
        "deletedMessageWebhook": "yes"
    }

    response = await greenAPI.partner.createInstanceAsync(settings)
    print(response.data) if response.code == 200 else print(response.error)

if __name__ == '__main__':
    asyncio.run(main())