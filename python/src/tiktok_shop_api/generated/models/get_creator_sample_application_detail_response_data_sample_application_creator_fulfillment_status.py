from enum import StrEnum


class GetCreatorSampleApplicationDetailResponseDataSampleApplicationCreatorFulfillmentStatus(StrEnum):
    CANCELLED = "CANCELLED"
    EXEMPTED = "EXEMPTED"
    FAILED = "FAILED"
    ONGOING = "ONGOING"
    OVERDUE = "OVERDUE"
    PENDING = "PENDING"
    REPEATED = "REPEATED"
    SUCCEED = "SUCCEED"
    SUSPEND = "SUSPEND"

    def __str__(self) -> str:
        return str(self.value)
