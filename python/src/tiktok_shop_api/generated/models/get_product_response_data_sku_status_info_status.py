from enum import StrEnum


class GetProductResponseDataSkuStatusInfoStatus(StrEnum):
    DEACTIVATED = "DEACTIVATED"
    NORMAL = "NORMAL"

    def __str__(self) -> str:
        return str(self.value)
