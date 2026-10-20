from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.partial_edit_product_request_replicated_product_sku_inventory import PartialEditProductRequestReplicatedProductSkuInventory
  from ..models.replicate_product_request_replicate_target_sku_price import ReplicateProductRequestReplicateTargetSkuPrice





T = TypeVar("T", bound="ReplicateProductRequestReplicateTargetSku")



@_attrs_define
class ReplicateProductRequestReplicateTargetSku:
    """ 
        Attributes:
            inventory (list[PartialEditProductRequestReplicatedProductSkuInventory] | Unset): SKU inventory information per
                warehouse.
                This field is only required if the inventory allocation mode for the warehouse is MANUAL. Otherwise, it is
                optional.
            price (ReplicateProductRequestReplicateTargetSkuPrice | Unset):
            source_sku_id (str | Unset): The ID of the SKU being replicated
            seller_sku (str | Unset): An internal code/name for managing SKUs, not visible to buyers.
                Valid length:
                - DE, ES, FR, IT, PL, NL, BE, CZ, AT, GR, PT, HU: 6-50 characters
                - Other regions: 1-50 characters
                Format:
                - DE, ES, FR, IT, PL, NL, BE, CZ, AT, GR, PT, HU: Use alphabets, numbers, hyphens (-), or underscores (_) only
                - Other regions: Text without spaces
     """

    inventory: list[PartialEditProductRequestReplicatedProductSkuInventory] | Unset = UNSET
    price: ReplicateProductRequestReplicateTargetSkuPrice | Unset = UNSET
    source_sku_id: str | Unset = UNSET
    seller_sku: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.partial_edit_product_request_replicated_product_sku_inventory import PartialEditProductRequestReplicatedProductSkuInventory # noqa: PLC0415
        from ..models.replicate_product_request_replicate_target_sku_price import ReplicateProductRequestReplicateTargetSkuPrice # noqa: PLC0415
        inventory: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.inventory, Unset):
            inventory = []
            for inventory_item_data in self.inventory:
                inventory_item = inventory_item_data.to_dict()
                inventory.append(inventory_item)



        price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.price, Unset):
            price = self.price.to_dict()

        source_sku_id = self.source_sku_id

        seller_sku = self.seller_sku


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if inventory is not UNSET:
            field_dict["inventory"] = inventory
        if price is not UNSET:
            field_dict["price"] = price
        if source_sku_id is not UNSET:
            field_dict["source_sku_id"] = source_sku_id
        if seller_sku is not UNSET:
            field_dict["seller_sku"] = seller_sku

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.partial_edit_product_request_replicated_product_sku_inventory import PartialEditProductRequestReplicatedProductSkuInventory # noqa: PLC0415
        from ..models.replicate_product_request_replicate_target_sku_price import ReplicateProductRequestReplicateTargetSkuPrice # noqa: PLC0415
        d = dict(src_dict)
        _inventory = d.pop("inventory", UNSET)
        inventory: list[PartialEditProductRequestReplicatedProductSkuInventory] | Unset = UNSET
        if _inventory is not UNSET:
            inventory = []
            for inventory_item_data in _inventory:
                inventory_item = PartialEditProductRequestReplicatedProductSkuInventory.from_dict(inventory_item_data)



                inventory.append(inventory_item)


        _price = d.pop("price", UNSET)
        price: ReplicateProductRequestReplicateTargetSkuPrice | Unset
        if isinstance(_price,  Unset):
            price = UNSET
        else:
            price = ReplicateProductRequestReplicateTargetSkuPrice.from_dict(_price)




        source_sku_id = d.pop("source_sku_id", UNSET)

        seller_sku = d.pop("seller_sku", UNSET)

        replicate_product_request_replicate_target_sku = cls(
            inventory=inventory,
            price=price,
            source_sku_id=source_sku_id,
            seller_sku=seller_sku,
        )


        replicate_product_request_replicate_target_sku.additional_properties = d
        return replicate_product_request_replicate_target_sku

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
