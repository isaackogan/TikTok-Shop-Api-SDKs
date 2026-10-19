from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UploadShoppablePhotoFileResponseDataPhotoFile")


@_attrs_define
class UploadShoppablePhotoFileResponseDataPhotoFile:
    """
    Attributes:
        photo_uri (str | Unset): In [Post Shoppable Photos], use this photo URI to fill photo_file_uris field
    """

    photo_uri: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        photo_uri = self.photo_uri

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if photo_uri is not UNSET:
            field_dict["photo_uri"] = photo_uri

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        photo_uri = d.pop("photo_uri", UNSET)

        upload_shoppable_photo_file_response_data_photo_file = cls(
            photo_uri=photo_uri,
        )

        upload_shoppable_photo_file_response_data_photo_file.additional_properties = d
        return upload_shoppable_photo_file_response_data_photo_file

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
