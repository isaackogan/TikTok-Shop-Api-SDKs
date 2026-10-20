from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.search_fbt_inventory_response_data_inventory import SearchFBTInventoryResponseDataInventory





T = TypeVar("T", bound="SearchFBTInventoryResponseData")



@_attrs_define
class SearchFBTInventoryResponseData:
    """ 
        Attributes:
            next_page_token (str | Unset): An opaque token used to retrieve the next page of a paginated result set. Provide
                this value in the `page_token` parameter of your next request. An empty `next_page_token` means there are no
                more pages.
            total_count (int | Unset): The total number of warehouse-goods inventory records that match the applied filters.
            inventory (list[SearchFBTInventoryResponseDataInventory] | Unset): A list of inventory records. Each item
                represents one goods item at one Fulfilled by TikTok warehouse and can include the associated SKU inventory
                breakdown.
     """

    next_page_token: str | Unset = UNSET
    total_count: int | Unset = UNSET
    inventory: list[SearchFBTInventoryResponseDataInventory] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.search_fbt_inventory_response_data_inventory import SearchFBTInventoryResponseDataInventory # noqa: PLC0415
        next_page_token = self.next_page_token

        total_count = self.total_count

        inventory: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.inventory, Unset):
            inventory = []
            for inventory_item_data in self.inventory:
                inventory_item = inventory_item_data.to_dict()
                inventory.append(inventory_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if inventory is not UNSET:
            field_dict["inventory"] = inventory

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_fbt_inventory_response_data_inventory import SearchFBTInventoryResponseDataInventory # noqa: PLC0415
        d = dict(src_dict)
        next_page_token = d.pop("next_page_token", UNSET)

        total_count = d.pop("total_count", UNSET)

        _inventory = d.pop("inventory", UNSET)
        inventory: list[SearchFBTInventoryResponseDataInventory] | Unset = UNSET
        if _inventory is not UNSET:
            inventory = []
            for inventory_item_data in _inventory:
                inventory_item = SearchFBTInventoryResponseDataInventory.from_dict(inventory_item_data)



                inventory.append(inventory_item)


        search_fbt_inventory_response_data = cls(
            next_page_token=next_page_token,
            total_count=total_count,
            inventory=inventory,
        )


        search_fbt_inventory_response_data.additional_properties = d
        return search_fbt_inventory_response_data

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
