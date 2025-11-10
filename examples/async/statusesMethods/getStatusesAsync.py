import asyncio
from whatsapp_api_client_python import API, response

greenAPI = API.GreenAPI(
    "1101000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)

async def main():
    tasks = [
        greenAPI.statuses.getIncomingStatusesAsync(1400),
        greenAPI.statuses.getOutgoingStatusesAsync(1400),
        greenAPI.statuses.getStatusStatisticAsync('BAE54F518532FCB1')
    ]

    responses = await asyncio.gather(*tasks, return_exceptions=True)
    [print(response.data) for response in responses if response.code == 200]

if __name__ == '__main__':
    asyncio.run(main())