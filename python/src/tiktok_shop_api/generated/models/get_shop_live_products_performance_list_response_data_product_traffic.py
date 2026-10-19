from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.click_to_order_rate import ClickToOrderRate
    from ..models.get_shop_live_products_performance_list_response_data_product_traffic_gpm import (
        GetShopLIVEProductsPerformanceListResponseDataProductTrafficGpm,
    )


T = TypeVar("T", bound="GetShopLIVEProductsPerformanceListResponseDataProductTraffic")


@_attrs_define
class GetShopLIVEProductsPerformanceListResponseDataProductTraffic:
    """
    Attributes:
        product_impressions (int | Unset): Number of product impressions for this product during the LIVE video,
            including for product lists and product cards
        ctr (str | Unset): Click-through rate: The number of product clicks for this product from the LIVE video,
            divided by the number of product impressions for this product from the LIVE video, including product clicks and
            product impressions for product lists and product cards
        add_to_cart_count (int | Unset): The number of times viewers add the product to their cart.
        click_to_order_rate (ClickToOrderRate | Unset):
        gpm (GetShopLIVEProductsPerformanceListResponseDataProductTrafficGpm | Unset):
        produt_clicks (int | Unset): The total number of times the product was clicked from this LIVE, including from
            the product list and product card
    """

    product_impressions: int | Unset = UNSET
    ctr: str | Unset = UNSET
    add_to_cart_count: int | Unset = UNSET
    click_to_order_rate: ClickToOrderRate | Unset = UNSET
    gpm: GetShopLIVEProductsPerformanceListResponseDataProductTrafficGpm | Unset = UNSET
    produt_clicks: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_impressions = self.product_impressions

        ctr = self.ctr

        add_to_cart_count = self.add_to_cart_count

        click_to_order_rate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.click_to_order_rate, Unset):
            click_to_order_rate = self.click_to_order_rate.to_dict()

        gpm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gpm, Unset):
            gpm = self.gpm.to_dict()

        produt_clicks = self.produt_clicks

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_impressions is not UNSET:
            field_dict["product_impressions"] = product_impressions
        if ctr is not UNSET:
            field_dict["ctr"] = ctr
        if add_to_cart_count is not UNSET:
            field_dict["add_to_cart_count"] = add_to_cart_count
        if click_to_order_rate is not UNSET:
            field_dict["click_to_order_rate"] = click_to_order_rate
        if gpm is not UNSET:
            field_dict["gpm"] = gpm
        if produt_clicks is not UNSET:
            field_dict["produt_clicks"] = produt_clicks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.click_to_order_rate import ClickToOrderRate  # noqa: PLC0415
        from ..models.get_shop_live_products_performance_list_response_data_product_traffic_gpm import (
            GetShopLIVEProductsPerformanceListResponseDataProductTrafficGpm,  # noqa: PLC0415
        )

        d = dict(src_dict)
        product_impressions = d.pop("product_impressions", UNSET)

        ctr = d.pop("ctr", UNSET)

        add_to_cart_count = d.pop("add_to_cart_count", UNSET)

        _click_to_order_rate = d.pop("click_to_order_rate", UNSET)
        click_to_order_rate: ClickToOrderRate | Unset
        if isinstance(_click_to_order_rate, Unset):
            click_to_order_rate = UNSET
        else:
            click_to_order_rate = ClickToOrderRate.from_dict(_click_to_order_rate)

        _gpm = d.pop("gpm", UNSET)
        gpm: GetShopLIVEProductsPerformanceListResponseDataProductTrafficGpm | Unset
        if isinstance(_gpm, Unset):
            gpm = UNSET
        else:
            gpm = GetShopLIVEProductsPerformanceListResponseDataProductTrafficGpm.from_dict(_gpm)

        produt_clicks = d.pop("produt_clicks", UNSET)

        get_shop_live_products_performance_list_response_data_product_traffic = cls(
            product_impressions=product_impressions,
            ctr=ctr,
            add_to_cart_count=add_to_cart_count,
            click_to_order_rate=click_to_order_rate,
            gpm=gpm,
            produt_clicks=produt_clicks,
        )

        get_shop_live_products_performance_list_response_data_product_traffic.additional_properties = d
        return get_shop_live_products_performance_list_response_data_product_traffic

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
