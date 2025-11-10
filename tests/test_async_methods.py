import typing
import pytest
from unittest.mock import Mock, patch, AsyncMock
import asyncio

from whatsapp_api_client_python.API import GreenAPI

api = GreenAPI("", "")
path = "examples/data/logo.jpg"

class TestAsyncMethods:
    
    @pytest.mark.asyncio
    async def test_single_async_method(self):
        """Тестируем только один метод для упрощения отладки"""
        # Создаем реальный мок-объект с нужными атрибутами
        mock_response = Mock()
        mock_response.code = 200
        mock_response.data = {"example": {"key": "value"}}
        
        # Создаем асинхронную функцию, которая возвращает наш мок
        async def mock_request(*args, **kwargs):
            return mock_response
        
        with patch("whatsapp_api_client_python.API.Session.request", side_effect=mock_request):
            # Тестируем только один метод
            response = await api.account.getSettingsAsync()
            
            assert response.code == 200
            assert response.data == {"example": {"key": "value"}}

    @pytest.mark.asyncio
    async def test_async_methods_with_different_status_codes(self):
        """Тестируем все методы с разными кодами ответа"""
        # Создаем список мок-ответов с разными статусами
        mock_responses = []
        for i in range(50):  # Создаем достаточно ответов
            mock_response = Mock()
            # Чередуем коды статусов: 200, 401, 403
            status_code = [200, 401, 403][i % 3]
            mock_response.code = status_code
            if status_code == 200:
                mock_response.data = {"example": {"key": "value"}}
            else:
                mock_response.data = {"error": "Unauthorized" if status_code == 401 else "Forbidden"}
            mock_responses.append(mock_response)
        
        async def mock_request(*args, **kwargs):
            return mock_responses.pop(0)
        
        with patch("whatsapp_api_client_python.API.Session.request", side_effect=mock_request):
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

            # Проверяем что все ответы имеют допустимые коды статуса
            valid_codes = [200, 401, 403]
            for response in responses:
                assert response.code in valid_codes
                if response.code == 200:
                    assert response.data == {"example": {"key": "value"}}
                else:
                    assert "error" in response.data

    @pytest.mark.asyncio
    async def test_async_methods_all_success(self):
        """Тестируем все методы с успешными ответами"""
        # Создаем мок для успешных ответов
        mock_response = Mock()
        mock_response.code = 200
        mock_response.data = {"example": {"key": "value"}}
        
        async def mock_request(*args, **kwargs):
            return mock_response
        
        with patch("whatsapp_api_client_python.API.Session.request", side_effect=mock_request):
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

    def account_methods(self) -> typing.List:
        return [
            api.account.getSettingsAsync(),
            api.account.getWaSettingsAsync(),
            api.account.setSettingsAsync({"key": "value"}),
            api.account.getStateInstanceAsync(),
            api.account.rebootAsync(),
            api.account.logoutAsync(),
            api.account.qrAsync(),
            api.account.setProfilePictureAsync(path),
            api.account.getAuthorizationCodeAsync(12345678)
        ]

    def group_methods(self) -> typing.List:
        return [
            api.groups.createGroupAsync("GroupName", ["1234567890@c.us"]),
            api.groups.updateGroupNameAsync("group_id", "NewGroupName"),
            api.groups.getGroupDataAsync("group_id"),
            api.groups.removeGroupParticipantAsync("group_id", "1234567890@c.us"),
            api.groups.addGroupParticipantAsync("group_id", "1234567890@c.us"),
            api.groups.setGroupAdminAsync("group_id", "1234567890@c.us"),
            api.groups.removeAdminAsync("group_id", "1234567890@c.us"),
            api.groups.setGroupPictureAsync("group_id", path),
            api.groups.leaveGroupAsync("group_id")
        ]

    def status_methods(self) -> typing.List:
        return [
            api.statuses.sendTextStatusAsync("Status text"),
            api.statuses.sendVoiceStatusAsync("status_id", path),
            api.statuses.sendMediaStatusAsync("status_id", path),
            api.statuses.deleteStatusAsync("status_id"),
            api.statuses.getStatusStatisticAsync("status_id"),
            api.statuses.getIncomingStatusesAsync(),
            api.statuses.getOutgoingStatusesAsync()
        ]

    def log_methods(self) -> typing.List:
        return [
            api.journals.getChatHistoryAsync("1234567890@c.us"),
            api.journals.getMessageAsync("chat_id", "message_id"),
            api.journals.lastIncomingMessagesAsync(),
            api.journals.lastOutgoingMessagesAsync()
        ]

    def queue_methods(self) -> typing.List:
        return [
            api.queues.showMessagesQueueAsync(),
            api.queues.clearMessagesQueueAsync()
        ]

    def read_mark_methods(self) -> typing.List:
        return [api.marking.readChatAsync("1234567890@c.us")]

    def receiving_methods(self) -> typing.List:
        return [
            api.receiving.receiveNotificationAsync(),
            api.receiving.deleteNotificationAsync(123),
            api.receiving.downloadFileAsync("file_id", "path/to/save")
        ]

    def sending_methods(self) -> typing.List:
        return [
            api.sending.sendMessageAsync("1234567890@c.us", "Hello"),
            api.sending.sendFileByUploadAsync("1234567890@c.us", path),
            api.sending.sendFileByUrlAsync("1234567890@c.us", "https://example.com/file.jpg", "file.jpg"),
            api.sending.uploadFileAsync(path),
            api.sending.sendLocationAsync("1234567890@c.us", 40.7128, -74.0060),
            api.sending.sendContactAsync("1234567890@c.us", {
                "name": {"firstName": "John", "lastName": "Doe"},
                "phone": "1234567890"
            }),
            api.sending.sendPollAsync("1234567890@c.us", "Question?", ["Option1", "Option2"])
        ]

    def service_methods(self) -> typing.List:
        return [
            api.serviceMethods.checkWhatsappAsync(1234567890),
            api.serviceMethods.getAvatarAsync("1234567890@c.us"),
            api.serviceMethods.getContactsAsync(),
            api.serviceMethods.getContactInfoAsync("1234567890@c.us"),
            api.serviceMethods.deleteMessageAsync("chat_id", "message_id"),
            api.serviceMethods.archiveChatAsync("1234567890@c.us"),
            api.serviceMethods.unarchiveChatAsync("1234567890@c.us"),
            api.serviceMethods.setDisappearingChatAsync("1234567890@c.us", 3600)
        ]

if __name__ == "__main__":
    pytest.main([__file__, "-v"])