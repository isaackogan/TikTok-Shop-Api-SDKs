from enum import StrEnum

class QueryCreatorPromotionDetailsInTargetCollaborationRequestQueryType(StrEnum):
    PRODUCT_ID = "PRODUCT_ID"
    PRODUCT_NAME = "PRODUCT_NAME"

    def __str__(self) -> str:
        return str(self.value)
