from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_shop_product_performance_detail_response_data_performance import (
        GetShopProductPerformanceDetailResponseDataPerformance,
    )


T = TypeVar("T", bound="GetShopProductPerformanceDetailResponseData")


@_attrs_define
class GetShopProductPerformanceDetailResponseData:
    """
    Attributes:
        performance (GetShopProductPerformanceDetailResponseDataPerformance | Unset):
        latest_available_date (datetime.date | Unset): Latest date in local timezone where data is ready (ISO 8601
            format).
    """

    performance: GetShopProductPerformanceDetailResponseDataPerformance | Unset = UNSET
    latest_available_date: datetime.date | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        performance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.performance, Unset):
            performance = self.performance.to_dict()

        latest_available_date: str | Unset = UNSET
        if not isinstance(self.latest_available_date, Unset):
            latest_available_date = self.latest_available_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if performance is not UNSET:
            field_dict["performance"] = performance
        if latest_available_date is not UNSET:
            field_dict["latest_available_date"] = latest_available_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shop_product_performance_detail_response_data_performance import (
            GetShopProductPerformanceDetailResponseDataPerformance,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _performance = d.pop("performance", UNSET)
        performance: GetShopProductPerformanceDetailResponseDataPerformance | Unset
        if isinstance(_performance, Unset):
            performance = UNSET
        else:
            performance = GetShopProductPerformanceDetailResponseDataPerformance.from_dict(_performance)

        _latest_available_date = d.pop("latest_available_date", UNSET)
        latest_available_date: datetime.date | Unset
        if isinstance(_latest_available_date, Unset):
            latest_available_date = UNSET
        else:
            latest_available_date = datetime.date.fromisoformat(_latest_available_date)

        get_shop_product_performance_detail_response_data = cls(
            performance=performance,
            latest_available_date=latest_available_date,
        )

        get_shop_product_performance_detail_response_data.additional_properties = d
        return get_shop_product_performance_detail_response_data

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
