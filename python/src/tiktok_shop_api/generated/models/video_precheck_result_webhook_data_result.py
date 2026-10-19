from enum import StrEnum


class VideoPrecheckResultWebhookDataResult(StrEnum):
    FAIL = "FAIL"
    PASS = "PASS"

    def __str__(self) -> str:
        return str(self.value)
