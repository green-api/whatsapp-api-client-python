import os.path
from whatsapp_api_client_python.response import Response


class Account:
    def __init__(self, restApi) -> None:
        self.restApi = restApi
        
    def getSettings(self) -> Response:
            'The method is aimed for getting the '\
            'current account settings.'
            
            return self.restApi.request('GET', 
                '{{host}}/waInstance{{idInstance}}'
                '/getSettings/{{apiTokenInstance}}')
            
    def getStateInstance(self) -> Response:
            'The method is aimed for getting the account state.'
            
            return self.restApi.request('GET', 
                '{{host}}/waInstance{{idInstance}}'
                '/getStateInstance/{{apiTokenInstance}}')

    def getStatusInstance(self) -> Response:
            'The method is aimed for getting the status of the account instance '\
            'socket connection with WhatsApp.'
            
            return self.restApi.request('GET', 
                '{{host}}/waInstance{{idInstance}}'
                '/getStatusInstance/{{apiTokenInstance}}')

    def logout(self) -> Response:
            'The method is aimed for logging out an account.'
            
            return self.restApi.request('GET', 
                '{{host}}/waInstance{{idInstance}}'
                '/Logout/{{apiTokenInstance}}')

    def qr(self) -> Response:
            'The method is aimed for getting QR code. To authorize your account, '\
            'you have to scan a QR code from application WhatsApp Business'\
            'on your phone. You can also get a QR code and authorize your'\
            'account in your profile.'
            
            return self.restApi.request('GET', 
                '{{host}}/waInstance{{idInstance}}'
                '/QR/{{apiTokenInstance}}')

    def reboot(self) -> Response:
            'The method is aimed for rebooting an account.'
            
            return self.restApi.request('GET', 
                '{{host}}/waInstance{{idInstance}}'
                '/Reboot/{{apiTokenInstance}}')

    def setProfilePicture(self, path) -> Response:
            'The method is aimed for setting an account picture.'

            pathParts = os.path.split(path)
            file = pathParts[1]

            files = [
                ('file',(file, open(path,'rb'),'image/jpeg'))
            ]
            
            return self.restApi.request('POST', 
                '{{host}}/waInstance{{idInstance}}'
                '/SetProfilePicture/{{apiTokenInstance}}', None, files)

    def setSettings(self, requestBody) -> Response:
            'The method is aimed for setting account settings. '\
            'When this method is requested, the account is rebooted.'
            
            return self.restApi.request('POST', 
                '{{host}}/waInstance{{idInstance}}'
                '/SetSettings/{{apiTokenInstance}}',
                requestBody)

    def setSettings(self) -> Response:
            'The method is aimed for setting a system proxy. '\
            'Use the method when you need to reset custom proxy '\
            'settings to system ones.'
            
            return self.restApi.request('GET', 
                '{{host}}/waInstance{{idInstance}}'
                '/SetSystemProxy/{{apiTokenInstance}}')