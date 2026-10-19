from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import File

T = TypeVar("T", bound="UploadShoppablePhotoFileRequest")


@_attrs_define
class UploadShoppablePhotoFileRequest:
    """
    Attributes:
        data (File): The local image file to upload.

            Requirements:
            - Supported formats: JPG, JPEG, PNG, WEBP, HEIC, BMP
            - Zero-byte files are rejected.
            - Maximum file size: 10 MiB (10,485,760 bytes).
            - Aspect ratio: 9:16 to 16:9
    """

    data: File
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_tuple()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("data", self.data.to_tuple()))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data = File(payload=BytesIO(d.pop("data")))

        upload_shoppable_photo_file_request = cls(
            data=data,
        )

        upload_shoppable_photo_file_request.additional_properties = d
        return upload_shoppable_photo_file_request

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
