from whatsapp_api_client_python.base import BaseCategory
from whatsapp_api_client_python.response import Response


class DeviceCategory(BaseCategory):
    def get_device_info(self) -> Response:
        """
        The method is designed to get information
        about the device (phone).
        """

        return self.api.request("GET", "GetDeviceInfo")
