from whatsapp_api_client_python.response import Response


class Device:
    def __init__(self, restApi) -> None:
        self.restApi = restApi
        
    def getDeviceInfo(self) -> Response:
            'The method is aimed for getting information about the device '\
            '(phone) running WhatsApp Business application.'
            
            return self.restApi.request('GET', 
                '{{host}}/waInstance{{idInstance}}'
                '/GetDeviceInfo/{{apiTokenInstance}}')