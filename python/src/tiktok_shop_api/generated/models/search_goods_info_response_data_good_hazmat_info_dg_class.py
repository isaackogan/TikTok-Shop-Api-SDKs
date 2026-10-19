from enum import StrEnum


class SearchGoodsInfoResponseDataGoodHazmatInfoDgClass(StrEnum):
    CLASS_2 = "CLASS_2"
    CLASS_3 = "CLASS_3"
    CLASS_9 = "CLASS_9"

    def __str__(self) -> str:
        return str(self.value)
