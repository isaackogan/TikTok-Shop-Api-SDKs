from enum import StrEnum


class OptimizeImagesResponseDataImageOptimizeStatus(StrEnum):
    IGNORE = "IGNORE"
    PROCESSING = "PROCESSING"
    SUCCESS = "SUCCESS"

    def __str__(self) -> str:
        return str(self.value)
