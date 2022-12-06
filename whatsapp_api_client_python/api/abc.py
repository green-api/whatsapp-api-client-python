from abc import ABC, abstractmethod
from typing import NoReturn, Optional, TYPE_CHECKING, Union

from whatsapp_api_client_python.categories import APICategories

if TYPE_CHECKING:
    from requests import Response


class AbstractAPI(ABC, APICategories):
    @abstractmethod
    def request(
            self,
            method: str,
            http_method: str = "GET",
            data: Optional[dict] = None,
            files: Optional[dict] = None
    ) -> Optional[dict]:
        pass

    @abstractmethod
    def validate_response(
            self, response: "Response"
    ) -> Union[Optional[dict], NoReturn]:
        pass


__all__ = ["AbstractAPI"]
