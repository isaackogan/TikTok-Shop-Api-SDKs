from enum import StrEnum


class GetBestsellingCreatorsAuthorType(StrEnum):
    AFFILIATE = "AFFILIATE"
    ALL = "ALL"
    CHANNEL = "CHANNEL"
    OFFICIAL = "OFFICIAL"

    def __str__(self) -> str:
        return str(self.value)
