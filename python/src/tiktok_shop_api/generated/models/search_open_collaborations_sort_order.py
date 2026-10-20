from enum import StrEnum


class SearchOpenCollaborationsSortOrder(StrEnum):
    ASC = "ASC"
    DESC = "DESC"

    def __str__(self) -> str:
        return str(self.value)
