from abc import ABC, abstractmethod
from typing import Any, Callable, List, Optional, TYPE_CHECKING

from .handlers import Handler, MessageHandler

if TYPE_CHECKING:
    from whatsapp_api_client_python.api import AbstractAPI
    from .handlers import AbstractHandler


class AbstractBot(ABC):
    api: "AbstractAPI"
    handlers: List["AbstractHandler"]

    @abstractmethod
    def handler(
            self, type_webhook: str
    ) -> Callable[[Callable[[dict], Any]], None]:
        pass

    @abstractmethod
    def run_forever(self) -> None:
        pass


class Bot(AbstractBot):
    def __init__(self, api: "AbstractAPI"):
        self.api = api

        self.handlers = []

    def handler(
            self, type_webhook: str
    ) -> Callable[[Callable[[dict], Any]], None]:
        def decorator(function: Callable[[dict], Any]) -> None:
            self.handlers.append(Handler(type_webhook, function))

        return decorator

    def message(
            self, message_text: Optional[str] = None
    ) -> Callable[[Callable[[dict], Any]], None]:
        def decorator(function: Callable[[dict], Any]) -> None:
            self.handlers.append(MessageHandler(function, message_text))

        return decorator

    def run_forever(self) -> None:
        while True:
            try:
                response = self.api.receiving.receive_notification()
                if not response:
                    continue

                body = response["body"]
                type_webhook = body["typeWebhook"]

                for handler in self.handlers:
                    if handler.type_webhook == type_webhook:
                        if isinstance(handler, Handler):
                            handler.function(body)
                        elif isinstance(handler, MessageHandler):
                            check_result = handler.check_message_text(body)
                            if check_result:
                                message = handler.function(body)
                                if isinstance(message, str):
                                    self.api.sending.send_message(
                                        chatId=body["senderData"]["chatId"],
                                        message=message
                                    )

                self.api.receiving.delete_notification(response["receiptId"])
            except KeyboardInterrupt:
                break


__all__ = ["AbstractBot", "Bot"]
