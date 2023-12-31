from .base import BaseCategory
from ..response import Response


class Device(BaseCategory):
    def getDeviceInfo(self) -> Response:
        """
        The method is aimed for getting information about the device
        (phone) running WhatsApp Business application.

        https://green-api.com/en/docs/api/phone/GetDeviceInfo/
        """

        return self.api.request(
            "GET", (
                "{{host}}/waInstance{{idInstance}}/"
                "getDeviceInfo/{{apiTokenInstance}}"
            )
        )


__all__ = ["Device"]
