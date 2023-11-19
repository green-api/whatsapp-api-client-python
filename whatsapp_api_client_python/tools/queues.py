from typing import TYPE_CHECKING

from ..response import Response

if TYPE_CHECKING:
    from ..API import GreenApi


class Queues:
    def __init__(self, api: "GreenApi"):
        self.api = api

    def showMessagesQueue(self) -> Response:
        """
        The method is aimed for getting a list of messages in the queue
        to be sent.
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
        """

        return self.api.request(
            "GET", (
                "{{host}}/waInstance{{idInstance}}/"
                "clearMessagesQueue/{{apiTokenInstance}}"
            )
        )
