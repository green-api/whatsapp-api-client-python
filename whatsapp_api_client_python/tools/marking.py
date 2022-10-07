class Marking:
    def __init__(self, restApi) -> None:
        self.restApi = restApi
        
    def readChat(self, chatId: str, idMessage: str):
            'The method returns the chat message history.'

            requestBody = {
                'chatId': chatId,
                'idMessage': idMessage,
            }

            return self.restApi.request('POST', 
                '{{host}}/waInstance{{idInstance}}'
                '/ReadChat/{{apiTokenInstance}}',
                requestBody)