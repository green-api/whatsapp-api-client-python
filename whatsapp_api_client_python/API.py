from array import array
import json
import requests
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

class RestApi:
    'REST API class'

    host: str
    idInstance: str
    apiTokenInstance: str

    def __init__(self, host: str, idInstance: str, apiTokenInstance: str) -> None:
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

    def request(self, method: str, url: str, data: any = None, files: array = None):
        url = url.replace('{{host}}', self.host)
        url = url.replace('{{idInstance}}', self.idInstance)
        url = url.replace('{{apiTokenInstance}}', self.apiTokenInstance)
        status_code = 0
        text = ''
        if method == 'GET':
            try:
                result = requests.get(url)
                result.raise_for_status()
            except requests.HTTPError as http_err:
                status_code = 0
                text = f'HTTP error occurred: {http_err}'
            except Exception as err:
                status_code = 0
                text = f'Other error occurred: {err}'
        elif method == 'POST':
            try:
                result = requests.post(url, json = data, files = files)
                result.raise_for_status()
                status_code = result.status_code
                text = result.text
            except requests.HTTPError as http_err:
                status_code = 0
                text = f'HTTP error occurred: {http_err}'
            except Exception as err:
                status_code = 0
                text = f'Other error occurred: {err}'
        elif method == 'DELETE':
            try:
                result = requests.delete(url, json = data, files = files)
                result.raise_for_status()
            except requests.HTTPError as http_err:
                status_code = 0
                text = f'HTTP error occurred: {http_err}'
            except Exception as err:
                status_code = 0
                text = f'Other error occurred: {err}'
        return Response(status_code, text)

class Response:
    code: int
    data: json
    error: str

    def __init__(self, code: int, text: str) -> None:
        self.code = code
        if code == 200:
            self.data = json.loads(text)
        else:
            self.error = text