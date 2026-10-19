from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="ReviewAftersalesRequestsRequestAftersalesRequestDecisionLineItemDecisionAlternativeSolutionDetail"
)


@_attrs_define
class ReviewAftersalesRequestsRequestAftersalesRequestDecisionLineItemDecisionAlternativeSolutionDetail:
    """
    Attributes:
        partial_refund_amount (str | Unset): Proposed refund amount.
        currency (str | Unset): Currency of the refund amount (ISO 4217). Must match the currency of the forward order.
    """

    partial_refund_amount: str | Unset = UNSET
    currency: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        partial_refund_amount = self.partial_refund_amount

        currency = self.currency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if partial_refund_amount is not UNSET:
            field_dict["partial_refund_amount"] = partial_refund_amount
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        partial_refund_amount = d.pop("partial_refund_amount", UNSET)

        currency = d.pop("currency", UNSET)

        review_aftersales_requests_request_aftersales_request_decision_line_item_decision_alternative_solution_detail = cls(
            partial_refund_amount=partial_refund_amount,
            currency=currency,
        )

        review_aftersales_requests_request_aftersales_request_decision_line_item_decision_alternative_solution_detail.additional_properties = d
        return review_aftersales_requests_request_aftersales_request_decision_line_item_decision_alternative_solution_detail

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
