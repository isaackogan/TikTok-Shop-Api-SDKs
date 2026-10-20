from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetCreatorProfileResponseDataAvatar")



@_attrs_define
class GetCreatorProfileResponseDataAvatar:
    """ 
        Attributes:
            width (int | Unset): The avatar image width in pixels.
            height (int | Unset): The avatar image height in pixels.
            url (str | Unset): The URL for the TikTok creator's avatar image file.
     """

    width: int | Unset = UNSET
    height: int | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        width = self.width

        height = self.height

        url = self.url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        url = d.pop("url", UNSET)

        get_creator_profile_response_data_avatar = cls(
            width=width,
            height=height,
            url=url,
        )


        get_creator_profile_response_data_avatar.additional_properties = d
        return get_creator_profile_response_data_avatar

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
