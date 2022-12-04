from typing import TYPE_CHECKING

from whatsapp_api_client_python.methods import (
    account,
    device,
    groups,
    journals,
    queues,
    read_mark,
    receiving,
    sending,
    service_methods
)

if TYPE_CHECKING:
    from whatsapp_api_client_python.api import AbstractAPI


class APICategories:
    def __init__(self, api: "AbstractAPI"):
        self.api = api

    @property
    def account(self) -> account.AccountCategory:
        return account.AccountCategory(self.api)

    @property
    def device(self) -> device.DeviceCategory:
        return device.DeviceCategory(self.api)

    @property
    def groups(self) -> groups.GroupsCategory:
        return groups.GroupsCategory(self.api)

    @property
    def journals(self) -> journals.JournalsCategory:
        return journals.JournalsCategory(self.api)

    @property
    def queues(self) -> queues.QueuesCategory:
        return queues.QueuesCategory(self.api)

    @property
    def read_mark(self) -> read_mark.ReadMarkCategory:
        return read_mark.ReadMarkCategory(self.api)

    @property
    def receiving(self) -> receiving.ReceivingCategory:
        return receiving.ReceivingCategory(self.api)

    @property
    def sending(self) -> sending.SendingCategory:
        return sending.SendingCategory(self.api)

    @property
    def service_methods(self) -> service_methods.ServiceMethodsCategory:
        return service_methods.ServiceMethodsCategory(self.api)


__all__ = ["APICategories"]
