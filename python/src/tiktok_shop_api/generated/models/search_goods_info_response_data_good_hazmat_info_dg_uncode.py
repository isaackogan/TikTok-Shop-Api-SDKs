from enum import StrEnum


class SearchGoodsInfoResponseDataGoodHazmatInfoDgUncode(StrEnum):
    OTHER = "OTHER"
    UN1263 = "UN1263"
    UN1266 = "UN1266"
    UN2807 = "UN2807"
    UN3065 = "UN3065"
    UN3090 = "UN3090"
    UN3091 = "UN3091"
    UN3480 = "UN3480"
    UN3481 = "UN3481"

    def __str__(self) -> str:
        return str(self.value)
