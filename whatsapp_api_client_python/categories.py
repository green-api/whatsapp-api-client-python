from .api import AbstractAPI
from .methods import (
    account,
    device,
    groups,
    journals,
    mark_read,
    queues,
    receiving,
    sending,
    service_methods
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
    def groups(self) -> groups.GroupCategory:
        return groups.GroupCategory(self.api)

    @property
    def journals(self) -> journals.JournalCategory:
        return journals.JournalCategory(self.api)

    @property
    def mark_read(self) -> mark_read.MarkReadCategory:
        return mark_read.MarkReadCategory(self.api)

    @property
    def queues(self) -> queues.QueueCategory:
        return queues.QueueCategory(self.api)

    @property
    def receiving(self) -> receiving.ReceivingCategory:
        return receiving.ReceivingCategory(self.api)

    @property
    def sending(self) -> sending.SendingCategory:
        return sending.SendingCategory(self.api)

    @property
    def service_methods(self) -> service_methods.ServiceMethodCategory:
        return service_methods.ServiceMethodCategory(self.api)


__all__ = ["APICategories"]
