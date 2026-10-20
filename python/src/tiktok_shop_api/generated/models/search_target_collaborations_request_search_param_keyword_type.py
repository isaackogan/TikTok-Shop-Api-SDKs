from enum import StrEnum

class SearchTargetCollaborationsRequestSearchParamKeywordType(StrEnum):
    PRODUCT_ID = "PRODUCT_ID"
    PRODUCT_NAME = "PRODUCT_NAME"
    TARGET_COLLABORATION_ID = "TARGET_COLLABORATION_ID"
    TARGET_COLLABORATION_NAME = "TARGET_COLLABORATION_NAME"

    def __str__(self) -> str:
        return str(self.value)
