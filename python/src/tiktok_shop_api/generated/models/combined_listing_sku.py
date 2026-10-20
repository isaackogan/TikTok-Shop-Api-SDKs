from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CombinedListingSku")


@_attrs_define
class CombinedListingSku:
    """
    Attributes:
        sku_id (str | Unset): The original `sku_id` related to the virtual bundle SKU.
        sku_count (int | Unset): The quantity of original SKU that compose the virtual bundle SKU.
        product_id (str | Unset): The original `product_id` related to the virtual bundle SKU.
        seller_sku (str | Unset): The original `seller_sku` (which is defined by sellers) related to the virtual bundle
            SKU.
    """

    sku_id: str | Unset = UNSET
    sku_count: int | Unset = UNSET
    product_id: str | Unset = UNSET
    seller_sku: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sku_id = self.sku_id

        sku_count = self.sku_count

        product_id = self.product_id

        seller_sku = self.seller_sku

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sku_id is not UNSET:
            field_dict["sku_id"] = sku_id
        if sku_count is not UNSET:
            field_dict["sku_count"] = sku_count
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if seller_sku is not UNSET:
            field_dict["seller_sku"] = seller_sku

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sku_id = d.pop("sku_id", UNSET)

        sku_count = d.pop("sku_count", UNSET)

        product_id = d.pop("product_id", UNSET)

        seller_sku = d.pop("seller_sku", UNSET)

        combined_listing_sku = cls(
            sku_id=sku_id,
            sku_count=sku_count,
            product_id=product_id,
            seller_sku=seller_sku,
        )

        combined_listing_sku.additional_properties = d
        return combined_listing_sku

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
