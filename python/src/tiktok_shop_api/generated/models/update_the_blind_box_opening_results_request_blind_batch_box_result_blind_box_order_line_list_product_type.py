from enum import StrEnum


class UpdateTheBlindBoxOpeningResultsRequestBlindBatchBoxResultBlindBoxOrderLineListProductType(StrEnum):
    GIFT = "GIFT"
    NORMAL = "NORMAL"

    def __str__(self) -> str:
        return str(self.value)
