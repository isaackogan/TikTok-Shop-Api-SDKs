from enum import StrEnum


class GetOrderDetailResponseDataOrderPaymentCardType(StrEnum):
    CREDIT = "Credit"
    DEBIT = "Debit"
    PREPAID = "Prepaid"

    def __str__(self) -> str:
        return str(self.value)
