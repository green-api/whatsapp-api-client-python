import asyncio
from os.path import basename
from urllib.parse import urlparse
from whatsapp_api_client_python import API

greenAPI = API.GreenAPI(
    "1101000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)

async def main():
    upload_file_response = await greenAPI.sending.uploadFileAsync("data/logo.jpg")
    
    if upload_file_response.code == 200:
        print(upload_file_response.data)
        
        url_file = upload_file_response.data["urlFile"]
        url = urlparse(url_file)
        file_name = basename(url.path)
        
        send_file_response = await greenAPI.sending.sendFileByUrlAsync(
            "11001234567@c.us", url_file, file_name
        )
        print(send_file_response.data) if send_file_response.code == 200 else print(send_file_response.error)
    else:
        print(upload_file_response.error)

if __name__ == '__main__':
    asyncio.run(main())