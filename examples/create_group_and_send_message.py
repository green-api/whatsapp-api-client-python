from os import environ

from whatsapp_api_client_python import GreenAPI

# First you need to set the environment variables.
ID_INSTANCE = environ["ID_INSTANCE"]
API_TOKEN_INSTANCE = environ["API_TOKEN_INSTANCE"]

greenAPI = GreenAPI(ID_INSTANCE, API_TOKEN_INSTANCE)


def main():
    create_group_response = greenAPI.groups.create_group(
        groupName="Group Name",
        chatIds=["79001234567@c.us"]
    )
    print(create_group_response.data)

    chatId = create_group_response.data["chatId"]
    send_message_response = greenAPI.sending.send_message(
        chatId=chatId,
        message="Any message"
    )
    print(send_message_response.data)


if __name__ == "__main__":
    main()
