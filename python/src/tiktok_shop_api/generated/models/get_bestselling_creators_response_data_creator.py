from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetBestsellingCreatorsResponseDataCreator")


@_attrs_define
class GetBestsellingCreatorsResponseDataCreator:
    """
    Attributes:
        rank (int | Unset): GMV rank of the creator.
        gmv_range (str | Unset): The creator's GMV range for the selected reporting period, expressed in the currency
            selected by `currency`.
        open_id (str | Unset): Creator's open id, use this open id to identify a creator.
        user_name (str | Unset): The creator's account handle.
        nick_name (str | Unset): The creator's display name.
        followers_count (int | Unset): Number of followers
        likes_count (int | Unset): Number of likes
    """

    rank: int | Unset = UNSET
    gmv_range: str | Unset = UNSET
    open_id: str | Unset = UNSET
    user_name: str | Unset = UNSET
    nick_name: str | Unset = UNSET
    followers_count: int | Unset = UNSET
    likes_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rank = self.rank

        gmv_range = self.gmv_range

        open_id = self.open_id

        user_name = self.user_name

        nick_name = self.nick_name

        followers_count = self.followers_count

        likes_count = self.likes_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rank is not UNSET:
            field_dict["rank"] = rank
        if gmv_range is not UNSET:
            field_dict["gmv_range"] = gmv_range
        if open_id is not UNSET:
            field_dict["open_id"] = open_id
        if user_name is not UNSET:
            field_dict["user_name"] = user_name
        if nick_name is not UNSET:
            field_dict["nick_name"] = nick_name
        if followers_count is not UNSET:
            field_dict["followers_count"] = followers_count
        if likes_count is not UNSET:
            field_dict["likes_count"] = likes_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rank = d.pop("rank", UNSET)

        gmv_range = d.pop("gmv_range", UNSET)

        open_id = d.pop("open_id", UNSET)

        user_name = d.pop("user_name", UNSET)

        nick_name = d.pop("nick_name", UNSET)

        followers_count = d.pop("followers_count", UNSET)

        likes_count = d.pop("likes_count", UNSET)

        get_bestselling_creators_response_data_creator = cls(
            rank=rank,
            gmv_range=gmv_range,
            open_id=open_id,
            user_name=user_name,
            nick_name=nick_name,
            followers_count=followers_count,
            likes_count=likes_count,
        )

        get_bestselling_creators_response_data_creator.additional_properties = d
        return get_bestselling_creators_response_data_creator

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
