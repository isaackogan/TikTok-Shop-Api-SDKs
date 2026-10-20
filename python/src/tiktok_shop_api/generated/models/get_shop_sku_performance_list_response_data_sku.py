from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.gmv import Gmv





T = TypeVar("T", bound="GetShopSKUPerformanceListResponseDataSku")



@_attrs_define
class GetShopSKUPerformanceListResponseDataSku:
    """ 
        Attributes:
            id (int | Unset): The ID of the SKU in the returned SKU performance record.
            product_id (int | Unset): The ID of the product that the returned SKU belongs to.
            gmv (Gmv | Unset):
            sku_orders (int | Unset): Total (sum of all) orders for a SKU
            units_sold (int | Unset): Number of units sold for a SKU
     """

    id: int | Unset = UNSET
    product_id: int | Unset = UNSET
    gmv: Gmv | Unset = UNSET
    sku_orders: int | Unset = UNSET
    units_sold: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.gmv import Gmv # noqa: PLC0415
        id = self.id

        product_id = self.product_id

        gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gmv, Unset):
            gmv = self.gmv.to_dict()

        sku_orders = self.sku_orders

        units_sold = self.units_sold


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if gmv is not UNSET:
            field_dict["gmv"] = gmv
        if sku_orders is not UNSET:
            field_dict["sku_orders"] = sku_orders
        if units_sold is not UNSET:
            field_dict["units_sold"] = units_sold

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gmv import Gmv # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        product_id = d.pop("product_id", UNSET)

        _gmv = d.pop("gmv", UNSET)
        gmv: Gmv | Unset
        if isinstance(_gmv,  Unset):
            gmv = UNSET
        else:
            gmv = Gmv.from_dict(_gmv)




        sku_orders = d.pop("sku_orders", UNSET)

        units_sold = d.pop("units_sold", UNSET)

        get_shop_sku_performance_list_response_data_sku = cls(
            id=id,
            product_id=product_id,
            gmv=gmv,
            sku_orders=sku_orders,
            units_sold=units_sold,
        )


        get_shop_sku_performance_list_response_data_sku.additional_properties = d
        return get_shop_sku_performance_list_response_data_sku

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
