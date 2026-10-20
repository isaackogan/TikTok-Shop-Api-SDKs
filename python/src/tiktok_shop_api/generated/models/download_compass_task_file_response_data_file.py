from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="DownloadCompassTaskFileResponseDataFile")



@_attrs_define
class DownloadCompassTaskFileResponseDataFile:
    """ 
        Attributes:
            base64 (str | Unset): The Base64-encoded contents of the export result file.
     """

    base64: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        base64 = self.base64


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if base64 is not UNSET:
            field_dict["base64"] = base64

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        base64 = d.pop("base64", UNSET)

        download_compass_task_file_response_data_file = cls(
            base64=base64,
        )


        download_compass_task_file_response_data_file.additional_properties = d
        return download_compass_task_file_response_data_file

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
