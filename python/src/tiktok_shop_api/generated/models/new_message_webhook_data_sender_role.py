from enum import StrEnum


class NewMessageWebhookDataSenderRole(StrEnum):
    BUYER = "BUYER"
    CUSTOMER_SERVICE = "CUSTOMER_SERVICE"
    ROBOT = "ROBOT"
    SHOP = "SHOP"
    SYSTEM = "SYSTEM"

    def __str__(self) -> str:
        return str(self.value)
