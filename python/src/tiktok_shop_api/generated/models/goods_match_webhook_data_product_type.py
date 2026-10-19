from enum import StrEnum


class GoodsMatchWebhookDataProductType(StrEnum):
    GLOBAL = "GLOBAL"
    LOCAL = "LOCAL"

    def __str__(self) -> str:
        return str(self.value)
