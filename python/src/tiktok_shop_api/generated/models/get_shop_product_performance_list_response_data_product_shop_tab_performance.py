from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_shop_product_performance_list_response_data_product_shop_tab_performance_shop_tab_gmv import GetShopProductPerformanceListResponseDataProductShopTabPerformanceShopTabGmv





T = TypeVar("T", bound="GetShopProductPerformanceListResponseDataProductShopTabPerformance")



@_attrs_define
class GetShopProductPerformanceListResponseDataProductShopTabPerformance:
    """ 
        Attributes:
            shop_tab_product_impressions (int | Unset): Number of product impressions from Shop Tab.
            shop_tab_product_clicks (int | Unset): Number of product clicks from Shop Tab.
            unique_shop_tab_product_clicks (int | Unset): Number of unique product clicks from Shop Tab.
            estimated_shop_tab_customers (int | Unset): Estimated number of customers from Shop Tab.
            shop_tab_ctr (str | Unset): Click-through rate from Shop Tab.
            shop_tab_ctor_sku (str | Unset): Click-to-order rate (SKU level) from Shop Tab.
            shop_tab_gmv (GetShopProductPerformanceListResponseDataProductShopTabPerformanceShopTabGmv | Unset):
            shop_tab_sold_items (int | Unset): Items sold via shop tab.
     """

    shop_tab_product_impressions: int | Unset = UNSET
    shop_tab_product_clicks: int | Unset = UNSET
    unique_shop_tab_product_clicks: int | Unset = UNSET
    estimated_shop_tab_customers: int | Unset = UNSET
    shop_tab_ctr: str | Unset = UNSET
    shop_tab_ctor_sku: str | Unset = UNSET
    shop_tab_gmv: GetShopProductPerformanceListResponseDataProductShopTabPerformanceShopTabGmv | Unset = UNSET
    shop_tab_sold_items: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_shop_product_performance_list_response_data_product_shop_tab_performance_shop_tab_gmv import GetShopProductPerformanceListResponseDataProductShopTabPerformanceShopTabGmv # noqa: PLC0415
        shop_tab_product_impressions = self.shop_tab_product_impressions

        shop_tab_product_clicks = self.shop_tab_product_clicks

        unique_shop_tab_product_clicks = self.unique_shop_tab_product_clicks

        estimated_shop_tab_customers = self.estimated_shop_tab_customers

        shop_tab_ctr = self.shop_tab_ctr

        shop_tab_ctor_sku = self.shop_tab_ctor_sku

        shop_tab_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shop_tab_gmv, Unset):
            shop_tab_gmv = self.shop_tab_gmv.to_dict()

        shop_tab_sold_items = self.shop_tab_sold_items


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if shop_tab_product_impressions is not UNSET:
            field_dict["shop_tab_product_impressions"] = shop_tab_product_impressions
        if shop_tab_product_clicks is not UNSET:
            field_dict["shop_tab_product_clicks"] = shop_tab_product_clicks
        if unique_shop_tab_product_clicks is not UNSET:
            field_dict["unique_shop_tab_product_clicks"] = unique_shop_tab_product_clicks
        if estimated_shop_tab_customers is not UNSET:
            field_dict["estimated_shop_tab_customers"] = estimated_shop_tab_customers
        if shop_tab_ctr is not UNSET:
            field_dict["shop_tab_ctr"] = shop_tab_ctr
        if shop_tab_ctor_sku is not UNSET:
            field_dict["shop_tab_ctor_sku"] = shop_tab_ctor_sku
        if shop_tab_gmv is not UNSET:
            field_dict["shop_tab_gmv"] = shop_tab_gmv
        if shop_tab_sold_items is not UNSET:
            field_dict["shop_tab_sold_items"] = shop_tab_sold_items

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shop_product_performance_list_response_data_product_shop_tab_performance_shop_tab_gmv import GetShopProductPerformanceListResponseDataProductShopTabPerformanceShopTabGmv # noqa: PLC0415
        d = dict(src_dict)
        shop_tab_product_impressions = d.pop("shop_tab_product_impressions", UNSET)

        shop_tab_product_clicks = d.pop("shop_tab_product_clicks", UNSET)

        unique_shop_tab_product_clicks = d.pop("unique_shop_tab_product_clicks", UNSET)

        estimated_shop_tab_customers = d.pop("estimated_shop_tab_customers", UNSET)

        shop_tab_ctr = d.pop("shop_tab_ctr", UNSET)

        shop_tab_ctor_sku = d.pop("shop_tab_ctor_sku", UNSET)

        _shop_tab_gmv = d.pop("shop_tab_gmv", UNSET)
        shop_tab_gmv: GetShopProductPerformanceListResponseDataProductShopTabPerformanceShopTabGmv | Unset
        if isinstance(_shop_tab_gmv,  Unset):
            shop_tab_gmv = UNSET
        else:
            shop_tab_gmv = GetShopProductPerformanceListResponseDataProductShopTabPerformanceShopTabGmv.from_dict(_shop_tab_gmv)




        shop_tab_sold_items = d.pop("shop_tab_sold_items", UNSET)

        get_shop_product_performance_list_response_data_product_shop_tab_performance = cls(
            shop_tab_product_impressions=shop_tab_product_impressions,
            shop_tab_product_clicks=shop_tab_product_clicks,
            unique_shop_tab_product_clicks=unique_shop_tab_product_clicks,
            estimated_shop_tab_customers=estimated_shop_tab_customers,
            shop_tab_ctr=shop_tab_ctr,
            shop_tab_ctor_sku=shop_tab_ctor_sku,
            shop_tab_gmv=shop_tab_gmv,
            shop_tab_sold_items=shop_tab_sold_items,
        )


        get_shop_product_performance_list_response_data_product_shop_tab_performance.additional_properties = d
        return get_shop_product_performance_list_response_data_product_shop_tab_performance

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
