from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetOffSitePerformanceDetailsResponseDataContentCreator")



@_attrs_define
class GetOffSitePerformanceDetailsResponseDataContentCreator:
    """ 
        Attributes:
            avatar_url (str | Unset): Avatar image URL of the video's creator, when available.
            id (str | Unset): TikTok user ID of the video's creator, expressed as a string.
            name (str | Unset): Display name of the video's creator, when available.
     """

    avatar_url: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        avatar_url = self.avatar_url

        id = self.id

        name = self.name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avatar_url = d.pop("avatar_url", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        get_off_site_performance_details_response_data_content_creator = cls(
            avatar_url=avatar_url,
            id=id,
            name=name,
        )


        get_off_site_performance_details_response_data_content_creator.additional_properties = d
        return get_off_site_performance_details_response_data_content_creator

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
