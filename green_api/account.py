from green_api.main import GreenApi
from green_api.response import Response


def getSettings(greenApi) -> Response:
        'The method is aimed for getting the '\
        'current account settings.'
        
        return greenApi.request('GET', 
            '{{host}}/waInstance{{idInstance}}'
            '/getSettings/{{apiTokenInstance}}')
        
def getStateInstance(greenApi) -> Response:
        'The method is aimed for getting the account state.'
        
        return greenApi.request('GET', 
            '{{host}}/waInstance{{idInstance}}'
            '/getStateInstance/{{apiTokenInstance}}')

def getStatusInstance(greenApi) -> Response:
        'The method is aimed for getting the status of the account instance '\
        'socket connection with WhatsApp.'
        
        return greenApi.request('GET', 
            '{{host}}/waInstance{{idInstance}}'
            '/getStatusInstance/{{apiTokenInstance}}')

def logout(greenApi) -> Response:
        'The method is aimed for logging out an account.'
        
        return greenApi.request('GET', 
            '{{host}}/waInstance{{idInstance}}'
            '/Logout/{{apiTokenInstance}}')

def qr(greenApi) -> Response:
        'The method is aimed for getting QR code. To authorize your account, '\
        'you have to scan a QR code from application WhatsApp Business'\
        'on your phone. You can also get a QR code and authorize your'\
        'account in your profile.'
        
        return greenApi.request('GET', 
            '{{host}}/waInstance{{idInstance}}'
            '/QR/{{apiTokenInstance}}')

def reboot(greenApi) -> Response:
        'The method is aimed for rebooting an account.'
        
        return greenApi.request('GET', 
            '{{host}}/waInstance{{idInstance}}'
            '/Reboot/{{apiTokenInstance}}')

def scanQRCode(greenApi) -> Response:
        'Along with getting a QR code using QR method, '\
        'it is possible to get a QR code via websocket connection. '\
        'Timeout for scanning a QR code is 100 seconds. '\
        'During this time, the QR code must be scanned. '\
        'To get a QR code, the account must be in an unauthorized state. '\
        'If the account is authorized, you have first to log out the account '\
        'using Logout method.'
        
        return greenApi.request('GET', 
            '{{host}}/waInstance{{idInstance}}'
            '/Scanqrcode/{{apiTokenInstance}}')

def setProfilePicture(greenApi: GreenApi) -> Response:
        'Along with getting a QR code using QR method, '\
        'it is possible to get a QR code via websocket connection. '\
        'Timeout for scanning a QR code is 100 seconds. '\
        'During this time, the QR code must be scanned. '\
        'To get a QR code, the account must be in an unauthorized state. '\
        'If the account is authorized, you have first to log out the account '\
        'using Logout method.'
        
        return greenApi.request('POST', 
            '{{host}}/waInstance{{idInstance}}'
            '/SetProfilePicture/{{apiTokenInstance}}')

def setSettings(greenApi) -> Response:
        'The method is aimed for setting account settings. '\
        'When this method is requested, the account is rebooted.'
        
        return greenApi.request('POST', 
            '{{host}}/waInstance{{idInstance}}'
            '/SetSettings/{{apiTokenInstance}}')

def setSettings(greenApi) -> Response:
        'The method is aimed for setting a system proxy. '\
        'Use the method when you need to reset custom proxy '\
        'settings to system ones.'
        
        return greenApi.request('GET', 
            '{{host}}/waInstance{{idInstance}}'
            '/SetSystemProxy/{{apiTokenInstance}}')