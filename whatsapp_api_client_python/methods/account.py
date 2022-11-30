from pathlib import Path
from typing import Optional

from whatsapp_api_client_python.base import BaseCategory
from whatsapp_api_client_python.response import Response


class AccountCategory(BaseCategory):
    def get_settings(self) -> Response:
        """
        The method is designed to get the current account settings.
        """

        return self.api.request("GET", "GetSettings")

    def set_settings(
            self,
            countryInstance: Optional[str] = None,
            webhookUrl: Optional[str] = None,
            webhookUrlToken: Optional[str] = None,
            delaySendMessagesMilliseconds: Optional[int] = None,
            markIncomingMessagesReaded: Optional[str] = None,
            markIncomingMessagesReadedOnReply: Optional[str] = None,
            proxyInstance: Optional[str] = None,
            outgoingWebhook: Optional[str] = None,
            outgoingMessageWebhook: Optional[str] = None,
            stateWebhook: Optional[str] = None,
            incomingWebhook: Optional[str] = None,
            deviceWebhook: Optional[str] = None,
            statusInstanceWebhook: Optional[str] = None,
            sendFromUTC: Optional[str] = None,
            sendToUTC: Optional[str] = None,
            sharedSession: Optional[str] = None
    ) -> Response:
        """The method is for setting account settings."""

        data = self.handle_parameters(locals())

        return self.api.request("POST", "SetSettings", data)

    def set_system_proxy(self) -> Response:
        """The method is for setting up a system proxy."""

        return self.api.request("GET", "SetSystemProxy")

    def get_state_instance(self) -> Response:
        """The method is designed to get the state of the account."""

        return self.api.request("GET", "getStateInstance")

    def get_status_instance(self) -> Response:
        """
        The method is designed to get the socket connection state
        of the account instance with WhatsApp.
        """

        return self.api.request("GET", "getStatusInstance")

    def reboot(self) -> Response:
        """The method is for restarting the account."""

        return self.api.request("GET", "Reboot")

    def logout(self) -> Response:
        """The method is for logging out of the account."""

        return self.api.request("GET", "Logout")

    def qr(self) -> Response:
        """The method is designed to get a QR code."""

        return self.api.request("GET", "qr")

    def set_profile_picture(self, file: str) -> Response:
        """The method is for setting an account avatar."""

        file_name = Path(file).name
        files = {"file": (file_name, open(file, "rb"), "image/jpg")}

        return self.api.request("POST", "setProfilePicture", files=files)
