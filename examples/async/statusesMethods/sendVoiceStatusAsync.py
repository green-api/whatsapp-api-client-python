import asyncio
from whatsapp_api_client_python import API

greenAPI = API.GreenAPI(
    "1101000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)

async def main():
    response = await greenAPI.statuses.sendVoiceStatusAsync(
        "https://example.com/file.mp3",
        "test.mp3" 
        "#54c774"
    )
    if response.code == 200:
        print(response.data)

if __name__ == '__main__':
    asyncio.run(main())
