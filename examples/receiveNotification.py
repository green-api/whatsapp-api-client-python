from whatsapp_api_client_python import GreenAPI, Webhook

ID_INSTANCE = "1101000001"
API_TOKEN_INSTANCE = "3e03ea9ff3324e228ae3dfdf4d48e409bfa1b1ad0b0c46bf8c"

greenAPI = GreenAPI(ID_INSTANCE, API_TOKEN_INSTANCE)

webhook = Webhook(greenAPI)


def main():
    webhook.start_receiving_notifications(handler)


def handler(body: dict) -> None:
    type_webhook = body["typeWebhook"]
    if type_webhook == "incomingMessageReceived":
        response = greenAPI.sending.send_message(
            chatId=body["senderData"]["chatId"],
            message="Any message"
        )

        print(response)


if __name__ == '__main__':
    main()
