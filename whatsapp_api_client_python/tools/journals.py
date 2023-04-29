from typing import Optional, TYPE_CHECKING

from ..response import Response

if TYPE_CHECKING:
    from ..API import GreenApi


class Journals:
    def __init__(self, api: GreenApi):
        self.api = api

    def get_chat_history(
            self, chat_id: str, count: Optional[int] = None
    ) -> Response:
        """The method returns the chat message history."""

        request_body = locals()
        if count is None:
            del request_body["count"]
        del request_body["self"]

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "GetChatHistory/{{apiTokenInstance}}"
            ), request_body
        )

    def get_message(self, chat_id: str, id_message: str) -> Response:
        """The method returns the chat message."""

        request_body = locals()
        del request_body["self"]

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "getMessage/{{apiTokenInstance}}"
            ), request_body
        )

    def last_incoming_messages(
            self, minutes: Optional[int] = None
    ) -> Response:
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

    def last_outgoing_messages(
            self, minutes: Optional[int] = None
    ) -> Response:
        """
        The method returns the last outgoing messages of the account.
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
