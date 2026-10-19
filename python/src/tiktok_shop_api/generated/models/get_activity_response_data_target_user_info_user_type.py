from enum import StrEnum


class GetActivityResponseDataTargetUserInfoUserType(StrEnum):
    ALL_USER = "ALL_USER"
    SHOP_ABANDONED_CHECKOUTS_CUSTOMER = "SHOP_ABANDONED_CHECKOUTS_CUSTOMER"
    SHOP_EXISTING_CUSTOMER = "SHOP_EXISTING_CUSTOMER"
    SHOP_NEW_CUSTOMER = "SHOP_NEW_CUSTOMER"
    SHOP_REPEAT_CUSTOMER = "SHOP_REPEAT_CUSTOMER"

    def __str__(self) -> str:
        return str(self.value)
