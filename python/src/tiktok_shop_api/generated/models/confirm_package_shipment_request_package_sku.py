from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ConfirmPackageShipmentRequestPackageSku")



@_attrs_define
class ConfirmPackageShipmentRequestPackageSku:
    """ 
        Attributes:
            id (str): The TikTok Shop SKU ID. The value must represent a positive base-10 integer.
            quantity (int): Quantity of this SKU in the package. Must be greater than `0`.
     """

    id: str
    quantity: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        quantity = self.quantity


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "quantity": quantity,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        quantity = d.pop("quantity")

        confirm_package_shipment_request_package_sku = cls(
            id=id,
            quantity=quantity,
        )


        confirm_package_shipment_request_package_sku.additional_properties = d
        return confirm_package_shipment_request_package_sku

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
