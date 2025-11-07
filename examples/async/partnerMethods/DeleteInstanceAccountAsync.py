import asyncio
from whatsapp_api_client_python import API

greenAPI = API.GreenApiPartner(
    "gac.abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrst"
)

async def main():
    response = await greenAPI.partner.deleteInstanceAccountAsync(0)
    print(response.data) if response.code == 200 else print(response.error)

if __name__ == '__main__':
    asyncio.run(main())
