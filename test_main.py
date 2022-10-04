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
        def test_getSettings():            
                result = restApi.account.getSettings()
                assert isinstance(result, Response) and result.code == 200

        def test_getStateInstance():            
                result = restApi.account.getStateInstance()
                assert isinstance(result, Response) and result.code == 200

        #def test_getDeviceInfo():            
        #        result = restApi.device.getDeviceInfo()
        #        assert isinstance(result, Response) and result.code == 200

        #if __name__ == "__main__":
        #        test_getDeviceInfo()
