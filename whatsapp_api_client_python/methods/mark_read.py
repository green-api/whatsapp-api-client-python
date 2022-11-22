from typing import Optional

from whatsapp_api_client_python.base import BaseCategory
from whatsapp_api_client_python.response import Response


class MarkReadCategory(BaseCategory):
    def read_chat(
            self, chatId: str, idMessage: Optional[str] = None
    ) -> Response:
        """The method is designed to mark chat messages as read."""

        data = locals()
        data.pop("self")

        return self.api.request("POST", "ReadChat", data)
