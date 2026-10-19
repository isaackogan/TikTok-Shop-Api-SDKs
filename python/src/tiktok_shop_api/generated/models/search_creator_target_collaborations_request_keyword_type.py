from enum import StrEnum


class SearchCreatorTargetCollaborationsRequestKeywordType(StrEnum):
    TARGET_COLLABORATIONS_ID = "TARGET_COLLABORATIONS_ID"
    TARGET_COLLABORATIONS_NAME = "TARGET_COLLABORATIONS_NAME"

    def __str__(self) -> str:
        return str(self.value)
