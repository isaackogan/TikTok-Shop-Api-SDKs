from enum import StrEnum


class DiagnoseAndOptimizeProductRequestOptimizationFieldsItem(StrEnum):
    ALL = "ALL"
    DESCRIPTION = "DESCRIPTION"
    IMAGE = "IMAGE"
    NONE = "NONE"
    TITLE = "TITLE"

    def __str__(self) -> str:
        return str(self.value)
