from enum import StrEnum


class GetInboundMethodDetailResponseDataPlacementTaskStatus(StrEnum):
    EXECUTING = "Executing"
    FAILED = "Failed"
    SUCCEED = "Succeed"

    def __str__(self) -> str:
        return str(self.value)
