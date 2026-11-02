from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.stat import Stat





T = TypeVar("T", bound="GetACCAudiencePreferenceSummaryResponseDataChannelSummaryLiveTypeTopItem")



@_attrs_define
class GetACCAudiencePreferenceSummaryResponseDataChannelSummaryLiveTypeTopItem:
    """ 
        Attributes:
            live_type (str | Unset): Stable LIVE type identifier, such as label1. Use this identifier as factor_id in Get
                ACC Audience Preference List for entity_type=LIVE; the localized display name is not a query value.
            live_type_name (str | Unset): Localized display name of the LIVE factor. Use live_type, rather than this display
                name, as the stable identifier for filtering LIVE preferences.
            stats (Stat | Unset):
     """

    live_type: str | Unset = UNSET
    live_type_name: str | Unset = UNSET
    stats: Stat | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.stat import Stat # noqa: PLC0415
        live_type = self.live_type

        live_type_name = self.live_type_name

        stats: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if live_type is not UNSET:
            field_dict["live_type"] = live_type
        if live_type_name is not UNSET:
            field_dict["live_type_name"] = live_type_name
        if stats is not UNSET:
            field_dict["stats"] = stats

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.stat import Stat # noqa: PLC0415
        d = dict(src_dict)
        live_type = d.pop("live_type", UNSET)

        live_type_name = d.pop("live_type_name", UNSET)

        _stats = d.pop("stats", UNSET)
        stats: Stat | Unset
        if isinstance(_stats,  Unset):
            stats = UNSET
        else:
            stats = Stat.from_dict(_stats)




        get_acc_audience_preference_summary_response_data_channel_summary_live_type_top_item = cls(
            live_type=live_type,
            live_type_name=live_type_name,
            stats=stats,
        )


        get_acc_audience_preference_summary_response_data_channel_summary_live_type_top_item.additional_properties = d
        return get_acc_audience_preference_summary_response_data_channel_summary_live_type_top_item

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
