from enum import StrEnum

class ReviewASampleApplicationRequestReviewResult(StrEnum):
    APPROVE = "APPROVE"
    REJECT = "REJECT"

    def __str__(self) -> str:
        return str(self.value)
