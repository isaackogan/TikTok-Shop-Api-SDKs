from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="LinkedProduct")



@_attrs_define
class LinkedProduct:
    """ 
        Attributes:
            product_id (str | Unset): ID of the product.
            product_image_url (str | Unset): URL of the product image.
            product_name (str | Unset): Name of the product.
            product_scan_url (str | Unset): URL associated with the linked product.
     """

    product_id: str | Unset = UNSET
    product_image_url: str | Unset = UNSET
    product_name: str | Unset = UNSET
    product_scan_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        product_image_url = self.product_image_url

        product_name = self.product_name

        product_scan_url = self.product_scan_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if product_image_url is not UNSET:
            field_dict["product_image_url"] = product_image_url
        if product_name is not UNSET:
            field_dict["product_name"] = product_name
        if product_scan_url is not UNSET:
            field_dict["product_scan_url"] = product_scan_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_id = d.pop("product_id", UNSET)

        product_image_url = d.pop("product_image_url", UNSET)

        product_name = d.pop("product_name", UNSET)

        product_scan_url = d.pop("product_scan_url", UNSET)

        linked_product = cls(
            product_id=product_id,
            product_image_url=product_image_url,
            product_name=product_name,
            product_scan_url=product_scan_url,
        )


        linked_product.additional_properties = d
        return linked_product

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
