from enum import StrEnum


class PublishResultStatus(StrEnum):
    DRAFT = "DRAFT"
    FAILED = "FAILED"
    SUCCESS = "SUCCESS"

    def __str__(self) -> str:
        return str(self.value)
