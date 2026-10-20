from enum import StrEnum


class SortSortField(StrEnum):
    CREATE_TIME = "CREATE_TIME"
    UPDATE_TIME = "UPDATE_TIME"

    def __str__(self) -> str:
        return str(self.value)
