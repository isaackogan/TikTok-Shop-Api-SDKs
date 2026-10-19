from enum import StrEnum


class ShoppableContentPostingWebhookDataEventScene(StrEnum):
    VIDEO = "VIDEO"

    def __str__(self) -> str:
        return str(self.value)
