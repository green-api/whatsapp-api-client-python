import asyncio
from whatsapp_api_client_python import API

greenAPI = API.GreenAPI(
    "1101000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)

async def main():
    tasks = [
        greenAPI.queues.getMessagesCountAsync(),
        greenAPI.queues.getWebhooksCountAsync(),
    ]

    responses = await asyncio.gather(*tasks, return_exceptions=True)
    [print(response.data) for response in responses if response.code == 200]

    # Clear webhooks queue (rate-limited to once per minute)
    response = await greenAPI.queues.clearWebhooksQueueAsync()
    print(response.data)


if __name__ == '__main__':
    asyncio.run(main())
