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





T = TypeVar("T", bound="GetACCAudiencePreferenceSummaryResponseDataChannelSummarySellerOwnTopItem")



@_attrs_define
class GetACCAudiencePreferenceSummaryResponseDataChannelSummarySellerOwnTopItem:
    """ 
        Attributes:
            content_type (str | Unset): Content classification associated with this content-author summary.
            seller_own_avatar_url (str | Unset): URL of the content author's avatar.
            seller_own_id (str | Unset): ID of the content author.
            seller_own_name (str | Unset): Display name of the content author.
            stats (Stat | Unset):
            sub_channel (str | Unset): Channel associated with this content-author summary.
     """

    content_type: str | Unset = UNSET
    seller_own_avatar_url: str | Unset = UNSET
    seller_own_id: str | Unset = UNSET
    seller_own_name: str | Unset = UNSET
    stats: Stat | Unset = UNSET
    sub_channel: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.stat import Stat # noqa: PLC0415
        content_type = self.content_type

        seller_own_avatar_url = self.seller_own_avatar_url

        seller_own_id = self.seller_own_id

        seller_own_name = self.seller_own_name

        stats: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()

        sub_channel = self.sub_channel


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if seller_own_avatar_url is not UNSET:
            field_dict["seller_own_avatar_url"] = seller_own_avatar_url
        if seller_own_id is not UNSET:
            field_dict["seller_own_id"] = seller_own_id
        if seller_own_name is not UNSET:
            field_dict["seller_own_name"] = seller_own_name
        if stats is not UNSET:
            field_dict["stats"] = stats
        if sub_channel is not UNSET:
            field_dict["sub_channel"] = sub_channel

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.stat import Stat # noqa: PLC0415
        d = dict(src_dict)
        content_type = d.pop("content_type", UNSET)

        seller_own_avatar_url = d.pop("seller_own_avatar_url", UNSET)

        seller_own_id = d.pop("seller_own_id", UNSET)

        seller_own_name = d.pop("seller_own_name", UNSET)

        _stats = d.pop("stats", UNSET)
        stats: Stat | Unset
        if isinstance(_stats,  Unset):
            stats = UNSET
        else:
            stats = Stat.from_dict(_stats)




        sub_channel = d.pop("sub_channel", UNSET)

        get_acc_audience_preference_summary_response_data_channel_summary_seller_own_top_item = cls(
            content_type=content_type,
            seller_own_avatar_url=seller_own_avatar_url,
            seller_own_id=seller_own_id,
            seller_own_name=seller_own_name,
            stats=stats,
            sub_channel=sub_channel,
        )


        get_acc_audience_preference_summary_response_data_channel_summary_seller_own_top_item.additional_properties = d
        return get_acc_audience_preference_summary_response_data_channel_summary_seller_own_top_item

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
