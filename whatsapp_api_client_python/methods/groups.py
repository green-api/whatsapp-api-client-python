from pathlib import Path
from typing import List

from whatsapp_api_client_python.base import BaseCategory
from whatsapp_api_client_python.response import Response


class GroupCategory(BaseCategory):
    def create_group(self, groupName: str, chatIds: List[str]) -> Response:
        """The method is designed to create a group chat."""

        data = self.handle_parameters(locals())

        return self.api.request("POST", "CreateGroup", data)

    def update_group_name(self, groupId: str, groupName: str) -> Response:
        """The method changes the name of the group chat."""

        data = self.handle_parameters(locals())

        return self.api.request("POST", "UpdateGroupName", data)

    def get_group_data(self, groupId: str) -> Response:
        """The method gets the group chat data."""

        data = self.handle_parameters(locals())

        return self.api.request("POST", "GetGroupData", data)

    def add_group_participant(
            self, groupId: str, participantChatId: str
    ) -> Response:
        """The method adds a participant to the group chat."""

        data = self.handle_parameters(locals())

        return self.api.request("POST", "AddGroupParticipant", data)

    def remove_group_participant(
            self, groupId: str, participantChatId: str
    ) -> Response:
        """The method removes the participant from the group chat."""

        data = self.handle_parameters(locals())

        return self.api.request("POST", "RemoveGroupParticipant", data)

    def set_group_admin(
            self, groupId: str, participantChatId: str
    ) -> Response:
        """
        The method designates a member of a group chat
        as an administrator.
        """

        data = self.handle_parameters(locals())

        return self.api.request("POST", "SetGroupAdmin", data)

    def remove_admin(self, groupId: str, participantChatId: str) -> Response:
        """
        The method deprives the participant of group chat
        administration rights.
        """

        data = self.handle_parameters(locals())

        return self.api.request("POST", "RemoveAdmin", data)

    def set_group_picture(self, file: str, groupId: str) -> Response:
        """The method sets the avatar of the group."""

        data = self.handle_parameters(locals())

        file_name = Path(file).name
        files = {"file": (file_name, open(file, "rb"), "image/jpg")}

        data.pop("file")

        return self.api.request("POST", "setGroupPicture", data, files=files)

    def leave_group(self, groupId: str) -> Response:
        """
        The method leaves the user of the current account
        from the group chat.
        """

        data = self.handle_parameters(locals())

        return self.api.request("POST", "LeaveGroup", data)
