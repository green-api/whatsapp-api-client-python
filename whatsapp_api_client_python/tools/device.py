
class Device:
    def __init__(self, restApi) -> None:
        self.restApi = restApi
        
    def getDeviceInfo(self):
            'The method is aimed for getting information about the device '\
            '(phone) running WhatsApp Business application.'
            
            return self.restApi.request('GET', 
                '{{host}}/waInstance{{idInstance}}'
                '/GetDeviceInfo/{{apiTokenInstance}}')