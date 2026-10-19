from enum import StrEnum


class GetShopProductPerformanceDetailResponseDataPerformanceRatingStars(StrEnum):
    VALUE_0 = "1_STAR"
    VALUE_1 = "2_STAR"
    VALUE_2 = "3_STAR"
    VALUE_3 = "4_STAR"
    VALUE_4 = "5_STAR"

    def __str__(self) -> str:
        return str(self.value)
