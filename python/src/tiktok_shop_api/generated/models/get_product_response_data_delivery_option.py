from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetProductResponseDataDeliveryOption")



@_attrs_define
class GetProductResponseDataDeliveryOption:
    """ 
        Attributes:
            id (str | Unset): The delivery option ID.
            is_available (bool | Unset): A flag indicating whether the delivery option is available for this product.
            name (str | Unset): The delivery option name.
     """

    id: str | Unset = UNSET
    is_available: bool | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        is_available = self.is_available

        name = self.name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if is_available is not UNSET:
            field_dict["is_available"] = is_available
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        is_available = d.pop("is_available", UNSET)

        name = d.pop("name", UNSET)

        get_product_response_data_delivery_option = cls(
            id=id,
            is_available=is_available,
            name=name,
        )


        get_product_response_data_delivery_option.additional_properties = d
        return get_product_response_data_delivery_option

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
