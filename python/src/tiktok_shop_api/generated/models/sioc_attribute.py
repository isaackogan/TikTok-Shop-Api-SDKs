from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sioc_file import SiocFile


T = TypeVar("T", bound="SiocAttribute")


@_attrs_define
class SiocAttribute:
    """
    Attributes:
        sioc_files (list[SiocFile] | Unset): Sioc files
    """

    sioc_files: list[SiocFile] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sioc_files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sioc_files, Unset):
            sioc_files = []
            for sioc_files_item_data in self.sioc_files:
                sioc_files_item = sioc_files_item_data.to_dict()
                sioc_files.append(sioc_files_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sioc_files is not UNSET:
            field_dict["sioc_files"] = sioc_files

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sioc_file import SiocFile  # noqa: PLC0415

        d = dict(src_dict)
        _sioc_files = d.pop("sioc_files", UNSET)
        sioc_files: list[SiocFile] | Unset = UNSET
        if _sioc_files is not UNSET:
            sioc_files = []
            for sioc_files_item_data in _sioc_files:
                sioc_files_item = SiocFile.from_dict(sioc_files_item_data)

                sioc_files.append(sioc_files_item)

        sioc_attribute = cls(
            sioc_files=sioc_files,
        )

        sioc_attribute.additional_properties = d
        return sioc_attribute

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
