from typing import TYPE_CHECKING, Optional

from ..response import Response

if TYPE_CHECKING:
    from ..API import GreenApi


class Queues:
    def __init__(self, api: "GreenApi"):
        self.api = api

    def showMessagesQueue(self) -> Response:
        """
        The method is aimed for getting a list of messages in the queue
        to be sent.

        https://green-api.com/en/docs/api/queues/ShowMessagesQueue/
        """

        return self.api.request(
            "GET", (
                "{{host}}/waInstance{{idInstance}}/"
                "showMessagesQueue/{{apiTokenInstance}}"
            )
        )

    async def showMessagesQueueAsync(self) -> Response:
        return await self.api.requestAsync(
            "GET", "{{host}}/waInstance{{idInstance}}/showMessagesQueue/{{apiTokenInstance}}"
        )

    def clearMessagesQueue(self) -> Response:
        """
        The method is aimed for clearing the queue of messages to be
        sent.

        https://green-api.com/en/docs/api/queues/ClearMessagesQueue/
        """

        return self.api.request(
            "GET", (
                "{{host}}/waInstance{{idInstance}}/"
                "clearMessagesQueue/{{apiTokenInstance}}"
            )
        )

    async def clearMessagesQueueAsync(self) -> Response:
        return await self.api.requestAsync(
            "GET", "{{host}}/waInstance{{idInstance}}/clearMessagesQueue/{{apiTokenInstance}}"
        )

    def getMessagesCount(self) -> Response:
        """
        The method returns the number of messages in the outgoing queue.

        https://green-api.com/en/docs/api/queues/GetMessagesCount/
        """

        return self.api.request(
            "GET", (
                "{{host}}/waInstance{{idInstance}}/"
                "getMessagesCount/{{apiTokenInstance}}"
            )
        )

    async def getMessagesCountAsync(self) -> Response:
        return await self.api.requestAsync(
            "GET", "{{host}}/waInstance{{idInstance}}/getMessagesCount/{{apiTokenInstance}}"
        )

    def getWebhooksCount(self) -> Response:
        """
        The method returns the number of notifications in the incoming
        webhooks queue.

        https://green-api.com/en/docs/api/queues/GetWebhooksCount/
        """

        return self.api.request(
            "GET", (
                "{{host}}/waInstance{{idInstance}}/"
                "getWebhooksCount/{{apiTokenInstance}}"
            )
        )

    async def getWebhooksCountAsync(self) -> Response:
        return await self.api.requestAsync(
            "GET", "{{host}}/waInstance{{idInstance}}/getWebhooksCount/{{apiTokenInstance}}"
        )

    def clearWebhooksQueue(self) -> Response:
        """
        The method clears the incoming webhooks queue.

        https://green-api.com/en/docs/api/queues/ClearWebhooksQueue/
        """

        return self.api.request(
            "DELETE", (
                "{{host}}/waInstance{{idInstance}}/"
                "clearWebhooksQueue/{{apiTokenInstance}}"
            )
        )

    async def clearWebhooksQueueAsync(self) -> Response:
        return await self.api.requestAsync(
            "DELETE", "{{host}}/waInstance{{idInstance}}/clearWebhooksQueue/{{apiTokenInstance}}"
        )