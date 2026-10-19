from enum import StrEnum


class GetShoppableVideoStatusResponseDataVideoPostStatus(StrEnum):
    FAIL = "FAIL"
    PROCESSING = "PROCESSING"
    SUCCESS = "SUCCESS"

    def __str__(self) -> str:
        return str(self.value)
