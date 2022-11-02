from os import environ

from whatsapp_api_client_python import API as API


ID_INSTANCE = environ['ID_INSTANCE']
API_TOKEN_INSTANCE = environ['API_TOKEN_INSTANCE']

greenAPI = API.GreenApi(ID_INSTANCE, API_TOKEN_INSTANCE)

class TestClass: 
        def test_getSettings(self):            
                result = greenAPI.account.getSettings()
                if result.code != 200:
                        print(result.error)
                assert isinstance(result, API.Response) and result.code == 200

        def test_getStateInstance(self):            
                result = greenAPI.account.getStateInstance()
                if result.code != 200:
                        print(result.error)
                assert isinstance(result, API.Response) and result.code == 200

def main():
        TestClass.test_getSettings(TestClass)
        TestClass.test_getStateInstance(TestClass)

if __name__ == "__main__":
    main()