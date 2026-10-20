from enum import StrEnum

class CreatePromotionActivityRequestParticipationLimitType(StrEnum):
    BUYER_LIMIT_ONLY_ONE = "BUYER_LIMIT_ONLY_ONE"
    BUYER_NO_LIMIT = "BUYER_NO_LIMIT"

    def __str__(self) -> str:
        return str(self.value)
