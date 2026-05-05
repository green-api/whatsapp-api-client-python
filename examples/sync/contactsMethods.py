from whatsapp_api_client_python import API

greenAPI = API.GreenAPI(
    "1101000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)


def main():
    # Add contact
    addContactResponse = greenAPI.contacts.addContact("79876543210@c.us", "Bruce", "Wayne", True)
    print(addContactResponse.data)
    # Edit contact
    editContactResponse = greenAPI.contacts.editContact("79876543210@c.us", "Batman", "", True)
    print(editContactResponse.data)

    # Delete contact
    deleteContactResponse = greenAPI.contacts.deleteContact("79876543210@c.us")
    print(deleteContactResponse.data)

if __name__ == '__main__':
    main()
