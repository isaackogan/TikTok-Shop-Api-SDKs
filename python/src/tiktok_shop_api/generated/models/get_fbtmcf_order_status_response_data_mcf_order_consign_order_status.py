from enum import StrEnum


class GetFBTMCFOrderStatusResponseDataMcfOrderConsignOrderStatus(StrEnum):
    ABNORMAL = "ABNORMAL"
    CLOSED = "CLOSED"
    COMPLETED = "COMPLETED"
    DAMAGE = "DAMAGE"
    HANDLE_BY_WAREHOUSE = "HANDLE_BY_WAREHOUSE"
    HANDOVER = "HANDOVER"
    LOST = "LOST"
    PENDING = "PENDING"
    RETURNED = "RETURNED"
    SCRAP = "SCRAP"
    SHIPPED = "SHIPPED"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
