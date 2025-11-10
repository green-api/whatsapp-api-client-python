import asyncio
from datetime import datetime
from json import dumps
from whatsapp_api_client_python import API

greenAPI = API.GreenAPI(
    "1101000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)

async def main():
    try:
        await greenAPI.webhooks.startReceivingNotificationsAsync(handler)
    except Exception as e:
        print(e)

def handler(type_webhook: str, body: dict) -> None:
    if type_webhook == "incomingMessageReceived":
        incoming_message_received(body)
    elif type_webhook == "outgoingMessageReceived":
        outgoing_message_received(body)
    elif type_webhook == "outgoingAPIMessageReceived":
        outgoing_api_message_received(body)
    elif type_webhook == "outgoingMessageStatus":
        outgoing_message_status(body)
    elif type_webhook == "stateInstanceChanged":
        state_instance_changed(body)
    elif type_webhook == "deviceInfo":
        device_info(body)
    elif type_webhook == "incomingCall":
        incoming_call(body)
    elif type_webhook == "statusInstanceChanged":
        status_instance_changed(body)

def get_notification_time(timestamp: int) -> str:
    return str(datetime.fromtimestamp(timestamp))

def incoming_message_received(body: dict) -> None:
    timestamp = body["timestamp"]
    time = get_notification_time(timestamp)
    data = dumps(body, ensure_ascii=False, indent=4)

    print(f"New incoming message at {time} with data: {data}", end="\n\n")

def outgoing_message_received(body: dict) -> None:
    timestamp = body["timestamp"]
    time = get_notification_time(timestamp)
    data = dumps(body, ensure_ascii=False, indent=4)

    print(f"New outgoing message at {time} with data: {data}", end="\n\n")

def outgoing_api_message_received(body: dict) -> None:
    timestamp = body["timestamp"]
    time = get_notification_time(timestamp)
    data = dumps(body, ensure_ascii=False, indent=4)

    print(f"New outgoing API message at {time} with data: {data}", end="\n\n")

def outgoing_message_status(body: dict) -> None:
    timestamp = body["timestamp"]
    time = get_notification_time(timestamp)
    data = dumps(body, ensure_ascii=False, indent=4)

    response = f"Status of sent message has been updated at {time} with data: {data}"
    print(response, end="\n\n")

def state_instance_changed(body: dict) -> None:
    timestamp = body["timestamp"]
    time = get_notification_time(timestamp)
    data = dumps(body, ensure_ascii=False, indent=4)

    print(f"Current instance state at {time} with data: {data}", end="\n\n")

def device_info(body: dict) -> None:
    timestamp = body["timestamp"]
    time = get_notification_time(timestamp)
    data = dumps(body, ensure_ascii=False, indent=4)

    response = f"Current device information at {time} with data: {data}"
    print(response, end="\n\n")

def incoming_call(body: dict) -> None:
    timestamp = body["timestamp"]
    time = get_notification_time(timestamp)
    data = dumps(body, ensure_ascii=False, indent=4)

    print(f"New incoming call at {time} with data: {data}", end="\n\n")

def status_instance_changed(body: dict) -> None:
    timestamp = body["timestamp"]
    time = get_notification_time(timestamp)
    data = dumps(body, ensure_ascii=False, indent=4)

    print(f"Current instance status at {time} with data: {data}", end="\n\n")

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n Application Stopped")