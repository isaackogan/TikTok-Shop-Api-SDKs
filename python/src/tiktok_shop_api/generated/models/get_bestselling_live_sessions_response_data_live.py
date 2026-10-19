from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetBestsellingLIVESessionsResponseDataLive")


@_attrs_define
class GetBestsellingLIVESessionsResponseDataLive:
    """
    Attributes:
        rank (int | Unset): GMV rank of the LIVE session
        gmv_range (str | Unset): GMV range of the LIVE session.
        id (str | Unset): LIVE session id
        title (str | Unset): LIVE session  title
        start_time (int | Unset): Start time of the LIVE session as a Unix timestamp in seconds (UTC+00:00).
        duration (int | Unset): LIVE session duration, in seconds.
        creator_name (str | Unset): The creator’s unique username used for system identification.
        open_id (str | Unset): The creator’s unique ID, uniquely identifying the creator in the system.
        creator_nick_name (str | Unset): The creator’s display nickname, visible externally.
    """

    rank: int | Unset = UNSET
    gmv_range: str | Unset = UNSET
    id: str | Unset = UNSET
    title: str | Unset = UNSET
    start_time: int | Unset = UNSET
    duration: int | Unset = UNSET
    creator_name: str | Unset = UNSET
    open_id: str | Unset = UNSET
    creator_nick_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rank = self.rank

        gmv_range = self.gmv_range

        id = self.id

        title = self.title

        start_time = self.start_time

        duration = self.duration

        creator_name = self.creator_name

        open_id = self.open_id

        creator_nick_name = self.creator_nick_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rank is not UNSET:
            field_dict["rank"] = rank
        if gmv_range is not UNSET:
            field_dict["gmv_range"] = gmv_range
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if duration is not UNSET:
            field_dict["duration"] = duration
        if creator_name is not UNSET:
            field_dict["creator_name"] = creator_name
        if open_id is not UNSET:
            field_dict["open_id"] = open_id
        if creator_nick_name is not UNSET:
            field_dict["creator_nick_name"] = creator_nick_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rank = d.pop("rank", UNSET)

        gmv_range = d.pop("gmv_range", UNSET)

        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        start_time = d.pop("start_time", UNSET)

        duration = d.pop("duration", UNSET)

        creator_name = d.pop("creator_name", UNSET)

        open_id = d.pop("open_id", UNSET)

        creator_nick_name = d.pop("creator_nick_name", UNSET)

        get_bestselling_live_sessions_response_data_live = cls(
            rank=rank,
            gmv_range=gmv_range,
            id=id,
            title=title,
            start_time=start_time,
            duration=duration,
            creator_name=creator_name,
            open_id=open_id,
            creator_nick_name=creator_nick_name,
        )

        get_bestselling_live_sessions_response_data_live.additional_properties = d
        return get_bestselling_live_sessions_response_data_live

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
