from enum import StrEnum


class GetStatementsSortOrder(StrEnum):
    ASC = "ASC"
    DESC = "DESC"

    def __str__(self) -> str:
        return str(self.value)
