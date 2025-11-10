import asyncio
from whatsapp_api_client_python import API

greenAPI = API.GreenAPI(
    "1101000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)

async def main():
    create_group_response = await greenAPI.groups.createGroupAsync(
        "SDK Python", ["11001234567@c.us", "11001234568@c.us"]
    )
    
    if create_group_response.code == 200:
        print(create_group_response.data)

        send_message_response = await greenAPI.sending.sendMessageAsync(
            create_group_response.data["chatId"], "Message text"
        )
        if send_message_response.code == 200:
            print(send_message_response.data) 

if __name__ == '__main__':
    asyncio.run(main())