from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetShopLIVEMinutePerformanceResponseDataPerformanceIntervalTraffic")



@_attrs_define
class GetShopLIVEMinutePerformanceResponseDataPerformanceIntervalTraffic:
    """ 
        Attributes:
            viewers (int | Unset): The number of viewers within this interval.
            views (int | Unset): The number of views or viewings in the LIVE room.
            product_impressions (int | Unset): Total number of times a product was viewed in LIVE, including product list
                and product card impressions.
            ctr (str | Unset): The number of clicks divided by numbers of views of the LIVE during selected time period
                including clicks on product lists and product cards
            enter_room_rate (str | Unset): LIVE views per LIVE room impressions.
            product_clicks (int | Unset): Total number of product link clicks from LIVE streams, including product list and
                product card clicks.
            impressions (int | Unset): The total number of times the LIVE was displayed to viewers.
     """

    viewers: int | Unset = UNSET
    views: int | Unset = UNSET
    product_impressions: int | Unset = UNSET
    ctr: str | Unset = UNSET
    enter_room_rate: str | Unset = UNSET
    product_clicks: int | Unset = UNSET
    impressions: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        viewers = self.viewers

        views = self.views

        product_impressions = self.product_impressions

        ctr = self.ctr

        enter_room_rate = self.enter_room_rate

        product_clicks = self.product_clicks

        impressions = self.impressions


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if viewers is not UNSET:
            field_dict["viewers"] = viewers
        if views is not UNSET:
            field_dict["views"] = views
        if product_impressions is not UNSET:
            field_dict["product_impressions"] = product_impressions
        if ctr is not UNSET:
            field_dict["ctr"] = ctr
        if enter_room_rate is not UNSET:
            field_dict["enter_room_rate"] = enter_room_rate
        if product_clicks is not UNSET:
            field_dict["product_clicks"] = product_clicks
        if impressions is not UNSET:
            field_dict["impressions"] = impressions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        viewers = d.pop("viewers", UNSET)

        views = d.pop("views", UNSET)

        product_impressions = d.pop("product_impressions", UNSET)

        ctr = d.pop("ctr", UNSET)

        enter_room_rate = d.pop("enter_room_rate", UNSET)

        product_clicks = d.pop("product_clicks", UNSET)

        impressions = d.pop("impressions", UNSET)

        get_shop_live_minute_performance_response_data_performance_interval_traffic = cls(
            viewers=viewers,
            views=views,
            product_impressions=product_impressions,
            ctr=ctr,
            enter_room_rate=enter_room_rate,
            product_clicks=product_clicks,
            impressions=impressions,
        )


        get_shop_live_minute_performance_response_data_performance_interval_traffic.additional_properties = d
        return get_shop_live_minute_performance_response_data_performance_interval_traffic

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
