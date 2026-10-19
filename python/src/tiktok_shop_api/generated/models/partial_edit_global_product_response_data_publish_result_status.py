from enum import StrEnum


class PartialEditGlobalProductResponseDataPublishResultStatus(StrEnum):
    FAILED = "FAILED"
    SUCCESS = "SUCCESS"

    def __str__(self) -> str:
        return str(self.value)
