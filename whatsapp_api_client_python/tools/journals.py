from whatsapp_api_client_python.response import Response

class Journals:
    def __init__(self, greenApi) -> None:
        self.greenApi = greenApi
        
    def getChatHistory(self, chatId: str, count: str) -> Response:
            'The method returns the chat message history.'

            requestBody = {
                'chatId': chatId,
                'count': count,
            }

            return self.greenApi.request('POST', 
                '{{host}}/waInstance{{idInstance}}'
                '/GetChatHistory/{{apiTokenInstance}}',
                requestBody)

    def lastIncomingMessages(self) -> Response:
            'The method returns the chat message history.'

            return self.greenApi.request('GET', 
                '{{host}}/waInstance{{idInstance}}'
                '/LastIncomingMessages/{{apiTokenInstance}}')

    def lastOutgoingMessages(self) -> Response:
            'The method returns the last outgoing messages of the account.'
            'Outgoing messages are stored on the server for 24 hours.'

            return self.greenApi.request('GET', 
                '{{host}}/waInstance{{idInstance}}'
                '/LastOutgoingMessages/{{apiTokenInstance}}')