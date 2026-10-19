from enum import StrEnum


class GenderDistributionGender(StrEnum):
    FEMALE = "FEMALE"
    MALE = "MALE"

    def __str__(self) -> str:
        return str(self.value)
