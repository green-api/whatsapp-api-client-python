import logging
from typing import Any, Callable, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from ..API import GreenApi


class Webhooks:
    _running: Optional[bool] = None

    def __init__(self, api: "GreenApi"):
        self.api = api

    @property
    def started(self) -> Optional[bool]:
        """Deprecated"""

        self.api.logger.log(logging.WARNING, "This property is deprecated.")

        return self._running

    @started.setter
    def started(self, value: bool) -> None:
        """Deprecated"""

        self.api.logger.log(logging.WARNING, "This property is deprecated.")

        self._running = value

    def startReceivingNotifications(
            self, onEvent: Callable[[str, dict], Any]
    ) -> None:
        self._running = True

        self._start_polling(onEvent)

    def stopReceivingNotifications(self) -> None:
        self._running = False

    def job(self, onEvent: Callable[[str, dict], Any]) -> None:
        """Deprecated"""

        self.api.logger.log(logging.WARNING, "This function is deprecated.")

        print((
            "Started receiving incoming notifications."
            " To stop the process, press Ctrl + C."
        ))

        while self.started:
            try:
                response = self.api.receiving.receiveNotification()
                if response.code == 200:
                    if not response.data:
                        continue
                    response = response.data

                    body = response["body"]
                    type_webhook = body["typeWebhook"]

                    onEvent(type_webhook, body)

                    self.api.receiving.deleteNotification(
                        response["receiptId"]
                    )
            except KeyboardInterrupt:
                break

        print("Stopped receiving incoming notifications.")

    def _start_polling(self, handler: Callable[[str, dict], Any]) -> None:
        self.api.session.headers["Connection"] = "keep-alive"

        self.api.logger.log(
            logging.INFO, "Started receiving incoming notifications."
        )

        while self._running:
            try:
                response = self.api.receiving.receiveNotification()
                if response.code == 200:
                    if not response.data:
                        continue
                    response = response.data

                    body = response["body"]
                    type_webhook = body["typeWebhook"]

                    handler(type_webhook, body)

                    self.api.receiving.deleteNotification(
                        response["receiptId"]
                    )
            except KeyboardInterrupt:
                break

        self.api.session.headers["Connection"] = "close"

        self.api.logger.log(
            logging.INFO, "Stopped receiving incoming notifications."
        )
