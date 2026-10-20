from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UploadShoppableVideoFileResponseDataVideoFile")



@_attrs_define
class UploadShoppableVideoFileResponseDataVideoFile:
    """ 
        Attributes:
            id (str | Unset): The id from of the uploaded video file.
            md5 (str | Unset): Upload file md5 checksum
     """

    id: str | Unset = UNSET
    md5: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        md5 = self.md5


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if md5 is not UNSET:
            field_dict["md5"] = md5

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        md5 = d.pop("md5", UNSET)

        upload_shoppable_video_file_response_data_video_file = cls(
            id=id,
            md5=md5,
        )


        upload_shoppable_video_file_response_data_video_file.additional_properties = d
        return upload_shoppable_video_file_response_data_video_file

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
