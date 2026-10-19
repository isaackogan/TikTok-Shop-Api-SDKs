from enum import StrEnum


class GetReturnRecordsResponseDataRecordRole(StrEnum):
    BUYER = "BUYER"
    OPERATOR = "OPERATOR"
    SELLER = "SELLER"
    SYSTEM = "SYSTEM"

    def __str__(self) -> str:
        return str(self.value)
