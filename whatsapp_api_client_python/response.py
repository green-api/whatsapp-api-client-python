from json import loads
from typing import Generic, Optional, Type, TypeVar

from .responses.base import BaseResponse

Model = TypeVar("Model", bound=BaseResponse)


class Response(Generic[Model]):
    code: Optional[int]
    data: Optional[dict] = None
    error: Optional[str] = None

    create_models: bool = False
    model: Optional[Model] = None

    def __init__(self, code: Optional[int], text: str, create_models: bool):
        self.code = code
        if self.code == 200:
            self.data = loads(text)
        else:
            self.error = text

        self.create_models = create_models

    def create_model(self, response_type: Type[BaseResponse]) -> None:
        if self.create_models:
            self.model = response_type(**self.data)


__all__ = ["Response"]
