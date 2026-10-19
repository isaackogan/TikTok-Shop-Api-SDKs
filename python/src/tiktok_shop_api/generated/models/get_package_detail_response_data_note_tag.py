from enum import StrEnum


class GetPackageDetailResponseDataNoteTag(StrEnum):
    BUYER_NOTED = "BUYER_NOTED"
    BUYER_UNNOTED = "BUYER_UNNOTED"

    def __str__(self) -> str:
        return str(self.value)
