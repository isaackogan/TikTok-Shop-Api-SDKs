from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.partial_edit_product_request_replicated_product_region import (
    PartialEditProductRequestReplicatedProductRegion,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.partial_edit_product_request_replicated_product_sku import (
        PartialEditProductRequestReplicatedProductSku,
    )


T = TypeVar("T", bound="PartialEditProductRequestReplicatedProduct")


@_attrs_define
class PartialEditProductRequestReplicatedProduct:
    """
    Attributes:
        region (PartialEditProductRequestReplicatedProductRegion): The local market replica region to which this
            product's updates should be synchronized.
            Possible values:
            - AT: Austria
            - BE:Belgium
            - CZ:Czech Republic
            - DE: Germany
            - ES: Spain
            - FR: France
            - GB: United Kingdom
            - GR: Greece
            - HU:Hungary
            - ID: Indonesia
            - IE: Ireland
            - IT: Italy
            - JP: Japan
            - MY: Malaysia
            - NL: Netherlands(NL)
            - PH: Philippines
            - PO: Poland
            - PT:Portugal
            - SG: Singapore
            - TH: Thailand
            - US: United States
            - VN: Vietnam
            - MX: Mexico
        inventory_mode (str | Unset): Defines the inventory mode for the duplicated target product. This parameter
            supports two modes: SHARED and EXCLUSIVE.

            - SHARED: In this mode, the inventory of all interconnected (shared) products must be strictly consistent;
            otherwise, an error will be returned.
            - EXCLUSIVE: In this mode, the inventory for each product can be set independently without affecting others.

            Applicability:
            This feature is applicable ONLY for the EU market.

            Default Value:
            If left empty, the system defaults to the EXCLUSIVE mode.
        skus (list[PartialEditProductRequestReplicatedProductSku] | Unset): The SKUs to be synced to the specified
            market.
            Specify this **only if** you are adding SKUs or changing the sales attribute id/name.
            **Note**:
            - You must pass in all existing SKUs. Any existing SKU IDs not listed here will result in the deletion of those
            SKUs. For example, if this product contains 5 SKUs and you only provide 2 SKU IDs, the remaining 3 will be
            deleted.
            - To create new SKUs, leave the SKU ID blank and provide the seller_sku.
    """

    region: PartialEditProductRequestReplicatedProductRegion
    inventory_mode: str | Unset = UNSET
    skus: list[PartialEditProductRequestReplicatedProductSku] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        region = self.region.value

        inventory_mode = self.inventory_mode

        skus: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.skus, Unset):
            skus = []
            for skus_item_data in self.skus:
                skus_item = skus_item_data.to_dict()
                skus.append(skus_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "region": region,
            }
        )
        if inventory_mode is not UNSET:
            field_dict["inventory_mode"] = inventory_mode
        if skus is not UNSET:
            field_dict["skus"] = skus

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.partial_edit_product_request_replicated_product_sku import (
            PartialEditProductRequestReplicatedProductSku,  # noqa: PLC0415
        )

        d = dict(src_dict)
        region = PartialEditProductRequestReplicatedProductRegion(d.pop("region"))

        inventory_mode = d.pop("inventory_mode", UNSET)

        _skus = d.pop("skus", UNSET)
        skus: list[PartialEditProductRequestReplicatedProductSku] | Unset = UNSET
        if _skus is not UNSET:
            skus = []
            for skus_item_data in _skus:
                skus_item = PartialEditProductRequestReplicatedProductSku.from_dict(skus_item_data)

                skus.append(skus_item)

        partial_edit_product_request_replicated_product = cls(
            region=region,
            inventory_mode=inventory_mode,
            skus=skus,
        )

        partial_edit_product_request_replicated_product.additional_properties = d
        return partial_edit_product_request_replicated_product

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
