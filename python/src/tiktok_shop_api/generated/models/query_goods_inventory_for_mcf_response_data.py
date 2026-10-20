from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.query_goods_inventory_for_mcf_response_data_goods_inventory_list import QueryGoodsInventoryForMCFResponseDataGoodsInventoryList





T = TypeVar("T", bound="QueryGoodsInventoryForMCFResponseData")



@_attrs_define
class QueryGoodsInventoryForMCFResponseData:
    """ 
        Attributes:
            goods_inventory_list (list[QueryGoodsInventoryForMCFResponseDataGoodsInventoryList] | Unset): Inventory entries
                for the requested goods. For MCF, only goods associated with the seller for the shop region and having an
                inventory-group result are returned. A requested goods ID without an inventory-group result is omitted; the API
                does not add an entry with `available_qty` set to `0`. The list is empty when none of the requested goods has an
                inventory-group result. Each entry represents one goods-and-inventory-group result, so the same `goods_id` may
                appear in multiple entries when it has multiple inventory groups. Request goods IDs are not deduplicated;
                repeating a `goods_id` may repeat the same inventory-group entries. Include each `goods_id` only once, and do
                not align response entries with request entries by list position.
     """

    goods_inventory_list: list[QueryGoodsInventoryForMCFResponseDataGoodsInventoryList] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.query_goods_inventory_for_mcf_response_data_goods_inventory_list import QueryGoodsInventoryForMCFResponseDataGoodsInventoryList # noqa: PLC0415
        goods_inventory_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.goods_inventory_list, Unset):
            goods_inventory_list = []
            for goods_inventory_list_item_data in self.goods_inventory_list:
                goods_inventory_list_item = goods_inventory_list_item_data.to_dict()
                goods_inventory_list.append(goods_inventory_list_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if goods_inventory_list is not UNSET:
            field_dict["goods_inventory_list"] = goods_inventory_list

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.query_goods_inventory_for_mcf_response_data_goods_inventory_list import QueryGoodsInventoryForMCFResponseDataGoodsInventoryList # noqa: PLC0415
        d = dict(src_dict)
        _goods_inventory_list = d.pop("goods_inventory_list", UNSET)
        goods_inventory_list: list[QueryGoodsInventoryForMCFResponseDataGoodsInventoryList] | Unset = UNSET
        if _goods_inventory_list is not UNSET:
            goods_inventory_list = []
            for goods_inventory_list_item_data in _goods_inventory_list:
                goods_inventory_list_item = QueryGoodsInventoryForMCFResponseDataGoodsInventoryList.from_dict(goods_inventory_list_item_data)



                goods_inventory_list.append(goods_inventory_list_item)


        query_goods_inventory_for_mcf_response_data = cls(
            goods_inventory_list=goods_inventory_list,
        )


        query_goods_inventory_for_mcf_response_data.additional_properties = d
        return query_goods_inventory_for_mcf_response_data

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
