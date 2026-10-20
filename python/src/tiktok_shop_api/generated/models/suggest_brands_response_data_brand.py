from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SuggestBrandsResponseDataBrand")



@_attrs_define
class SuggestBrandsResponseDataBrand:
    """ 
        Attributes:
            id (str | Unset): Brand ID.
            is_authorized (bool | Unset): Whether the brand is authorized for the shop. False if authorization status is
                absent.
            name (str | Unset): Brand name.
     """

    id: str | Unset = UNSET
    is_authorized: bool | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        is_authorized = self.is_authorized

        name = self.name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if is_authorized is not UNSET:
            field_dict["is_authorized"] = is_authorized
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        is_authorized = d.pop("is_authorized", UNSET)

        name = d.pop("name", UNSET)

        suggest_brands_response_data_brand = cls(
            id=id,
            is_authorized=is_authorized,
            name=name,
        )


        suggest_brands_response_data_brand.additional_properties = d
        return suggest_brands_response_data_brand

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
