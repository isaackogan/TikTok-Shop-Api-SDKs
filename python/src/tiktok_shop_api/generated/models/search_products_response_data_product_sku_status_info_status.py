from enum import StrEnum


class SearchProductsResponseDataProductSkuStatusInfoStatus(StrEnum):
    DEACTIVATED = "DEACTIVATED"
    NORMAL = "NORMAL"

    def __str__(self) -> str:
        return str(self.value)
