from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_product_response_data_sku_fee_additional_attribute import (
    GetProductResponseDataSkuFeeAdditionalAttribute,
)
from ..models.get_product_response_data_sku_fee_type import GetProductResponseDataSkuFeeType
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetProductResponseDataSkuFee")


@_attrs_define
class GetProductResponseDataSkuFee:
    """
    Attributes:
        additional_attribute (GetProductResponseDataSkuFeeAdditionalAttribute | Unset): Possible values for Pfand:
            - SINGLE_USE
            - REUSABLE
            - NOT_APPLICABLE
        amount (str | Unset): The fee amount.
            Valid range:
            - PFAND: [0.00 - 6300.00]
        type_ (GetProductResponseDataSkuFeeType | Unset): The type of fee.
            Possible values: PFAND
    """

    additional_attribute: GetProductResponseDataSkuFeeAdditionalAttribute | Unset = UNSET
    amount: str | Unset = UNSET
    type_: GetProductResponseDataSkuFeeType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        additional_attribute: str | Unset = UNSET
        if not isinstance(self.additional_attribute, Unset):
            additional_attribute = self.additional_attribute.value

        amount = self.amount

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_attribute is not UNSET:
            field_dict["additional_attribute"] = additional_attribute
        if amount is not UNSET:
            field_dict["amount"] = amount
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _additional_attribute = d.pop("additional_attribute", UNSET)
        additional_attribute: GetProductResponseDataSkuFeeAdditionalAttribute | Unset
        if isinstance(_additional_attribute, Unset):
            additional_attribute = UNSET
        else:
            additional_attribute = GetProductResponseDataSkuFeeAdditionalAttribute(_additional_attribute)

        amount = d.pop("amount", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: GetProductResponseDataSkuFeeType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = GetProductResponseDataSkuFeeType(_type_)

        get_product_response_data_sku_fee = cls(
            additional_attribute=additional_attribute,
            amount=amount,
            type_=type_,
        )

        get_product_response_data_sku_fee.additional_properties = d
        return get_product_response_data_sku_fee

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
