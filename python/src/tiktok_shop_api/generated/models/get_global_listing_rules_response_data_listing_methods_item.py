from enum import StrEnum


class GetGlobalListingRulesResponseDataListingMethodsItem(StrEnum):
    GLOBAL_PUBLISHING = "GLOBAL_PUBLISHING"
    LOCAL_REPLICATION = "LOCAL_REPLICATION"

    def __str__(self) -> str:
        return str(self.value)
