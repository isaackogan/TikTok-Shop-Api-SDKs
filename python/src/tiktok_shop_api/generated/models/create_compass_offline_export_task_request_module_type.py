from enum import StrEnum

class CreateCompassOfflineExportTaskRequestModuleType(StrEnum):
    BASE = "BASE"
    CREATOR = "CREATOR"

    def __str__(self) -> str:
        return str(self.value)
