from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.edit_product_request_replicated_product_region import EditProductRequestReplicatedProductRegion
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.edit_product_request_replicated_product_sku import EditProductRequestReplicatedProductSku


T = TypeVar("T", bound="EditProductRequestReplicatedProduct")


@_attrs_define
class EditProductRequestReplicatedProduct:
    """
    Attributes:
        region (EditProductRequestReplicatedProductRegion): The market where you want to sync the changes to. The market
            must already contain a replica. Use the Get Global Replicated Products to check the markets that contain a
            replica.
            Possible values:
            - DE: Germany
            - ES: Spain
            - FR: France
            - GB: United Kingdom
            - ID: Indonesia
            - IE: Ireland
            - IT: Italy
            - JP: Japan
            - MY: Malaysia
            - PH: Philippines
            - SG: Singapore
            - TH: Thailand
            - US: United States
            - VN: Vietnam
        skus (list[EditProductRequestReplicatedProductSku] | Unset): The SKUs to be synced to the specified market.

            **Note**:
            - You must pass in all existing SKUs. Any existing SKU IDs not listed here will result in the deletion of those
            SKUs. For example, if this product contains 5 SKUs and you only provide 2 SKU IDs, the remaining 3 will be
            deleted.
            - To create new SKUs, leave the SKU ID blank and provide the seller_sku.
        inventory_mode (str | Unset): Defines the inventory mode for the duplicated target product. This parameter
            supports two modes: SHARED and EXCLUSIVE.

            - SHARED: In this mode, the inventory of all interconnected (shared) products must be strictly consistent;
            otherwise, an error will be returned.
            - EXCLUSIVE: In this mode, the inventory for each product can be set independently without affecting others.

            Applicability:
            This feature is applicable ONLY for the EU market.

            Default Value:
            If left empty, the system defaults to the EXCLUSIVE mode.
    """

    region: EditProductRequestReplicatedProductRegion
    skus: list[EditProductRequestReplicatedProductSku] | Unset = UNSET
    inventory_mode: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        region = self.region.value

        skus: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.skus, Unset):
            skus = []
            for skus_item_data in self.skus:
                skus_item = skus_item_data.to_dict()
                skus.append(skus_item)

        inventory_mode = self.inventory_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "region": region,
            }
        )
        if skus is not UNSET:
            field_dict["skus"] = skus
        if inventory_mode is not UNSET:
            field_dict["inventory_mode"] = inventory_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.edit_product_request_replicated_product_sku import (
            EditProductRequestReplicatedProductSku,  # noqa: PLC0415
        )

        d = dict(src_dict)
        region = EditProductRequestReplicatedProductRegion(d.pop("region"))

        _skus = d.pop("skus", UNSET)
        skus: list[EditProductRequestReplicatedProductSku] | Unset = UNSET
        if _skus is not UNSET:
            skus = []
            for skus_item_data in _skus:
                skus_item = EditProductRequestReplicatedProductSku.from_dict(skus_item_data)

                skus.append(skus_item)

        inventory_mode = d.pop("inventory_mode", UNSET)

        edit_product_request_replicated_product = cls(
            region=region,
            skus=skus,
            inventory_mode=inventory_mode,
        )

        edit_product_request_replicated_product.additional_properties = d
        return edit_product_request_replicated_product

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
