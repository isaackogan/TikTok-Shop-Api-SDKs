from enum import StrEnum


class GetProductResponseDataSkuFeeType(StrEnum):
    PFAND = "PFAND"

    def __str__(self) -> str:
        return str(self.value)
