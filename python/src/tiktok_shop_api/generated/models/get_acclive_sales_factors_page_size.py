from enum import IntEnum

class GetAccliveSalesFactorsPageSize(IntEnum):
    VALUE_10 = 10
    VALUE_20 = 20
    VALUE_50 = 50
    VALUE_100 = 100

    def __str__(self) -> str:
        return str(self.value)
