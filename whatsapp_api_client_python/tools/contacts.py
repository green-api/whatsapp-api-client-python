from typing import Optional, TYPE_CHECKING

from ..response import Response

if TYPE_CHECKING:
    from ..API import GreenApi

class Contacts:
    def __init__(self, api: "GreenApi"):
        self.api = api

    def addContact(
            self, 
            chatId: str, 
            firstName: str,
            lastName: Optional[str] = None,
            saveInAddressbook: Optional[bool] = True
    ) -> Response:
        """
        The method adds a contact to the user's contact list.

        https://green-api.com/en/docs/api/contacts/AddContact/
        """

        request_body = self.__handle_parameters(locals())

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "addContact/{{apiTokenInstance}}"
            ), request_body
        )

    async def addContactAsync(
            self, 
            chatId: str, 
            firstName: str,
            lastName: Optional[str] = None,
            saveInAddressbook: Optional[bool] = True
    ) -> Response:
        request_body = self.__handle_parameters(locals())

        return await self.api.requestAsync(
            "POST",
            "{{host}}/waInstance{{idInstance}}/addContact/{{apiTokenInstance}}",
            request_body
        )

    def editContact(
            self, 
            chatId: str, 
            firstName: str,
            lastName: Optional[str] = None,
            saveInAddressbook: Optional[bool] = True
    ) -> Response:
        """
        The method edits a contact in the user's contact list.

        https://green-api.com/en/docs/api/contacts/EditContact/
        """

        request_body = self.__handle_parameters(locals())

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "editContact/{{apiTokenInstance}}"
            ), request_body
        )

    async def editContactAsync(
            self, 
            chatId: str, 
            firstName: str,
            lastName: Optional[str] = None,
            saveInAddressbook: Optional[bool] = True
    ) -> Response:
        request_body = self.__handle_parameters(locals())

        return await self.api.requestAsync(
            "POST",
            "{{host}}/waInstance{{idInstance}}/editContact/{{apiTokenInstance}}",
            request_body
        )

    def deleteContact(
            self, 
            chatId: str
    ) -> Response:
        """
        The method deletes a contact from the user's contact list.

        https://green-api.com/en/docs/api/contacts/DeleteContact/
        """

        request_body = self.__handle_parameters(locals())

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "deleteContact/{{apiTokenInstance}}"
            ), request_body
        )

    async def deleteContactAsync(
            self, 
            chatId: str
    ) -> Response:
        request_body = self.__handle_parameters(locals())

        return await self.api.requestAsync(
            "POST",
            "{{host}}/waInstance{{idInstance}}/deleteContact/{{apiTokenInstance}}",
            request_body
        )
    
    @classmethod
    def __handle_parameters(cls, parameters: dict) -> dict:
        handled_parameters = parameters.copy()
        handled_parameters.pop("self")

        for key, value in parameters.items():
            if value is None:
                handled_parameters.pop(key)

        return handled_parameters