import array
import json
import typing

import requests

from whatsapp_api_client_python.response import Response
from whatsapp_api_client_python.tools import (
    account,
    device,
    groups,
    journals,
    marking,
    queues,
    receiving,
    sending,
    serviceMethods,
    webhooks
)


class GreenAPI:
    """REST API class"""

    def __init__(self, id_instance: str, token: str, host: str = "https://api.green-api.com") -> None:
        self.id_instance = id_instance
        self.token = token
        self.host = host

    @property
    def account(self) -> account.Account:
        return account.Account(self)

    @property
    def device(self) -> device.Device:
        return device.Device(self)

    @property
    def groups(self) -> groups.Groups:
        return groups.Groups(self)

    @property
    def journals(self) -> journals.Journals:
        return journals.Journals(self)

    @property
    def marking(self) -> marking.Marking:
        return marking.Marking(self)

    @property
    def queues(self) -> queues.Queues:
        return queues.Queues(self)

    @property
    def receiving(self) -> receiving.Receiving:
        return receiving.Receiving(self)

    @property
    def sending(self) -> sending.Sending:
        return sending.Sending(self)

    @property
    def service_methods(self) -> serviceMethods.ServiceMethods:
        return serviceMethods.ServiceMethods(self)

    @property
    def webhooks(self) -> webhooks.Webhooks:
        return webhooks.Webhooks(self)

    def request(
            self,
            method: typing.Literal["DELETE", "GET", "POST"],
            url: str,
            payload: typing.Optional[typing.Any] = None,
            files: typing.Optional[array.array] = None
    ):
        url = url.replace('{{host}}', self.host)
        url = url.replace('{{idInstance}}', self.id_instance)
        url = url.replace('{{apiTokenInstance}}', self.token)

        headers = {}
        payload_data = None
        if payload:
            if not files:
                headers["Content-Type"] = "application/json"
                payload_data = json.dumps(payload)
            else:
                payload_data = payload

        response = requests.request(
            method, url, headers=headers, data=payload_data, files=files
        )

        status_code = response.status_code
        text = response.text
        try:
            response.raise_for_status()
        except requests.HTTPError:
            return Response(status_code, text)
        except Exception as error:
            status_code = 0
            text = f'Other error occurred: {error}'
        return Response(status_code, text)
