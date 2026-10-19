from enum import StrEnum


class GoodsMatchWebhookDataMatchType(StrEnum):
    MATCH = "MATCH"
    UNMATCH = "UNMATCH"

    def __str__(self) -> str:
        return str(self.value)
