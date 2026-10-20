from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSPSMetricTopItemsResponseDataOtdrLogisticsItem")


@_attrs_define
class GetSPSMetricTopItemsResponseDataOtdrLogisticsItem:
    """
    Attributes:
        delivered_order_count (int | Unset): Total number of delivered orders.
        logistics_provider (str | Unset): Logistics provider name.
        on_time_deliver_order_count (int | Unset): Number of orders delivered on time.
        on_time_deliver_rate (str | Unset): On-time delivery rate as a ratio from 0 to 1.
    """

    delivered_order_count: int | Unset = UNSET
    logistics_provider: str | Unset = UNSET
    on_time_deliver_order_count: int | Unset = UNSET
    on_time_deliver_rate: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delivered_order_count = self.delivered_order_count

        logistics_provider = self.logistics_provider

        on_time_deliver_order_count = self.on_time_deliver_order_count

        on_time_deliver_rate = self.on_time_deliver_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delivered_order_count is not UNSET:
            field_dict["delivered_order_count"] = delivered_order_count
        if logistics_provider is not UNSET:
            field_dict["logistics_provider"] = logistics_provider
        if on_time_deliver_order_count is not UNSET:
            field_dict["on_time_deliver_order_count"] = on_time_deliver_order_count
        if on_time_deliver_rate is not UNSET:
            field_dict["on_time_deliver_rate"] = on_time_deliver_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        delivered_order_count = d.pop("delivered_order_count", UNSET)

        logistics_provider = d.pop("logistics_provider", UNSET)

        on_time_deliver_order_count = d.pop("on_time_deliver_order_count", UNSET)

        on_time_deliver_rate = d.pop("on_time_deliver_rate", UNSET)

        get_sps_metric_top_items_response_data_otdr_logistics_item = cls(
            delivered_order_count=delivered_order_count,
            logistics_provider=logistics_provider,
            on_time_deliver_order_count=on_time_deliver_order_count,
            on_time_deliver_rate=on_time_deliver_rate,
        )

        get_sps_metric_top_items_response_data_otdr_logistics_item.additional_properties = d
        return get_sps_metric_top_items_response_data_otdr_logistics_item

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
