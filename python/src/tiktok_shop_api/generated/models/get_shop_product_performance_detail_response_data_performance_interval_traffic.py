from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_shop_product_performance_detail_response_data_performance_interval_traffic_breakdown import (
        GetShopProductPerformanceDetailResponseDataPerformanceIntervalTrafficBreakdown,
    )


T = TypeVar("T", bound="GetShopProductPerformanceDetailResponseDataPerformanceIntervalTraffic")


@_attrs_define
class GetShopProductPerformanceDetailResponseDataPerformanceIntervalTraffic:
    """
    Attributes:
        breakdowns (list[GetShopProductPerformanceDetailResponseDataPerformanceIntervalTrafficBreakdown] | Unset):
            Traffic breakdowns.
    """

    breakdowns: list[GetShopProductPerformanceDetailResponseDataPerformanceIntervalTrafficBreakdown] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        breakdowns: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.breakdowns, Unset):
            breakdowns = []
            for breakdowns_item_data in self.breakdowns:
                breakdowns_item = breakdowns_item_data.to_dict()
                breakdowns.append(breakdowns_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if breakdowns is not UNSET:
            field_dict["breakdowns"] = breakdowns

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shop_product_performance_detail_response_data_performance_interval_traffic_breakdown import (
            GetShopProductPerformanceDetailResponseDataPerformanceIntervalTrafficBreakdown,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _breakdowns = d.pop("breakdowns", UNSET)
        breakdowns: list[GetShopProductPerformanceDetailResponseDataPerformanceIntervalTrafficBreakdown] | Unset = UNSET
        if _breakdowns is not UNSET:
            breakdowns = []
            for breakdowns_item_data in _breakdowns:
                breakdowns_item = (
                    GetShopProductPerformanceDetailResponseDataPerformanceIntervalTrafficBreakdown.from_dict(
                        breakdowns_item_data
                    )
                )

                breakdowns.append(breakdowns_item)

        get_shop_product_performance_detail_response_data_performance_interval_traffic = cls(
            breakdowns=breakdowns,
        )

        get_shop_product_performance_detail_response_data_performance_interval_traffic.additional_properties = d
        return get_shop_product_performance_detail_response_data_performance_interval_traffic

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
