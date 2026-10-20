from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IdentifierCode")


@_attrs_define
class IdentifierCode:
    """
    Attributes:
        code (str | Unset): The identifier code.

            **Format**:
            - GTIN: 14 digits
            - EAN: 8, 13, or 14 digits
            - UPC: 12 digits
            - ISBN: 13 digits, or 9 digits ending in capital `X`
            - JAN: 8 or 13 digits
            **Note**: The identifier code must be unique for each SKU, with no repetition allowed.
        type_ (str | Unset): The type of identifier code.
            Possible values:
            - GTIN
            - EAN
            - UPC
            - ISBN
            - JAN
    """

    code: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        type_ = d.pop("type", UNSET)

        identifier_code = cls(
            code=code,
            type_=type_,
        )

        identifier_code.additional_properties = d
        return identifier_code

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
