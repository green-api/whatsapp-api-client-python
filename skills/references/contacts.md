# Contacts (`greenAPI.contacts`)

Class: `Contacts` in `tools/contacts.py`.  
Index: https://green-api.com/en/docs/api/contacts/

These manage the WhatsApp **address book** of the linked account (add/edit/delete contact).
For listing contacts / contact info, use `serviceMethods.getContacts` / `getContactInfo`.

| Method | Params | Docs |
| --- | --- | --- |
| `addContact` | `chatId`, `firstName`, optional `lastName`, `saveInAddressbook=True` | https://green-api.com/en/docs/api/contacts/AddContact/ |
| `editContact` | same | https://green-api.com/en/docs/api/contacts/EditContact/ |
| `deleteContact` | `chatId` | https://green-api.com/en/docs/api/contacts/DeleteContact/ |

```python
greenAPI.contacts.addContact("79876543210@c.us", "John", lastName="Doe")
```

All have `*Async` variants.
