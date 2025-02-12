from json import loads
from typing import Optional


class Response:
    code: Optional[int]
    data: Optional[dict] = None
    error: Optional[str] = None

    def __init__(self, code: Optional[int], text: str):
        self.code = code
        if self.code == 200:
            try:
                self.data = loads(text)
            except:
                self.data = "[]"
        else:
            self.error = text
