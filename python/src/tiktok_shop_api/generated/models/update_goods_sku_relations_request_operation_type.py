from enum import StrEnum


class UpdateGoodsSKURelationsRequestOperationType(StrEnum):
    BIND = "BIND"
    UN_BIND = "UN_BIND"

    def __str__(self) -> str:
        return str(self.value)
