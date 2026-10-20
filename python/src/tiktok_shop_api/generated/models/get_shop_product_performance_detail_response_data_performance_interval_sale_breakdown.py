from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_shop_product_performance_detail_response_data_performance_interval_sale_breakdown_sale import (
        GetShopProductPerformanceDetailResponseDataPerformanceIntervalSaleBreakdownSale,
    )


T = TypeVar("T", bound="GetShopProductPerformanceDetailResponseDataPerformanceIntervalSaleBreakdown")


@_attrs_define
class GetShopProductPerformanceDetailResponseDataPerformanceIntervalSaleBreakdown:
    """
    Attributes:
        content_type (str | Unset): Sales breakdown content type.
            Possible values:
            - VIDEO: Video content.
            - LIVE: Live stream content.
            - PRODUCT_CARD: Product card.
        sales (GetShopProductPerformanceDetailResponseDataPerformanceIntervalSaleBreakdownSale | Unset):
    """

    content_type: str | Unset = UNSET
    sales: GetShopProductPerformanceDetailResponseDataPerformanceIntervalSaleBreakdownSale | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content_type = self.content_type

        sales: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sales, Unset):
            sales = self.sales.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if sales is not UNSET:
            field_dict["sales"] = sales

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shop_product_performance_detail_response_data_performance_interval_sale_breakdown_sale import (
            GetShopProductPerformanceDetailResponseDataPerformanceIntervalSaleBreakdownSale,  # noqa: PLC0415
        )

        d = dict(src_dict)
        content_type = d.pop("content_type", UNSET)

        _sales = d.pop("sales", UNSET)
        sales: GetShopProductPerformanceDetailResponseDataPerformanceIntervalSaleBreakdownSale | Unset
        if isinstance(_sales, Unset):
            sales = UNSET
        else:
            sales = GetShopProductPerformanceDetailResponseDataPerformanceIntervalSaleBreakdownSale.from_dict(_sales)

        get_shop_product_performance_detail_response_data_performance_interval_sale_breakdown = cls(
            content_type=content_type,
            sales=sales,
        )

        get_shop_product_performance_detail_response_data_performance_interval_sale_breakdown.additional_properties = d
        return get_shop_product_performance_detail_response_data_performance_interval_sale_breakdown

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
