import asyncio
from whatsapp_api_client_python import API

greenAPI = API.GreenAPI(
    "1101000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)

async def main():
    tasks = [
        # Large link preview
        greenAPI.sending.sendMessageAsync(
            "79876543210@c.us",
            "Check out our website!",
            typePreview="large"
        ),
        # Custom preview
        greenAPI.sending.sendMessageAsync(
            "79876543210@c.us",
            "Check out our website!",
            linkPreview=True,
            customPreview={
                "title": "My Website",
                "description": "The best website in the world",
                "link": "example.com"
            }
        ),
        # No preview
        greenAPI.sending.sendMessageAsync(
            "79876543210@c.us",
            "https://example.com — visit us!",
            linkPreview=False
        ),
    ]

    responses = await asyncio.gather(*tasks, return_exceptions=True)
    [print(response.data) for response in responses if response.code == 200]


if __name__ == '__main__':
    asyncio.run(main())
