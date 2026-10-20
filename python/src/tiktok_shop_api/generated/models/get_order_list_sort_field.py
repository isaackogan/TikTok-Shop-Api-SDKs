from enum import StrEnum


class GetOrderListSortField(StrEnum):
    CREATE_TIME = "create_time"
    UPDATE_TIME = "update_time"

    def __str__(self) -> str:
        return str(self.value)
