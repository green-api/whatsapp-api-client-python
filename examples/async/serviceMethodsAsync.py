import asyncio
from whatsapp_api_client_python import API

greenAPI = API.GreenAPI(
    "1101000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)

async def main():
    tasks = [
        greenAPI.serviceMethods.checkWhatsappAsync(79001234567),
        greenAPI.serviceMethods.getContactsAsync(),
        greenAPI.serviceMethods.deleteMessageAsync("11001234567@c.us", "BAE52A7F04F452F9", True),
        greenAPI.serviceMethods.deleteMessageAsync("11001234567@c.us", "BAE52A7F04F452F9"),
        greenAPI.serviceMethods.editMessageAsync("11001234567@c.us", "BAE5F793F61411D0", "Edited message text")
    ]

    responses = await asyncio.gather(*tasks, return_exceptions=True)
    [print(response.data) for response in responses if response.code == 200]

if __name__ == '__main__':
    asyncio.run(main())