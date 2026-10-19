from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SiocFile")


@_attrs_define
class SiocFile:
    """
    Attributes:
        sioc_certification_url (str | Unset): sico attachment url
        sioc_file_type (str | Unset): sioc attachment type:
            - PHOTO
            - DOCUMENT
            - DROP_TEST_VIDEO
    """

    sioc_certification_url: str | Unset = UNSET
    sioc_file_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sioc_certification_url = self.sioc_certification_url

        sioc_file_type = self.sioc_file_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sioc_certification_url is not UNSET:
            field_dict["sioc_certification_url"] = sioc_certification_url
        if sioc_file_type is not UNSET:
            field_dict["sioc_file_type"] = sioc_file_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sioc_certification_url = d.pop("sioc_certification_url", UNSET)

        sioc_file_type = d.pop("sioc_file_type", UNSET)

        sioc_file = cls(
            sioc_certification_url=sioc_certification_url,
            sioc_file_type=sioc_file_type,
        )

        sioc_file.additional_properties = d
        return sioc_file

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
