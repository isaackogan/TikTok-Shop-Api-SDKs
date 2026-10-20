from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_shop_live_products_performance_list_response_data_product_sale import GetShopLIVEProductsPerformanceListResponseDataProductSale
  from ..models.get_shop_live_products_performance_list_response_data_product_traffic import GetShopLIVEProductsPerformanceListResponseDataProductTraffic





T = TypeVar("T", bound="GetShopLIVEProductsPerformanceListResponseDataProduct")



@_attrs_define
class GetShopLIVEProductsPerformanceListResponseDataProduct:
    """ 
        Attributes:
            id (str | Unset): Product id
            name (str | Unset): Product name
            sales (GetShopLIVEProductsPerformanceListResponseDataProductSale | Unset):
            traffic (GetShopLIVEProductsPerformanceListResponseDataProductTraffic | Unset):
     """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    sales: GetShopLIVEProductsPerformanceListResponseDataProductSale | Unset = UNSET
    traffic: GetShopLIVEProductsPerformanceListResponseDataProductTraffic | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_shop_live_products_performance_list_response_data_product_sale import GetShopLIVEProductsPerformanceListResponseDataProductSale # noqa: PLC0415
        from ..models.get_shop_live_products_performance_list_response_data_product_traffic import GetShopLIVEProductsPerformanceListResponseDataProductTraffic # noqa: PLC0415
        id = self.id

        name = self.name

        sales: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sales, Unset):
            sales = self.sales.to_dict()

        traffic: dict[str, Any] | Unset = UNSET
        if not isinstance(self.traffic, Unset):
            traffic = self.traffic.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if sales is not UNSET:
            field_dict["sales"] = sales
        if traffic is not UNSET:
            field_dict["traffic"] = traffic

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shop_live_products_performance_list_response_data_product_sale import GetShopLIVEProductsPerformanceListResponseDataProductSale # noqa: PLC0415
        from ..models.get_shop_live_products_performance_list_response_data_product_traffic import GetShopLIVEProductsPerformanceListResponseDataProductTraffic # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _sales = d.pop("sales", UNSET)
        sales: GetShopLIVEProductsPerformanceListResponseDataProductSale | Unset
        if isinstance(_sales,  Unset):
            sales = UNSET
        else:
            sales = GetShopLIVEProductsPerformanceListResponseDataProductSale.from_dict(_sales)




        _traffic = d.pop("traffic", UNSET)
        traffic: GetShopLIVEProductsPerformanceListResponseDataProductTraffic | Unset
        if isinstance(_traffic,  Unset):
            traffic = UNSET
        else:
            traffic = GetShopLIVEProductsPerformanceListResponseDataProductTraffic.from_dict(_traffic)




        get_shop_live_products_performance_list_response_data_product = cls(
            id=id,
            name=name,
            sales=sales,
            traffic=traffic,
        )


        get_shop_live_products_performance_list_response_data_product.additional_properties = d
        return get_shop_live_products_performance_list_response_data_product

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
