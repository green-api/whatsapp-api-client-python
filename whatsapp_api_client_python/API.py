from typing import Optional

from requests import Session
from requests.adapters import HTTPAdapter, Retry

from .response import Response
from .tools import (
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


class GreenApi:
    host: str
    media: str
    idInstance: str
    apiTokenInstance: str

    def __init__(
            self,
            idInstance: str,
            apiTokenInstance: str,
            host: str = "https://api.green-api.com",
            media: str = "https://media.green-api.com"
    ):
        self.host = host
        self.media = media
        self.idInstance = idInstance
        self.apiTokenInstance = apiTokenInstance

        self.session = Session()
        self.__prepare_session()

        self.account = account.Account(self)
        self.device = device.Device(self)
        self.groups = groups.Groups(self)
        self.journals = journals.Journals(self)
        self.marking = marking.Marking(self)
        self.queues = queues.Queues(self)
        self.receiving = receiving.Receiving(self)
        self.sending = sending.Sending(self)
        self.serviceMethods = serviceMethods.ServiceMethods(self)
        self.webhooks = webhooks.Webhooks(self)

    def request(
            self,
            method: str,
            url: str,
            payload: Optional[dict] = None,
            files: Optional[dict] = None
    ) -> Response:
        url = url.replace("{{host}}", self.host)
        url = url.replace("{{media}}", self.media)
        url = url.replace("{{idInstance}}", self.idInstance)
        url = url.replace("{{apiTokenInstance}}", self.apiTokenInstance)

        try:
            if not files:
                response = self.session.request(
                    method=method, url=url, json=payload
                )
            else:
                response = self.session.request(
                    method=method, url=url, data=payload, files=files
                )
        except Exception as error:
            return Response(None, f"Other error occurred: {error}.")
        return Response(response.status_code, response.text)

    def __prepare_session(self) -> None:
        retry = Retry(
            total=3,
            backoff_factor=1.0,
            allowed_methods=None,
            status_forcelist=[400, 429]
        )

        self.session.mount("http://", HTTPAdapter(max_retries=retry))
        self.session.mount("https://", HTTPAdapter(max_retries=retry))
