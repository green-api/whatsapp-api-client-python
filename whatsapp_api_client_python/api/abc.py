from abc import ABC, abstractmethod
from typing import Optional

from whatsapp_api_client_python.response import Response


class AbstractAPI(ABC):
    @abstractmethod
    def request(
            self,
            http_method: str,
            method: str,
            data: Optional[dict] = None,
            files: Optional[dict] = None
    ) -> Response:
        pass
