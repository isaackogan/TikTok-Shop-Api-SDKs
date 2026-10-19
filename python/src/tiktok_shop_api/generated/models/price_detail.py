from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PriceDetail")


@_attrs_define
class PriceDetail:
    """
    Attributes:
        currency (str | Unset): Ignore this field. It is not yet supported.
        refund_total (str | Unset): Ignore this field. It is not yet supported.
        refund_subtotal (str | Unset): Ignore this field. It is not yet supported.
        refund_shipping_fee (str | Unset): Ignore this field. It is not yet supported.
        refund_tax (str | Unset): Ignore this field. It is not yet supported.
    """

    currency: str | Unset = UNSET
    refund_total: str | Unset = UNSET
    refund_subtotal: str | Unset = UNSET
    refund_shipping_fee: str | Unset = UNSET
    refund_tax: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency = self.currency

        refund_total = self.refund_total

        refund_subtotal = self.refund_subtotal

        refund_shipping_fee = self.refund_shipping_fee

        refund_tax = self.refund_tax

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency is not UNSET:
            field_dict["currency"] = currency
        if refund_total is not UNSET:
            field_dict["refund_total"] = refund_total
        if refund_subtotal is not UNSET:
            field_dict["refund_subtotal"] = refund_subtotal
        if refund_shipping_fee is not UNSET:
            field_dict["refund_shipping_fee"] = refund_shipping_fee
        if refund_tax is not UNSET:
            field_dict["refund_tax"] = refund_tax

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currency = d.pop("currency", UNSET)

        refund_total = d.pop("refund_total", UNSET)

        refund_subtotal = d.pop("refund_subtotal", UNSET)

        refund_shipping_fee = d.pop("refund_shipping_fee", UNSET)

        refund_tax = d.pop("refund_tax", UNSET)

        price_detail = cls(
            currency=currency,
            refund_total=refund_total,
            refund_subtotal=refund_subtotal,
            refund_shipping_fee=refund_shipping_fee,
            refund_tax=refund_tax,
        )

        price_detail.additional_properties = d
        return price_detail

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
