from enum import StrEnum


class SearchCAPAffiliateOrdersResponseDataSkuOrderAttributionType(StrEnum):
    DIRECT = "Direct"
    INDIRECT = "Indirect"

    def __str__(self) -> str:
        return str(self.value)
