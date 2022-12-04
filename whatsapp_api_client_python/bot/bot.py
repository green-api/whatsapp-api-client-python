from abc import ABC
from typing import Any, Callable, List, Optional

from whatsapp_api_client_python.api import AbstractAPI


class AbstractHandler(ABC):
    type_webhook: str
    function: Callable[[dict], Any]


class Handler(AbstractHandler):
    def __init__(self, type_webhook: str, function: Callable[[dict], Any]):
        self.type_webhook = type_webhook
        self.function = function


class MessageHandler(AbstractHandler):
    type_webhook = "incomingMessageReceived"

    def __init__(
            self,
            function: Callable[[dict], Any],
            text: Optional[str] = None
    ):
        self.function = function
        self.text = text

    def check_text(self, body: dict) -> Optional[bool]:
        if not self.text:
            return True

        message_data = body["messageData"]
        type_message = message_data["typeMessage"]
        if type_message == "textMessage":
            text_message = message_data["textMessageData"]["textMessage"]
            if text_message == self.text:
                return True


class Bot:
    def __init__(self, api: AbstractAPI):
        self.api = api

        self.handlers: List[AbstractHandler] = []

    def handler(self, type_webhook: str):
        def decorator(function: Callable[[dict], Any]):
            self.handlers.append(Handler(type_webhook, function))

        return decorator

    def message(self, text: Optional[str] = None):
        def decorator(function: Callable[[dict], Any]):
            self.handlers.append(MessageHandler(function, text))

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
                    if isinstance(handler, Handler):
                        if handler.type_webhook == type_webhook:
                            handler.function(body)
                    elif isinstance(handler, MessageHandler):
                        check_result = handler.check_text(body)
                        if check_result:
                            handler_response = handler.function(body)
                            if isinstance(handler_response, str):
                                self.api.sending.send_message(
                                    chatId=body["senderData"]["chatId"],
                                    message=handler_response
                                )

                self.api.receiving.delete_notification(response["receiptId"])
            except KeyboardInterrupt:
                break
