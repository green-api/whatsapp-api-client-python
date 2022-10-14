from array import array
import mimetypes
import requests
import json
from whatsapp_api_client_python.response import Response

from whatsapp_api_client_python.tools.account import Account
from whatsapp_api_client_python.tools.device import Device
from whatsapp_api_client_python.tools.groups import Groups
from whatsapp_api_client_python.tools.journals import Journals
from whatsapp_api_client_python.tools.marking import Marking
from whatsapp_api_client_python.tools.queues import Queues
from whatsapp_api_client_python.tools.receiving import Receiving
from whatsapp_api_client_python.tools.sending import Sending
from whatsapp_api_client_python.tools.serviceMethods import ServiceMethods
from whatsapp_api_client_python.tools.webhooks import Webhooks


class RestApi:
    'REST API class'

    host: str
    idInstance: str
    apiTokenInstance: str

    def __init__(self, 
                    idInstance: str, 
                    apiTokenInstance: str,
                    host: str = 'https://api.green-api.com') -> None:
        self.host = host
        self.idInstance = idInstance
        self.apiTokenInstance = apiTokenInstance

        self.account = Account(self)
        self.device = Device(self)
        self.groups = Groups(self)
        self.journals = Journals(self)
        self.marking = Marking(self)
        self.queues = Queues(self)
        self.receiving = Receiving(self)
        self.sending = Sending(self)
        self.serviceMethods = ServiceMethods(self)
        self.webhooks = Webhooks(self)

    def request(self, method: str, url: str, 
                payload: any = None, files: array = None):
        url = url.replace('{{host}}', self.host)
        url = url.replace('{{idInstance}}', self.idInstance)
        url = url.replace('{{apiTokenInstance}}', self.apiTokenInstance)
        status_code = 0
        text = ''
        try:
            headers = {}
            payloadData = None
            if payload != None:
                if files == None:
                    headers = {
                        'Content-Type': 'application/json'
                    }
                    payloadData = json.dumps(payload)
                else:
                    payloadData = payload   
            result = requests.request(method, url, headers = headers, 
                                        data = payloadData, 
                                        files = files)
            result.raise_for_status()
            status_code = result.status_code
            text = result.text
        except requests.HTTPError as http_err:
            status_code = 0
            text = f'HTTP {method} error occurred: {http_err}'
        except Exception as err:
            status_code = 0
            text = f'Other error occurred: {err}'
        return Response(status_code, text)