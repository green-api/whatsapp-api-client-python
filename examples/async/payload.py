import asyncio
from whatsapp_api_client_python import API

class GreenAPIDemo:
    def __init__(self):
        self.greenAPI = API.GreenAPI("1101000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345")
        self.test_chat = "11001234567@c.us"

    async def run_demo(self):
        await self.demo_account_management()
        await self.demo_contacts()
        await self.demo_sending_messages()
        await self.demo_journals()
        await self.demo_queues()

    async def demo_account_management(self):
        response = await self.greenAPI.account.getStateInstanceAsync()
        print(f"getStateInstanceAsync: {response.data.get('stateInstance') if response.code == 200 else response.error}")

        response = await self.greenAPI.account.getSettingsAsync()
        if response.code == 200:
            settings = response.data
            print(f"getSettingsAsync:")
            print(f"   - delaySendMessagesMilliseconds: {settings.get('delaySendMessagesMilliseconds', 'N/A')}ms")
            print(f"   - incomingWebhook: {settings.get('incomingWebhook', 'N/A')}")
            print(f"   - outgoingWebhook: {settings.get('outgoingWebhook', 'N/A')}")

        new_settings = {"delaySendMessagesMilliseconds": 1000, "outgoingWebhook": "yes", "incomingWebhook": "yes"}
        response = await self.greenAPI.account.setSettingsAsync(new_settings)
        print(f"setSettingsAsync: {'Success' if response.code == 200 else 'Error'}")

        response = await self.greenAPI.account.qrAsync()
        if response.code == 200:
            print(f"qrAsync received (data size: {len(response.data)} bytes)")

    async def demo_contacts(self):
        response = await self.greenAPI.serviceMethods.getContactsAsync()
        if response.code == 200:
            contacts = response.data
            print(f"getContactsAsync: {len(contacts)} contacts were received")

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
        print(f"Text message {'sent' if response.code == 200 else 'error'}")

        response = await self.greenAPI.sending.sendMessageAsync(
            self.test_chat,
            "Checking link preview: https://green-api.com",
            linkPreview=True
        )
        print(f"Message with preview {'sent' if response.code == 200 else 'error'}")

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
        print(f"Poll message {'sent' if response.code == 200 else 'error'}")

        contact = {
            "phoneContact": 79001234567,
            "firstName": "Jane",
            "lastName": "Doe"
        }
        response = await self.greenAPI.sending.sendContactAsync(
            self.test_chat,
            contact
        )
        print(f"Contact message {'sent' if response.code == 200 else 'error'}")

        response = await self.greenAPI.sending.sendLocationAsync(
            self.test_chat,
            55.755826,
            37.617300,
            "Red Square,"
            "Moscow, Russia"
        )
        print(f"Location message {'sent' if response.code == 200 else 'error'}")

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

        print(f"Waiting 5 seconds... (for all messages to send)")
        await asyncio.sleep(5)

        response = await self.greenAPI.queues.clearMessagesQueueAsync()
        print(f"Queue cleared: {'success' if response.code == 200 else 'error'}")

async def main():
    demo = GreenAPIDemo()
    try:
        await demo.run_demo()
    except Exception as e:
        print(f"error: {e}")
if __name__ == '__main__':
    asyncio.run(main())