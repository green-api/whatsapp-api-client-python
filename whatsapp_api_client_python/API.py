import json
import logging
from typing import Any, NoReturn, Optional

from requests import Response, Session
from requests.adapters import HTTPAdapter, Retry

from .response import Response as GreenAPIResponse
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
    webhooks,
    partner,
    statuses
)


class GreenApi:
    host: str
    media: str
    idInstance: str
    apiTokenInstance: str
    directHost: bool #Flag for determining and using a direct host

    def __init__(
            self,
            idInstance: str,
            apiTokenInstance: str,
            debug_mode: bool = False,
            raise_errors: bool = False,
            directHost: bool = False,
            host: str = "https://api.green-api.com",
            media: str = "https://media.green-api.com",
            host_timeout: float = 180, # sec per retry
            media_timeout: float = 10800, # sec per retry
    ):
        self.host = host
        self.media = media
        self.debug_mode = debug_mode
        self.raise_errors = raise_errors
        self.directHost = directHost
        if self.directHost:
            self.host, self.media = self._determine_host(idInstance)
        else:
            self.host = host
            self.media = media

        self.host_timeout = host_timeout
        self.media_timeout = media_timeout

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
        self.statuses = statuses.Statuses(self)

        self.logger = logging.getLogger("whatsapp-api-client-python")
        self.__prepare_logger()

    def _determine_host(self, idInstance: str) -> str: #Method for determining a direct host
        mapping = {
            "1103": (f"https://{idInstance[:4]}.api.green-api.com", f"https://{idInstance[:4]}.media.green-api.com"),
            "1104": (f"https://1103.api.green-api.com", f"https://1103.media.green-api.com"),
            "5700": (f"https://{idInstance[:4]}.api.green-api.com", f"https://{idInstance[:4]}.media.green-api.com") ,
            "7723": ("https://7700.api.greenapi.com", "https://7700.media.greenapi.com"),
            "7726": ("https://api.greenapi.com", "https://media.greenapi.com"),
            "7": (f"https://{idInstance[:4]}.api.greenapi.com", f"https://{idInstance[:4]}.media.greenapi.com")
        }
        return next((url for key, url in mapping.items() if idInstance.startswith(key)), ("https://api.green-api.com", "https://media.green-api.com"))

    def request(
            self,
            method: str,
            url: str,
            payload: Optional[dict] = None,
            files: Optional[dict] = None
    ) -> GreenAPIResponse:
        url = url.replace("{{host}}", self.host)
        url = url.replace("{{media}}", self.media)
        url = url.replace("{{idInstance}}", self.idInstance)
        url = url.replace("{{apiTokenInstance}}", self.apiTokenInstance)

        headers = {
            'User-Agent': 'GREEN-API_SDK_PY/1.0'
        }

        try:
            if not files:
                response = self.session.request(
                    method=method, url=url, json=payload, timeout=self.host_timeout, headers=headers
                )
            else:
                response = self.session.request(
                    method=method, url=url, data=payload, files=files, timeout=self.media_timeout, headers=headers
                )
        except Exception as error:
            error_message = f"Request was failed with error: {error}."

            if self.raise_errors:
                raise GreenAPIError(error_message)
            self.logger.log(logging.CRITICAL, error_message)

            return GreenAPIResponse(None, error_message)

        self.__handle_response(response)

        return GreenAPIResponse(response.status_code, response.text)

    def raw_request(self, **arguments: Any) -> GreenAPIResponse:
        try:
            response = self.session.request(**arguments)
        except Exception as error:
            error_message = f"Request was failed with error: {error}."

            if self.raise_errors:
                raise GreenAPIError(error_message)
            self.logger.log(logging.CRITICAL, error_message)

            return GreenAPIResponse(None, error_message)

        self.__handle_response(response)

        return GreenAPIResponse(response.status_code, response.text)

    def __handle_response(self, response: Response) -> Optional[NoReturn]:
        status_code = response.status_code
        if status_code != 200 or self.debug_mode:
            try:
                data = json.dumps(
                    json.loads(response.text), ensure_ascii=False, indent=4
                )
            except json.JSONDecodeError:
                data = response.text

            if status_code != 200:
                error_message = (
                    f"Request was failed with status code: {status_code}."
                    f" Data: {data}"
                )

                if self.raise_errors:
                    raise GreenAPIError(error_message)
                self.logger.log(logging.ERROR, error_message)

                return None

            self.logger.log(
                logging.DEBUG, f"Request was successful with data: {data}"
            )

    def __prepare_logger(self) -> None:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter(
            (
                "%(asctime)s:%(name)s:"
                "%(levelname)s:%(message)s"
            ), datefmt="%Y-%m-%d %H:%M:%S"
        ))

        self.logger.addHandler(handler)

        if not self.debug_mode:
            self.logger.setLevel(logging.INFO)
        else:
            self.logger.setLevel(logging.DEBUG)

    def __prepare_session(self) -> None:
        self.session.headers["Connection"] = "close"

        retry = Retry(
            total=3,
            backoff_factor=1.0,
            allowed_methods=None,
            status_forcelist=[429]
        )

        self.session.mount("http://", HTTPAdapter(max_retries=retry))
        self.session.mount("https://", HTTPAdapter(max_retries=retry))

class GreenAPI(GreenApi):
    pass


class GreenAPIError(Exception):
    pass

class GreenApiPartner(GreenApi):
    def __init__(
            self,
            partnerToken: str,
            email: str = None,
            host: str = "https://api.green-api.com"
    ):

        super().__init__(
            idInstance="",
            apiTokenInstance="",
            host=host
        )
        
        self.partnerToken = partnerToken
        self.email = email
        self.partner = partner.Partner(self)

    def request(
            self,
            method: str,
            url: str,
            payload: Optional[dict] = None,
            files: Optional[dict] = None
    ) -> GreenAPIResponse:

        url = url.replace("{{partnerToken}}", self.partnerToken)

        return super().request(method, url, payload, files)