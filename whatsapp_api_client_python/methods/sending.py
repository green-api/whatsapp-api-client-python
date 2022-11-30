import mimetypes
import pathlib
from typing import Dict, List, Optional, Union

from whatsapp_api_client_python.base import BaseCategory
from whatsapp_api_client_python.response import Response


class SendingCategory(BaseCategory):
    def send_message(
            self,
            chatId: str,
            message: str,
            quotedMessageId: Optional[str] = None,
            archiveChat: Optional[bool] = None
    ) -> Response:
        """
        The method is designed to send a text message
        to a personal or group chat.
        """

        data = self.handle_parameters(locals())

        return self.api.request("POST", "SendMessage", data)

    def send_buttons(
            self,
            chatId: str,
            message: str,
            buttons: List[Dict[str, Union[int, str]]],
            footer: Optional[str] = None,
            quotedMessageId: Optional[str] = None,
            archiveChat: Optional[bool] = None
    ) -> Response:
        """
        The method is designed to send a message with buttons
        to a personal or group chat.
        """

        data = self.handle_parameters(locals())

        return self.api.request("POST", "SendButtons", data)

    def send_template_buttons(
            self,
            chatId: str,
            message: str,
            templateButtons: List[Dict[str, Union[int, Dict[str, str]]]],
            footer: Optional[str] = None,
            quotedMessageId: Optional[str] = None,
            archiveChat: Optional[bool] = None
    ) -> Response:
        """
        The method is designed to send a message
        with interactive buttons from the list
        of templates to a personal or group chat.
        """

        data = self.handle_parameters(locals())

        return self.api.request("POST", "sendTemplateButtons", data)

    def send_list_message(
            self,
            chatId: str,
            message: str,
            sections: List[Dict[str, Union[str, List[Dict[str, str]]]]],
            title: Optional[str] = None,
            footer: Optional[str] = None,
            buttonText: Optional[str] = None,
            quotedMessageId: Optional[str] = None,
            archiveChat: Optional[bool] = None
    ) -> Response:
        """
        The method is designed to send a message
        with a selection button from a list
        of values to a personal or group chat.
        """

        data = self.handle_parameters(locals())

        return self.api.request("POST", "SendListMessage", data)

    def send_file_by_upload(
            self,
            chatId: str,
            file: str,
            fileName: Optional[str] = None,
            caption: Optional[str] = None,
            quotedMessageId: Optional[str] = None
    ) -> Response:
        """
        The method is designed to send a file
        loaded through a form (form-data).
        """

        data = self.handle_parameters(locals())

        file_name = pathlib.Path(file).name
        mime_type = mimetypes.guess_type(file_name)[0]
        files = {"file": (file_name, open(file, "rb"), mime_type)}

        data.pop("file")

        return self.api.request("POST", "SendFileByUpload", data, files=files)

    def send_file_by_url(
            self,
            chatId: str,
            urlFile: str,
            fileName: str,
            caption: Optional[str] = None,
            quotedMessageId: Optional[str] = None,
            archiveChat: Optional[bool] = None
    ) -> Response:
        """The method is for sending a file downloaded from a link."""

        data = self.handle_parameters(locals())

        return self.api.request("POST", "SendFileByUrl", data)

    def send_location(
            self,
            chatId: str,
            latitude: float,
            longitude: float,
            nameLocation: Optional[str] = None,
            address: Optional[str] = None,
            quotedMessageId: Optional[str] = None
    ) -> Response:
        """The method is for sending a geolocation message."""

        data = self.handle_parameters(locals())

        return self.api.request("POST", "sendLocation", data)

    def send_contact(
            self,
            chatId: str,
            contact: Dict[str, Union[int, str]],
            quotedMessageId: Optional[str] = None
    ) -> Response:
        """The method is for sending a message with a contact."""

        data = self.handle_parameters(locals())

        return self.api.request("POST", "sendContact", data)

    def send_link(
            self,
            chatId: str,
            urlLink: str,
            quotedMessageId: Optional[str] = None
    ) -> Response:
        """
        The method is designed to send a message
        with a link that will add an image preview,
        title and description.
        """

        data = self.handle_parameters(locals())

        return self.api.request("POST", "sendLink", data)
