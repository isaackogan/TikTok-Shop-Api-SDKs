from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field
import json
from .. import types

from ..types import UNSET, Unset

from ..types import File, FileTypes
from io import BytesIO






T = TypeVar("T", bound="UploadSellerImageRequest")



@_attrs_define
class UploadSellerImageRequest:
    """ 
        Attributes:
            image_data (File): The local image file to upload to TOS.

                Requirements:
                - Supported formats: JPG, JPEG, PNG, WEBP, HEIC, BMP.
                - Zero-byte files are rejected.
                - Maximum file size: 10 MiB (10,485,760 bytes).
     """

    image_data: File
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        image_data = self.image_data.to_tuple()



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "image_data": image_data,
        })

        return field_dict


    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("image_data", self.image_data.to_tuple()))




        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))



        return files


    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        image_data = File(
             payload = BytesIO(d.pop("image_data"))
        )




        upload_seller_image_request = cls(
            image_data=image_data,
        )


        upload_seller_image_request.additional_properties = d
        return upload_seller_image_request

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
