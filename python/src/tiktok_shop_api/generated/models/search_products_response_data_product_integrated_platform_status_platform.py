from enum import StrEnum


class SearchProductsResponseDataProductIntegratedPlatformStatusPlatform(StrEnum):
    TOKOPEDIA = "TOKOPEDIA"

    def __str__(self) -> str:
        return str(self.value)
