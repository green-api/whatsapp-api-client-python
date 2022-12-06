from whatsapp_api_client_python.base import BaseCategory


class QueuesCategory(BaseCategory):
    def show_messages_queue(self) -> dict:
        """
        The method is designed to get the list of messages that are in
        the queue to be sent.
        """

        return self.api.request("ShowMessagesQueue")

    def clear_messages_queue(self) -> dict:
        """
        The method is designed to clear the queue of messages to be
        sent.
        """

        return self.api.request("ClearMessagesQueue")


__all__ = ["QueuesCategory"]
