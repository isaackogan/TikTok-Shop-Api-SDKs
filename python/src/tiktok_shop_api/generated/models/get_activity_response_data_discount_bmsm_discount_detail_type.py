from enum import StrEnum


class GetActivityResponseDataDiscountBmsmDiscountDetailType(StrEnum):
    AMOUNT_OFF = "AMOUNT_OFF"
    PERCENTAGE_OFF = "PERCENTAGE_OFF"

    def __str__(self) -> str:
        return str(self.value)
