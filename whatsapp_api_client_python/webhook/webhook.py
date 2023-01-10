from typing import Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from whatsapp_api_client_python.api import AbstractAPI


class Webhook:
    running: bool = False

    def __init__(self, api: "AbstractAPI"):
        self.api = api

    def start_receiving_notifications(
            self, function: Callable[[dict], Any]
    ) -> None:
        self.running = True

        self.run_forever(function)

    def stop_receiving_notifications(self) -> None:
        self.running = False

    def run_forever(self, function: Callable[[dict], Any]) -> None:
        while self.running:
            try:
                response = self.api.receiving.receive_notification()
                if not response:
                    continue

                function(response["body"])

                self.api.receiving.delete_notification(response["receiptId"])
            except KeyboardInterrupt:
                break


__all__ = ["Webhook"]
