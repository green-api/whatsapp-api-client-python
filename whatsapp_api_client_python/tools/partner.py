from typing import Dict, TYPE_CHECKING, Union

from ..response import Response

if TYPE_CHECKING:
    from ..API import GreenApiPartner

class Partner:
    def __init__(self, api: "GreenApiPartner"):
        self.api = api
   
    def getInstances(self) -> Response:
        """
        The method is aimed for getting all the account instances created by the partner.

        https://green-api.com/en/docs/partners/getInstances/
        """

        return self.api.request(
            "GET", (
                "{{host}}/partner/"
                "getInstances/{{partnerToken}}"
            )
        )

    async def getInstancesAsync(self) -> Response:
        return await self.api.requestAsync(
            "GET", "{{host}}/partner/getInstances/{{partnerToken}}"
        )

    def createInstance(self, requestBody: Dict[str, Union[int, str]]) -> Response:
        """
        The method is aimed for creating a messenger account instance on the partner's part.

        https://green-api.com/en/docs/partners/createInstance/
        """

        return self.api.request(
            "POST", (
                "{{host}}/partner/"
                "createInstance/{{partnerToken}}"
            ), requestBody
        )

    async def createInstanceAsync(self, requestBody: Dict[str, Union[int, str]]) -> Response:
        return await self.api.requestAsync(
            "POST",
            "{{host}}/partner/createInstance/{{partnerToken}}",
            requestBody
        )

    def deleteInstanceAccount(self, idInstance: int) -> Response:
        """
        The method is aimed for deleting an instance of the partners's account.

        https://green-api.com/en/docs/partners/deleteInstanceAccount/
        """

        request_body = self.__handle_parameters(locals())

        return self.api.request(
            "POST", (
                "{{host}}/partner/"
                "deleteInstanceAccount/{{partnerToken}}"
            ), request_body
        )

    async def deleteInstanceAccountAsync(self, idInstance: int) -> Response:
        request_body = self.__handle_parameters(locals())

        return await self.api.requestAsync(
            "POST",
            "{{host}}/partner/deleteInstanceAccount/{{partnerToken}}",
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