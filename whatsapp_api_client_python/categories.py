from .api import AbstractAPI
from .methods import (
    account,
    device,
    mark_read,
    queues
)


class APICategories:
    def __init__(self, api: AbstractAPI):
        self.api = api

    @property
    def account(self) -> account.AccountCategory:
        return account.AccountCategory(self.api)

    @property
    def device(self) -> device.DeviceCategory:
        return device.DeviceCategory(self.api)

    @property
    def mark_read(self) -> mark_read.MarkReadCategory:
        return mark_read.MarkReadCategory(self.api)

    @property
    def queues(self) -> queues.QueueCategory:
        return queues.QueueCategory(self.api)


__all__ = ["APICategories"]
