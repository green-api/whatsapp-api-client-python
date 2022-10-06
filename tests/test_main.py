from os import environ
from re import T

from whatsapp_api_client_python import API
from whatsapp_api_client_python.response import Response


ID_INSTANCE = environ['ID_INSTANCE']
API_TOKEN_INSTANCE = environ['API_TOKEN_INSTANCE']

API = API.RestApi('https://api.green-api.com', 
                        ID_INSTANCE, 
                        API_TOKEN_INSTANCE)

class TestClass: 
        def test_getSettings(self):            
                result = API.account.getSettings()
                assert isinstance(result, Response) and result.code == 200

        def test_getStateInstance(self):            
                result = API.account.getStateInstance()
                assert isinstance(result, Response) and result.code == 200