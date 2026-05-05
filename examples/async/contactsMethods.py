import asyncio
from whatsapp_api_client_python import API

greenAPI = API.GreenAPI(
    "1101000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)

async def main():
    tasks = [
        greenAPI.contacts.addContact("79876543210@c.us", "Bruce", "Wayne", True),
        greenAPI.contacts.editContact("79876543210@c.us", "Batman", "", True),
        greenAPI.contacts.deleteContact("79876543210@c.us")
    ]
    responses = await asyncio.gather(*tasks, return_exceptions=True)
    [print(response.data) for response in responses if response.code == 200]

if __name__ == '__main__':
    asyncio.run(main())
