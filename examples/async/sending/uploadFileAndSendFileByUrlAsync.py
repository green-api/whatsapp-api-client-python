import asyncio
import os
from urllib.parse import urlparse
from whatsapp_api_client_python import API

greenAPI = API.GreenAPI(
    "1101000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)

async def main():
    file_path = "data/logo.jpg"
    if not os.path.exists(file_path):
        print(f"File {file_path} not found")
        return

    upload_file_response = await greenAPI.sending.uploadFileAsync(file_path)
    
    if upload_file_response.code == 200:
        print(upload_file_response.data)
        
        url_file = upload_file_response.data["urlFile"]
        url = urlparse(url_file)
        file_name = basename(url.path)
        
        send_file_response = await greenAPI.sending.sendFileByUrlAsync(
            "11001234567@c.us", url_file, file_name
        )

        if send_file_response.code == 200:
            print(send_file_response.data)

if __name__ == '__main__':
    asyncio.run(main())