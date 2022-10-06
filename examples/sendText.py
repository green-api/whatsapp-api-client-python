from os import environ

import src as greenAPI

ID_INSTANCE = environ['ID_INSTANCE']
API_TOKEN_INSTANCE = environ['API_TOKEN_INSTANCE']

restApi = greenAPI.RestApi('https://api.green-api.com', 
                        ID_INSTANCE, 
                        API_TOKEN_INSTANCE)

def main():
    restApi.sending.sendMessage('120363025955348359@g.us', 'Message text')

if __name__ == "__main__":
    main()