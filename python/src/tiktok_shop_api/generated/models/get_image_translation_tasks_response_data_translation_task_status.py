from enum import StrEnum


class GetImageTranslationTasksResponseDataTranslationTaskStatus(StrEnum):
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    PROCESSING = "PROCESSING"

    def __str__(self) -> str:
        return str(self.value)
