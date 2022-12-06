from pathlib import Path
from typing import List

from whatsapp_api_client_python.base import BaseCategory


class GroupsCategory(BaseCategory):
    def create_group(self, groupName: str, chatIds: List[str]) -> dict:
        """The method is designed to create a group chat."""

        data = self.handle_parameters(locals())

        return self.api.request("CreateGroup", "POST", data)

    def update_group_name(self, groupId: str, groupName: str) -> dict:
        """The method changes the name of the group chat."""

        data = self.handle_parameters(locals())

        return self.api.request("UpdateGroupName", "POST", data)

    def get_group_data(self, groupId: str) -> dict:
        """The method gets the group chat data."""

        data = self.handle_parameters(locals())

        return self.api.request("GetGroupData", "POST", data)

    def add_group_participant(
            self, groupId: str, participantChatId: str
    ) -> dict:
        """The method adds a participant to the group chat."""

        data = self.handle_parameters(locals())

        return self.api.request("AddGroupParticipant", "POST", data)

    def remove_group_participant(
            self, groupId: str, participantChatId: str
    ) -> dict:
        """The method removes the participant from the group chat."""

        data = self.handle_parameters(locals())

        return self.api.request("RemoveGroupParticipant", "POST", data)

    def set_group_admin(self, groupId: str, participantChatId: str) -> dict:
        """
        The method designates a member of a group chat as an
        administrator.
        """

        data = self.handle_parameters(locals())

        return self.api.request("SetGroupAdmin", "POST", data)

    def remove_admin(self, groupId: str, participantChatId: str) -> dict:
        """
        The method deprives the participant of group chat
        administration rights.
        """

        data = self.handle_parameters(locals())

        return self.api.request("RemoveAdmin", "POST", data)

    def set_group_picture(self, file: str, groupId: str) -> dict:
        """The method sets the avatar of the group."""

        data = self.handle_parameters(locals())

        file_name = Path(file).name
        files = {"file": (file_name, open(file, "rb"), "image/jpeg")}

        data.pop("file")

        return self.api.request("setGroupPicture", "POST", data, files=files)

    def leave_group(self, groupId: str) -> dict:
        """
        The method logs the user of the current account out of the
        group chat.
        """

        data = self.handle_parameters(locals())

        return self.api.request("LeaveGroup", "POST", data)


__all__ = ["GroupsCategory"]
