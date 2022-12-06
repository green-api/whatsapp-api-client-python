from typing import Optional

from whatsapp_api_client_python.base import BaseCategory


class ServiceMethodsCategory(BaseCategory):
    def check_whatsapp(self, phoneNumber: int) -> dict:
        """
        The method checks if there is a WhatsApp account on the phone
        number.
        """

        data = self.handle_parameters(locals())

        return self.api.request("CheckWhatsapp", "POST", data)

    def get_avatar(self, chatId: str) -> dict:
        """
        The method returns the avatar of the correspondent or group
        chat.
        """

        data = self.handle_parameters(locals())

        return self.api.request("GetAvatar", "POST", data)

    def get_contacts(self) -> dict:
        """
        The method is designed to get the list of contacts of the
        current account.
        """

        return self.api.request("GetContacts")

    def get_contact_info(self, chatId: str) -> dict:
        """
        The method is designed to get information about the contact.
        """

        data = self.handle_parameters(locals())

        return self.api.request("getContactInfo", "POST", data)

    def delete_message(self, chatId: str, idMessage: str) -> dict:
        """The method deletes the message from the chat."""

        data = self.handle_parameters(locals())

        return self.api.request("deleteMessage", "POST", data)

    def archive_chat(self, chatId: str) -> dict:
        """The method archives the chat."""

        data = self.handle_parameters(locals())

        return self.api.request("archiveChat", "POST", data)

    def unarchive_chat(self, chatId: str) -> dict:
        """The method unarchives the chat."""

        data = self.handle_parameters(locals())

        return self.api.request("unarchiveChat", "POST", data)

    def set_disappearing_chat(
            self, chatId: str, ephemeralExpiration: Optional[int] = None
    ) -> dict:
        """
        The method is designed to change the settings of disappearing
        messages in chats.
        """

        data = self.handle_parameters(locals())

        return self.api.request("setDisappearingChat", "POST", data)


__all__ = ["ServiceMethodsCategory"]
