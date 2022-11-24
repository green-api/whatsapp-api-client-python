from os import environ
from typing import Union

from whatsapp_api_client_python import GreenAPI
from whatsapp_api_client_python.tools import Webhook

# First you need to set the environment variables.
ID_INSTANCE = environ["ID_INSTANCE"]
API_TOKEN_INSTANCE = environ["API_TOKEN_INSTANCE"]

greenAPI = GreenAPI(ID_INSTANCE, API_TOKEN_INSTANCE)


def main():
    webhook = Webhook(greenAPI)

    webhook.run_forever(handler)


def handler(type_webhook: str, body: Union[dict, list]):
    if type_webhook == "incomingMessageReceived":
        sender_data = body["senderData"]
        message_data = body["messageData"]

        type_message = message_data["typeMessage"]
        if type_message == "textMessage":
            text_message = message_data["textMessageData"]["textMessage"]

            greenAPI.sending.send_message(
                chatId=sender_data["chatId"],
                message=f"You wrote: {text_message}."
            )


if __name__ == "__main__":
    main()
