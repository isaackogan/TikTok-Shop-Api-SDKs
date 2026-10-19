from enum import StrEnum


class GetGlobalAttributesResponseDataAttributeRequirementConditionConditionType(StrEnum):
    VALUE_ID_MATCH = "VALUE_ID_MATCH"

    def __str__(self) -> str:
        return str(self.value)
