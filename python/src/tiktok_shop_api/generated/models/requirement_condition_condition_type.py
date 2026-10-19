from enum import StrEnum


class RequirementConditionConditionType(StrEnum):
    VALUE_ID_MATCH = "VALUE_ID_MATCH"

    def __str__(self) -> str:
        return str(self.value)
