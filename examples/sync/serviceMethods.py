from whatsapp_api_client_python import API

greenAPI = API.GreenAPI(
    "1101000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)


def main():
    # CheckWhatsapp — preferred: use chatId
    response = greenAPI.serviceMethods.checkWhatsapp(chatId="79876543210@c.us")
    print(response.data)

    # CheckWhatsapp — bypass cache and query WhatsApp directly
    response = greenAPI.serviceMethods.checkWhatsapp(chatId="79876543210@c.us", force=True)
    print(response.data)

    # CheckWhatsapp — old-style call still works (backward compatible)
    response = greenAPI.serviceMethods.checkWhatsapp(79876543210)
    print(response.data)

    # GetContacts — all contacts
    response = greenAPI.serviceMethods.getContacts()
    print(response.data)

    # GetContacts — only groups
    response = greenAPI.serviceMethods.getContacts(group=True)
    print(response.data)

    # GetContacts — only personal chats, limit to 20
    response = greenAPI.serviceMethods.getContacts(group=False, count=20)
    print(response.data)

    # GetChats — all chats sorted by activity
    response = greenAPI.serviceMethods.getChats()
    print(response.data)

    # GetChats — last 10 active chats
    response = greenAPI.serviceMethods.getChats(count=10)
    print(response.data)

    # DeleteMessage for sender
    response = greenAPI.serviceMethods.deleteMessage("79876543210@c.us", "BAE52A7F04F452F9", True)

    # DeleteMessage for all (default)
    response = greenAPI.serviceMethods.deleteMessage("79876543210@c.us", "BAE5558FFC7565C2")

    # EditMessage
    response = greenAPI.serviceMethods.editMessage("79876543210@c.us", "BAE5F793F61411D0", "New text")
    print(response.data)

if __name__ == '__main__':
    main()
