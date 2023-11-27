import mimetypes
import pathlib
from typing import Dict, List, Optional, TYPE_CHECKING, Union

from ..response import Response

if TYPE_CHECKING:
    from ..API import GreenApi


class Sending:
    def __init__(self, api: "GreenApi"):
        self.api = api

    def sendMessage(
            self,
            chatId: str,
            message: str,
            quotedMessageId: Optional[str] = None,
            archiveChat: Optional[bool] = None,
            linkPreview: Optional[bool] = None
    ) -> Response:
        """
        The method is aimed for sending a text message to a personal or
        a group chat.

        https://green-api.com/en/docs/api/sending/SendMessage/
        """

        request_body = self.__handle_parameters(locals())

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "sendMessage/{{apiTokenInstance}}"
            ), request_body
        )

    def sendButtons(
            self,
            chatId: str,
            message: str,
            buttons: List[Dict[str, Union[int, str]]],
            footer: Optional[str] = None,
            quotedMessageId: Optional[str] = None,
            archiveChat: Optional[bool] = None
    ) -> Response:
        """
        The method is aimed for sending a button message to a personal
        or a group chat.

        https://green-api.com/en/docs/api/sending/SendButtons/
        """

        request_body = self.__handle_parameters(locals())

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "sendButtons/{{apiTokenInstance}}"
            ), request_body
        )

    def sendTemplateButtons(
            self,
            chatId: str,
            message: str,
            templateButtons: List[Dict[str, Union[int, Dict[str, str]]]],
            footer: Optional[str] = None,
            quotedMessageId: Optional[str] = None,
            archiveChat: Optional[bool] = None
    ) -> Response:
        """
        The method is aimed for sending a message with template list
        interactive buttons to a personal or a group chat.

        https://green-api.com/en/docs/api/sending/SendTemplateButtons/
        """

        request_body = self.__handle_parameters(locals())

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "sendTemplateButtons/{{apiTokenInstance}}"
            ), request_body
        )

    def sendListMessage(
            self,
            chatId: str,
            message: str,
            buttonText: str,
            sections: List[Dict[str, Union[str, List[Dict[str, str]]]]],
            title: Optional[str] = None,
            footer: Optional[str] = None,
            quotedMessageId: Optional[str] = None,
            archiveChat: Optional[bool] = None
    ) -> Response:
        """
        The method is aimed for sending a message with a select button
        from a list of values to a personal or a group chat.

        https://green-api.com/en/docs/api/sending/SendListMessage/
        """

        request_body = self.__handle_parameters(locals())

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "sendListMessage/{{apiTokenInstance}}"
            ), request_body
        )

    def sendFileByUpload(
            self,
            chatId: str,
            path: str,
            fileName: Optional[str] = None,
            caption: Optional[str] = None,
            quotedMessageId: Optional[str] = None
    ) -> Response:
        """
        The method is aimed for sending a file uploaded by form
        (form-data).

        https://green-api.com/en/docs/api/sending/SendFileByUpload/
        """

        request_body = self.__handle_parameters(locals())

        file_name = pathlib.Path(path).name
        content_type = mimetypes.guess_type(file_name)[0]

        files = {"file": (file_name, open(path, "rb"), content_type)}

        request_body.pop("path")

        return self.api.request(
            "POST", (
                "{{media}}/waInstance{{idInstance}}/"
                "sendFileByUpload/{{apiTokenInstance}}"
            ), request_body, files
        )

    def sendFileByUrl(
            self,
            chatId: str,
            urlFile: str,
            fileName: str,
            caption: Optional[str] = None,
            quotedMessageId: Optional[str] = None,
            archiveChat: Optional[bool] = None
    ) -> Response:
        """
        The method is aimed for sending a file uploaded by URL.

        https://green-api.com/en/docs/api/sending/SendFileByUrl/
        """

        request_body = self.__handle_parameters(locals())

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "sendFileByUrl/{{apiTokenInstance}}"
            ), request_body
        )

    def uploadFile(self, path: str) -> Response:
        """
        The method is designed to upload a file to the cloud storage,
        which can be sent using the sendFileByUrl method.

        https://green-api.com/en/docs/api/sending/UploadFile/
        """

        file_name = pathlib.Path(path).name
        content_type = mimetypes.guess_type(file_name)[0]

        with open(path, "rb") as file:
            return self.api.raw_request(
                method="POST",
                url=(
                    f"{self.api.media}/waInstance{self.api.idInstance}/"
                    f"uploadFile/{self.api.apiTokenInstance}"
                ),
                data=file.read(),
                headers={"Content-Type": content_type}
            )

    def sendLocation(
            self,
            chatId: str,
            latitude: float,
            longitude: float,
            nameLocation: Optional[str] = None,
            address: Optional[str] = None,
            quotedMessageId: Optional[str] = None
    ) -> Response:
        """
        The method is aimed for sending location message.

        https://green-api.com/en/docs/api/sending/SendLocation/
        """

        request_body = self.__handle_parameters(locals())

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "sendLocation/{{apiTokenInstance}}"
            ), request_body
        )

    def sendContact(
            self,
            chatId: str,
            contact: Dict[str, Union[int, str]],
            quotedMessageId: Optional[str] = None
    ) -> Response:
        """
        The method is aimed for sending a contact message.

        https://green-api.com/en/docs/api/sending/SendContact/
        """

        request_body = self.__handle_parameters(locals())

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "sendContact/{{apiTokenInstance}}"
            ), request_body
        )

    def sendLink(
            self,
            chatId: str,
            urlLink: str,
            quotedMessageId: Optional[str] = None
    ) -> Response:
        """
        The method is deprecated. Please use SendMessage.

        The method is aimed for sending a message with a link, by which
        an image preview, title and description will be added.

        https://green-api.com/en/docs/api/sending/SendLink/
        """

        request_body = self.__handle_parameters(locals())

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "sendLink/{{apiTokenInstance}}"
            ), request_body
        )

    def forwardMessages(
            self,
            chatId: str,
            chatIdFrom: str,
            messages: List[str]
    ) -> Response:
        """
        The method is intended for forwarding messages to a personal or
        group chat.

        https://green-api.com/en/docs/api/sending/ForwardMessages/
        """

        request_body = self.__handle_parameters(locals())

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "forwardMessages/{{apiTokenInstance}}"
            ), request_body
        )

    def sendPoll(
            self,
            chatId: str,
            message: str,
            options: List[Dict[str, str]],
            multipleAnswers: Optional[bool] = None,
            quotedMessageId: Optional[str] = None
    ) -> Response:
        """
        This method is intended for sending messages with a poll to a
        private or group chat.

        https://green-api.com/en/docs/api/sending/SendPoll/
        """

        request_body = self.__handle_parameters(locals())

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "sendPoll/{{apiTokenInstance}}"
            ), request_body
        )

    @classmethod
    def __handle_parameters(cls, parameters: dict) -> dict:
        handled_parameters = parameters.copy()

        handled_parameters.pop("self")

        for key, value in parameters.items():
            if value is None:
                handled_parameters.pop(key)

        return handled_parameters
