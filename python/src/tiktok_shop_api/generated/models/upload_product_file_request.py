from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import File

T = TypeVar("T", bound="UploadProductFileRequest")


@_attrs_define
class UploadProductFileRequest:
    """
    Attributes:
        data (File): The local file to be uploaded.

            **Note**:
            - Supported formats: PDF, MP4, MOV, MKV, WMV, WEBM, AVI, 3GP, FLV, MPEG
            - Zero-byte files are rejected.
            - Max PDF size: 20 MB
            - Max video size: 100 MB
            - Video aspect ratio: 9:16 to 16:9

            **Recommendations for product videos**:
            - Aspect ratio: 1:1
            - Resolution: HD 720p or higher
            - Duration: 20 - 60 seconds
        name (str): The name of the file, including the file extension (e.g. `certification.pdf`)

            **Note**:
            - Do not use additional periods, except the one preceding the file extension.
            - Do not begin the name with symbols.
            - Do not include spaces.
    """

    data: File
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_tuple()

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "name": name,
            }
        )

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("data", self.data.to_tuple()))

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data = File(payload=BytesIO(d.pop("data")))

        name = d.pop("name")

        upload_product_file_request = cls(
            data=data,
            name=name,
        )

        upload_product_file_request.additional_properties = d
        return upload_product_file_request

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
