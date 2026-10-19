from enum import StrEnum


class GetEngagementFeaturePermissionsResponseDataFeatureName(StrEnum):
    CUSTOM_MSG = "CUSTOM_MSG"
    FUNDAMENTAL = "FUNDAMENTAL"

    def __str__(self) -> str:
        return str(self.value)
