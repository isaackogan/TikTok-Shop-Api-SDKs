from enum import StrEnum


class GetStatementsResponseDataStatementPaymentStatus(StrEnum):
    FAILED = "FAILED"
    PAID = "PAID"
    PROCESSING = "PROCESSING"
    SETTLED = "SETTLED"

    def __str__(self) -> str:
        return str(self.value)
