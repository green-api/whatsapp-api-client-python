from array import array
import requests
from src.account import Account
from src.device import Device
from src.groups import Groups
from src.journals import Journals
from src.marking import Marking
from src.queues import Queues
from src.receiving import Receiving
from src.response import Response
from src.sending import Sending
from src.serviceMethods import ServiceMethods

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
                print(f'HTTP error occurred: {http_err}')
            except Exception as err:
                print(f'Other error occurred: {err}')
        elif method == 'POST':
            try:
                result = requests.post(url, json = data, files = files)
                result.raise_for_status()
            except requests.HTTPError as http_err:
                print(f'HTTP error occurred: {http_err}')
            except Exception as err:
                print(f'Other error occurred: {err}')
        elif method == 'DELETE':
            try:
                result = requests.delete(url, json = data, files = files)
                result.raise_for_status()
            except requests.HTTPError as http_err:
                print(f'HTTP error occurred: {http_err}')
            except Exception as err:
                print(f'Other error occurred: {err}')
        return Response(result.status_code, result.text)