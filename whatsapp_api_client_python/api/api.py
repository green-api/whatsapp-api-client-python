import json
from typing import Optional

import requests

from whatsapp_api_client_python.api.abc import AbstractAPI
from whatsapp_api_client_python.categories import APICategories
from whatsapp_api_client_python.response import Response


class GreenAPI(AbstractAPI, APICategories):
    """REST API class"""

    def __init__(
            self,
            id_instance: str,
            api_token_instance: str,
            host: str = "https://api.green-api.com"
    ):
        self.id_instance = id_instance
        self.api_token_instance = api_token_instance
        self.host = host

        super(GreenAPI, self).__init__(self)

    def request(
            self,
            http_method: str,
            method: str,
            data: Optional[dict] = None,
            files: Optional[dict] = None
    ) -> Response:
        url = (
            f"{self.host}/waInstance{self.id_instance}/"
            f"{method}/{self.api_token_instance}"
        )
        headers = {}

        if data and not files:
            data = json.dumps(data)

            headers = {"Content-Type": "application/json"}

        response = requests.request(
            http_method, url, headers=headers, data=data, files=files
        )

        return Response(response.status_code, response.text)
