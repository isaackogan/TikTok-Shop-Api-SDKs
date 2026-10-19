from enum import StrEnum


class ProductInformationChangeWebhookDataChangeSource(StrEnum):
    OPEN_API = "OPEN_API"
    SELLER_CENTER = "SELLER_CENTER"

    def __str__(self) -> str:
        return str(self.value)
