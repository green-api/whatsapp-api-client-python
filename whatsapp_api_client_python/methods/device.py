from whatsapp_api_client_python.base import BaseCategory


class DeviceCategory(BaseCategory):
    def get_device_info(self) -> dict:
        """
        The method is designed to get information about the device
        (phone) on which WhatsApp Business is running.
        """

        return self.api.request("GetDeviceInfo")


__all__ = ["DeviceCategory"]
