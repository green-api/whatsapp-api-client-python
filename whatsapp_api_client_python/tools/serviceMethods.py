from typing import Optional, TYPE_CHECKING

from ..response import Response

if TYPE_CHECKING:
    from ..API import GreenApi


class ServiceMethods:
    def __init__(self, api: "GreenApi"):
        self.api = api

    def checkWhatsapp(self, phoneNumber: int) -> Response:
        """
        The method checks WhatsApp account availability on a phone
        number.

        https://green-api.com/en/docs/api/service/CheckWhatsapp/
        """

        request_body = locals()
        request_body.pop("self")

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "checkWhatsapp/{{apiTokenInstance}}"
            ), request_body
        )

    def getAvatar(self, chatId: str) -> Response:
        """
        The method returns a user or a group chat avatar.

        https://green-api.com/en/docs/api/service/GetAvatar/
        """

        request_body = locals()
        request_body.pop("self")

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "getAvatar/{{apiTokenInstance}}"
            ), request_body
        )

    def getContacts(self) -> Response:
        """
        The method is aimed for getting a list of the current account
        contacts.

        https://green-api.com/en/docs/api/service/GetContacts/
        """

        return self.api.request(
            "GET", (
                "{{host}}/waInstance{{idInstance}}/"
                "getContacts/{{apiTokenInstance}}"
            )
        )

    def getContactInfo(self, chatId: str) -> Response:
        """
        The method is aimed for getting information on a contact.

        https://green-api.com/en/docs/api/service/GetContactInfo/
        """

        request_body = locals()
        request_body.pop("self")

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "getContactInfo/{{apiTokenInstance}}"
            ), request_body
        )

    def deleteMessage(self, chatId: str, idMessage: str) -> Response:
        """
        The method deletes a message from a chat.

        https://green-api.com/en/docs/api/service/deleteMessage/
        """

        request_body = locals()
        request_body.pop("self")

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "deleteMessage/{{apiTokenInstance}}"
            ), request_body
        )

    def archiveChat(self, chatId: str) -> Response:
        """
        The method archives a chat.

        https://green-api.com/en/docs/api/service/archiveChat/
        """

        request_body = locals()
        request_body.pop("self")

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "archiveChat/{{apiTokenInstance}}"
            ), request_body
        )

    def unarchiveChat(self, chatId: str) -> Response:
        """
        The method unarchives a chat.

        https://green-api.com/en/docs/api/service/unarchiveChat/
        """

        request_body = locals()
        request_body.pop("self")

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "unarchiveChat/{{apiTokenInstance}}"
            ), request_body
        )

    def setDisappearingChat(
            self, chatId: str, ephemeralExpiration: Optional[int] = None
    ) -> Response:
        """
        The method is aimed for changing settings of disappearing
        messages in chats.

        https://green-api.com/en/docs/api/service/SetDisappearingChat/
        """

        request_body = locals()
        if ephemeralExpiration is None:
            request_body.pop("ephemeralExpiration")
        request_body.pop("self")

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "setDisappearingChat/{{apiTokenInstance}}"
            ), request_body
        )
