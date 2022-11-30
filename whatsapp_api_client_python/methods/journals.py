from typing import Optional

from whatsapp_api_client_python.base import BaseCategory
from whatsapp_api_client_python.response import Response


class JournalCategory(BaseCategory):
    def get_chat_history(
            self, chatId: str, count: Optional[int] = None
    ) -> Response:
        """The method returns the chat message history."""

        data = self.handle_parameters(locals())

        return self.api.request("POST", "GetChatHistory", data)

    def last_incoming_messages(
            self, minutes: Optional[int] = None
    ) -> Response:
        """
        The method returns the most recent incoming messages
        of the account.
        """

        data = self.handle_parameters(locals())

        return self.api.request("GET", "lastIncomingMessages", data)

    def last_outgoing_messages(
            self, minutes: Optional[int] = None
    ) -> Response:
        """The method returns the last sent messages of the account."""

        data = self.handle_parameters(locals())

        return self.api.request("GET", "LastOutgoingMessages", data)
