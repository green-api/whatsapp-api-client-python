from typing import Optional, TYPE_CHECKING

from ..response import Response

if TYPE_CHECKING:
    from ..API import GreenApi


class Journals:
    def __init__(self, api: "GreenApi"):
        self.api = api

    def getChatHistory(
            self, chatId: str, count: Optional[int] = None
    ) -> Response:
        """The method returns the chat message history."""

        request_body = locals()
        if count is None:
            request_body.pop("count")
        request_body.pop("self")

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "getChatHistory/{{apiTokenInstance}}"
            ), request_body
        )

    def getMessage(self, chatId: str, idMessage: str) -> Response:
        """The method returns the chat message."""

        request_body = locals()
        request_body.pop("self")

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "getMessage/{{apiTokenInstance}}"
            ), request_body
        )

    def lastIncomingMessages(self, minutes: Optional[int] = None) -> Response:
        """
        The method returns the last incoming messages of the account.
        """

        request_body = None
        if minutes is not None:
            request_body = {"minutes": minutes}

        return self.api.request(
            "GET", (
                "{{host}}/waInstance{{idInstance}}/"
                "lastIncomingMessages/{{apiTokenInstance}}"
            ), request_body
        )

    def lastOutgoingMessages(self, minutes: Optional[int] = None) -> Response:
        """
        The method returns the last outgoing messages of the account.
        """

        request_body = None
        if minutes is not None:
            request_body = {"minutes": minutes}

        return self.api.request(
            "GET", (
                "{{host}}/waInstance{{idInstance}}/"
                "lastOutgoingMessages/{{apiTokenInstance}}"
            ), request_body
        )
