from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UploadFileInitResponseData")



@_attrs_define
class UploadFileInitResponseData:
    """ 
        Attributes:
            upload_url (str | Unset): The URL provided by platform where the file can be uploaded.
            upload_token (str | Unset): The upload token used when uploading the file to the returned upload URL.
     """

    upload_url: str | Unset = UNSET
    upload_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        upload_url = self.upload_url

        upload_token = self.upload_token


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if upload_url is not UNSET:
            field_dict["upload_url"] = upload_url
        if upload_token is not UNSET:
            field_dict["upload_token"] = upload_token

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        upload_url = d.pop("upload_url", UNSET)

        upload_token = d.pop("upload_token", UNSET)

        upload_file_init_response_data = cls(
            upload_url=upload_url,
            upload_token=upload_token,
        )


        upload_file_init_response_data.additional_properties = d
        return upload_file_init_response_data

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
