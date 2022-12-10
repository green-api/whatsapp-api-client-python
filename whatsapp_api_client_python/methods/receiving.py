from whatsapp_api_client_python.base import BaseCategory


class ReceivingCategory(BaseCategory):
    def receive_notification(self) -> dict:
        return self.api.request("ReceiveNotification")

    def delete_notification(self, receiptId: int) -> dict:
        data = self.handle_parameters(locals())

        return self.api.request("DeleteNotification", "DELETE", data)

    def download_file(self, chatId: str, idMessage: str) -> dict:
        data = self.handle_parameters(locals())

        return self.api.request("downloadFile", "POST", data)


__all__ = ["ReceivingCategory"]
