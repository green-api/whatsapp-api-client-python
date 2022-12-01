import unittest
from os import environ

from whatsapp_api_client_python import GreenAPI

ID_INSTANCE = environ["ID_INSTANCE"]
API_TOKEN_INSTANCE = environ["API_TOKEN_INSTANCE"]

greenAPI = GreenAPI(ID_INSTANCE, API_TOKEN_INSTANCE)


class GreenAPITestCase(unittest.TestCase):
    def test_getSettings(self):
        response = greenAPI.account.get_settings()

        self.assertEqual(response.status_code, 200, response.error)

    def test_getStateInstance(self):
        response = greenAPI.account.get_state_instance()

        self.assertEqual(response.status_code, 200, response.error)


if __name__ == '__main__':
    unittest.main()
