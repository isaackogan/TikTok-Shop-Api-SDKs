from enum import StrEnum

class GetBestsellingCreatorsTimeSlot(StrEnum):
    VALUE_0 = "1D"
    VALUE_1 = "7D"
    VALUE_2 = "30D"

    def __str__(self) -> str:
        return str(self.value)
