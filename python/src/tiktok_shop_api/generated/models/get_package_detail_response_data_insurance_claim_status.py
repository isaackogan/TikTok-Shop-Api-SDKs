from enum import StrEnum


class GetPackageDetailResponseDataInsuranceClaimStatus(StrEnum):
    APPROVED = "APPROVED"
    CLAIM_PENDING = "CLAIM_PENDING"
    DECLINED = "DECLINED"
    NOT_STARTED = "NOT_STARTED"

    def __str__(self) -> str:
        return str(self.value)
