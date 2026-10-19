from enum import StrEnum


class GetCreatorConversationMessagesResponseDataMessageMessageBodyType(StrEnum):
    CRM_TEXT_WITH_IMAGE_CARD = "CRM_TEXT_WITH_IMAGE_CARD"
    CRM_TEXT_WITH_PRODUCTS_CARD = "CRM_TEXT_WITH_PRODUCTS_CARD"
    EMOTICONS = "EMOTICONS"
    FREE_SAMPLE_CARD = "FREE_SAMPLE_CARD"
    IMAGE = "IMAGE"
    NOTIFICATION = "NOTIFICATION"
    PRODUCT_CARD = "PRODUCT_CARD"
    SYSTEM = "SYSTEM"
    TARGET_COLLABORATION_CARD = "TARGET_COLLABORATION_CARD"
    TEXT = "TEXT"

    def __str__(self) -> str:
        return str(self.value)
