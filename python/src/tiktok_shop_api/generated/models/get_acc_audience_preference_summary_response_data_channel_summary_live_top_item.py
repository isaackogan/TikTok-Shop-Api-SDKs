from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.stat import Stat





T = TypeVar("T", bound="GetACCAudiencePreferenceSummaryResponseDataChannelSummaryLiveTopItem")



@_attrs_define
class GetACCAudiencePreferenceSummaryResponseDataChannelSummaryLiveTopItem:
    """ 
        Attributes:
            live_room_type (str | Unset): Livestream room category label.
            live_start_time (datetime.date | Unset): Date when the livestream started, in YYYY-MM-DD format (UTC).
            live_type (str | Unset): Livestream type label.
            replay_url (str | Unset): URL of the livestream replay.
            room_id (str | Unset): ID of the livestream room.
            room_image_url (str | Unset): URL of the livestream cover image.
            room_title (str | Unset): Title of the livestream.
            seller_own_id (str | Unset): ID of the content author.
            seller_own_name (str | Unset): Display name of the content author.
            stats (Stat | Unset):
     """

    live_room_type: str | Unset = UNSET
    live_start_time: datetime.date | Unset = UNSET
    live_type: str | Unset = UNSET
    replay_url: str | Unset = UNSET
    room_id: str | Unset = UNSET
    room_image_url: str | Unset = UNSET
    room_title: str | Unset = UNSET
    seller_own_id: str | Unset = UNSET
    seller_own_name: str | Unset = UNSET
    stats: Stat | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.stat import Stat # noqa: PLC0415
        live_room_type = self.live_room_type

        live_start_time: str | Unset = UNSET
        if not isinstance(self.live_start_time, Unset):
            live_start_time = self.live_start_time.isoformat()

        live_type = self.live_type

        replay_url = self.replay_url

        room_id = self.room_id

        room_image_url = self.room_image_url

        room_title = self.room_title

        seller_own_id = self.seller_own_id

        seller_own_name = self.seller_own_name

        stats: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if live_room_type is not UNSET:
            field_dict["live_room_type"] = live_room_type
        if live_start_time is not UNSET:
            field_dict["live_start_time"] = live_start_time
        if live_type is not UNSET:
            field_dict["live_type"] = live_type
        if replay_url is not UNSET:
            field_dict["replay_url"] = replay_url
        if room_id is not UNSET:
            field_dict["room_id"] = room_id
        if room_image_url is not UNSET:
            field_dict["room_image_url"] = room_image_url
        if room_title is not UNSET:
            field_dict["room_title"] = room_title
        if seller_own_id is not UNSET:
            field_dict["seller_own_id"] = seller_own_id
        if seller_own_name is not UNSET:
            field_dict["seller_own_name"] = seller_own_name
        if stats is not UNSET:
            field_dict["stats"] = stats

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.stat import Stat # noqa: PLC0415
        d = dict(src_dict)
        live_room_type = d.pop("live_room_type", UNSET)

        _live_start_time = d.pop("live_start_time", UNSET)
        live_start_time: datetime.date | Unset
        if isinstance(_live_start_time,  Unset):
            live_start_time = UNSET
        else:
            live_start_time = datetime.date.fromisoformat(_live_start_time)




        live_type = d.pop("live_type", UNSET)

        replay_url = d.pop("replay_url", UNSET)

        room_id = d.pop("room_id", UNSET)

        room_image_url = d.pop("room_image_url", UNSET)

        room_title = d.pop("room_title", UNSET)

        seller_own_id = d.pop("seller_own_id", UNSET)

        seller_own_name = d.pop("seller_own_name", UNSET)

        _stats = d.pop("stats", UNSET)
        stats: Stat | Unset
        if isinstance(_stats,  Unset):
            stats = UNSET
        else:
            stats = Stat.from_dict(_stats)




        get_acc_audience_preference_summary_response_data_channel_summary_live_top_item = cls(
            live_room_type=live_room_type,
            live_start_time=live_start_time,
            live_type=live_type,
            replay_url=replay_url,
            room_id=room_id,
            room_image_url=room_image_url,
            room_title=room_title,
            seller_own_id=seller_own_id,
            seller_own_name=seller_own_name,
            stats=stats,
        )


        get_acc_audience_preference_summary_response_data_channel_summary_live_top_item.additional_properties = d
        return get_acc_audience_preference_summary_response_data_channel_summary_live_top_item

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
