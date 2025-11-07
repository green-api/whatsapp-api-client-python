import asyncio
from whatsapp_api_client_python import API, response

greenAPI = API.GreenAPI(
    "1101000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)

async def main():
    response1 = await greenAPI.statuses.getIncomingStatusesAsync(1400)
    print(response1.data) if response.code == 200 else print(response1.error)

    response2 = await greenAPI.statuses.getOutgoingStatusesAsync(1400)
    print(response2.data) if response.code == 200 else print(response2.error)

    response3 = await greenAPI.statuses.getStatusStatisticAsync('BAE54F518532FCB1')
    print(response3.data) if response.code == 200 else print(response3.error)

if __name__ == '__main__':
    asyncio.run(main())