from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CreateImageTranslationTasksResponseDataTranslationTask")



@_attrs_define
class CreateImageTranslationTasksResponseDataTranslationTask:
    """ 
        Attributes:
            image_uri (str | Unset): The URI of the image to translate.
            target_language (str | Unset): The target language for this translation task. This value corresponds to one of
                the `target_languages` submitted for the task's `image_uri`.
            id (str | Unset): The ID to identify the image translation task.
                Pass this ID to the [Get Image Translation Tasks API](684f8b2d535a9d048f234564) to retrieve the task status and
                the translated image URIs.
     """

    image_uri: str | Unset = UNSET
    target_language: str | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        image_uri = self.image_uri

        target_language = self.target_language

        id = self.id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if image_uri is not UNSET:
            field_dict["image_uri"] = image_uri
        if target_language is not UNSET:
            field_dict["target_language"] = target_language
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        image_uri = d.pop("image_uri", UNSET)

        target_language = d.pop("target_language", UNSET)

        id = d.pop("id", UNSET)

        create_image_translation_tasks_response_data_translation_task = cls(
            image_uri=image_uri,
            target_language=target_language,
            id=id,
        )


        create_image_translation_tasks_response_data_translation_task.additional_properties = d
        return create_image_translation_tasks_response_data_translation_task

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
