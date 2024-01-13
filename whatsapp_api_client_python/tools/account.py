from pathlib import Path
from typing import Dict, Union

from .base import BaseCategory
from ..response import Response
from ..responses.account import (
    GetAuthorizationCodeResponse,
    GetSettingsResponse,
    GetStateInstanceResponse,
    GetStatusInstanceResponse,
    GetWASettingsResponse,
    LogoutResponse,
    QRResponse,
    RebootResponse,
    SetProfilePictureResponse,
    SetSettingsResponse
)


class Account(BaseCategory):
    def getSettings(self) -> Response[GetSettingsResponse]:
        """
        The method is aimed for getting the current account settings.

        https://green-api.com/en/docs/api/account/GetSettings/
        """

        response = self.api.request(
            "GET", (
                "{{host}}/waInstance{{idInstance}}/"
                "getSettings/{{apiTokenInstance}}"
            )
        )

        response.create_model(GetSettingsResponse)

        return response

    def getWaSettings(self) -> Response[GetWASettingsResponse]:
        """
        The method is aimed to get information about the WhatsApp
        account.

        https://green-api.com/en/docs/api/account/GetWaSettings/
        """

        response = self.api.request(
            "GET", (
                "{{host}}/waInstance{{idInstance}}/"
                "getWaSettings/{{apiTokenInstance}}"
            )
        )

        response.create_model(GetWASettingsResponse)

        return response

    def setSettings(
            self, requestBody: Dict[str, Union[int, str]]
    ) -> Response[SetSettingsResponse]:
        """
        The method is aimed for setting account settings.

        https://green-api.com/en/docs/api/account/SetSettings/
        """

        response = self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "setSettings/{{apiTokenInstance}}"
            ), requestBody
        )

        response.create_model(SetSettingsResponse)

        return response

    def getStateInstance(self) -> Response[GetStateInstanceResponse]:
        """
        The method is aimed for getting the account state.

        https://green-api.com/en/docs/api/account/GetStateInstance/
        """

        response = self.api.request(
            "GET", (
                "{{host}}/waInstance{{idInstance}}/"
                "getStateInstance/{{apiTokenInstance}}"
            )
        )

        response.create_model(GetStateInstanceResponse)

        return response

    def getStatusInstance(self) -> Response[GetStatusInstanceResponse]:
        """
        The method is aimed for getting the status of the account
        instance socket connection with WhatsApp.

        https://green-api.com/en/docs/api/account/GetStatusInstance/
        """

        response = self.api.request(
            "GET", (
                "{{host}}/waInstance{{idInstance}}/"
                "getStatusInstance/{{apiTokenInstance}}"
            )
        )

        response.create_model(GetStatusInstanceResponse)

        return response

    def reboot(self) -> Response[RebootResponse]:
        """
        The method is aimed for rebooting an account.

        https://green-api.com/en/docs/api/account/Reboot/
        """

        response = self.api.request(
            "GET", (
                "{{host}}/waInstance{{idInstance}}/reboot/{{apiTokenInstance}}"
            )
        )

        response.create_model(RebootResponse)

        return response

    def logout(self) -> Response[LogoutResponse]:
        """
        The method is aimed for logging out an account.

        https://green-api.com/en/docs/api/account/Logout/
        """

        response = self.api.request(
            "GET", (
                "{{host}}/waInstance{{idInstance}}/logout/{{apiTokenInstance}}"
            )
        )

        response.create_model(LogoutResponse)

        return response

    def qr(self) -> Response[QRResponse]:
        """
        The method is aimed for getting QR code.

        https://green-api.com/en/docs/api/account/QR/
        """

        response = self.api.request(
            "GET", "{{host}}/waInstance{{idInstance}}/qr/{{apiTokenInstance}}"
        )

        response.create_model(QRResponse)

        return response

    def setProfilePicture(
            self, path: str
    ) -> Response[SetProfilePictureResponse]:
        """
        The method is aimed for setting an account picture.

        https://green-api.com/en/docs/api/account/SetProfilePicture/
        """

        file_name = Path(path).name
        files = {"file": (file_name, open(path, "rb"), "image/jpeg")}

        response = self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "setProfilePicture/{{apiTokenInstance}}"
            ), files=files
        )

        response.create_model(SetProfilePictureResponse)

        return response

    def getAuthorizationCode(
            self, phoneNumber: int
    ) -> Response[GetAuthorizationCodeResponse]:
        """
        The method is designed to authorize an instance by phone number.

        https://green-api.com/en/docs/api/account/GetAuthorizationCode/
        """

        request_body = locals()
        request_body.pop("self")

        response = self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "getAuthorizationCode/{{apiTokenInstance}}"
            ), request_body
        )

        response.create_model(GetAuthorizationCodeResponse)

        return response


__all__ = ["Account"]
