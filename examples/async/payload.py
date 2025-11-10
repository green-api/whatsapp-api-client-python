import asyncio
from whatsapp_api_client_python import API

class GreenAPIDemo:
    def __init__(self):
        self.greenAPI = API.GreenAPI("1101000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345")
        self.test_chat = "11001234567@c.us"

    async def run_demo(self):
        tasks = [
            self.demo_account_management(),
            self.demo_contacts(),
            self.demo_sending_messages(),
            self.demo_journals(),
            self.demo_queues()
        ]
        await asyncio.gather(*tasks, return_exceptions=True)


    async def demo_account_management(self):
        response = await self.greenAPI.account.getStateInstanceAsync()
        if response.code == 200:
            print(response.data)
            
        response = await self.greenAPI.account.getSettingsAsync()
        if response.code == 200:
            settings = response.data
            print("getSettings:")
            print(f"   - delaySendMessagesMilliseconds: {settings.get('delaySendMessagesMilliseconds', 'N/A')}ms")
            print(f"   - incomingWebhook: {settings.get('incomingWebhook', 'N/A')}")
            print(f"   - outgoingWebhook: {settings.get('outgoingWebhook', 'N/A')}")

        new_settings = {"delaySendMessagesMilliseconds": 1000, "outgoingWebhook": "yes", "incomingWebhook": "yes"}
        response = await self.greenAPI.account.setSettingsAsync(new_settings)
        if response.code == 200:
            print("setSettings: ", response.data)

        response = await self.greenAPI.account.qrAsync()
        if response.code == 200:
            print(f"QR received (data size: {len(response.data)} bytes)")

    async def demo_contacts(self):
        response = await self.greenAPI.serviceMethods.getContactsAsync()
        if response.code == 200:
            contacts = response.data
            print(f"getContacts: {len(contacts)} contacts were received")

            for i, contact in enumerate(contacts[:3]):
                print(f"   {i+1}. {contact.get('name', 'No name')} - {contact.get('id')}")
        
        test_numbers = [79001234567, 79001234568]
        for number in test_numbers:
            response = await self.greenAPI.serviceMethods.checkWhatsappAsync(number)
            if response.code == 200:
                exists = response.data.get('existsWhatsapp', False)
                status = "Whatsapp exists" if exists else "WhatsApp don't exist"
                print(f"Phone: {number}: {status}")

    async def demo_sending_messages(self):
        response = await self.greenAPI.sending.sendMessageAsync(
            self.test_chat,
            "This message was sent from Green-API SDK Python"
        )
        if response.code == 200:
            print("Text message sent: ", response.data)

        response = await self.greenAPI.sending.sendMessageAsync(
            self.test_chat,
            "Checking link preview: https://green-api.com",
            linkPreview=True
        )
        if response.code == 200:
            print("Message with preview sent: ", response.data)

        response = await self.greenAPI.sending.sendPollAsync(
            self.test_chat,
            "Wake me up",
            [
                {"optionName": "Wake me up inside"},
                {"optionName": "Before you go go"},
                {"optionName": "When september ends"}
            ],
            multipleAnswers=False
        )
        if response.code == 200:
            print("Poll message sent: ", response.data)

        contact = {
            "phoneContact": 79001234567,
            "firstName": "Jane",
            "lastName": "Doe"
        }
        response = await self.greenAPI.sending.sendContactAsync(
            self.test_chat,
            contact
        )
        if response.code == 200:
            print("Contact message sent: ", response.data)

        response = await self.greenAPI.sending.sendLocationAsync(
            "79001234567@c.us",
            44.9370129,
            89.8728409,
            "Restaurant",
            "123456, Best Place"
        )
        if response.code == 200:
            print("Location message sent: ", response.data)

    async def demo_journals(self):
        response = await self.greenAPI.journals.lastIncomingMessagesAsync(minutes=1440)
        if response.code == 200:
            messages = response.data
            print(f"lastIncomingMessages: {len(messages)}")
            for msg in messages[:2]:
                print(f"   - From: {msg.get('senderId')}")
                print(f"     Text: {msg.get('textMessage', 'Media/File')}")

    async def demo_queues(self):
        response = await self.greenAPI.queues.showMessagesQueueAsync()
        if response.code == 200:
            queue = response.data
            print(f"MessagesQueue: {len(queue)}")

        print("Waiting 5 seconds... (for all messages to send)")
        await asyncio.sleep(5)

        response = await self.greenAPI.queues.clearMessagesQueueAsync()
        if response.code == 200:
            print("Queue cleared: ", response.data)

async def main():
    demo = GreenAPIDemo()
    try:
        await demo.run_demo()
    except Exception as e:
        print(f"error: {e}")

if __name__ == '__main__':
    asyncio.run(main())