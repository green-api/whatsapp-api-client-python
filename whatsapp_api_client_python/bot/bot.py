from typing import Any, Callable, List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from whatsapp_api_client_python.api import AbstractAPI


class AbstractHandler:
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
            message_text: Optional[str] = None
    ):
        self.function = function
        self.message_text = message_text

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


class Bot:
    def __init__(self, api: "AbstractAPI"):
        self.api = api

        self.handlers: List[AbstractHandler] = []

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


__all__ = ["Bot"]
