from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.aov import Aov
  from ..models.get_shop_product_performance_list_response_data_product_total_performance_gmv_incl_tax import GetShopProductPerformanceListResponseDataProductTotalPerformanceGmvInclTax
  from ..models.get_shop_product_performance_list_response_data_product_total_performance_gross_merchandise_value import GetShopProductPerformanceListResponseDataProductTotalPerformanceGrossMerchandiseValue
  from ..models.gmv import Gmv
  from ..models.refund import Refund
  from ..models.shipping_fee import ShippingFee
  from ..models.tax import Tax





T = TypeVar("T", bound="GetShopProductPerformanceListResponseDataProductTotalPerformance")



@_attrs_define
class GetShopProductPerformanceListResponseDataProductTotalPerformance:
    """ 
        Attributes:
            gmv (Gmv | Unset):
            orders (int | Unset): Number of orders.
            sku_orders (int | Unset): Number of SKU orders.
            items_sold (int | Unset): Number of items sold.
            estimated_customers (int | Unset): Estimated number of customers.
            aov (Aov | Unset):
            product_impressions (int | Unset): Number of product impressions.
            product_clicks (int | Unset): Number of product clicks.
            ctr (str | Unset): Click-through rate.
            add_cart_count (int | Unset): Number of times products were added to the cart.
            add_cart_rate (str | Unset): Add to cart rate.
            click_order_rate (str | Unset): Click to order rate.
            unique_product_impressions (int | Unset): Unique product impressions.
            unique_clicks (int | Unset): Total number of unique product clicks across the product performance channels.
            unique_ctr (str | Unset): Unique click-through rate.
            add_cart_users (int | Unset): Number of users who added to cart.
            unique_atc_rate (str | Unset): Unique add to cart rate.
            unique_click_order_rate (str | Unset): Unique click to order rate.
            gmv_incl_tax (GetShopProductPerformanceListResponseDataProductTotalPerformanceGmvInclTax | Unset):
            tax (Tax | Unset):
            gross_merchandise_value (GetShopProductPerformanceListResponseDataProductTotalPerformanceGrossMerchandiseValue |
                Unset):
            shipping_fees (ShippingFee | Unset):
            refunds (Refund | Unset):
            refunded_items (int | Unset): Number of items refunded.
            refund_customers (int | Unset): Number of customers who received refunds.
     """

    gmv: Gmv | Unset = UNSET
    orders: int | Unset = UNSET
    sku_orders: int | Unset = UNSET
    items_sold: int | Unset = UNSET
    estimated_customers: int | Unset = UNSET
    aov: Aov | Unset = UNSET
    product_impressions: int | Unset = UNSET
    product_clicks: int | Unset = UNSET
    ctr: str | Unset = UNSET
    add_cart_count: int | Unset = UNSET
    add_cart_rate: str | Unset = UNSET
    click_order_rate: str | Unset = UNSET
    unique_product_impressions: int | Unset = UNSET
    unique_clicks: int | Unset = UNSET
    unique_ctr: str | Unset = UNSET
    add_cart_users: int | Unset = UNSET
    unique_atc_rate: str | Unset = UNSET
    unique_click_order_rate: str | Unset = UNSET
    gmv_incl_tax: GetShopProductPerformanceListResponseDataProductTotalPerformanceGmvInclTax | Unset = UNSET
    tax: Tax | Unset = UNSET
    gross_merchandise_value: GetShopProductPerformanceListResponseDataProductTotalPerformanceGrossMerchandiseValue | Unset = UNSET
    shipping_fees: ShippingFee | Unset = UNSET
    refunds: Refund | Unset = UNSET
    refunded_items: int | Unset = UNSET
    refund_customers: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.aov import Aov # noqa: PLC0415
        from ..models.get_shop_product_performance_list_response_data_product_total_performance_gmv_incl_tax import GetShopProductPerformanceListResponseDataProductTotalPerformanceGmvInclTax # noqa: PLC0415
        from ..models.get_shop_product_performance_list_response_data_product_total_performance_gross_merchandise_value import GetShopProductPerformanceListResponseDataProductTotalPerformanceGrossMerchandiseValue # noqa: PLC0415
        from ..models.gmv import Gmv # noqa: PLC0415
        from ..models.refund import Refund # noqa: PLC0415
        from ..models.shipping_fee import ShippingFee # noqa: PLC0415
        from ..models.tax import Tax # noqa: PLC0415
        gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gmv, Unset):
            gmv = self.gmv.to_dict()

        orders = self.orders

        sku_orders = self.sku_orders

        items_sold = self.items_sold

        estimated_customers = self.estimated_customers

        aov: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aov, Unset):
            aov = self.aov.to_dict()

        product_impressions = self.product_impressions

        product_clicks = self.product_clicks

        ctr = self.ctr

        add_cart_count = self.add_cart_count

        add_cart_rate = self.add_cart_rate

        click_order_rate = self.click_order_rate

        unique_product_impressions = self.unique_product_impressions

        unique_clicks = self.unique_clicks

        unique_ctr = self.unique_ctr

        add_cart_users = self.add_cart_users

        unique_atc_rate = self.unique_atc_rate

        unique_click_order_rate = self.unique_click_order_rate

        gmv_incl_tax: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gmv_incl_tax, Unset):
            gmv_incl_tax = self.gmv_incl_tax.to_dict()

        tax: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tax, Unset):
            tax = self.tax.to_dict()

        gross_merchandise_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gross_merchandise_value, Unset):
            gross_merchandise_value = self.gross_merchandise_value.to_dict()

        shipping_fees: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shipping_fees, Unset):
            shipping_fees = self.shipping_fees.to_dict()

        refunds: dict[str, Any] | Unset = UNSET
        if not isinstance(self.refunds, Unset):
            refunds = self.refunds.to_dict()

        refunded_items = self.refunded_items

        refund_customers = self.refund_customers


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if gmv is not UNSET:
            field_dict["gmv"] = gmv
        if orders is not UNSET:
            field_dict["orders"] = orders
        if sku_orders is not UNSET:
            field_dict["sku_orders"] = sku_orders
        if items_sold is not UNSET:
            field_dict["items_sold"] = items_sold
        if estimated_customers is not UNSET:
            field_dict["estimated_customers"] = estimated_customers
        if aov is not UNSET:
            field_dict["aov"] = aov
        if product_impressions is not UNSET:
            field_dict["product_impressions"] = product_impressions
        if product_clicks is not UNSET:
            field_dict["product_clicks"] = product_clicks
        if ctr is not UNSET:
            field_dict["ctr"] = ctr
        if add_cart_count is not UNSET:
            field_dict["add_cart_count"] = add_cart_count
        if add_cart_rate is not UNSET:
            field_dict["add_cart_rate"] = add_cart_rate
        if click_order_rate is not UNSET:
            field_dict["click_order_rate"] = click_order_rate
        if unique_product_impressions is not UNSET:
            field_dict["unique_product_impressions"] = unique_product_impressions
        if unique_clicks is not UNSET:
            field_dict["unique_clicks"] = unique_clicks
        if unique_ctr is not UNSET:
            field_dict["unique_ctr"] = unique_ctr
        if add_cart_users is not UNSET:
            field_dict["add_cart_users"] = add_cart_users
        if unique_atc_rate is not UNSET:
            field_dict["unique_atc_rate"] = unique_atc_rate
        if unique_click_order_rate is not UNSET:
            field_dict["unique_click_order_rate"] = unique_click_order_rate
        if gmv_incl_tax is not UNSET:
            field_dict["gmv_incl_tax"] = gmv_incl_tax
        if tax is not UNSET:
            field_dict["tax"] = tax
        if gross_merchandise_value is not UNSET:
            field_dict["gross_merchandise_value"] = gross_merchandise_value
        if shipping_fees is not UNSET:
            field_dict["shipping_fees"] = shipping_fees
        if refunds is not UNSET:
            field_dict["refunds"] = refunds
        if refunded_items is not UNSET:
            field_dict["refunded_items"] = refunded_items
        if refund_customers is not UNSET:
            field_dict["refund_customers"] = refund_customers

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aov import Aov # noqa: PLC0415
        from ..models.get_shop_product_performance_list_response_data_product_total_performance_gmv_incl_tax import GetShopProductPerformanceListResponseDataProductTotalPerformanceGmvInclTax # noqa: PLC0415
        from ..models.get_shop_product_performance_list_response_data_product_total_performance_gross_merchandise_value import GetShopProductPerformanceListResponseDataProductTotalPerformanceGrossMerchandiseValue # noqa: PLC0415
        from ..models.gmv import Gmv # noqa: PLC0415
        from ..models.refund import Refund # noqa: PLC0415
        from ..models.shipping_fee import ShippingFee # noqa: PLC0415
        from ..models.tax import Tax # noqa: PLC0415
        d = dict(src_dict)
        _gmv = d.pop("gmv", UNSET)
        gmv: Gmv | Unset
        if isinstance(_gmv,  Unset):
            gmv = UNSET
        else:
            gmv = Gmv.from_dict(_gmv)




        orders = d.pop("orders", UNSET)

        sku_orders = d.pop("sku_orders", UNSET)

        items_sold = d.pop("items_sold", UNSET)

        estimated_customers = d.pop("estimated_customers", UNSET)

        _aov = d.pop("aov", UNSET)
        aov: Aov | Unset
        if isinstance(_aov,  Unset):
            aov = UNSET
        else:
            aov = Aov.from_dict(_aov)




        product_impressions = d.pop("product_impressions", UNSET)

        product_clicks = d.pop("product_clicks", UNSET)

        ctr = d.pop("ctr", UNSET)

        add_cart_count = d.pop("add_cart_count", UNSET)

        add_cart_rate = d.pop("add_cart_rate", UNSET)

        click_order_rate = d.pop("click_order_rate", UNSET)

        unique_product_impressions = d.pop("unique_product_impressions", UNSET)

        unique_clicks = d.pop("unique_clicks", UNSET)

        unique_ctr = d.pop("unique_ctr", UNSET)

        add_cart_users = d.pop("add_cart_users", UNSET)

        unique_atc_rate = d.pop("unique_atc_rate", UNSET)

        unique_click_order_rate = d.pop("unique_click_order_rate", UNSET)

        _gmv_incl_tax = d.pop("gmv_incl_tax", UNSET)
        gmv_incl_tax: GetShopProductPerformanceListResponseDataProductTotalPerformanceGmvInclTax | Unset
        if isinstance(_gmv_incl_tax,  Unset):
            gmv_incl_tax = UNSET
        else:
            gmv_incl_tax = GetShopProductPerformanceListResponseDataProductTotalPerformanceGmvInclTax.from_dict(_gmv_incl_tax)




        _tax = d.pop("tax", UNSET)
        tax: Tax | Unset
        if isinstance(_tax,  Unset):
            tax = UNSET
        else:
            tax = Tax.from_dict(_tax)




        _gross_merchandise_value = d.pop("gross_merchandise_value", UNSET)
        gross_merchandise_value: GetShopProductPerformanceListResponseDataProductTotalPerformanceGrossMerchandiseValue | Unset
        if isinstance(_gross_merchandise_value,  Unset):
            gross_merchandise_value = UNSET
        else:
            gross_merchandise_value = GetShopProductPerformanceListResponseDataProductTotalPerformanceGrossMerchandiseValue.from_dict(_gross_merchandise_value)




        _shipping_fees = d.pop("shipping_fees", UNSET)
        shipping_fees: ShippingFee | Unset
        if isinstance(_shipping_fees,  Unset):
            shipping_fees = UNSET
        else:
            shipping_fees = ShippingFee.from_dict(_shipping_fees)




        _refunds = d.pop("refunds", UNSET)
        refunds: Refund | Unset
        if isinstance(_refunds,  Unset):
            refunds = UNSET
        else:
            refunds = Refund.from_dict(_refunds)




        refunded_items = d.pop("refunded_items", UNSET)

        refund_customers = d.pop("refund_customers", UNSET)

        get_shop_product_performance_list_response_data_product_total_performance = cls(
            gmv=gmv,
            orders=orders,
            sku_orders=sku_orders,
            items_sold=items_sold,
            estimated_customers=estimated_customers,
            aov=aov,
            product_impressions=product_impressions,
            product_clicks=product_clicks,
            ctr=ctr,
            add_cart_count=add_cart_count,
            add_cart_rate=add_cart_rate,
            click_order_rate=click_order_rate,
            unique_product_impressions=unique_product_impressions,
            unique_clicks=unique_clicks,
            unique_ctr=unique_ctr,
            add_cart_users=add_cart_users,
            unique_atc_rate=unique_atc_rate,
            unique_click_order_rate=unique_click_order_rate,
            gmv_incl_tax=gmv_incl_tax,
            tax=tax,
            gross_merchandise_value=gross_merchandise_value,
            shipping_fees=shipping_fees,
            refunds=refunds,
            refunded_items=refunded_items,
            refund_customers=refund_customers,
        )


        get_shop_product_performance_list_response_data_product_total_performance.additional_properties = d
        return get_shop_product_performance_list_response_data_product_total_performance

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
