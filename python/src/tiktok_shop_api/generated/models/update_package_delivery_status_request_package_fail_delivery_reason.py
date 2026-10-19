from enum import StrEnum


class UpdatePackageDeliveryStatusRequestPackageFailDeliveryReason(StrEnum):
    BUYER_REFUSED = "BUYER_REFUSED"
    DELAY_DELIVERY = "DELAY_DELIVERY"
    FORCE_MAJEURE = "FORCE_MAJEURE"
    INVALID_ADDRESS = "INVALID_ADDRESS"
    OTHER = "OTHER"
    PACKAGE_DAMAGE = "PACKAGE_DAMAGE"
    PACKAGE_LOST = "PACKAGE_LOST"
    UNABLE_CONTACT_BUYER = "UNABLE_CONTACT_BUYER"
    UNABLE_RECEIVE = "UNABLE_RECEIVE"

    def __str__(self) -> str:
        return str(self.value)
