from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProductCreationWebhookData")


@_attrs_define
class ProductCreationWebhookData:
    """
    Attributes:
        product_id (int | Unset): The identification of a TikTok Shop product
        product_types (list[str] | Unset): The type of product, including:

             * COMBINED_PRODUCT: Virtual bundle product.
             * GPR_PRODUCT: Target products created using the GPR tool
        update_time (int | Unset): The time when the product was created, represented as a Unix timestamp (seconds).
    """

    product_id: int | Unset = UNSET
    product_types: list[str] | Unset = UNSET
    update_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        product_types: list[str] | Unset = UNSET
        if not isinstance(self.product_types, Unset):
            product_types = self.product_types

        update_time = self.update_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if product_types is not UNSET:
            field_dict["product_types"] = product_types
        if update_time is not UNSET:
            field_dict["update_time"] = update_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_id = d.pop("product_id", UNSET)

        product_types = cast(list[str], d.pop("product_types", UNSET))

        update_time = d.pop("update_time", UNSET)

        product_creation_webhook_data = cls(
            product_id=product_id,
            product_types=product_types,
            update_time=update_time,
        )

        product_creation_webhook_data.additional_properties = d
        return product_creation_webhook_data

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
