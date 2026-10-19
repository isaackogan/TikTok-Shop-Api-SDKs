from enum import StrEnum


class HandlingDurationType(StrEnum):
    BUSINESS_DAY = "BUSINESS_DAY"
    CALENDAR_DAY = "CALENDAR_DAY"

    def __str__(self) -> str:
        return str(self.value)
