import unittest
from os import environ

from whatsapp_api_client_python import GreenAPI, Bot
from whatsapp_api_client_python.bot import Handler, MessageHandler

ID_INSTANCE = environ["ID_INSTANCE"]
API_TOKEN_INSTANCE = environ["API_TOKEN_INSTANCE"]

greenAPI = GreenAPI(ID_INSTANCE, API_TOKEN_INSTANCE)

bot = Bot(greenAPI)


class BotTestCase(unittest.TestCase):
    def test_handler(self):
        type_webhook = "incomingMessageReceived"

        @bot.handler(type_webhook=type_webhook)
        def handler(body: dict) -> None:
            self.assertEqual(body["typeWebhook"], type_webhook)

        self.run_forever()

    def test_message_handler(self):
        message_text = "Hello"

        @bot.message(message_text=message_text)
        def message_handler(body: dict) -> str:
            message_data = body["messageData"]
            text_message_data = message_data["textMessageData"]
            text_message = text_message_data["textMessage"]

            self.assertEqual(text_message, message_text)

            return "Response"

        self.run_forever()

    def run_forever(self):
        response = {
            "body": {
                "typeWebhook": "incomingMessageReceived",
                "messageData": {
                    "typeMessage": "textMessage",
                    "textMessageData": {
                        "textMessage": "Hello"
                    }
                }
            }
        }

        body = response["body"]
        type_webhook = body["typeWebhook"]

        for handler in bot.handlers:
            if handler.type_webhook == type_webhook:
                if isinstance(handler, Handler):
                    handler.function(body)
                elif isinstance(handler, MessageHandler):
                    check_result = handler.check_message_text(body)
                    if check_result:
                        message = handler.function(body)
                        if isinstance(message, str):
                            self.assertEqual(message, "Response")


if __name__ == '__main__':
    unittest.main()
