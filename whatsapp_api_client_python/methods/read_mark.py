from typing import Optional

from whatsapp_api_client_python.base import BaseCategory


class ReadMarkCategory(BaseCategory):
    def read_chat(self, chatId: str, idMessage: Optional[str] = None) -> dict:
        """The method is designed to mark chat messages as read."""

        data = self.handle_parameters(locals())

        return self.api.request("ReadChat", "POST", data)


__all__ = ["ReadMarkCategory"]
