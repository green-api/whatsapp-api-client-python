from whatsapp_api_client_python.base import BaseCategory
from whatsapp_api_client_python.response import Response


class AccountCategory(BaseCategory):
    def get_settings(self) -> Response:
        """
        The method is designed to get the settings
        of the current account.
        """

        return self.api.request("GET", "getSettings")

    def get_state_instance(self) -> Response:
        """The method is designed to get the state of the account."""

        return self.api.request("GET", "getStateInstance")
