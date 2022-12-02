from abc import ABC, abstractmethod
from typing import NoReturn, Optional, Union

from requests import Response

from whatsapp_api_client_python.categories import APICategories


class AbstractAPI(ABC, APICategories):
    @abstractmethod
    def request(
            self,
            method: str,
            http_method: str = "GET",
            data: Optional[dict] = None,
            files: Optional[dict] = None
    ) -> dict:
        pass

    @abstractmethod
    def validate_response(self, response: Response) -> Union[dict, NoReturn]:
        pass


__all__ = ["AbstractAPI"]
