from enum import StrEnum


class GetProductResponseDataIntegratedPlatformStatusPlatform(StrEnum):
    TOKOPEDIA = "TOKOPEDIA"

    def __str__(self) -> str:
        return str(self.value)
