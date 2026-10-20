from enum import StrEnum

class SearchTargetCollaborationsRequestCreatorAcceptStatus(StrEnum):
    ACCEPT = "ACCEPT"
    ALL = "ALL"

    def __str__(self) -> str:
        return str(self.value)
