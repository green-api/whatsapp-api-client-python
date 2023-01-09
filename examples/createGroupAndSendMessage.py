from whatsapp_api_client_python import GreenAPI

greenAPI = GreenAPI("ID_INSTANCE", "API_TOKEN_INSTANCE")


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
