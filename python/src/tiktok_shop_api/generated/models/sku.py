from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="Sku")



@_attrs_define
class Sku:
    """ 
        Attributes:
            sku_id (str): TikTok Shop SKU ID to include in the refund calculation.
            quantity (int): Quantity of this SKU to include in the refund calculation.
     """

    sku_id: str
    quantity: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        sku_id = self.sku_id

        quantity = self.quantity


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "sku_id": sku_id,
            "quantity": quantity,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sku_id = d.pop("sku_id")

        quantity = d.pop("quantity")

        sku = cls(
            sku_id=sku_id,
            quantity=quantity,
        )


        sku.additional_properties = d
        return sku

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
