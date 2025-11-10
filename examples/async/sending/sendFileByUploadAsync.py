import asyncio
import os
from whatsapp_api_client_python import API

greenAPI = API.GreenAPI(
    "1101000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)

async def main():
    file_path = "data/logo.jpg"
    if not os.path.exists(file_path):
        print(f"File {file_path} not found")
    else:
        response = await greenAPI.sending.sendFileByUploadAsync(
            "11001234567@c.us",
            file_path,
            "logo.jpg",
            "logo"
        )
        if response.code == 200:
            print(response.data)

if __name__ == '__main__':
    asyncio.run(main())