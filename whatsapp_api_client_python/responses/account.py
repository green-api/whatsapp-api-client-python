from typing import Optional

from .base import BaseResponse


class GetSettingsResponse(BaseResponse):
    wid: Optional[str] = None
    webhook_url: Optional[str] = None
    webhook_url_token: Optional[str] = None
    delay_send_messages_milliseconds: Optional[int] = None
    mark_incoming_messages_read: Optional[bool] = None
    mark_incoming_messages_read_on_reply: Optional[bool] = None
    outgoing_webhook: Optional[bool] = None
    outgoing_message_webhook: Optional[bool] = None
    outgoing_api_message_webhook: Optional[bool] = None
    incoming_webhook: Optional[bool] = None
    device_webhook: Optional[bool] = None
    state_webhook: Optional[bool] = None
    keep_online_status: Optional[bool] = None
    poll_message_webhook: Optional[bool] = None
    incoming_block_webhook: Optional[bool] = None


class GetWASettingsResponse(BaseResponse):
    avatar: Optional[str] = None
    phone: Optional[str] = None
    state_instance: Optional[str] = None
    device_id: Optional[str] = None


class SetSettingsResponse(BaseResponse):
    save_settings: Optional[bool] = None


class GetStateInstanceResponse(BaseResponse):
    state_instance: Optional[str] = None


class GetStatusInstanceResponse(BaseResponse):
    status_instance: Optional[str] = None


class RebootResponse(BaseResponse):
    is_reboot: Optional[bool] = None


class LogoutResponse(BaseResponse):
    is_logout: Optional[bool] = None


class QRResponse(BaseResponse):
    type: Optional[str] = None
    message: Optional[str] = None


class SetProfilePictureResponse(BaseResponse):
    reason: Optional[str] = None
    url_avatar: Optional[str] = None
    set_profile_picture: Optional[bool] = None


class GetAuthorizationCodeResponse(BaseResponse):
    status: Optional[bool] = None
    code: Optional[str] = None


__all__ = [
    "GetSettingsResponse",
    "GetWASettingsResponse",
    "SetSettingsResponse",
    "GetStateInstanceResponse",
    "GetStatusInstanceResponse",
    "RebootResponse",
    "LogoutResponse",
    "QRResponse",
    "SetProfilePictureResponse",
    "GetAuthorizationCodeResponse"
]
