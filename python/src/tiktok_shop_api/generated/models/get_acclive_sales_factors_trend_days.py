from enum import IntEnum

class GetAccliveSalesFactorsTrendDays(IntEnum):
    VALUE_7 = 7
    VALUE_14 = 14
    VALUE_30 = 30

    def __str__(self) -> str:
        return str(self.value)
