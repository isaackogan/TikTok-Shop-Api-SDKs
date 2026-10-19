from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_shop_live_minute_performance_response_data_performance import (
        GetShopLIVEMinutePerformanceResponseDataPerformance,
    )


T = TypeVar("T", bound="GetShopLIVEMinutePerformanceResponseData")


@_attrs_define
class GetShopLIVEMinutePerformanceResponseData:
    """
    Attributes:
        performance (GetShopLIVEMinutePerformanceResponseDataPerformance | Unset):
        next_page_token (str | Unset): Page token for retrieving the next page. An empty value means there are no more
            pages.
        total_count (int | Unset): Total number of minute-level intervals across all pages.
    """

    performance: GetShopLIVEMinutePerformanceResponseDataPerformance | Unset = UNSET
    next_page_token: str | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        performance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.performance, Unset):
            performance = self.performance.to_dict()

        next_page_token = self.next_page_token

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if performance is not UNSET:
            field_dict["performance"] = performance
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shop_live_minute_performance_response_data_performance import (
            GetShopLIVEMinutePerformanceResponseDataPerformance,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _performance = d.pop("performance", UNSET)
        performance: GetShopLIVEMinutePerformanceResponseDataPerformance | Unset
        if isinstance(_performance, Unset):
            performance = UNSET
        else:
            performance = GetShopLIVEMinutePerformanceResponseDataPerformance.from_dict(_performance)

        next_page_token = d.pop("next_page_token", UNSET)

        total_count = d.pop("total_count", UNSET)

        get_shop_live_minute_performance_response_data = cls(
            performance=performance,
            next_page_token=next_page_token,
            total_count=total_count,
        )

        get_shop_live_minute_performance_response_data.additional_properties = d
        return get_shop_live_minute_performance_response_data

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
