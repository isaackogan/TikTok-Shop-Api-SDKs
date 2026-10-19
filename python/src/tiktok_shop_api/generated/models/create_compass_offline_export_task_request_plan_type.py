from enum import StrEnum


class CreateCompassOfflineExportTaskRequestPlanType(StrEnum):
    ALL = "ALL"
    OPEN = "OPEN"
    PARTNER = "PARTNER"
    TARGET = "TARGET"

    def __str__(self) -> str:
        return str(self.value)
