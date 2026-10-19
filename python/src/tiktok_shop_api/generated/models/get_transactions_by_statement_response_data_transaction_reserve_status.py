from enum import StrEnum


class GetTransactionsByStatementResponseDataTransactionReserveStatus(StrEnum):
    COLLECTED = "COLLECTED"
    RELEASED = "RELEASED"

    def __str__(self) -> str:
        return str(self.value)
