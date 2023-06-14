from whatsapp_api_client_python import API

greenAPI = API.GreenApi(
    "1101000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)


def main():
    create_group_response = greenAPI.groups.createGroup(
        "Group Name", ["11001234567@c.us"]
    )
    if create_group_response.code == 200:
        print(create_group_response.data)

        send_message_response = greenAPI.sending.sendMessage(
            create_group_response.data["chatId"], "Message text"
        )
        if send_message_response.code == 200:
            print(send_message_response.data)
        else:
            print(send_message_response.error)
    else:
        print(create_group_response.error)


if __name__ == '__main__':
    main()
