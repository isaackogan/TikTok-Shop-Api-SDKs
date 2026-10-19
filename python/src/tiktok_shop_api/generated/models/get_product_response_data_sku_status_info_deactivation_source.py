from enum import StrEnum


class GetProductResponseDataSkuStatusInfoDeactivationSource(StrEnum):
    COMBO_RELATION = "COMBO_RELATION"
    PLATFORM = "PLATFORM"
    SELLER = "SELLER"

    def __str__(self) -> str:
        return str(self.value)
