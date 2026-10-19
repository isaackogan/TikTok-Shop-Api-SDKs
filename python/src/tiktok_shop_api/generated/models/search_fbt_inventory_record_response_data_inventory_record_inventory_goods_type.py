from enum import StrEnum


class SearchFBTInventoryRecordResponseDataInventoryRecordInventoryGoodsType(StrEnum):
    DEFECTIVE = "DEFECTIVE"
    NORMAL = "NORMAL"

    def __str__(self) -> str:
        return str(self.value)
