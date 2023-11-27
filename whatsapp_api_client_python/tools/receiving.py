from typing import TYPE_CHECKING

from ..response import Response

if TYPE_CHECKING:
    from ..API import GreenApi


class Receiving:
    def __init__(self, api: "GreenApi"):
        self.api = api

    def receiveNotification(self) -> Response:
        """
        The method is aimed for receiving one incoming notification
        from the notifications queue.

        https://green-api.com/en/docs/api/receiving/technology-http-api/ReceiveNotification/
        """

        return self.api.request(
            "GET", (
                "{{host}}/waInstance{{idInstance}}/"
                "receiveNotification/{{apiTokenInstance}}"
            )
        )

    def deleteNotification(self, receiptId: int) -> Response:
        """
        The method is aimed for deleting an incoming notification from
        the notification queue.

        https://green-api.com/en/docs/api/receiving/technology-http-api/DeleteNotification/
        """

        url = (
            "{{host}}/waInstance{{idInstance}}/"
            "deleteNotification/{{apiTokenInstance}}"
        )

        return self.api.request("DELETE", f"{url}/{receiptId}")

    def downloadFile(self, chatId: str, idMessage: str) -> Response:
        """
        The method is aimed for downloading incoming and outgoing files.

        https://green-api.com/en/docs/api/receiving/files/DownloadFile/
        """

        request_body = locals()
        request_body.pop("self")

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "downloadFile/{{apiTokenInstance}}"
            ), request_body
        )
