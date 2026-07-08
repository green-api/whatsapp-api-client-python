from typing import Optional, TYPE_CHECKING

from ..response import Response

if TYPE_CHECKING:
    from ..API import GreenApi

class ServiceMethods:
    def __init__(self, api: "GreenApi"):
        self.api = api

    def checkWhatsapp(
            self,
            phoneNumber: Optional[int] = None,
            chatId: Optional[str] = None,
            force: Optional[bool] = None
    ) -> Response:
        """
        The method checks WhatsApp account availability on a phone number.
        Use chatId (e.g. "79001234567@c.us") as the preferred parameter.
        phoneNumber is kept for backward compatibility.

        https://green-api.com/en/docs/api/service/CheckWhatsapp/
        """

        request_body = locals()
        if phoneNumber is None:
            request_body.pop("phoneNumber")
        if chatId is None:
            request_body.pop("chatId")
        if force is None:
            request_body.pop("force")
        request_body.pop("self")

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "checkWhatsapp/{{apiTokenInstance}}"
            ), request_body
        )

    async def checkWhatsappAsync(
            self,
            phoneNumber: Optional[int] = None,
            chatId: Optional[str] = None,
            force: Optional[bool] = None
    ) -> Response:
        request_body = locals()
        if phoneNumber is None:
            request_body.pop("phoneNumber")
        if chatId is None:
            request_body.pop("chatId")
        if force is None:
            request_body.pop("force")
        request_body.pop("self")

        return await self.api.requestAsync(
            "POST",
            "{{host}}/waInstance{{idInstance}}/checkWhatsapp/{{apiTokenInstance}}",
            request_body
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

    async def getAvatarAsync(self, chatId: str) -> Response:
        request_body = locals()
        request_body.pop("self")

        return await self.api.requestAsync(
            "POST",
            "{{host}}/waInstance{{idInstance}}/getAvatar/{{apiTokenInstance}}",
            request_body
        )

    def getContacts(
            self,
            group: Optional[bool] = None,
            count: Optional[int] = None
    ) -> Response:
        """
        The method is aimed for getting a list of the current account
        contacts.

        https://green-api.com/en/docs/api/service/GetContacts/
        """

        url = (
            "{{host}}/waInstance{{idInstance}}/"
            "getContacts/{{apiTokenInstance}}"
        )
        query_parts = []
        if group is not None:
            query_parts.append(f"group={'true' if group else 'false'}")
        if count is not None:
            query_parts.append(f"count={count}")
        if query_parts:
            url = f"{url}?{'&'.join(query_parts)}"

        return self.api.request("GET", url)

    async def getContactsAsync(
            self,
            group: Optional[bool] = None,
            count: Optional[int] = None
    ) -> Response:
        url = "{{host}}/waInstance{{idInstance}}/getContacts/{{apiTokenInstance}}"
        query_parts = []
        if group is not None:
            query_parts.append(f"group={'true' if group else 'false'}")
        if count is not None:
            query_parts.append(f"count={count}")
        if query_parts:
            url = f"{url}?{'&'.join(query_parts)}"

        return await self.api.requestAsync("GET", url)

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

    async def getContactInfoAsync(self, chatId: str) -> Response:
        request_body = locals()
        request_body.pop("self")

        return await self.api.requestAsync(
            "POST",
            "{{host}}/waInstance{{idInstance}}/getContactInfo/{{apiTokenInstance}}",
            request_body
        )

    def deleteMessage(self, chatId: str, idMessage: str, onlySenderDelete: Optional[bool] = None) -> Response:
        """
        The method deletes a message from a chat.

        https://green-api.com/en/docs/api/service/deleteMessage/
        """

        request_body = locals()
        if onlySenderDelete is None:
            request_body.pop("onlySenderDelete")
        request_body.pop("self")
        print(request_body)

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "deleteMessage/{{apiTokenInstance}}"
            ), request_body
        )

    async def deleteMessageAsync(self, chatId: str, idMessage: str, onlySenderDelete: Optional[bool] = None) -> Response:
        request_body = locals()
        if onlySenderDelete is None:
            request_body.pop("onlySenderDelete")
        request_body.pop("self")

        return await self.api.requestAsync(
            "POST",
            "{{host}}/waInstance{{idInstance}}/deleteMessage/{{apiTokenInstance}}",
            request_body
        )

    def editMessage(self, chatId: str, idMessage: str, message: str) -> Response:
        """
        The method edits a message in chat.

        https://green-api.com/en/docs/api/service/editMessage/
        """

        request_body = locals()
        request_body.pop("self")

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "editMessage/{{apiTokenInstance}}"
            ), request_body
        )

    async def editMessageAsync(self, chatId: str, idMessage: str, message: str) -> Response:
        request_body = locals()
        request_body.pop("self")

        return await self.api.requestAsync(
            "POST",
            "{{host}}/waInstance{{idInstance}}/editMessage/{{apiTokenInstance}}",
            request_body
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

    async def archiveChatAsync(self, chatId: str) -> Response:
        request_body = locals()
        request_body.pop("self")

        return await self.api.requestAsync(
            "POST",
            "{{host}}/waInstance{{idInstance}}/archiveChat/{{apiTokenInstance}}",
            request_body
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

    async def unarchiveChatAsync(self, chatId: str) -> Response:
        request_body = locals()
        request_body.pop("self")

        return await self.api.requestAsync(
            "POST",
            "{{host}}/waInstance{{idInstance}}/unarchiveChat/{{apiTokenInstance}}",
            request_body
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

    async def setDisappearingChatAsync(
            self, chatId: str, ephemeralExpiration: Optional[int] = None
    ) -> Response:
        request_body = locals()
        if ephemeralExpiration is None:
            request_body.pop("ephemeralExpiration")
        request_body.pop("self")

        return await self.api.requestAsync(
            "POST",
            "{{host}}/waInstance{{idInstance}}/setDisappearingChat/{{apiTokenInstance}}",
            request_body
        )
    
    def sendTyping(
            self, chatId: str, typingTime: Optional[int] = None, typingType: Optional[str] = None,
    ) -> Response:
        """
        The method is used to send a notification about typing or recording audio in a chat.

        https://green-api.com/en/docs/api/service/SendTyping/
        """

        request_body = locals()
        if typingTime is None:
            request_body.pop("typingTime")
        if typingType is None:
            request_body.pop("typingType")
        request_body.pop("self")

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "sendTyping/{{apiTokenInstance}}"
            ), request_body
        )

    async def sendTypingAsync(
            self, chatId: str, typingTime: Optional[int] = None, typingType: Optional[str] = None,
    ) -> Response:
        request_body = locals()
        if typingTime is None:
            request_body.pop("typingTime")
        if typingType is None:
            request_body.pop("typingType")
        request_body.pop("self")

        return await self.api.requestAsync(
            "POST",
            "{{host}}/waInstance{{idInstance}}/sendTyping/{{apiTokenInstance}}",
            request_body
        )

    def getChats(self, count: Optional[int] = None) -> Response:
        """
        The method returns a list of chats sorted by message activity time.

        https://green-api.com/en/docs/api/service/GetChats/
        """

        url = (
            "{{host}}/waInstance{{idInstance}}/"
            "getChats/{{apiTokenInstance}}"
        )
        if count is not None:
            url = f"{url}?count={count}"

        return self.api.request("GET", url)

    async def getChatsAsync(self, count: Optional[int] = None) -> Response:
        url = "{{host}}/waInstance{{idInstance}}/getChats/{{apiTokenInstance}}"
        if count is not None:
            url = f"{url}?count={count}"

        return await self.api.requestAsync("GET", url)