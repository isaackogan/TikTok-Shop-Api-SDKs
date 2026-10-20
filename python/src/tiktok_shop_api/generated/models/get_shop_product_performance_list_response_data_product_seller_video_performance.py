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
  from ..models.attributed_gmv import AttributedGmv





T = TypeVar("T", bound="GetShopProductPerformanceListResponseDataProductSellerVideoPerformance")



@_attrs_define
class GetShopProductPerformanceListResponseDataProductSellerVideoPerformance:
    """ 
        Attributes:
            attributed_gmv (AttributedGmv | Unset):
            attributed_orders (int | Unset): Number of attributed orders.
            attributed_sku_orders (int | Unset): Number of attributed SKU orders.
            attributed_sold_items (int | Unset): Number of attributed items sold.
            estimated_customers (int | Unset): Estimated number of customers.
            aov (Aov | Unset):
            new_video_count (int | Unset): Number of new videos.
            product_impressions (int | Unset): Number of product impressions.
            product_clicks (int | Unset): Number of product clicks.
            ctr (str | Unset): Click-through rate.
            add_cart_count (int | Unset): Number of times products were added to the cart.
            add_cart_rate (str | Unset): Add to cart rate.
            click_order_rate (str | Unset): Click to order rate.
            unique_product_impressions (int | Unset): Number of unique product impressions from seller video content.
            unique_clicks (int | Unset): Number of unique product clicks from seller video content.
            unique_ctr (str | Unset): Unique click-through rate.
            add_cart_users (int | Unset): Number of users who added to cart.
            unique_atc_rate (str | Unset): Unique add to cart rate.
            unique_click_order_rate (str | Unset): Unique click to order rate.
     """

    attributed_gmv: AttributedGmv | Unset = UNSET
    attributed_orders: int | Unset = UNSET
    attributed_sku_orders: int | Unset = UNSET
    attributed_sold_items: int | Unset = UNSET
    estimated_customers: int | Unset = UNSET
    aov: Aov | Unset = UNSET
    new_video_count: int | Unset = UNSET
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
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.aov import Aov # noqa: PLC0415
        from ..models.attributed_gmv import AttributedGmv # noqa: PLC0415
        attributed_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributed_gmv, Unset):
            attributed_gmv = self.attributed_gmv.to_dict()

        attributed_orders = self.attributed_orders

        attributed_sku_orders = self.attributed_sku_orders

        attributed_sold_items = self.attributed_sold_items

        estimated_customers = self.estimated_customers

        aov: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aov, Unset):
            aov = self.aov.to_dict()

        new_video_count = self.new_video_count

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


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if attributed_gmv is not UNSET:
            field_dict["attributed_gmv"] = attributed_gmv
        if attributed_orders is not UNSET:
            field_dict["attributed_orders"] = attributed_orders
        if attributed_sku_orders is not UNSET:
            field_dict["attributed_sku_orders"] = attributed_sku_orders
        if attributed_sold_items is not UNSET:
            field_dict["attributed_sold_items"] = attributed_sold_items
        if estimated_customers is not UNSET:
            field_dict["estimated_customers"] = estimated_customers
        if aov is not UNSET:
            field_dict["aov"] = aov
        if new_video_count is not UNSET:
            field_dict["new_video_count"] = new_video_count
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

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aov import Aov # noqa: PLC0415
        from ..models.attributed_gmv import AttributedGmv # noqa: PLC0415
        d = dict(src_dict)
        _attributed_gmv = d.pop("attributed_gmv", UNSET)
        attributed_gmv: AttributedGmv | Unset
        if isinstance(_attributed_gmv,  Unset):
            attributed_gmv = UNSET
        else:
            attributed_gmv = AttributedGmv.from_dict(_attributed_gmv)




        attributed_orders = d.pop("attributed_orders", UNSET)

        attributed_sku_orders = d.pop("attributed_sku_orders", UNSET)

        attributed_sold_items = d.pop("attributed_sold_items", UNSET)

        estimated_customers = d.pop("estimated_customers", UNSET)

        _aov = d.pop("aov", UNSET)
        aov: Aov | Unset
        if isinstance(_aov,  Unset):
            aov = UNSET
        else:
            aov = Aov.from_dict(_aov)




        new_video_count = d.pop("new_video_count", UNSET)

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

        get_shop_product_performance_list_response_data_product_seller_video_performance = cls(
            attributed_gmv=attributed_gmv,
            attributed_orders=attributed_orders,
            attributed_sku_orders=attributed_sku_orders,
            attributed_sold_items=attributed_sold_items,
            estimated_customers=estimated_customers,
            aov=aov,
            new_video_count=new_video_count,
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
        )


        get_shop_product_performance_list_response_data_product_seller_video_performance.additional_properties = d
        return get_shop_product_performance_list_response_data_product_seller_video_performance

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
