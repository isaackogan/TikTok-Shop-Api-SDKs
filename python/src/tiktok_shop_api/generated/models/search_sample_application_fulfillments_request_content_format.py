from enum import StrEnum


class SearchSampleApplicationFulfillmentsRequestContentFormat(StrEnum):
    LIVE = "LIVE"
    VIDEO = "VIDEO"

    def __str__(self) -> str:
        return str(self.value)
