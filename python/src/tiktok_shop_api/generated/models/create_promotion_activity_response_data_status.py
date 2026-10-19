from enum import StrEnum


class CreatePromotionActivityResponseDataStatus(StrEnum):
    DEACTIVATED = "DEACTIVATED"
    DRAFT = "DRAFT"
    EXPIRED = "EXPIRED"
    NOT_EFFECTIVE = "NOT_EFFECTIVE"
    NOT_START = "NOT_START"
    ONGOING = "ONGOING"

    def __str__(self) -> str:
        return str(self.value)
