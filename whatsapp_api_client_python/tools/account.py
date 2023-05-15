from pathlib import Path
from typing import Dict, TYPE_CHECKING, Union

from ..response import Response

if TYPE_CHECKING:
    from ..API import GreenApi


class Account:
    def __init__(self, api: "GreenApi"):
        self.api = api

    def getSettings(self) -> Response:
        """
        The method is aimed for getting the current account settings.
        """

        return self.api.request(
            "GET", (
                "{{host}}/waInstance{{idInstance}}/"
                "getSettings/{{apiTokenInstance}}"
            )
        )

    def setSettings(self, requestBody: Dict[str, Union[int, str]]) -> Response:
        """The method is aimed for setting account settings."""

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "setSettings/{{apiTokenInstance}}"
            ), requestBody
        )

    def getStateInstance(self) -> Response:
        """The method is aimed for getting the account state."""

        return self.api.request(
            "GET", (
                "{{host}}/waInstance{{idInstance}}/"
                "getStateInstance/{{apiTokenInstance}}"
            )
        )

    def getStatusInstance(self) -> Response:
        """
        The method is aimed for getting the status of the account
        instance socket connection with WhatsApp.
        """

        return self.api.request(
            "GET", (
                "{{host}}/waInstance{{idInstance}}/"
                "getStatusInstance/{{apiTokenInstance}}"
            )
        )

    def reboot(self) -> Response:
        """The method is aimed for rebooting an account."""

        return self.api.request(
            "GET", (
                "{{host}}/waInstance{{idInstance}}/reboot/{{apiTokenInstance}}"
            )
        )

    def logout(self) -> Response:
        """The method is aimed for logging out an account."""

        return self.api.request(
            "GET", (
                "{{host}}/waInstance{{idInstance}}/logout/{{apiTokenInstance}}"
            )
        )

    def qr(self) -> Response:
        """The method is aimed for getting QR code."""

        return self.api.request(
            "GET", "{{host}}/waInstance{{idInstance}}/qr/{{apiTokenInstance}}"
        )

    def setProfilePicture(self, path: str) -> Response:
        """The method is aimed for setting an account picture."""

        file_name = Path(path).name
        files = {"file": (file_name, open(path, "rb"), "image/jpeg")}

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "setProfilePicture/{{apiTokenInstance}}"
            ), files=files
        )
