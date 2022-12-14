from os import environ

from whatsapp_api_client_python import GreenAPI, Bot

ID_INSTANCE = environ["ID_INSTANCE"]
API_TOKEN_INSTANCE = environ["API_TOKEN_INSTANCE"]

greenAPI = GreenAPI(ID_INSTANCE, API_TOKEN_INSTANCE)

bot = Bot(greenAPI)


@bot.handler(type_webhook="incomingMessageReceived")
def handler(body: dict) -> None:
    greenAPI.read_mark.read_chat(
        chatId=body["senderData"]["chatId"],
        idMessage=body["idMessage"]
    )


@bot.message(message_text="Hello")
def message_handler(body: dict) -> str:
    sender_name = body["senderData"]["senderName"]

    return f"Hello, {sender_name}."


bot.run_forever()
