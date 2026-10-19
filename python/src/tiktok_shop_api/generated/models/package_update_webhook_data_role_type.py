from enum import StrEnum


class PackageUpdateWebhookDataRoleType(StrEnum):
    ROLE_OPERATOR = "ROLE_OPERATOR"
    ROLE_SELLER = "ROLE_SELLER"
    ROLE_SYSTEM = "ROLE_SYSTEM"
    ROLE_USER = "ROLE_USER"

    def __str__(self) -> str:
        return str(self.value)
