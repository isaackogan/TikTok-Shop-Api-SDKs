from enum import StrEnum

class GetShopVideoPerformanceListSortOrder(StrEnum):
    ASC = "ASC"
    DESC = "DESC"

    def __str__(self) -> str:
        return str(self.value)
