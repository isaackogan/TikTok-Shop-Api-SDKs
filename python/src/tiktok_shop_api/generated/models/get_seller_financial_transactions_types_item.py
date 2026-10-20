from enum import StrEnum


class GetSellerFinancialTransactionsTypesItem(StrEnum):
    PAYMENT = "PAYMENT"
    REFUND = "REFUND"
    REVERSE = "REVERSE"
    SETTLE = "SETTLE"
    TRANSFER = "TRANSFER"
    WITHDRAW = "WITHDRAW"

    def __str__(self) -> str:
        return str(self.value)
