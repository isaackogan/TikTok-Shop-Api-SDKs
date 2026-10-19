from enum import StrEnum


class GetCompassTaskListResponseDataTaskModuleType(StrEnum):
    BASE = "BASE"
    CREATOR = "CREATOR"

    def __str__(self) -> str:
        return str(self.value)
