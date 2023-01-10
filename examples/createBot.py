from whatsapp_api_client_python import GreenAPI, Bot

ID_INSTANCE = "1101000001"
API_TOKEN_INSTANCE = "3e03ea9ff3324e228ae3dfdf4d48e409bfa1b1ad0b0c46bf8c"

greenAPI = GreenAPI(ID_INSTANCE, API_TOKEN_INSTANCE)

bot = Bot(greenAPI)


def main():
    bot.run_forever()


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


if __name__ == '__main__':
    main()
