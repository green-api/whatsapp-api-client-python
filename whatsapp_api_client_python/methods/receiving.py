from whatsapp_api_client_python.base import BaseCategory


class ReceivingCategory(BaseCategory):
    def receive_notification(self) -> dict:
        """https://green-api.com/en/docs/api/receiving/technology-http-api/ReceiveNotification/"""

        return self.api.request("ReceiveNotification")

    def delete_notification(self, receiptId: int) -> dict:
        """https://green-api.com/en/docs/api/receiving/technology-http-api/DeleteNotification/"""

        data = self.handle_parameters(locals())

        return self.api.request("DeleteNotification", "DELETE", data)

    def download_file(self, chatId: str, idMessage: str) -> dict:
        """https://green-api.com/en/docs/api/receiving/files/DownloadFile/"""

        data = self.handle_parameters(locals())

        return self.api.request("downloadFile", "POST", data)


__all__ = ["ReceivingCategory"]
