from os import environ

from whatsapp_api_client_python import API as API


ID_INSTANCE = environ['ID_INSTANCE']
API_TOKEN_INSTANCE = environ['API_TOKEN_INSTANCE']

RestApi = API.RestApi('https://api.green-api.com', 
                        ID_INSTANCE, 
                        API_TOKEN_INSTANCE)

class TestClass: 
        def test_getSettings():            
                result = RestApi.account.getSettings()
                assert isinstance(result, API.Response) and result.code == 200

        def test_getStateInstance():            
                result = RestApi.account.getStateInstance()
                assert isinstance(result, API.Response) and result.code == 200

def main():
        TestClass.test_getSettings()
        TestClass.test_getStateInstance()

if __name__ == "__main__":
    main()