import typing
import pytest
from unittest.mock import Mock, patch

from whatsapp_api_client_python.API import GreenAPI

api = GreenAPI("", "")
path = "examples/data/logo.jpg"

class TestAsyncMethods:
    
    @pytest.mark.asyncio
    @patch("whatsapp_api_client_python.API.Session.request")
    async def test_async_methods(self, mock_raw_request):
        mock_response = Mock()
        mock_response.code = 200
        mock_response.data = {"example": {"key": "value"}}
        mock_raw_request.return_value = mock_response

        methods_coroutines = []
        methods_coroutines.extend(self.account_methods())
        methods_coroutines.extend(self.group_methods())
        methods_coroutines.extend(self.status_methods())
        methods_coroutines.extend(self.log_methods())
        methods_coroutines.extend(self.queue_methods())
        methods_coroutines.extend(self.read_mark_methods())
        methods_coroutines.extend(self.receiving_methods())
        methods_coroutines.extend(self.sending_methods())
        methods_coroutines.extend(self.service_methods())

        responses = []
        for coro in methods_coroutines:
            response = await coro
            responses.append(response)

        for response in responses:
            assert response.code == 200
            assert response.data == {"example": {"key": "value"}}

        assert mock_raw_request.call_count == len(responses)

    def account_methods(self) -> typing.List:
        return [
            api.account.getSettingsAsync(),
            api.account.getWaSettingsAsync(),
            api.account.setSettingsAsync({}),
            api.account.getStateInstanceAsync(),
            api.account.rebootAsync(),
            api.account.logoutAsync(),
            api.account.qrAsync(),
            api.account.setProfilePictureAsync(path),
            api.account.getAuthorizationCodeAsync(0)
        ]

    def group_methods(self) -> typing.List:
        return [
            api.groups.createGroupAsync("", []),
            api.groups.updateGroupNameAsync(""),
            api.groups.getGroupDataAsync(""),
            api.groups.removeGroupParticipantAsync("", ""),
            api.groups.addGroupParticipantAsync("", ""),
            api.groups.setGroupAdminAsync("", ""),
            api.groups.removeAdminAsync("", ""),
            api.groups.setGroupPictureAsync("", ""),
            api.groups.leaveGroupAsync("")
        ]

    def status_methods(self) -> typing.List:
        return [
            api.statuses.sendTextStatusAsync(""),
            api.statuses.sendVoiceStatusAsync("", ""),
            api.statuses.sendMediaStatusAsync("", ""),
            api.statuses.deleteStatusAsync(""),
            api.statuses.getStatusStatisticAsync(""),
            api.statuses.getIncomingStatusesAsync(),
            api.statuses.getOutgoingStatusesAsync()
        ]

    def log_methods(self) -> typing.List:
        return [
            api.journals.getChatHistoryAsync(""),
            api.journals.getMessageAsync("", ""),
            api.journals.lastIncomingMessagesAsync(),
            api.journals.lastOutgoingMessagesAsync()
        ]

    def queue_methods(self) -> typing.List:
        return [
            api.queues.showMessagesQueueAsync(),
            api.queues.clearMessagesQueueAsync()
        ]

    def read_mark_methods(self) -> typing.List:
        return [api.marking.readChatAsync("")]

    def receiving_methods(self) -> typing.List:
        return [
            api.receiving.receiveNotificationAsync(),
            api.receiving.deleteNotificationAsync(0),
            api.receiving.downloadFileAsync("", "")
        ]

    def sending_methods(self) -> typing.List:
        return [
            api.sending.sendMessageAsync("", ""),
            api.sending.sendFileByUploadAsync("", ""),
            api.sending.sendFileByUrlAsync("", "", ""),
            api.sending.uploadFileAsync("image_path"),
            api.sending.sendLocationAsync("", 0.0, 0.0),
            api.sending.sendContactAsync("", {}),
            api.sending.sendPollAsync("", "", [])
        ]

    def service_methods(self) -> typing.List:
        return [
            api.serviceMethods.checkWhatsappAsync(0),
            api.serviceMethods.getAvatarAsync(""),
            api.serviceMethods.getContactsAsync(),
            api.serviceMethods.getContactInfoAsync(""),
            api.serviceMethods.deleteMessageAsync("", ""),
            api.serviceMethods.archiveChatAsync(""),
            api.serviceMethods.unarchiveChatAsync(""),
            api.serviceMethods.setDisappearingChatAsync("")
        ]

if __name__ == "__main__":
    pytest.main([__file__, "-v"])