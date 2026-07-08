import asyncio
from whatsapp_api_client_python import API

greenAPI = API.GreenAPI(
    "1101000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)

async def main():
    tasks = [
        greenAPI.account.getSettingsAsync(),
        greenAPI.account.getWaSettingsAsync(),
        greenAPI.account.setSettingsAsync({"outgoingWebhook": "yes", "incomingWebhook": "yes"}),
        greenAPI.account.getStateInstanceAsync(),
        greenAPI.account.getStateInstanceHistoryAsync(count=50),
        greenAPI.account.rebootAsync(),
        greenAPI.account.qrAsync(),
        greenAPI.account.getAuthorizationCodeAsync(79876543210)
    ]

    responses = await asyncio.gather(*tasks, return_exceptions=True)
    [print(response.data) for response in responses if response.code == 200]

    # Refresh API token (beta). The old token becomes invalid after this call.
    response = await greenAPI.account.updateApiTokenAsync()
    print(response.data)

if __name__ == '__main__':
    asyncio.run(main())