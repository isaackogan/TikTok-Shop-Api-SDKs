from enum import StrEnum


class GetCategoryRulesResponseDataFeeType(StrEnum):
    PFAND = "PFAND"

    def __str__(self) -> str:
        return str(self.value)
