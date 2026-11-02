from enum import StrEnum

class GetOffSitePerformanceDetailsSortOrder(StrEnum):
    ASC = "ASC"
    DEFAULT = "Default"

    def __str__(self) -> str:
        return str(self.value)
