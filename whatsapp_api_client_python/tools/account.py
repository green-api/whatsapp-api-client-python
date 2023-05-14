from pathlib import Path
from typing import Optional, TYPE_CHECKING

from ..response import Response

if TYPE_CHECKING:
    from ..API import GreenApi


class Account:
    def __init__(self, api: "GreenApi"):
        self.api = api

    def get_settings(self) -> Response:
        """
        The method is aimed for getting the current account settings.
        """

        return self.api.request(
            "GET", (
                "{{host}}/waInstance{{idInstance}}/"
                "GetSettings/{{apiTokenInstance}}"
            )
        )

    def set_settings(
            self,
            countryInstance: Optional[str] = None,
            webhookUrl: Optional[str] = None,
            webhookUrlToken: Optional[str] = None,
            delaySendMessagesMilliseconds: Optional[int] = None,
            markIncomingMessagesReaded: Optional[str] = None,
            markIncomingMessagesReadedOnReply: Optional[str] = None,
            outgoingWebhook: Optional[str] = None,
            outgoingMessageWebhook: Optional[str] = None,
            stateWebhook: Optional[str] = None,
            incomingWebhook: Optional[str] = None,
            deviceWebhook: Optional[str] = None,
            statusInstanceWebhook: Optional[str] = None,
            sendFromUTC: Optional[str] = None,
            sendToUTC: Optional[str] = None
    ) -> Response:
        """The method is aimed for setting account settings."""

        parameters = locals()
        request_body = parameters.copy()

        del request_body["self"]

        for key, value in parameters.items():
            if value is None:
                del request_body[key]

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "SetSettings/{{apiTokenInstance}}"
            ), request_body
        )

    def get_state_instance(self) -> Response:
        """The method is aimed for getting the account state."""

        return self.api.request(
            "GET", (
                "{{host}}/waInstance{{idInstance}}/"
                "getStateInstance/{{apiTokenInstance}}"
            )
        )

    def get_status_instance(self) -> Response:
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
                "{{host}}/waInstance{{idInstance}}/Reboot/{{apiTokenInstance}}"
            )
        )

    def logout(self) -> Response:
        """The method is aimed for logging out an account."""

        return self.api.request(
            "GET", (
                "{{host}}/waInstance{{idInstance}}/Logout/{{apiTokenInstance}}"
            )
        )

    def qr(self) -> Response:
        """The method is aimed for getting QR code."""

        return self.api.request(
            "GET", "{{host}}/waInstance{{idInstance}}/qr/{{apiTokenInstance}}"
        )

    def set_profile_picture(self, file: str) -> Response:
        """The method is aimed for setting an account picture."""

        file_name = Path(file).name
        files = {"file": (file_name, open(file, "rb"), "image/jpeg")}

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "SetSettings/{{apiTokenInstance}}"
            ), files=files
        )
