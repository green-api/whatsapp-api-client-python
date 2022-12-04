from os import environ

from whatsapp_api_client_python import GreenAPI, Bot

# First you need to set the environment variables.
ID_INSTANCE = environ["ID_INSTANCE"]
API_TOKEN_INSTANCE = environ["API_TOKEN_INSTANCE"]

greenAPI = GreenAPI(ID_INSTANCE, API_TOKEN_INSTANCE)

bot = Bot(greenAPI)


@bot.handler("stateInstanceChanged")
def handler(body: dict):
    print(body["instanceData"])
    print("stateInstanceChanged")


@bot.message("Привет")
def message(body: dict) -> str:
    print(body["senderData"])
    print("incomingMessageReceived")

    return f"""Привет, {body["senderData"]["senderName"]}"""


bot.run_forever()
