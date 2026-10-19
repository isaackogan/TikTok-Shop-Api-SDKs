from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gmv import Gmv


T = TypeVar("T", bound="GetShopLIVEMinutePerformanceResponseDataPerformanceIntervalSale")


@_attrs_define
class GetShopLIVEMinutePerformanceResponseDataPerformanceIntervalSale:
    """
    Attributes:
        gmv (Gmv | Unset):
        items_sold (int | Unset): The number of items sold directly within this interval.
        customers (int | Unset): The total number of customers who placed orders within this interval, including
            customers who made returns or refunds.
        sku_orders (int | Unset): The total number of paid SKU orders placed within this interval.
        main_orders (int | Unset): Total number of paid main orders placed. Main orders refer to the single purchase
            transaction a customer makes.
    """

    gmv: Gmv | Unset = UNSET
    items_sold: int | Unset = UNSET
    customers: int | Unset = UNSET
    sku_orders: int | Unset = UNSET
    main_orders: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gmv, Unset):
            gmv = self.gmv.to_dict()

        items_sold = self.items_sold

        customers = self.customers

        sku_orders = self.sku_orders

        main_orders = self.main_orders

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gmv is not UNSET:
            field_dict["gmv"] = gmv
        if items_sold is not UNSET:
            field_dict["items_sold"] = items_sold
        if customers is not UNSET:
            field_dict["customers"] = customers
        if sku_orders is not UNSET:
            field_dict["sku_orders"] = sku_orders
        if main_orders is not UNSET:
            field_dict["main_orders"] = main_orders

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gmv import Gmv  # noqa: PLC0415

        d = dict(src_dict)
        _gmv = d.pop("gmv", UNSET)
        gmv: Gmv | Unset
        if isinstance(_gmv, Unset):
            gmv = UNSET
        else:
            gmv = Gmv.from_dict(_gmv)

        items_sold = d.pop("items_sold", UNSET)

        customers = d.pop("customers", UNSET)

        sku_orders = d.pop("sku_orders", UNSET)

        main_orders = d.pop("main_orders", UNSET)

        get_shop_live_minute_performance_response_data_performance_interval_sale = cls(
            gmv=gmv,
            items_sold=items_sold,
            customers=customers,
            sku_orders=sku_orders,
            main_orders=main_orders,
        )

        get_shop_live_minute_performance_response_data_performance_interval_sale.additional_properties = d
        return get_shop_live_minute_performance_response_data_performance_interval_sale

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
