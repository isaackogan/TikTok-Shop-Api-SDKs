from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_image_translation_tasks_request_image_target_languages_item import (
    CreateImageTranslationTasksRequestImageTargetLanguagesItem,
)

T = TypeVar("T", bound="CreateImageTranslationTasksRequestImage")


@_attrs_define
class CreateImageTranslationTasksRequestImage:
    """
    Attributes:
        image_uri (str): The URI of the image, retrieved from the [Upload Product Image
            API](https://partner.tiktokshop.com/docv2/page/6509df95defece02be598a22)

            **Recommendation**: Specify up to 5 images to avoid exceeding the task limit per call.
        target_languages (list[CreateImageTranslationTasksRequestImageTargetLanguagesItem]): The target languages to
            translate the image into. You can specify multiple target languages for each image.
            Possible values:
            - `cs-CZ`
            - `da-DK`
            - `de-AT`
            - `de-BE`
            - `de-DE`
            - `el-GR`
            - `en-GB`
            - `en-IE`
            - `es-ES`
            - `fi-FI`
            - `fr-FR`
            - `fr-BE`
            - `hu-HU`
            - `it-IT`
            - `nl-NL`
            - `nl-BE`
            - `pl-PL`
            - `pt-PT`
            - `sv-SE`
            Recommendation: Specify up to 20 languages to avoid exceeding the task limit per call.
    """

    image_uri: str
    target_languages: list[CreateImageTranslationTasksRequestImageTargetLanguagesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image_uri = self.image_uri

        target_languages = []
        for target_languages_item_data in self.target_languages:
            target_languages_item = target_languages_item_data.value
            target_languages.append(target_languages_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "image_uri": image_uri,
                "target_languages": target_languages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        image_uri = d.pop("image_uri")

        target_languages = []
        _target_languages = d.pop("target_languages")
        for target_languages_item_data in _target_languages:
            target_languages_item = CreateImageTranslationTasksRequestImageTargetLanguagesItem(
                target_languages_item_data
            )

            target_languages.append(target_languages_item)

        create_image_translation_tasks_request_image = cls(
            image_uri=image_uri,
            target_languages=target_languages,
        )

        create_image_translation_tasks_request_image.additional_properties = d
        return create_image_translation_tasks_request_image

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
