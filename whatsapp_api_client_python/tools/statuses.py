from typing import List, Optional, TYPE_CHECKING

from ..response import Response

if TYPE_CHECKING:
    from ..API import GreenApi


class Statuses:
    def __init__(self, api: "GreenApi"):
        self.api = api

    def sendTextStatus(
            self,
            message: str,
            backgroundColor: Optional[str] = None,
            font: Optional[str] = None,
            participants: Optional[List[str]] = None
    ) -> Response:
        """
        The method is aimed for sending a text status.

        https://green-api.com/en/docs/api/statuses/SendTextStatus/
        """

        request_body = self.__handle_parameters(locals())

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "sendTextStatus/{{apiTokenInstance}}"
            ), request_body
        )

    def sendVoiceStatus(
            self,
            urlFile: str,
            fileName: str,
            backgroundColor: Optional[str] = None,
            participants: Optional[List[str]] = None
    ) -> Response:
        """
        The method is aimed for sending a voice status.

        https://green-api.com/en/docs/api/statuses/SendVoiceStatus/
        """

        request_body = self.__handle_parameters(locals())

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "sendVoiceStatus/{{apiTokenInstance}}"
            ), request_body
        )

    def sendMediaStatus(
            self,
            urlFile: str,
            fileName: str,
            caption: Optional[str] = None,
            participants: Optional[List[str]] = None
    ) -> Response:
        """
        The method is aimed for sending a pictures or video status.

        https://green-api.com/en/docs/api/statuses/SendMediaStatus/
        """

        request_body = self.__handle_parameters(locals())

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "sendMediaStatus/{{apiTokenInstance}}"
            ), request_body
        )

    def deleteStatus(
            self,
            idMessage: str
    ) -> Response:
        """
        The method is aimed for deleting a certain status.

        https://green-api.com/en/docs/api/statuses/DeleteStatus/
        """

        request_body = self.__handle_parameters(locals())

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "deleteStatus/{{apiTokenInstance}}"
            ), request_body
        )

    def getStatusStatistic(
            self,
            idMessage: str
    ) -> Response:
        """
        The method returns an array of recipients marked sent/delivered/read for a given status.

        https://green-api.com/en/docs/api/statuses/GetStatusStatistic/
        """
        url = (
            "{{host}}/waInstance{{idInstance}}/"
            "getStatusStatistic/{{apiTokenInstance}}"
        )

        return self.api.request("GET", f"{url}?idMessage={idMessage}")

    def getIncomingStatuses(
            self,
            minutes: Optional[int] = None
    ) -> Response:
        """
        The method returns the incoming statuses of the account
        If no argument passed, the incoming statuses for the past 24 hours are returned.

        https://green-api.com/en/docs/api/statuses/GetIncomingStatuses/
        """
        url = (
            "{{host}}/waInstance{{idInstance}}/"
            "getIncomingStatuses/{{apiTokenInstance}}"
        )

        if minutes:
            return self.api.request("GET", f"{url}?minutes={minutes}")
        else:
            return self.api.request("GET", f"{url}")

    def getOutgoingStatuses(
            self,
            minutes: Optional[int] = None
    ) -> Response:
        """
        The method returns the outgoing statuses of the account
        If no argument passed, the outgoing statuses for the past 24 hours are returned.

        https://green-api.com/en/docs/api/statuses/GetOutgoingStatuses/
        """
        url = (
            "{{host}}/waInstance{{idInstance}}/"
            "getOutgoingStatuses/{{apiTokenInstance}}"
        )

        if minutes:
            return self.api.request("GET", f"{url}?minutes={minutes}")
        else:
            return self.api.request("GET", f"{url}")

    @classmethod
    def __handle_parameters(cls, parameters: dict) -> dict:
        handled_parameters = parameters.copy()

        handled_parameters.pop("self")

        for key, value in parameters.items():
            if value is None:
                handled_parameters.pop(key)

        return handled_parameters
