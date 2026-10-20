from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="PostShoppablePhotosRequestPhotosInfo")



@_attrs_define
class PostShoppablePhotosRequestPhotosInfo:
    """ 
        Attributes:
            photo_file_uris (str): Photo file uris, not a file upload. Use [Upload Shoppable Photo File] to upload the image
                and obtain the photo_file_uri, then pass that URI in this field
     """

    photo_file_uris: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        photo_file_uris = self.photo_file_uris


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "photo_file_uris": photo_file_uris,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        photo_file_uris = d.pop("photo_file_uris")

        post_shoppable_photos_request_photos_info = cls(
            photo_file_uris=photo_file_uris,
        )


        post_shoppable_photos_request_photos_info.additional_properties = d
        return post_shoppable_photos_request_photos_info

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
