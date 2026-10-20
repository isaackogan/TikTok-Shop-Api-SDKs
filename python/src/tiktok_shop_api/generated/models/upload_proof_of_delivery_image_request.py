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






T = TypeVar("T", bound="UploadProofOfDeliveryImageRequest")



@_attrs_define
class UploadProofOfDeliveryImageRequest:
    """ 
        Attributes:
            data (File): The image file to upload as binary data in this multipart/form-data field.

                Requirements:
                - Format: `JPG`, `JPEG`, or `PNG`.
                - Resolution: between 100 x 100 and 20,000 x 20,000 pixels.
                - File size: no more than 5 MB.
     """

    data: File
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_tuple()



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "data": data,
        })

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
        data = File(
             payload = BytesIO(d.pop("data"))
        )




        upload_proof_of_delivery_image_request = cls(
            data=data,
        )


        upload_proof_of_delivery_image_request.additional_properties = d
        return upload_proof_of_delivery_image_request

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
