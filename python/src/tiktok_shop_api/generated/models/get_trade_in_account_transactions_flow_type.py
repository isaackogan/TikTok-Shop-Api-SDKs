from enum import StrEnum


class GetTradeInAccountTransactionsFlowType(StrEnum):
    RECHARGE = "RECHARGE"
    REVERSE = "REVERSE"
    WITHDRAW = "WITHDRAW"

    def __str__(self) -> str:
        return str(self.value)
