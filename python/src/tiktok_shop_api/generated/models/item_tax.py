from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.item_tax_tax_type import ItemTaxTaxType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ItemTax")


@_attrs_define
class ItemTax:
    """
    Attributes:
        tax_type (ItemTaxTaxType | Unset): Tax type.
            Available values:
            - `SALES_TAX` (US market sales tax)

            **Note**: Currently only sales tax is available.
        tax_amount (str | Unset): Tax amount.
        tax_rate (str | Unset): Tax rate.
    """

    tax_type: ItemTaxTaxType | Unset = UNSET
    tax_amount: str | Unset = UNSET
    tax_rate: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tax_type: str | Unset = UNSET
        if not isinstance(self.tax_type, Unset):
            tax_type = self.tax_type.value

        tax_amount = self.tax_amount

        tax_rate = self.tax_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tax_type is not UNSET:
            field_dict["tax_type"] = tax_type
        if tax_amount is not UNSET:
            field_dict["tax_amount"] = tax_amount
        if tax_rate is not UNSET:
            field_dict["tax_rate"] = tax_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _tax_type = d.pop("tax_type", UNSET)
        tax_type: ItemTaxTaxType | Unset
        if isinstance(_tax_type, Unset):
            tax_type = UNSET
        else:
            tax_type = ItemTaxTaxType(_tax_type)

        tax_amount = d.pop("tax_amount", UNSET)

        tax_rate = d.pop("tax_rate", UNSET)

        item_tax = cls(
            tax_type=tax_type,
            tax_amount=tax_amount,
            tax_rate=tax_rate,
        )

        item_tax.additional_properties = d
        return item_tax

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
