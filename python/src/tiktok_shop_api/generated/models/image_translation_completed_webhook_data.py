from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_translation_completed_webhook_data_translation_task import (
        ImageTranslationCompletedWebhookDataTranslationTask,
    )


T = TypeVar("T", bound="ImageTranslationCompletedWebhookData")


@_attrs_define
class ImageTranslationCompletedWebhookData:
    """
    Attributes:
        translation_task (ImageTranslationCompletedWebhookDataTranslationTask | Unset):
    """

    translation_task: ImageTranslationCompletedWebhookDataTranslationTask | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        translation_task: dict[str, Any] | Unset = UNSET
        if not isinstance(self.translation_task, Unset):
            translation_task = self.translation_task.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if translation_task is not UNSET:
            field_dict["translation_task"] = translation_task

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_translation_completed_webhook_data_translation_task import (
            ImageTranslationCompletedWebhookDataTranslationTask,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _translation_task = d.pop("translation_task", UNSET)
        translation_task: ImageTranslationCompletedWebhookDataTranslationTask | Unset
        if isinstance(_translation_task, Unset):
            translation_task = UNSET
        else:
            translation_task = ImageTranslationCompletedWebhookDataTranslationTask.from_dict(_translation_task)

        image_translation_completed_webhook_data = cls(
            translation_task=translation_task,
        )

        image_translation_completed_webhook_data.additional_properties = d
        return image_translation_completed_webhook_data

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
