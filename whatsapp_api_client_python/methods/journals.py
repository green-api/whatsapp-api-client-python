from typing import Optional

from whatsapp_api_client_python.base import BaseCategory


class JournalsCategory(BaseCategory):
    def get_chat_history(
            self, chatId: str, count: Optional[int] = None
    ) -> dict:
        """The method returns the chat message history."""

        data = self.handle_parameters(locals())

        return self.api.request("GetChatHistory", "POST", data)

    def last_incoming_messages(self, minutes: Optional[int] = None) -> dict:
        """
        The method returns the most recent incoming messages of the
        account.
        """

        data = self.handle_parameters(locals())

        if not data:
            return self.api.request("lastIncomingMessages")
        return self.api.request("lastIncomingMessages", "POST", data)

    def last_outgoing_messages(self, minutes: Optional[int] = None) -> dict:
        """The method returns the last sent messages of the account."""

        data = self.handle_parameters(locals())

        if not data:
            return self.api.request("LastOutgoingMessages")
        return self.api.request("LastOutgoingMessages", "POST", data)


__all__ = ["JournalsCategory"]
