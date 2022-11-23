from whatsapp_api_client_python.base import BaseCategory
from whatsapp_api_client_python.response import Response


class ReceivingCategory(BaseCategory):
    def receive_notification(self) -> Response:
        """https://green-api.com/en/docs/api/receiving/technology-http-api/ReceiveNotification/"""

        return self.api.request("GET", "ReceiveNotification")

    def delete_notification(self, receiptId: int) -> Response:
        """https://green-api.com/en/docs/api/receiving/technology-http-api/DeleteNotification/"""

        data = self.handle_parameters(locals())

        return self.api.request("DELETE", "DeleteNotification", data)

    def download_file(self, chatId: str, idMessage: str) -> Response:
        """https://green-api.com/en/docs/api/receiving/files/DownloadFile/"""

        data = self.handle_parameters(locals())

        return self.api.request("DELETE", "downloadFile", data)
