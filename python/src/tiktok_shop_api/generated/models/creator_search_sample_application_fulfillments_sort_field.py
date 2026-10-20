from enum import StrEnum

class CreatorSearchSampleApplicationFulfillmentsSortField(StrEnum):
    CREATE_TIME = "create_time"
    EXPIRED_TIME = "expired_time"

    def __str__(self) -> str:
        return str(self.value)
