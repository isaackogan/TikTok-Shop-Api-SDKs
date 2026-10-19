from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PartialRefundAmount")


@_attrs_define
class PartialRefundAmount:
    """
    Attributes:
        partial_refund_total (str | Unset): Partial refund amount. When `decision` is
            `OFFER_PARTIAL_REFUND_AFTER_RECEIVING_PKG`, this field is required and must be a numeric string representing an
            amount greater than 0.
        currency (str | Unset): Currency of the partial refund amount. When `decision` is
            `OFFER_PARTIAL_REFUND_AFTER_RECEIVING_PKG`, this field is required and must match the return order's currency.
    """

    partial_refund_total: str | Unset = UNSET
    currency: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        partial_refund_total = self.partial_refund_total

        currency = self.currency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if partial_refund_total is not UNSET:
            field_dict["partial_refund_total"] = partial_refund_total
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        partial_refund_total = d.pop("partial_refund_total", UNSET)

        currency = d.pop("currency", UNSET)

        partial_refund_amount = cls(
            partial_refund_total=partial_refund_total,
            currency=currency,
        )

        partial_refund_amount.additional_properties = d
        return partial_refund_amount

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
