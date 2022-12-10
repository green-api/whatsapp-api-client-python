from typing import NoReturn, Optional, TYPE_CHECKING, Union

from requests import Session

from .abc import AbstractAPI

if TYPE_CHECKING:
    from requests import Response


class GreenAPI(AbstractAPI):
    API_URL: str = "https://api.green-api.com/waInstance"

    def __init__(self, id_instance: Union[int, str], api_token_instance: str):
        self.id_instance = id_instance
        self.api_token_instance = api_token_instance

        super().__init__(self)

    def request(
            self,
            method: str,
            http_method: str = "GET",
            data: Optional[dict] = None,
            files: Optional[dict] = None
    ) -> Optional[dict]:
        url = (
            f"{self.API_URL}{self.id_instance}/"
            f"{method}/{self.api_token_instance}"
        )

        with Session() as session:
            if not files:
                if http_method == "DELETE":
                    response = session.request(
                        method=http_method,
                        url=f"""{url}/{data["receiptId"]}"""
                    )
                else:
                    response = session.request(
                        method=http_method, url=url, json=data
                    )
            else:
                response = session.request(
                    method=http_method, url=url, data=data, files=files
                )

        response = self.validate_response(response)

        return response

    def validate_response(
            self, response: "Response"
    ) -> Union[Optional[dict], NoReturn]:
        if response.status_code == 200:
            return response.json()
        raise GreenAPIError(response.status_code, response.text)


class GreenAPIError(Exception):
    def __init__(self, status_code: int, error_message: str):
        self.status_code = status_code
        self.error_message = error_message

    def __str__(self) -> str:
        return (
            f"status_code={self.status_code}, "
            f"error_message={self.error_message}"
        )


__all__ = ["GreenAPI", "GreenAPIError"]
