from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetAvailableReviewDecisionsResponseDataLineItemDecisionPartialRefundAmountRange")



@_attrs_define
class GetAvailableReviewDecisionsResponseDataLineItemDecisionPartialRefundAmountRange:
    """ 
        Attributes:
            min_amount (str | Unset): The minimum partial refund amount the seller may offer.
            max_amount (str | Unset): The maximum partial refund amount the seller may offer.
            currency (str | Unset): The currency of the partial refund amount range, matching the currency of the current
                return request.
     """

    min_amount: str | Unset = UNSET
    max_amount: str | Unset = UNSET
    currency: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        min_amount = self.min_amount

        max_amount = self.max_amount

        currency = self.currency


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if min_amount is not UNSET:
            field_dict["min_amount"] = min_amount
        if max_amount is not UNSET:
            field_dict["max_amount"] = max_amount
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        min_amount = d.pop("min_amount", UNSET)

        max_amount = d.pop("max_amount", UNSET)

        currency = d.pop("currency", UNSET)

        get_available_review_decisions_response_data_line_item_decision_partial_refund_amount_range = cls(
            min_amount=min_amount,
            max_amount=max_amount,
            currency=currency,
        )


        get_available_review_decisions_response_data_line_item_decision_partial_refund_amount_range.additional_properties = d
        return get_available_review_decisions_response_data_line_item_decision_partial_refund_amount_range

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
