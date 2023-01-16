import json


class Response:
    code: int
    data: json
    error: str

    def __init__(self, code: int, text: str) -> None:
        self.code = code
        if code == 200:
            self.data = json.loads(text)
            self.error = None
        else:
            self.error = text
            self.data = None