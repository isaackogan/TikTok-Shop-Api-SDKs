from enum import StrEnum


class CreateCompassOfflineExportTaskRequestWindowType(StrEnum):
    PAST_24H = "PAST_24H"
    PAST_30_DAYS = "PAST_30_DAYS"
    PAST_7_DAYS = "PAST_7_DAYS"

    def __str__(self) -> str:
        return str(self.value)
