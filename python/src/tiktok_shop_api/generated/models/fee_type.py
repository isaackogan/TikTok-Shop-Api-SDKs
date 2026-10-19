from enum import StrEnum


class FeeType(StrEnum):
    PFAND = "PFAND"

    def __str__(self) -> str:
        return str(self.value)
