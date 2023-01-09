from whatsapp_api_client_python import GreenAPI

ID_INSTANCE = "1101000001"
API_TOKEN_INSTANCE = "3e03ea9ff3324e228ae3dfdf4d48e409bfa1b1ad0b0c46bf8c"

greenAPI = GreenAPI(ID_INSTANCE, API_TOKEN_INSTANCE)


def main():
    create_group_response = greenAPI.groups.create_group(
        groupName="Group Name",
        chatIds=["11001234567@c.us"]
    )

    print(create_group_response)

    send_message_response = greenAPI.sending.send_message(
        chatId=create_group_response["chatId"],
        message="Any message"
    )

    print(send_message_response)


if __name__ == "__main__":
    main()
