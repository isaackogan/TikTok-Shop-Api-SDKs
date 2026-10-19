from enum import StrEnum


class DiagnosisResultQualityTier(StrEnum):
    FAIR = "FAIR"
    GOOD = "GOOD"

    def __str__(self) -> str:
        return str(self.value)
