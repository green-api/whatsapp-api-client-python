from whatsapp_api_client_python import API

greenAPI = API.GreenAPI(
    "1101000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)


def main():
    # Allow only admins to send messages
    response = greenAPI.groups.updateGroupSettings(
        "1234567890@g.us",
        allowParticipantsSendMessages=False
    )
    print(response.data)

    # Allow participants to edit group settings
    response = greenAPI.groups.updateGroupSettings(
        "1234567890@g.us",
        allowParticipantsEditGroupSettings=True
    )
    print(response.data)

    # Change both settings at once
    response = greenAPI.groups.updateGroupSettings(
        "1234567890@g.us",
        allowParticipantsEditGroupSettings=False,
        allowParticipantsSendMessages=True
    )
    print(response.data)


if __name__ == '__main__':
    main()
