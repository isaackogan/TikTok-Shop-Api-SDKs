from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_global_listing_rules_response_data_inventory_rule import (
        GetGlobalListingRulesResponseDataInventoryRule,
    )


T = TypeVar("T", bound="GetGlobalListingRulesResponseData")


@_attrs_define
class GetGlobalListingRulesResponseData:
    """
    Attributes:
        listing_methods (list[str] | Unset): The methods at which sellers can list products in this shop.
            Possible values:
            - GLOBAL_PUBLISHING: Create a global product, then publish it to target local markets.
            - LOCAL_REPLICATION: Create local product, then replicate it to other target local markets.
        inventory_rules (list[GetGlobalListingRulesResponseDataInventoryRule] | Unset): A list of inventory allocation
            rules for all warehouses linked to the shop.
    """

    listing_methods: list[str] | Unset = UNSET
    inventory_rules: list[GetGlobalListingRulesResponseDataInventoryRule] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        listing_methods: list[str] | Unset = UNSET
        if not isinstance(self.listing_methods, Unset):
            listing_methods = self.listing_methods

        inventory_rules: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.inventory_rules, Unset):
            inventory_rules = []
            for inventory_rules_item_data in self.inventory_rules:
                inventory_rules_item = inventory_rules_item_data.to_dict()
                inventory_rules.append(inventory_rules_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if listing_methods is not UNSET:
            field_dict["listing_methods"] = listing_methods
        if inventory_rules is not UNSET:
            field_dict["inventory_rules"] = inventory_rules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_global_listing_rules_response_data_inventory_rule import (
            GetGlobalListingRulesResponseDataInventoryRule,  # noqa: PLC0415
        )

        d = dict(src_dict)
        listing_methods = cast(list[str], d.pop("listing_methods", UNSET))

        _inventory_rules = d.pop("inventory_rules", UNSET)
        inventory_rules: list[GetGlobalListingRulesResponseDataInventoryRule] | Unset = UNSET
        if _inventory_rules is not UNSET:
            inventory_rules = []
            for inventory_rules_item_data in _inventory_rules:
                inventory_rules_item = GetGlobalListingRulesResponseDataInventoryRule.from_dict(
                    inventory_rules_item_data
                )

                inventory_rules.append(inventory_rules_item)

        get_global_listing_rules_response_data = cls(
            listing_methods=listing_methods,
            inventory_rules=inventory_rules,
        )

        get_global_listing_rules_response_data.additional_properties = d
        return get_global_listing_rules_response_data

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
