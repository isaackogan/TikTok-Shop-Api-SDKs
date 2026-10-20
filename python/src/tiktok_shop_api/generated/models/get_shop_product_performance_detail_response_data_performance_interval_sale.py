from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_shop_product_performance_detail_response_data_performance_interval_sale_breakdown import (
        GetShopProductPerformanceDetailResponseDataPerformanceIntervalSaleBreakdown,
    )
    from ..models.gmv import Gmv


T = TypeVar("T", bound="GetShopProductPerformanceDetailResponseDataPerformanceIntervalSale")


@_attrs_define
class GetShopProductPerformanceDetailResponseDataPerformanceIntervalSale:
    """
    Attributes:
        gmv (Gmv | Unset):
        orders (int | Unset): Total (sum of all) orders for the product.
        items_sold (int | Unset): Number of items sold for the product.
        breakdowns (list[GetShopProductPerformanceDetailResponseDataPerformanceIntervalSaleBreakdown] | Unset): Sales
            breakdowns.
    """

    gmv: Gmv | Unset = UNSET
    orders: int | Unset = UNSET
    items_sold: int | Unset = UNSET
    breakdowns: list[GetShopProductPerformanceDetailResponseDataPerformanceIntervalSaleBreakdown] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gmv, Unset):
            gmv = self.gmv.to_dict()

        orders = self.orders

        items_sold = self.items_sold

        breakdowns: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.breakdowns, Unset):
            breakdowns = []
            for breakdowns_item_data in self.breakdowns:
                breakdowns_item = breakdowns_item_data.to_dict()
                breakdowns.append(breakdowns_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gmv is not UNSET:
            field_dict["gmv"] = gmv
        if orders is not UNSET:
            field_dict["orders"] = orders
        if items_sold is not UNSET:
            field_dict["items_sold"] = items_sold
        if breakdowns is not UNSET:
            field_dict["breakdowns"] = breakdowns

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shop_product_performance_detail_response_data_performance_interval_sale_breakdown import (
            GetShopProductPerformanceDetailResponseDataPerformanceIntervalSaleBreakdown,  # noqa: PLC0415
        )
        from ..models.gmv import Gmv  # noqa: PLC0415

        d = dict(src_dict)
        _gmv = d.pop("gmv", UNSET)
        gmv: Gmv | Unset
        if isinstance(_gmv, Unset):
            gmv = UNSET
        else:
            gmv = Gmv.from_dict(_gmv)

        orders = d.pop("orders", UNSET)

        items_sold = d.pop("items_sold", UNSET)

        _breakdowns = d.pop("breakdowns", UNSET)
        breakdowns: list[GetShopProductPerformanceDetailResponseDataPerformanceIntervalSaleBreakdown] | Unset = UNSET
        if _breakdowns is not UNSET:
            breakdowns = []
            for breakdowns_item_data in _breakdowns:
                breakdowns_item = GetShopProductPerformanceDetailResponseDataPerformanceIntervalSaleBreakdown.from_dict(
                    breakdowns_item_data
                )

                breakdowns.append(breakdowns_item)

        get_shop_product_performance_detail_response_data_performance_interval_sale = cls(
            gmv=gmv,
            orders=orders,
            items_sold=items_sold,
            breakdowns=breakdowns,
        )

        get_shop_product_performance_detail_response_data_performance_interval_sale.additional_properties = d
        return get_shop_product_performance_detail_response_data_performance_interval_sale

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
