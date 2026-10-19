from enum import StrEnum


class NewMessageListenerWebhookDataMsgType(StrEnum):
    FREE_SAMPLE_CARD = "FREE_SAMPLE_CARD"
    PRODUCT_CARD = "PRODUCT_CARD"
    TARGET_COLLABORATION_CARD = "TARGET_COLLABORATION_CARD"
    TEXT = "TEXT"

    def __str__(self) -> str:
        return str(self.value)
