from os import environ

from whatsapp_api_client_python import greenAPI as greenAPI


ID_INSTANCE = environ['ID_INSTANCE']
API_TOKEN_INSTANCE = environ['API_TOKEN_INSTANCE']

RestApi = greenAPI.RestApi('https://api.green-api.com', 
                        ID_INSTANCE, 
                        API_TOKEN_INSTANCE)

class TestClass: 
        def test_getSettings(self):            
                result = RestApi.account.getSettings()
                if result.code != 200:
                        print(result.error)
                assert isinstance(result, greenAPI.Response) and result.code == 200

        def test_getStateInstance(self):            
                result = RestApi.account.getStateInstance()
                if result.code != 200:
                        print(result.error)
                assert isinstance(result, greenAPI.Response) and result.code == 200

def main():
        TestClass.test_getSettings(TestClass)
        TestClass.test_getStateInstance(TestClass)

if __name__ == "__main__":
    main()