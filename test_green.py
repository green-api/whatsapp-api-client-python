from os import environ
from re import T
from green_api.account import *
from green_api.main import GreenApi


ID_INSTANCE = environ['ID_INSTANCE']
API_TOKEN_INSTANCE = environ['API_TOKEN_INSTANCE']

g = GreenApi('https://api.green-api.com', 
                        ID_INSTANCE, 
                        API_TOKEN_INSTANCE)

class TestClass: 
        def test_one(self):            
                r = getSettings(g)
                assert isinstance(r, Response)