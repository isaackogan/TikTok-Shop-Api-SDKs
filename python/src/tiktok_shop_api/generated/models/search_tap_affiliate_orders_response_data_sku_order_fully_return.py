from enum import StrEnum


class SearchTAPAffiliateOrdersResponseDataSkuOrderFullyReturn(StrEnum):
    NO = "No"
    YES = "Yes"

    def __str__(self) -> str:
        return str(self.value)
