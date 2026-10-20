from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="UploadFileInitRequest")



@_attrs_define
class UploadFileInitRequest:
    """ 
        Attributes:
            file_name (str): The name of the file to upload for this upload session.
            file_type (str): The type of file to upload. Currently, only video is supported.
            file_size (int): file size, bytes
            total_chunk_count (int): The total number of upload chunks. Must be greater than 0. For files of 5 MiB
                (5,242,880 bytes) or less, set this value to 1.
            target_path (str): After the video is uploaded, use this interface to bind the video resource to the specific
                material
     """

    file_name: str
    file_type: str
    file_size: int
    total_chunk_count: int
    target_path: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        file_name = self.file_name

        file_type = self.file_type

        file_size = self.file_size

        total_chunk_count = self.total_chunk_count

        target_path = self.target_path


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "file_name": file_name,
            "file_type": file_type,
            "file_size": file_size,
            "total_chunk_count": total_chunk_count,
            "target_path": target_path,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_name = d.pop("file_name")

        file_type = d.pop("file_type")

        file_size = d.pop("file_size")

        total_chunk_count = d.pop("total_chunk_count")

        target_path = d.pop("target_path")

        upload_file_init_request = cls(
            file_name=file_name,
            file_type=file_type,
            file_size=file_size,
            total_chunk_count=total_chunk_count,
            target_path=target_path,
        )


        upload_file_init_request.additional_properties = d
        return upload_file_init_request

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
