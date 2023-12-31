from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..API import GreenApi


class BaseCategory:
    def __init__(self, api: "GreenApi"):
        self.api = api

    @classmethod
    def __handle_parameters(cls, parameters: dict) -> dict:
        handled_parameters = parameters.copy()

        handled_parameters.pop("self")

        for key, value in parameters.items():
            if value is None:
                handled_parameters.pop(key)

        return handled_parameters


__all__ = ["BaseCategory"]
