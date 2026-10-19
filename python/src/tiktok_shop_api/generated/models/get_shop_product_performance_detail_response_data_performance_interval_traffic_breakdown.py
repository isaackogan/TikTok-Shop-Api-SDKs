from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_shop_product_performance_detail_response_data_performance_interval_traffic_breakdown_content_type import (
    GetShopProductPerformanceDetailResponseDataPerformanceIntervalTrafficBreakdownContentType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_shop_product_performance_detail_response_data_performance_interval_traffic_breakdown_traffic import (
        GetShopProductPerformanceDetailResponseDataPerformanceIntervalTrafficBreakdownTraffic,
    )


T = TypeVar("T", bound="GetShopProductPerformanceDetailResponseDataPerformanceIntervalTrafficBreakdown")


@_attrs_define
class GetShopProductPerformanceDetailResponseDataPerformanceIntervalTrafficBreakdown:
    """
    Attributes:
        traffic (GetShopProductPerformanceDetailResponseDataPerformanceIntervalTrafficBreakdownTraffic | Unset):
        content_type (GetShopProductPerformanceDetailResponseDataPerformanceIntervalTrafficBreakdownContentType |
            Unset): Traffic breakdown content type.
            Possible values:
            - VIDEO: Video content.
            - LIVE: Live stream content.
            - PRODUCT_CARD: Product card.
    """

    traffic: GetShopProductPerformanceDetailResponseDataPerformanceIntervalTrafficBreakdownTraffic | Unset = UNSET
    content_type: GetShopProductPerformanceDetailResponseDataPerformanceIntervalTrafficBreakdownContentType | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        traffic: dict[str, Any] | Unset = UNSET
        if not isinstance(self.traffic, Unset):
            traffic = self.traffic.to_dict()

        content_type: str | Unset = UNSET
        if not isinstance(self.content_type, Unset):
            content_type = self.content_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if traffic is not UNSET:
            field_dict["traffic"] = traffic
        if content_type is not UNSET:
            field_dict["content_type"] = content_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shop_product_performance_detail_response_data_performance_interval_traffic_breakdown_traffic import (
            GetShopProductPerformanceDetailResponseDataPerformanceIntervalTrafficBreakdownTraffic,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _traffic = d.pop("traffic", UNSET)
        traffic: GetShopProductPerformanceDetailResponseDataPerformanceIntervalTrafficBreakdownTraffic | Unset
        if isinstance(_traffic, Unset):
            traffic = UNSET
        else:
            traffic = GetShopProductPerformanceDetailResponseDataPerformanceIntervalTrafficBreakdownTraffic.from_dict(
                _traffic
            )

        _content_type = d.pop("content_type", UNSET)
        content_type: GetShopProductPerformanceDetailResponseDataPerformanceIntervalTrafficBreakdownContentType | Unset
        if isinstance(_content_type, Unset):
            content_type = UNSET
        else:
            content_type = GetShopProductPerformanceDetailResponseDataPerformanceIntervalTrafficBreakdownContentType(
                _content_type
            )

        get_shop_product_performance_detail_response_data_performance_interval_traffic_breakdown = cls(
            traffic=traffic,
            content_type=content_type,
        )

        get_shop_product_performance_detail_response_data_performance_interval_traffic_breakdown.additional_properties = d
        return get_shop_product_performance_detail_response_data_performance_interval_traffic_breakdown

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
