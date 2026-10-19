from enum import StrEnum


class SearchGoodsInfoResponseDataGoodHazmatInfoFlammableLiquidsExtraInfoFlammableLiquidsType(StrEnum):
    ALCOHOLIC = "ALCOHOLIC"
    OTHER = "OTHER"
    PAINT = "PAINT"
    PERFUMERY = "PERFUMERY"

    def __str__(self) -> str:
        return str(self.value)
