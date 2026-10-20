from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="InventorySearchResponseDataInventorySkuTotalAvailableInventoryDistributionCreatorInventory")



@_attrs_define
class InventorySearchResponseDataInventorySkuTotalAvailableInventoryDistributionCreatorInventory:
    """ 
        Attributes:
            quantity (int | Unset): The number of units allocated.
            creator_name (str | Unset): The name of the associated TikTok creator.
     """

    quantity: int | Unset = UNSET
    creator_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        quantity = self.quantity

        creator_name = self.creator_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if creator_name is not UNSET:
            field_dict["creator_name"] = creator_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        quantity = d.pop("quantity", UNSET)

        creator_name = d.pop("creator_name", UNSET)

        inventory_search_response_data_inventory_sku_total_available_inventory_distribution_creator_inventory = cls(
            quantity=quantity,
            creator_name=creator_name,
        )


        inventory_search_response_data_inventory_sku_total_available_inventory_distribution_creator_inventory.additional_properties = d
        return inventory_search_response_data_inventory_sku_total_available_inventory_distribution_creator_inventory

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
