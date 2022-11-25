from whatsapp_api_client_python.response import Response


class Marking:
    def __init__(self, greenApi) -> None:
        self.greenApi = greenApi
        
    def readChat(self, chatId: str, idMessage: str) -> Response:
            'The method returns the chat message history.'

            requestBody = {
                'chatId': chatId,
                'idMessage': idMessage,
            }

            return self.greenApi.request('POST', 
                '{{host}}/waInstance{{idInstance}}'
                '/ReadChat/{{apiTokenInstance}}',
                requestBody)