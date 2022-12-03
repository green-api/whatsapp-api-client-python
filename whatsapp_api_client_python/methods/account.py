from pathlib import Path
from typing import Optional

from whatsapp_api_client_python.base import BaseCategory


class AccountCategory(BaseCategory):
    def get_settings(self) -> dict:
        """
        The method is designed to get the current account settings.
        """

        return self.api.request("GetSettings")

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
    ) -> dict:
        """The method is for setting the account settings."""

        data = self.handle_parameters(locals())

        if not data:
            return self.api.request("SetSettings")
        return self.api.request("SetSettings", "POST", data)

    def set_system_proxy(self) -> dict:
        """The method is for setting up a system proxy."""

        return self.api.request("SetSystemProxy")

    def get_state_instance(self) -> dict:
        """The method is designed to get the state of the account."""

        return self.api.request("getStateInstance")

    def get_status_instance(self) -> dict:
        """
        The method is designed to get the socket connection state of
        the account instance with WhatsApp.
        """

        return self.api.request("getStatusInstance")

    def reboot(self) -> dict:
        """The method is for restarting the account."""

        return self.api.request("Reboot")

    def logout(self) -> dict:
        """The method is designed to logout the account."""

        return self.api.request("Logout")

    def qr(self) -> dict:
        """The method is designed to get a QR code."""

        return self.api.request("qr")

    def set_profile_picture(self, file: str) -> dict:
        """The method is for setting an account avatar."""

        file_name = Path(file).name
        files = {"file": (file_name, open(file, "rb"), "image/jpeg")}

        return self.api.request("setProfilePicture", "POST", files=files)


__all__ = ["AccountCategory"]
