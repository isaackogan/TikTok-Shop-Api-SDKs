from enum import StrEnum


class GetStatementsPaymentStatus(StrEnum):
    FAILED = "FAILED"
    PAID = "PAID"
    PROCESSING = "PROCESSING"

    def __str__(self) -> str:
        return str(self.value)
