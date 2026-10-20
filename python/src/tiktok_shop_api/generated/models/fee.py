from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Fee")


@_attrs_define
class Fee:
    """
    Attributes:
        type_ (str | Unset): The type of fee.
            Possible values: PFAND
        amount (str | Unset): The fee amount.
            Valid range:
            - PFAND: [0.00 - 6300.00]
        additional_attribute (str | Unset): An optional attribute that provides additional context for the fee. The
            accepted values may vary by fee type and market.

            Possible values for Pfand:
            - SINGLE_USE
            - REUSABLE
            - NOT_APPLICABLE
    """

    type_: str | Unset = UNSET
    amount: str | Unset = UNSET
    additional_attribute: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        amount = self.amount

        additional_attribute = self.additional_attribute

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if amount is not UNSET:
            field_dict["amount"] = amount
        if additional_attribute is not UNSET:
            field_dict["additional_attribute"] = additional_attribute

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        amount = d.pop("amount", UNSET)

        additional_attribute = d.pop("additional_attribute", UNSET)

        fee = cls(
            type_=type_,
            amount=amount,
            additional_attribute=additional_attribute,
        )

        fee.additional_properties = d
        return fee

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
