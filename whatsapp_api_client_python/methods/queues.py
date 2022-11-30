from whatsapp_api_client_python.base import BaseCategory
from whatsapp_api_client_python.response import Response


class QueueCategory(BaseCategory):
    def show_messages_queue(self) -> Response:
        """
        The method is designed to get the list of messages
        that are in the queue to be sent.
        """

        return self.api.request("GET", "ShowMessagesQueue")

    def clear_messages_queue(self) -> Response:
        """
        The method is designed to clear the queue
        of messages to be sent.
        """

        return self.api.request("GET", "ClearMessagesQueue")
