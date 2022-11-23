from whatsapp_api_client_python.api import AbstractAPI


class BaseCategory:
    def __init__(self, api: AbstractAPI):
        self.api = api

    @classmethod
    def handle_parameters(cls, parameters: dict):
        new_parameters = parameters.copy()

        new_parameters.pop("self")

        for key, value in parameters.items():
            if value is None:
                new_parameters.pop(key)

        return new_parameters
