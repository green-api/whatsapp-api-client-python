from typing import Optional

from whatsapp_api_client_python.base import BaseCategory
from whatsapp_api_client_python.response import Response


class ServiceMethodCategory(BaseCategory):
    def check_whatsapp(self, phoneNumber: int) -> Response:
        """
        The method checks if there is a WhatsApp account
        on the phone number.
        """

        data = self.handle_parameters(locals())

        return self.api.request("POST", "CheckWhatsapp", data)

    def get_avatar(self, chatId: str) -> Response:
        """
        The method returns the avatar of the correspondent or
        group chat.
        """

        data = self.handle_parameters(locals())

        return self.api.request("POST", "GetAvatar", data)

    def get_contacts(self) -> Response:
        """
        The method is designed to get the list of contacts
        of the current account.
        """

        return self.api.request("GET", "GetContacts")

    def get_contact_info(self, chatId: str) -> Response:
        """
        The method is designed to get information about the contact.
        """

        data = self.handle_parameters(locals())

        return self.api.request("POST", "getContactInfo", data)

    def delete_message(self, chatId: str, idMessage: str) -> Response:
        """The method deletes the message from the chat."""

        data = self.handle_parameters(locals())

        return self.api.request("POST", "deleteMessage", data)

    def archive_chat(self, chatId: str) -> Response:
        """The method archives the chat."""

        data = self.handle_parameters(locals())

        return self.api.request("POST", "archiveChat", data)

    def unarchive_chat(self, chatId: str) -> Response:
        """The method unarchives the chat."""

        data = self.handle_parameters(locals())

        return self.api.request("POST", "unarchiveChat", data)

    def set_disappearing_chat(
            self, chatId: str, ephemeralExpiration: Optional[int] = None
    ) -> Response:
        """
        The method is designed to change the settings
        of disappearing messages in chats.
        """

        data = self.handle_parameters(locals())

        return self.api.request("POST", "setDisappearingChat", data)
