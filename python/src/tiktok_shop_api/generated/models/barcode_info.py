from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BarcodeInfo")


@_attrs_define
class BarcodeInfo:
    """
    Attributes:
        barcode_type (str | Unset): Type of barcode provided for the goods, such as UPC.
        barcode_value (str | Unset): Barcode value. UPC must contain 8 or 12 digits; EAN must contain 8 or 13 digits;
            and GTIN must contain 8, 12, 13, or 14 digits. UPC, EAN, and GTIN values must have a valid checksum.
            ASIN_OR_FNSKU must contain 10 uppercase letters or digits and start with B or X. MERCHANT_SKU_ID must contain 1
            to 32 printable ASCII characters with no whitespace.
    """

    barcode_type: str | Unset = UNSET
    barcode_value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        barcode_type = self.barcode_type

        barcode_value = self.barcode_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if barcode_type is not UNSET:
            field_dict["barcode_type"] = barcode_type
        if barcode_value is not UNSET:
            field_dict["barcode_value"] = barcode_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        barcode_type = d.pop("barcode_type", UNSET)

        barcode_value = d.pop("barcode_value", UNSET)

        barcode_info = cls(
            barcode_type=barcode_type,
            barcode_value=barcode_value,
        )

        barcode_info.additional_properties = d
        return barcode_info

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
