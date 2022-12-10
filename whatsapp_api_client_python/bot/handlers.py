from abc import ABC, abstractmethod
from typing import Any, Callable, Optional


class AbstractHandler(ABC):
    type_webhook: str
    function: Callable[[dict], Any]

    @abstractmethod
    def check_event(self, body: dict) -> bool:
        pass


class Handler(AbstractHandler):
    def __init__(self, type_webhook: str, function: Callable[[dict], Any]):
        self.type_webhook = type_webhook
        self.function = function

    def check_event(self, body: dict) -> bool:
        return True


class MessageHandler(AbstractHandler):
    type_webhook = "incomingMessageReceived"

    def __init__(
            self,
            function: Callable[[dict], Any],
            message_text: Optional[str] = None
    ):
        self.function = function

        self.message_text = message_text

    def check_event(self, body: dict) -> bool:
        return self.check_message_text(body)

    def check_message_text(self, body: dict) -> bool:
        if self.message_text is None:
            return True

        message_data = body["messageData"]
        type_message = message_data["typeMessage"]
        if type_message == "textMessage":
            text_message = message_data["textMessageData"]["textMessage"]
            if text_message == self.message_text:
                return True

        return False


__all__ = ["AbstractHandler", "Handler", "MessageHandler"]
