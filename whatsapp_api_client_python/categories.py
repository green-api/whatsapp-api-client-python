from .api import AbstractAPI
from .methods import (
    account
)


class APICategories:
    def __init__(self, api: AbstractAPI):
        self.api = api

    @property
    def account(self) -> account.AccountCategory:
        return account.AccountCategory(self.api)


__all__ = ["APICategories"]
