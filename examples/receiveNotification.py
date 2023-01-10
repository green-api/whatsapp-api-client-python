from datetime import datetime

from whatsapp_api_client_python import GreenAPI

ID_INSTANCE = "1101000001"
API_TOKEN_INSTANCE = "3e03ea9ff3324e228ae3dfdf4d48e409bfa1b1ad0b0c46bf8c"

greenAPI = GreenAPI(ID_INSTANCE, API_TOKEN_INSTANCE)


def main():
    greenAPI.webhook.start_receiving_notifications(handler)


def handler(body: dict) -> None:
    type_webhook = body["typeWebhook"]
    if type_webhook == "incomingMessageReceived":
        incoming_message_received_handler(body)
    elif type_webhook == "outgoingMessageReceived":
        outgoing_message_received_handler(body)
    elif type_webhook == "stateInstanceChanged":
        state_instance_changed_handler(body)
    elif type_webhook == "deviceInfo":
        device_info_handler(body)
    elif type_webhook == "incomingCall":
        incoming_call_handler(body)
    elif type_webhook == "statusInstanceChanged":
        status_instance_changed_handler(body)


def incoming_message_received_handler(body: dict) -> None:
    print("incomingMessageReceived", body)

    greenAPI.sending.send_message(
        chatId=body["senderData"]["chatId"],
        message="Any message"
    )


def outgoing_message_received_handler(body: dict) -> None:
    print("outgoingMessageReceived", body)

    greenAPI.read_mark.read_chat(
        chatId=body["senderData"]["chatId"]
    )


def state_instance_changed_handler(body: dict) -> None:
    print("stateInstanceChanged", body)

    print(body["stateInstance"])


def device_info_handler(body: dict) -> None:
    print("deviceInfo", body)

    device_data = body["deviceData"]
    print(
        device_data["platform"],
        device_data["deviceManufacturer"],
        device_data["deviceModel"],
        device_data["osVersion"],
        device_data["waVersion"],
        device_data["battery"]
    )


def incoming_call_handler(body: dict) -> None:
    print("incomingCall", body)

    print(
        body["from"],
        str(datetime.fromtimestamp(body["timestamp"])),
        body["idMessage"]
    )


def status_instance_changed_handler(body: dict) -> None:
    print("statusInstanceChanged", body)

    print(body["statusInstance"])


if __name__ == '__main__':
    main()
