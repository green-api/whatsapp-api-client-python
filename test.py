import os
from green_api.account import *
from green_api.main import GreenApi

ID_INSTANCE = os.environ['ID_INSTANCE']
API_TOKEN_INSTANCE = os.environ['API_TOKEN_INSTANCE']


def main():
        g = GreenApi('https://api.green-api.com', 
                ID_INSTANCE, 
                API_TOKEN_INSTANCE)
        r = getSettings(g)
        print(r.data)

if __name__ == '__main__':
    main()