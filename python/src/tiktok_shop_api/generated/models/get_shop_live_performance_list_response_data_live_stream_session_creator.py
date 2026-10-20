from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetShopLIVEPerformanceListResponseDataLiveStreamSessionCreator")


@_attrs_define
class GetShopLIVEPerformanceListResponseDataLiveStreamSessionCreator:
    """
    Attributes:
        author_type (str | Unset): The creator account type.
        creator_country (str | Unset): The creator's country or region code.
        nick_name (str | Unset): The creator's nickname.
        open_id (str | Unset): The creator's Open ID.
        user_name (str | Unset): The creator's username.
    """

    author_type: str | Unset = UNSET
    creator_country: str | Unset = UNSET
    nick_name: str | Unset = UNSET
    open_id: str | Unset = UNSET
    user_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        author_type = self.author_type

        creator_country = self.creator_country

        nick_name = self.nick_name

        open_id = self.open_id

        user_name = self.user_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if author_type is not UNSET:
            field_dict["author_type"] = author_type
        if creator_country is not UNSET:
            field_dict["creator_country"] = creator_country
        if nick_name is not UNSET:
            field_dict["nick_name"] = nick_name
        if open_id is not UNSET:
            field_dict["open_id"] = open_id
        if user_name is not UNSET:
            field_dict["user_name"] = user_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        author_type = d.pop("author_type", UNSET)

        creator_country = d.pop("creator_country", UNSET)

        nick_name = d.pop("nick_name", UNSET)

        open_id = d.pop("open_id", UNSET)

        user_name = d.pop("user_name", UNSET)

        get_shop_live_performance_list_response_data_live_stream_session_creator = cls(
            author_type=author_type,
            creator_country=creator_country,
            nick_name=nick_name,
            open_id=open_id,
            user_name=user_name,
        )

        get_shop_live_performance_list_response_data_live_stream_session_creator.additional_properties = d
        return get_shop_live_performance_list_response_data_live_stream_session_creator

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
