from typing import TYPE_CHECKING

from ..response import Response

if TYPE_CHECKING:
    from ..API import GreenAPI


class Device:
    def __init__(self, api: "GreenAPI"):
        self.api = api

    def getDeviceInfo(self) -> Response:
        """
        The method is aimed for getting information about the device
        (phone) running WhatsApp Business application.
        """

        return self.api.request(
            "GET", (
                "{{host}}/waInstance{{idInstance}}/"
                "getDeviceInfo/{{apiTokenInstance}}"
            )
        )
