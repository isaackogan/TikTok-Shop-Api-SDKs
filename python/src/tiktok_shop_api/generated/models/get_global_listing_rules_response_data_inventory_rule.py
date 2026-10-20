from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_global_listing_rules_response_data_inventory_rule_associated_warehouse import GetGlobalListingRulesResponseDataInventoryRuleAssociatedWarehouse





T = TypeVar("T", bound="GetGlobalListingRulesResponseDataInventoryRule")



@_attrs_define
class GetGlobalListingRulesResponseDataInventoryRule:
    """ 
        Attributes:
            local_warehouse_id (str | Unset): The warehouse ID associated with the shop.
            allocation_mode (str | Unset): The inventory allocation mode used for this warehouse in the local market.
                `SHARED` – Inventory is pooled across all covered markets. An inventory deduction in one market reflects across
                all.
                `DYNAMIC` – Inventory is divided proportionally among covered markets. An inventory deduction in one market
                affects only that market.
                `MANUAL` – Inventory is configured independently by sellers for each market. An inventory deduction in one
                market affects only that market.
            associated_warehouses (list[GetGlobalListingRulesResponseDataInventoryRuleAssociatedWarehouse] | Unset): A list
                of associated warehouses whose inventory is shared with or dynamically allocated from this warehouse. Each item
                identifies a warehouse and its region.
                **Note**: Applicable only when `allocation_mode` is `SHARED` or `DYNAMIC`.
     """

    local_warehouse_id: str | Unset = UNSET
    allocation_mode: str | Unset = UNSET
    associated_warehouses: list[GetGlobalListingRulesResponseDataInventoryRuleAssociatedWarehouse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_global_listing_rules_response_data_inventory_rule_associated_warehouse import GetGlobalListingRulesResponseDataInventoryRuleAssociatedWarehouse # noqa: PLC0415
        local_warehouse_id = self.local_warehouse_id

        allocation_mode = self.allocation_mode

        associated_warehouses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.associated_warehouses, Unset):
            associated_warehouses = []
            for associated_warehouses_item_data in self.associated_warehouses:
                associated_warehouses_item = associated_warehouses_item_data.to_dict()
                associated_warehouses.append(associated_warehouses_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if local_warehouse_id is not UNSET:
            field_dict["local_warehouse_id"] = local_warehouse_id
        if allocation_mode is not UNSET:
            field_dict["allocation_mode"] = allocation_mode
        if associated_warehouses is not UNSET:
            field_dict["associated_warehouses"] = associated_warehouses

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_global_listing_rules_response_data_inventory_rule_associated_warehouse import GetGlobalListingRulesResponseDataInventoryRuleAssociatedWarehouse # noqa: PLC0415
        d = dict(src_dict)
        local_warehouse_id = d.pop("local_warehouse_id", UNSET)

        allocation_mode = d.pop("allocation_mode", UNSET)

        _associated_warehouses = d.pop("associated_warehouses", UNSET)
        associated_warehouses: list[GetGlobalListingRulesResponseDataInventoryRuleAssociatedWarehouse] | Unset = UNSET
        if _associated_warehouses is not UNSET:
            associated_warehouses = []
            for associated_warehouses_item_data in _associated_warehouses:
                associated_warehouses_item = GetGlobalListingRulesResponseDataInventoryRuleAssociatedWarehouse.from_dict(associated_warehouses_item_data)



                associated_warehouses.append(associated_warehouses_item)


        get_global_listing_rules_response_data_inventory_rule = cls(
            local_warehouse_id=local_warehouse_id,
            allocation_mode=allocation_mode,
            associated_warehouses=associated_warehouses,
        )


        get_global_listing_rules_response_data_inventory_rule.additional_properties = d
        return get_global_listing_rules_response_data_inventory_rule

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
