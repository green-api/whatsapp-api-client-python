from typing import Dict, List, Optional, TYPE_CHECKING, Union

from ..response import Response

if TYPE_CHECKING:
    from ..API import GreenApiPartner

class Partner:
    def __init__(self, api: "GreenApiPartner"):
        self.api = api

    def getInstances(
            self
    ) -> Response:
        
        request_body = self.__handle_parameters(locals())

        return self.api.request(
            "GET", (
                "{{host}}/partner/"
                "getInstances/{{partnerToken}}"
            ), request_body
        ) ### GOOD
    
    def createInstance(
            self,
            name: Optional[str] = None,
            webhookUrl: Optional[str] = None,
            webhookUrlToken: Optional[str] = None,
            delaySendMessagesMilliseconds: Optional[int] = None,
            markIncomingMessagesReaded: Optional[str] = None,
            markIncomingMessagesReadedOnReply: Optional[str] = None,
            outgoingWebhook: Optional[str] = None,
            outgoingMessageWebhook: Optional[str] = None,
            outgoingAPIMessageWebhook: Optional[str] = None,
            stateWebhook: Optional[str] = None,
            incomingWebhook: Optional[str] = None,
            deviceWebhook: Optional[str] = None,
            keepOnlineStatus: Optional[str] = None,
            pollMessageWebhook: Optional[str] = None,
            incomingBlockWebhook: Optional[str] = None,
            incomingCallWebhook: Optional[str] = None,
            editedMessageWebhook: Optional[str] = None,
            deletedMessageWebhook: Optional[str] = None
    ) -> Response:
        
        request_body = self.__handle_parameters(locals())

        return self.api.request(
            "POST", (
                "{{host}}/partner/"
                "createInstance/{{partnerToken}}"
            ), request_body
        )   ### NOT FINISHED!!!!
    
    def deleteInstanceAccount(
            self,
            idInstance: int
    ) -> Response:

        request_body = self.__handle_parameters(locals())

        return self.api.request(
            "POST", (
                "{{host}}/partner/"
                "deleteInstanceAccount/{{partnerToken}}"
            ), request_body
        )        ###GOOD

    @classmethod
    def __handle_parameters(cls, parameters: dict) -> dict:
        handled_parameters = parameters.copy()

        handled_parameters.pop("self")

        for key, value in parameters.items():
            if value is None:
                handled_parameters.pop(key)

        return handled_parameters