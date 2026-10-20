from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ImageTranslationCompletedWebhookDataTranslationTaskTranslatedImage")



@_attrs_define
class ImageTranslationCompletedWebhookDataTranslationTaskTranslatedImage:
    """ 
        Attributes:
            uri (str | Unset): The URI of the translated image.
            url (str | Unset): The URL of the translated image.
     """

    uri: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        uri = self.uri

        url = self.url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if uri is not UNSET:
            field_dict["uri"] = uri
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uri = d.pop("uri", UNSET)

        url = d.pop("url", UNSET)

        image_translation_completed_webhook_data_translation_task_translated_image = cls(
            uri=uri,
            url=url,
        )


        image_translation_completed_webhook_data_translation_task_translated_image.additional_properties = d
        return image_translation_completed_webhook_data_translation_task_translated_image

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
