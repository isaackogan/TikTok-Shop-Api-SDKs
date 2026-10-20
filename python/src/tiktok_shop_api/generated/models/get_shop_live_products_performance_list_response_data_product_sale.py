from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_shop_live_products_performance_list_response_data_product_sale_avg_price import (
        GetShopLIVEProductsPerformanceListResponseDataProductSaleAvgPrice,
    )
    from ..models.get_shop_live_products_performance_list_response_data_product_sale_direct_gmv import (
        GetShopLIVEProductsPerformanceListResponseDataProductSaleDirectGmv,
    )


T = TypeVar("T", bound="GetShopLIVEProductsPerformanceListResponseDataProductSale")


@_attrs_define
class GetShopLIVEProductsPerformanceListResponseDataProductSale:
    """
    Attributes:
        direct_gmv (GetShopLIVEProductsPerformanceListResponseDataProductSaleDirectGmv | Unset):
        items_sold (int | Unset): The number of product items sold
        customers (int | Unset): The total numbers of customers who ordered this product directly from the LIVE,
            including customers who made returns or refunds.
        created_sku_orders (int | Unset): The total number of SKU orders created directly from the LIVE for this
            product.
        avg_price (GetShopLIVEProductsPerformanceListResponseDataProductSaleAvgPrice | Unset):
        sku_orders (int | Unset): The total number of paid SKU orders placed directly from the LIVE for this product.
        main_orders (int | Unset): Total number of paid main orders placed. Main orders refer to the single purchase
            transaction a customer makes.
        payment_rate (str | Unset): Main order paid / Main order created of this product
    """

    direct_gmv: GetShopLIVEProductsPerformanceListResponseDataProductSaleDirectGmv | Unset = UNSET
    items_sold: int | Unset = UNSET
    customers: int | Unset = UNSET
    created_sku_orders: int | Unset = UNSET
    avg_price: GetShopLIVEProductsPerformanceListResponseDataProductSaleAvgPrice | Unset = UNSET
    sku_orders: int | Unset = UNSET
    main_orders: int | Unset = UNSET
    payment_rate: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        direct_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.direct_gmv, Unset):
            direct_gmv = self.direct_gmv.to_dict()

        items_sold = self.items_sold

        customers = self.customers

        created_sku_orders = self.created_sku_orders

        avg_price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.avg_price, Unset):
            avg_price = self.avg_price.to_dict()

        sku_orders = self.sku_orders

        main_orders = self.main_orders

        payment_rate = self.payment_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if direct_gmv is not UNSET:
            field_dict["direct_gmv"] = direct_gmv
        if items_sold is not UNSET:
            field_dict["items_sold"] = items_sold
        if customers is not UNSET:
            field_dict["customers"] = customers
        if created_sku_orders is not UNSET:
            field_dict["created_sku_orders"] = created_sku_orders
        if avg_price is not UNSET:
            field_dict["avg_price"] = avg_price
        if sku_orders is not UNSET:
            field_dict["sku_orders"] = sku_orders
        if main_orders is not UNSET:
            field_dict["main_orders"] = main_orders
        if payment_rate is not UNSET:
            field_dict["payment_rate"] = payment_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shop_live_products_performance_list_response_data_product_sale_avg_price import (
            GetShopLIVEProductsPerformanceListResponseDataProductSaleAvgPrice,  # noqa: PLC0415
        )
        from ..models.get_shop_live_products_performance_list_response_data_product_sale_direct_gmv import (
            GetShopLIVEProductsPerformanceListResponseDataProductSaleDirectGmv,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _direct_gmv = d.pop("direct_gmv", UNSET)
        direct_gmv: GetShopLIVEProductsPerformanceListResponseDataProductSaleDirectGmv | Unset
        if isinstance(_direct_gmv, Unset):
            direct_gmv = UNSET
        else:
            direct_gmv = GetShopLIVEProductsPerformanceListResponseDataProductSaleDirectGmv.from_dict(_direct_gmv)

        items_sold = d.pop("items_sold", UNSET)

        customers = d.pop("customers", UNSET)

        created_sku_orders = d.pop("created_sku_orders", UNSET)

        _avg_price = d.pop("avg_price", UNSET)
        avg_price: GetShopLIVEProductsPerformanceListResponseDataProductSaleAvgPrice | Unset
        if isinstance(_avg_price, Unset):
            avg_price = UNSET
        else:
            avg_price = GetShopLIVEProductsPerformanceListResponseDataProductSaleAvgPrice.from_dict(_avg_price)

        sku_orders = d.pop("sku_orders", UNSET)

        main_orders = d.pop("main_orders", UNSET)

        payment_rate = d.pop("payment_rate", UNSET)

        get_shop_live_products_performance_list_response_data_product_sale = cls(
            direct_gmv=direct_gmv,
            items_sold=items_sold,
            customers=customers,
            created_sku_orders=created_sku_orders,
            avg_price=avg_price,
            sku_orders=sku_orders,
            main_orders=main_orders,
            payment_rate=payment_rate,
        )

        get_shop_live_products_performance_list_response_data_product_sale.additional_properties = d
        return get_shop_live_products_performance_list_response_data_product_sale

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
