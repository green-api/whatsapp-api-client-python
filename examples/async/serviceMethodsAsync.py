import asyncio
from whatsapp_api_client_python import API

greenAPI = API.GreenAPI(
    "1101000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)

async def main():
    tasks = [
        # Preferred: use chatId
        greenAPI.serviceMethods.checkWhatsappAsync(chatId="79876543210@c.us"),
        # Bypass cache
        greenAPI.serviceMethods.checkWhatsappAsync(chatId="79876543210@c.us", force=True),
        # Old-style call still works (backward compatible)
        greenAPI.serviceMethods.checkWhatsappAsync(79876543210),
        # All contacts
        greenAPI.serviceMethods.getContactsAsync(),
        # Only groups
        greenAPI.serviceMethods.getContactsAsync(group=True),
        # Only personal chats, limit 20
        greenAPI.serviceMethods.getContactsAsync(group=False, count=20),
        # Last 10 active chats
        greenAPI.serviceMethods.getChatsAsync(count=10),
        greenAPI.serviceMethods.deleteMessageAsync("79876543210@c.us", "BAE52A7F04F452F9", True),
        greenAPI.serviceMethods.deleteMessageAsync("79876543210@c.us", "BAE52A7F04F452F9"),
        greenAPI.serviceMethods.editMessageAsync("79876543210@c.us", "BAE5F793F61411D0", "Edited message text")
    ]

    responses = await asyncio.gather(*tasks, return_exceptions=True)
    [print(response.data) for response in responses if response.code == 200]

if __name__ == '__main__':
    asyncio.run(main())