from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.replicate_product_request_inventory_mode import ReplicateProductRequestInventoryMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.replicate_product_request_replicate_target import ReplicateProductRequestReplicateTarget


T = TypeVar("T", bound="ReplicateProductRequest")


@_attrs_define
class ReplicateProductRequest:
    """
    Attributes:
        inventory_mode (ReplicateProductRequestInventoryMode | Unset): The inventory mode for the source product in the
            source shop. This field is applicable only to EU markets. Possible values:
            - SHARED: Inventory for interconnected products must remain consistent; otherwise, an error is returned.
            - EXCLUSIVE: Inventory for each product can be set independently without affecting the others.

            If omitted, the inventory mode defaults to EXCLUSIVE.
        replicate_target (list[ReplicateProductRequestReplicateTarget] | Unset): Target markets for replicating the
            local product.
    """

    inventory_mode: ReplicateProductRequestInventoryMode | Unset = UNSET
    replicate_target: list[ReplicateProductRequestReplicateTarget] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inventory_mode: str | Unset = UNSET
        if not isinstance(self.inventory_mode, Unset):
            inventory_mode = self.inventory_mode.value

        replicate_target: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.replicate_target, Unset):
            replicate_target = []
            for replicate_target_item_data in self.replicate_target:
                replicate_target_item = replicate_target_item_data.to_dict()
                replicate_target.append(replicate_target_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inventory_mode is not UNSET:
            field_dict["inventory_mode"] = inventory_mode
        if replicate_target is not UNSET:
            field_dict["replicate_target"] = replicate_target

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.replicate_product_request_replicate_target import (
            ReplicateProductRequestReplicateTarget,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _inventory_mode = d.pop("inventory_mode", UNSET)
        inventory_mode: ReplicateProductRequestInventoryMode | Unset
        if isinstance(_inventory_mode, Unset):
            inventory_mode = UNSET
        else:
            inventory_mode = ReplicateProductRequestInventoryMode(_inventory_mode)

        _replicate_target = d.pop("replicate_target", UNSET)
        replicate_target: list[ReplicateProductRequestReplicateTarget] | Unset = UNSET
        if _replicate_target is not UNSET:
            replicate_target = []
            for replicate_target_item_data in _replicate_target:
                replicate_target_item = ReplicateProductRequestReplicateTarget.from_dict(replicate_target_item_data)

                replicate_target.append(replicate_target_item)

        replicate_product_request = cls(
            inventory_mode=inventory_mode,
            replicate_target=replicate_target,
        )

        replicate_product_request.additional_properties = d
        return replicate_product_request

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
