import mimetypes
import pathlib
import typing

from whatsapp_api_client_python.base import BaseCategory


class SendingCategory(BaseCategory):
    def send_message(
            self,
            chatId: str,
            message: str,
            quotedMessageId: typing.Optional[str] = None,
            archiveChat: typing.Optional[bool] = None
    ) -> dict:
        """
        The method is designed to send a text message to a personal or
        group chat.
        """

        data = self.handle_parameters(locals())

        return self.api.request("SendMessage", "POST", data)

    def send_buttons(
            self,
            chatId: str,
            message: str,
            buttons: typing.List[typing.Dict[str, typing.Union[int, str]]],
            footer: typing.Optional[str] = None,
            quotedMessageId: typing.Optional[str] = None,
            archiveChat: typing.Optional[bool] = None
    ) -> dict:
        """
        The method is designed to send a message with buttons to a
        personal or group chat.
        """

        data = self.handle_parameters(locals())

        return self.api.request("SendButtons", "POST", data)

    def send_template_buttons(
            self,
            chatId: str,
            message: str,
            templateButtons: typing.List[
                typing.Dict[str, typing.Union[int, typing.Dict[str, str]]]
            ],
            footer: typing.Optional[str] = None,
            quotedMessageId: typing.Optional[str] = None,
            archiveChat: typing.Optional[bool] = None
    ) -> dict:
        """
        The method is designed to send a message with interactive
        buttons from the list of templates to a personal or group chat.
        """

        data = self.handle_parameters(locals())

        return self.api.request("sendTemplateButtons", "POST", data)

    def send_list_message(
            self,
            chatId: str,
            message: str,
            sections: typing.List[
                typing.Dict[
                    str, typing.Union[str, typing.List[typing.Dict[str, str]]]
                ]
            ],
            title: typing.Optional[str] = None,
            footer: typing.Optional[str] = None,
            buttonText: typing.Optional[str] = None,
            quotedMessageId: typing.Optional[str] = None,
            archiveChat: typing.Optional[bool] = None
    ) -> dict:
        """
        The method is designed to send a message with a selection
        button from a list of values to a personal or group chat.
        """

        data = self.handle_parameters(locals())

        return self.api.request("SendListMessage", "POST", data)

    def send_file_by_upload(
            self,
            chatId: str,
            file: str,
            fileName: typing.Optional[str] = None,
            caption: typing.Optional[str] = None,
            quotedMessageId: typing.Optional[str] = None
    ) -> dict:
        """
        The method is designed to send a file loaded through a form
        (form-data).
        """

        data = self.handle_parameters(locals())

        file_name = pathlib.Path(file).name
        content_type = mimetypes.guess_type(file_name)[0]

        files = {"file": (file_name, open(file, "rb"), content_type)}

        data.pop("file")

        return self.api.request("SendFileByUpload", "POST", data, files=files)

    def send_file_by_url(
            self,
            chatId: str,
            urlFile: str,
            fileName: str,
            caption: typing.Optional[str] = None,
            quotedMessageId: typing.Optional[str] = None,
            archiveChat: typing.Optional[bool] = None
    ) -> dict:
        """The method is for sending a file downloaded from a link."""

        data = self.handle_parameters(locals())

        return self.api.request("SendFileByUrl", "POST", data)

    def send_location(
            self,
            chatId: str,
            latitude: float,
            longitude: float,
            nameLocation: typing.Optional[str] = None,
            address: typing.Optional[str] = None,
            quotedMessageId: typing.Optional[str] = None
    ) -> dict:
        """The method is for sending a geolocation message."""

        data = self.handle_parameters(locals())

        return self.api.request("sendLocation", "POST", data)

    def send_contact(
            self,
            chatId: str,
            contact: typing.Dict[str, typing.Union[int, str]],
            quotedMessageId: typing.Optional[str] = None
    ) -> dict:
        """The method is for sending a message with a contact."""

        data = self.handle_parameters(locals())

        return self.api.request("sendContact", "POST", data)

    def send_link(
            self,
            chatId: str,
            urlLink: str,
            quotedMessageId: typing.Optional[str] = None
    ) -> dict:
        """
        The method is designed to send a message with a link that will
        add an image preview, title and description.
        """

        data = self.handle_parameters(locals())

        return self.api.request("sendLink", "POST", data)


__all__ = ["SendingCategory"]
