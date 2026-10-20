from enum import StrEnum


class SearchOpenCollaborationProductsSortOrder(StrEnum):
    ASC = "ASC"
    DESC = "DESC"

    def __str__(self) -> str:
        return str(self.value)
