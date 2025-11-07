import asyncio
from whatsapp_api_client_python import API

greenAPI = API.GreenAPI(
    "1101000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)

async def main():
    response = await greenAPI.sending.sendMessageAsync("11001234567@c.us", "Message Text (async)")
    print(response.data) if response.code == 200 else print(response.error)

if __name__ == '__main__':
    asyncio.run(main())