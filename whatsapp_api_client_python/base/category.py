from whatsapp_api_client_python.api import AbstractAPI


class BaseCategory:
    def __init__(self, api: AbstractAPI):
        self.api = api
