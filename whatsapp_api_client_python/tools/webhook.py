from typing import Any, Callable, Union

from whatsapp_api_client_python.api import GreenAPI


class Webhook:
    def __init__(self, api: GreenAPI):
        self.api = api

    def run_forever(self, handler: Callable[[str, Union[dict, list]], Any]):
        print("Start receiving notifications. To interrupt, press Ctrl+C")

        while True:
            try:
                response = self.api.receiving.receive_notification()
                if response.status_code == 200:
                    if response.data is None:
                        continue

                    body = response.data["body"]
                    type_webhook = body["typeWebhook"]

                    handler(type_webhook, body)

                    self.api.receiving.delete_notification(
                        response.data["receiptId"]
                    )
            except KeyboardInterrupt:
                print("KeyboardInterrupt")

                break
