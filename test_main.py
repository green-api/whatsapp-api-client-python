from os import environ
from re import T
from src.account import *
from src.restApi import RestApi


ID_INSTANCE = environ['ID_INSTANCE']
API_TOKEN_INSTANCE = environ['API_TOKEN_INSTANCE']

restApi = RestApi('https://api.green-api.com', 
                        ID_INSTANCE, 
                        API_TOKEN_INSTANCE)

class TestClass: 
        def test_getSettings(self):            
                result = restApi.account.getSettings()
                assert isinstance(result, Response) and result.code == 200

        def test_getStateInstance(self):            
                result = restApi.account.getStateInstance()
                assert isinstance(result, Response) and result.code == 200

        def test_sendButtons(self):            
                result = restApi.sending.sendButtons('120363025955348359@g.us',
                        'Message', 'Footer', 
                        [
                                {"buttonId": "1", "buttonText": "test"}, 
                                {"buttonId": "2", "buttonText": "test2"}
                        ])
                assert isinstance(result, Response) and result.code == 200
