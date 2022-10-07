from array import array
import requests
from response import Response
from tools.account import Account
from tools.device import Device
from tools.groups import Groups
from tools.journals import Journals
from tools.marking import Marking
from tools.queues import Queues
from tools.receiving import Receiving
from tools.sending import Sending
from tools.serviceMethods import ServiceMethods

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