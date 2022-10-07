from os import environ

from whatsapp_api_client_python import API as API


ID_INSTANCE = environ['ID_INSTANCE']
API_TOKEN_INSTANCE = environ['API_TOKEN_INSTANCE']

API = API.RestApi('https://api.green-api.com', 
                        ID_INSTANCE, 
                        API_TOKEN_INSTANCE)

class TestClass: 
        def test_getSettings(self):            
                result = API.account.getSettings()
                assert isinstance(result, API.Response) and result.code == 200

        def test_getStateInstance(self):            
                result = API.account.getStateInstance()
                assert isinstance(result, API.Response) and result.code == 200