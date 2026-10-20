from enum import StrEnum


class SearchAffiliateOrdersByCreatorRequestTimeType(StrEnum):
    CREATE_TIME = "CREATE_TIME"
    DELIVERY_TIME = "DELIVERY_TIME"
    PAY_TIME = "PAY_TIME"
    SETTLE_TIME = "SETTLE_TIME"

    def __str__(self) -> str:
        return str(self.value)
