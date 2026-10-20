from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_global_seller_warehouses_response_data_global_warehouse import GetGlobalSellerWarehousesResponseDataGlobalWarehouse





T = TypeVar("T", bound="GetGlobalSellerWarehousesResponseData")



@_attrs_define
class GetGlobalSellerWarehousesResponseData:
    """ 
        Attributes:
            global_warehouses (list[GetGlobalSellerWarehousesResponseDataGlobalWarehouse] | Unset): A list of global
                warehouses associated with the seller.
     """

    global_warehouses: list[GetGlobalSellerWarehousesResponseDataGlobalWarehouse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_global_seller_warehouses_response_data_global_warehouse import GetGlobalSellerWarehousesResponseDataGlobalWarehouse # noqa: PLC0415
        global_warehouses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.global_warehouses, Unset):
            global_warehouses = []
            for global_warehouses_item_data in self.global_warehouses:
                global_warehouses_item = global_warehouses_item_data.to_dict()
                global_warehouses.append(global_warehouses_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if global_warehouses is not UNSET:
            field_dict["global_warehouses"] = global_warehouses

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_global_seller_warehouses_response_data_global_warehouse import GetGlobalSellerWarehousesResponseDataGlobalWarehouse # noqa: PLC0415
        d = dict(src_dict)
        _global_warehouses = d.pop("global_warehouses", UNSET)
        global_warehouses: list[GetGlobalSellerWarehousesResponseDataGlobalWarehouse] | Unset = UNSET
        if _global_warehouses is not UNSET:
            global_warehouses = []
            for global_warehouses_item_data in _global_warehouses:
                global_warehouses_item = GetGlobalSellerWarehousesResponseDataGlobalWarehouse.from_dict(global_warehouses_item_data)



                global_warehouses.append(global_warehouses_item)


        get_global_seller_warehouses_response_data = cls(
            global_warehouses=global_warehouses,
        )


        get_global_seller_warehouses_response_data.additional_properties = d
        return get_global_seller_warehouses_response_data

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
