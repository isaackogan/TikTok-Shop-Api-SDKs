from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetLiveRoomGMVAndOrderTrendsResponseDataGmvTrendPerformanceDataPointGmv")


@_attrs_define
class GetLiveRoomGMVAndOrderTrendsResponseDataGmvTrendPerformanceDataPointGmv:
    """
    Attributes:
        currency (str | Unset): The ISO 4217 currency code for the GMV amount.
        amount (str | Unset): The amount of GMV
    """

    currency: str | Unset = UNSET
    amount: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency = self.currency

        amount = self.amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency is not UNSET:
            field_dict["currency"] = currency
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currency = d.pop("currency", UNSET)

        amount = d.pop("amount", UNSET)

        get_live_room_gmv_and_order_trends_response_data_gmv_trend_performance_data_point_gmv = cls(
            currency=currency,
            amount=amount,
        )

        get_live_room_gmv_and_order_trends_response_data_gmv_trend_performance_data_point_gmv.additional_properties = d
        return get_live_room_gmv_and_order_trends_response_data_gmv_trend_performance_data_point_gmv

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
