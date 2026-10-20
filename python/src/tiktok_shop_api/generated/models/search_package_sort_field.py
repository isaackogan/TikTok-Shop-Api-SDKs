from enum import StrEnum

class SearchPackageSortField(StrEnum):
    CREATE_TIME = "create_time"
    ORDER_PAY_TIME = "order_pay_time"
    UPDATE_TIME = "update_time"

    def __str__(self) -> str:
        return str(self.value)
