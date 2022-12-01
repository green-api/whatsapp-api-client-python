import json
import typing


class Response:
    data: typing.Optional[typing.Union[dict, list]] = None
    error: typing.Optional[str] = None
    status_code: int

    def __init__(self, status_code: int, text: str) -> None:
        self.status_code = status_code
        if status_code == 200:
            self.data = json.loads(text)
        else:
            self.error = text
