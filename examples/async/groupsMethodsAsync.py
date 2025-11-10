import asyncio
from whatsapp_api_client_python import API

greenAPI = API.GreenAPI(
    "1101000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)

async def main():
    tasks = [
        greenAPI.groups.createGroupAsync("SDK Python", ["11001234567@c.us", "11001234568@c.us"]),
        greenAPI.groups.addGroupParticipantAsync("1234567890@g.us", "11001234567@c.us"),
        greenAPI.groups.getGroupDataAsync("1234567890@g.us")
    ]

    responses = await asyncio.gather(*tasks, return_exceptions=True)
    [print(response.data) for response in responses if response.code == 200]

if __name__ == '__main__':
    asyncio.run(main())