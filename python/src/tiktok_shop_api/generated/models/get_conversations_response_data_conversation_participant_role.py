from enum import StrEnum


class GetConversationsResponseDataConversationParticipantRole(StrEnum):
    BUYER = "BUYER"
    CUSTOMER_SERVICE = "CUSTOMER_SERVICE"
    SHOP = "SHOP"

    def __str__(self) -> str:
        return str(self.value)
