from pathlib import Path
from typing import List, TYPE_CHECKING

from ..response import Response

if TYPE_CHECKING:
    from ..API import GreenApi


class Groups:
    def __init__(self, api: "GreenApi"):
        self.api = api

    def createGroup(self, groupName: str, chatIds: List[str]) -> Response:
        """The method is aimed for creating a group chat."""

        request_body = self.__handle_parameters(locals())

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "createGroup/{{apiTokenInstance}}"
            ), request_body
        )

    def updateGroupName(self, groupId: str, groupName: str) -> Response:
        """The method changes a group chat name."""

        request_body = self.__handle_parameters(locals())

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "updateGroupName/{{apiTokenInstance}}"
            ), request_body
        )

    def getGroupData(self, groupId: str) -> Response:
        """The method gets group chat data."""

        request_body = self.__handle_parameters(locals())

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "getGroupData/{{apiTokenInstance}}"
            ), request_body
        )

    def addGroupParticipant(
            self, groupId: str, participantChatId: str
    ) -> Response:
        """The method adds a participant to a group chat."""

        request_body = self.__handle_parameters(locals())

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "addGroupParticipant/{{apiTokenInstance}}"
            ), request_body
        )

    def removeGroupParticipant(
            self, groupId: str, participantChatId: str
    ) -> Response:
        """The method removes a participant from a group chat."""

        request_body = self.__handle_parameters(locals())

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "removeGroupParticipant/{{apiTokenInstance}}"
            ), request_body
        )

    def setGroupAdmin(self, groupId: str, participantChatId: str) -> Response:
        """
        The method sets a group chat participant as an administrator.
        """

        request_body = self.__handle_parameters(locals())

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "setGroupAdmin/{{apiTokenInstance}}"
            ), request_body
        )

    def removeAdmin(self, groupId: str, participantChatId: str) -> Response:
        """
        The method removes a participant from group chat administration
        rights.
        """

        request_body = self.__handle_parameters(locals())

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "removeAdmin/{{apiTokenInstance}}"
            ), request_body
        )

    def setGroupPicture(self, groupId: str, path: str) -> Response:
        """The method sets a group picture."""

        request_body = self.__handle_parameters(locals())

        file_name = Path(path).name
        files = {"file": (file_name, open(path, "rb"), "image/jpeg")}

        request_body.pop("path")

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "setGroupPicture/{{apiTokenInstance}}"
            ), request_body, files
        )

    def leaveGroup(self, groupId: str) -> Response:
        """
        The method makes the current account user leave the group chat.
        """

        request_body = self.__handle_parameters(locals())

        return self.api.request(
            "POST", (
                "{{host}}/waInstance{{idInstance}}/"
                "leaveGroup/{{apiTokenInstance}}"
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
