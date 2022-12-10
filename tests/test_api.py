import unittest
from os import environ

from whatsapp_api_client_python import GreenAPI

ID_INSTANCE = environ["ID_INSTANCE"]
API_TOKEN_INSTANCE = environ["API_TOKEN_INSTANCE"]

greenAPI = GreenAPI(ID_INSTANCE, API_TOKEN_INSTANCE)


class GreenAPITestCase(unittest.TestCase):
    def test_GetStateInstance(self):
        response = greenAPI.account.get_state_instance()

        self.assertTrue(response)

    def test_CheckWhatsapp(self):
        response = greenAPI.service_methods.check_whatsapp(79001234567)

        self.assertTrue(response)


if __name__ == '__main__':
    unittest.main()
