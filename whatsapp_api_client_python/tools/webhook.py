from typing import Any, Callable

from requests import JSONDecodeError

from whatsapp_api_client_python.api import AbstractAPI


class Webhook:
    def __init__(self, api: AbstractAPI):
        self.api = api

    def run_forever(self, handler: Callable[[str, dict], Any]) -> None:
        print("Start receiving notifications. To interrupt, press Ctrl+C")

        while True:
            try:
                try:
                    response = self.api.receiving.receive_notification()
                except JSONDecodeError:
                    continue

                body = response["body"]
                type_webhook = body["typeWebhook"]

                handler(type_webhook, body)

                self.api.receiving.delete_notification(
                    response["receiptId"]
                )
            except KeyboardInterrupt:
                print("KeyboardInterrupt")

                break
