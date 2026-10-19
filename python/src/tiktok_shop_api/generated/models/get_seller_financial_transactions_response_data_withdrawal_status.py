from enum import StrEnum


class GetSellerFinancialTransactionsResponseDataWithdrawalStatus(StrEnum):
    CLOSED = "CLOSED"
    EXCEPTION = "EXCEPTION"
    FAILED = "FAILED"
    INIT = "INIT"
    ORDERED = "ORDERED"
    PROCESSED = "PROCESSED"
    PROCESSING = "PROCESSING"
    RECEIVED = "RECEIVED"
    REVERSED = "REVERSED"
    SUCCESS = "SUCCESS"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
