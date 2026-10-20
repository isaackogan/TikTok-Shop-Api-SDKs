from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.image_translation_completed_webhook_data_translation_task_original_image import ImageTranslationCompletedWebhookDataTranslationTaskOriginalImage
  from ..models.image_translation_completed_webhook_data_translation_task_translated_image import ImageTranslationCompletedWebhookDataTranslationTaskTranslatedImage





T = TypeVar("T", bound="ImageTranslationCompletedWebhookDataTranslationTask")



@_attrs_define
class ImageTranslationCompletedWebhookDataTranslationTask:
    """ 
        Attributes:
            id (str | Unset): The ID to identify the image translation task.
            status (str | Unset): The translation status.
                 Possible values:
                 - PROCESSING: Translation is underway and has not yet completed.
                 - COMPLETED: Translation has completed and results are ready.
                 - FAILED: Translation did not complete due to an error.
            fail_reason (str | Unset): The reason why the translation task failed.
            target_language (str | Unset): The target language to translate the image into.
                 Possible values:
                 - de-DE
                 - en-IE
                 - es-ES
                 - fr-FR
                 - it-IT
            original_image (ImageTranslationCompletedWebhookDataTranslationTaskOriginalImage | Unset):
            translated_image (ImageTranslationCompletedWebhookDataTranslationTaskTranslatedImage | Unset):
     """

    id: str | Unset = UNSET
    status: str | Unset = UNSET
    fail_reason: str | Unset = UNSET
    target_language: str | Unset = UNSET
    original_image: ImageTranslationCompletedWebhookDataTranslationTaskOriginalImage | Unset = UNSET
    translated_image: ImageTranslationCompletedWebhookDataTranslationTaskTranslatedImage | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.image_translation_completed_webhook_data_translation_task_original_image import ImageTranslationCompletedWebhookDataTranslationTaskOriginalImage # noqa: PLC0415
        from ..models.image_translation_completed_webhook_data_translation_task_translated_image import ImageTranslationCompletedWebhookDataTranslationTaskTranslatedImage # noqa: PLC0415
        id = self.id

        status = self.status

        fail_reason = self.fail_reason

        target_language = self.target_language

        original_image: dict[str, Any] | Unset = UNSET
        if not isinstance(self.original_image, Unset):
            original_image = self.original_image.to_dict()

        translated_image: dict[str, Any] | Unset = UNSET
        if not isinstance(self.translated_image, Unset):
            translated_image = self.translated_image.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if fail_reason is not UNSET:
            field_dict["fail_reason"] = fail_reason
        if target_language is not UNSET:
            field_dict["target_language"] = target_language
        if original_image is not UNSET:
            field_dict["original_image"] = original_image
        if translated_image is not UNSET:
            field_dict["translated_image"] = translated_image

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_translation_completed_webhook_data_translation_task_original_image import ImageTranslationCompletedWebhookDataTranslationTaskOriginalImage # noqa: PLC0415
        from ..models.image_translation_completed_webhook_data_translation_task_translated_image import ImageTranslationCompletedWebhookDataTranslationTaskTranslatedImage # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        status = d.pop("status", UNSET)

        fail_reason = d.pop("fail_reason", UNSET)

        target_language = d.pop("target_language", UNSET)

        _original_image = d.pop("original_image", UNSET)
        original_image: ImageTranslationCompletedWebhookDataTranslationTaskOriginalImage | Unset
        if isinstance(_original_image,  Unset):
            original_image = UNSET
        else:
            original_image = ImageTranslationCompletedWebhookDataTranslationTaskOriginalImage.from_dict(_original_image)




        _translated_image = d.pop("translated_image", UNSET)
        translated_image: ImageTranslationCompletedWebhookDataTranslationTaskTranslatedImage | Unset
        if isinstance(_translated_image,  Unset):
            translated_image = UNSET
        else:
            translated_image = ImageTranslationCompletedWebhookDataTranslationTaskTranslatedImage.from_dict(_translated_image)




        image_translation_completed_webhook_data_translation_task = cls(
            id=id,
            status=status,
            fail_reason=fail_reason,
            target_language=target_language,
            original_image=original_image,
            translated_image=translated_image,
        )


        image_translation_completed_webhook_data_translation_task.additional_properties = d
        return image_translation_completed_webhook_data_translation_task

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
