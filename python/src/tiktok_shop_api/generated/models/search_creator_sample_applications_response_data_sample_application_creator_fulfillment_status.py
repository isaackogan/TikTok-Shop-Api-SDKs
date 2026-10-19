from enum import StrEnum


class SearchCreatorSampleApplicationsResponseDataSampleApplicationCreatorFulfillmentStatus(StrEnum):
    CANCELLED = "CANCELLED"
    EXEMPTED = "EXEMPTED"
    FAILED = "FAILED"
    ONGOING = "ONGOING"
    OVERDUE = "OVERDUE"
    PENDING = "PENDING"
    SUCCEED = "SUCCEED"
    SUSPEND = "SUSPEND"

    def __str__(self) -> str:
        return str(self.value)
