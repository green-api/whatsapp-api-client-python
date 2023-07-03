from typing import Optional, TYPE_CHECKING

from ..response import Response

if TYPE_CHECKING:
    from ..API import GreenApi


class Marking:
    def __init__(self, api: "GreenApi"):
        self.api = api

    def readChat(
            self, chatId: str, idMessage: Optional[str] = None
    ) -> Response:
        """
        The method is aimed for marking messages in a chat as read.
        """

        request_body = locals()
        if idMessage is None:
            request_body.pop("idMessage")
        request_body.pop("self")

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "readChat/{{apiTokenInstance}}"
            ), request_body
        )
