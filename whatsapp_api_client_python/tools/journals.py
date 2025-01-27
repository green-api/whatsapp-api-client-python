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
        """
        The method returns the chat message history.

        https://green-api.com/en/docs/api/journals/GetChatHistory/
        """

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
        """
        The method returns the chat message.

        https://green-api.com/en/docs/api/journals/GetMessage/
        """

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

        https://green-api.com/en/docs/api/journals/LastIncomingMessages/
        """

        append_minutes = ""
        if minutes is not None:
            append_minutes = f"?minutes={minutes}"

        return self.api.request(
            "GET", (
                "{{host}}/waInstance{{idInstance}}/"
                "lastIncomingMessages/{{apiTokenInstance}}"+append_minutes
            )
        )

    def lastOutgoingMessages(self, minutes: Optional[int] = None) -> Response:
        """
        The method returns the last outgoing messages of the account.

        https://green-api.com/en/docs/api/journals/LastOutgoingMessages/
        """

        append_minutes = ""
        if minutes is not None:
            append_minutes = f"?minutes={minutes}"

        return self.api.request(
            "GET", (
                "{{host}}/waInstance{{idInstance}}/"
                "lastOutgoingMessages/{{apiTokenInstance}}"+append_minutes
            )
        )
