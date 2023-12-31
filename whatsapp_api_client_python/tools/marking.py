from typing import Optional

from base import BaseCategory
from ..response import Response


class Marking(BaseCategory):
    def readChat(
            self, chatId: str, idMessage: Optional[str] = None
    ) -> Response:
        """
        The method is aimed for marking messages in a chat as read.

        https://green-api.com/en/docs/api/marks/ReadChat/
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


__all__ = ["Marking"]
