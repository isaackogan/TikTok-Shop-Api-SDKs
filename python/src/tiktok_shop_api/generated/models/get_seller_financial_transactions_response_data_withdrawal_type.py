from enum import StrEnum


class GetSellerFinancialTransactionsResponseDataWithdrawalType(StrEnum):
    PAYMENT = "PAYMENT"
    POLICY_VIOLATION_DEDUCTION = "POLICY_VIOLATION_DEDUCTION"
    REFUND = "REFUND"
    REVERSE = "REVERSE"
    REWARD = "REWARD"
    SETTLE = "SETTLE"
    TRANSFER = "TRANSFER"
    UNKNOWN = "UNKNOWN"
    WITHDRAW = "WITHDRAW"

    def __str__(self) -> str:
        return str(self.value)
