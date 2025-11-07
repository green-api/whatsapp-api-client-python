import asyncio
from whatsapp_api_client_python import API

greenAPI = API.GreenAPI(
    "1101000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)

async def main():
    response = await greenAPI.account.getSettingsAsync()
    print(response.data) if response.code == 200 else print(response.error)

    response = await greenAPI.account.getWaSettingsAsync()
    print(response.data) if response.code == 200 else print(response.error)

    settings = {"outgoingWebhook": "yes", "incomingWebhook": "yes"}
    response = await greenAPI.account.setSettingsAsync(settings)
    print(response.data) if response.code == 200 else print(response.error)

    response = await greenAPI.account.getStateInstanceAsync()
    print(response.data) if response.code == 200 else print(response.error)

    response = await greenAPI.account.rebootAsync()
    print(response.data) if response.code == 200 else print(response.error)
    
    response = await greenAPI.account.qrAsync()
    print(response.data) if response.code == 200 else print(response.error)

    response = await greenAPI.account.getAuthorizationCodeAsync(79876543210)
    print(response.data) if response.code == 200 else print(response.error)

if __name__ == '__main__':
    asyncio.run(main())