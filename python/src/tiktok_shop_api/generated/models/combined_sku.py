from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CombinedSku")


@_attrs_define
class CombinedSku:
    """
    Attributes:
        product_id (str): The ID of the source product included in the virtual bundle.
        sku_id (str): The ID of the source SKU included in the virtual bundle.
        sku_count (int): The quantity of the source SKU included in the virtual bundle.
    """

    product_id: str
    sku_id: str
    sku_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        sku_id = self.sku_id

        sku_count = self.sku_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "product_id": product_id,
                "sku_id": sku_id,
                "sku_count": sku_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_id = d.pop("product_id")

        sku_id = d.pop("sku_id")

        sku_count = d.pop("sku_count")

        combined_sku = cls(
            product_id=product_id,
            sku_id=sku_id,
            sku_count=sku_count,
        )

        combined_sku.additional_properties = d
        return combined_sku

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
