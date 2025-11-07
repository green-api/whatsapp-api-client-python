import asyncio
from whatsapp_api_client_python import API

greenAPI = API.GreenAPI(
    "1101000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)

async def main():

    response = await greenAPI.serviceMethods.checkWhatsappAsync(79001234567)
    print(response.data) if response.code == 200 else print(response.error)

    response = await greenAPI.serviceMethods.getContactsAsync()
    print(response.data) if response.code == 200 else print(response.error)

    response = await greenAPI.serviceMethods.deleteMessageAsync(
        "11001234567@c.us", "BAE52A7F04F452F9", True
    )
    print(response.data) if response.code == 200 else print(response.error)

    response = await greenAPI.serviceMethods.deleteMessageAsync(
        "11001234567@c.us", "BAE52A7F04F452F9"
    )
    print(response.data) if response.code == 200 else print(response.error)

    response = await greenAPI.serviceMethods.editMessageAsync(
        "11001234567@c.us", "BAE5F793F61411D0", "New text (async)"
    )
    print(response.data) if response.code == 200 else print(response.error)

if __name__ == '__main__':
    asyncio.run(main())