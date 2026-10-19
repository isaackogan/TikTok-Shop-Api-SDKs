from enum import StrEnum


class GetConversationListConversationStatus(StrEnum):
    ALL = "ALL"
    ARCHIVED = "ARCHIVED"
    STARRED = "STARRED"
    UNREAD = "UNREAD"
    UNREPLIED = "UNREPLIED"

    def __str__(self) -> str:
        return str(self.value)
