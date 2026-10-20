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






T = TypeVar("T", bound="UploadProofOfDeliveryFileRequest")



@_attrs_define
class UploadProofOfDeliveryFileRequest:
    """ 
        Attributes:
            data (File): PDF file data to be uploaded to TikTok Shop.
                Prerequisites：
                - Only `PDF` file format is supported.
                - Original file size must not exceed 10MB.
            name (str): The name of the uploaded file. The file name must include the file type.
     """

    data: File
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_tuple()


        name = self.name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "data": data,
            "name": name,
        })

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
        data = File(
             payload = BytesIO(d.pop("data"))
        )




        name = d.pop("name")

        upload_proof_of_delivery_file_request = cls(
            data=data,
            name=name,
        )


        upload_proof_of_delivery_file_request.additional_properties = d
        return upload_proof_of_delivery_file_request

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
