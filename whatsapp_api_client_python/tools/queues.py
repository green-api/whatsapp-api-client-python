from base import BaseCategory
from ..response import Response


class Queues(BaseCategory):
    def showMessagesQueue(self) -> Response:
        """
        The method is aimed for getting a list of messages in the queue
        to be sent.

        https://green-api.com/en/docs/api/queues/ShowMessagesQueue/
        """

        return self.api.request(
            "GET", (
                "{{host}}/waInstance{{idInstance}}/"
                "showMessagesQueue/{{apiTokenInstance}}"
            )
        )

    def clearMessagesQueue(self) -> Response:
        """
        The method is aimed for clearing the queue of messages to be
        sent.

        https://green-api.com/en/docs/api/queues/ClearMessagesQueue/
        """

        return self.api.request(
            "GET", (
                "{{host}}/waInstance{{idInstance}}/"
                "clearMessagesQueue/{{apiTokenInstance}}"
            )
        )


__all__ = ["Queues"]
