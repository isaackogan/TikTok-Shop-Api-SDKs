from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.available_reject_reason import AvailableRejectReason
    from ..models.get_available_review_decisions_response_data_line_item_decision_partial_refund_amount_range import (
        GetAvailableReviewDecisionsResponseDataLineItemDecisionPartialRefundAmountRange,
    )


T = TypeVar("T", bound="GetAvailableReviewDecisionsResponseDataLineItemDecision")


@_attrs_define
class GetAvailableReviewDecisionsResponseDataLineItemDecision:
    """
    Attributes:
        decision (str | Unset): Seller review decision evaluated for this line item.
            Possible values:
            - `APPROVE_REQUEST_CANCEL`
            - `APPROVE_REFUND`
            - `APPROVE_RETURN`
            - `APPROVE_RECEIVED_PACKAGE`
            - `APPROVE_REPLACEMENT`
            - `ISSUE_REPLACEMENT_REFUND`
            - `DIRECT_REFUND`
            - `REJECT_REQUEST_CANCEL`
            - `REJECT_REFUND`
            - `REJECT_RETURN`
            - `REJECT_RECEIVED_PACKAGE`
            - `REJECT_REPLACEMENT`
            - `ISSUE_EXCHANGE_REFUND`
            - `OFFER_PARTIAL_REFUND`
            - `OFFER_PARTIAL_REFUND_AFTER_RECEIVING_PKG`
        eligible (bool | Unset): Whether this decision is currently eligible for the line item. When `false`,
            `ineligible_code` and `ineligible_reason` explain why the decision is ineligible; these fields are omitted when
            `true`.
        ineligible_code (int | Unset): The reason code for an ineligible decision.
        ineligible_reason (str | Unset): The reason for an ineligible decision.
        available_reject_reasons (list[AvailableRejectReason] | Unset): Rejection reasons, if available, for this
            eligible decision. Each item contains a machine-readable name and display text.
        partial_refund_amount_range (GetAvailableReviewDecisionsResponseDataLineItemDecisionPartialRefundAmountRange |
            Unset):
    """

    decision: str | Unset = UNSET
    eligible: bool | Unset = UNSET
    ineligible_code: int | Unset = UNSET
    ineligible_reason: str | Unset = UNSET
    available_reject_reasons: list[AvailableRejectReason] | Unset = UNSET
    partial_refund_amount_range: (
        GetAvailableReviewDecisionsResponseDataLineItemDecisionPartialRefundAmountRange | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        decision = self.decision

        eligible = self.eligible

        ineligible_code = self.ineligible_code

        ineligible_reason = self.ineligible_reason

        available_reject_reasons: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.available_reject_reasons, Unset):
            available_reject_reasons = []
            for available_reject_reasons_item_data in self.available_reject_reasons:
                available_reject_reasons_item = available_reject_reasons_item_data.to_dict()
                available_reject_reasons.append(available_reject_reasons_item)

        partial_refund_amount_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.partial_refund_amount_range, Unset):
            partial_refund_amount_range = self.partial_refund_amount_range.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if decision is not UNSET:
            field_dict["decision"] = decision
        if eligible is not UNSET:
            field_dict["eligible"] = eligible
        if ineligible_code is not UNSET:
            field_dict["ineligible_code"] = ineligible_code
        if ineligible_reason is not UNSET:
            field_dict["ineligible_reason"] = ineligible_reason
        if available_reject_reasons is not UNSET:
            field_dict["available_reject_reasons"] = available_reject_reasons
        if partial_refund_amount_range is not UNSET:
            field_dict["partial_refund_amount_range"] = partial_refund_amount_range

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.available_reject_reason import AvailableRejectReason  # noqa: PLC0415
        from ..models.get_available_review_decisions_response_data_line_item_decision_partial_refund_amount_range import (
            GetAvailableReviewDecisionsResponseDataLineItemDecisionPartialRefundAmountRange,  # noqa: PLC0415
        )

        d = dict(src_dict)
        decision = d.pop("decision", UNSET)

        eligible = d.pop("eligible", UNSET)

        ineligible_code = d.pop("ineligible_code", UNSET)

        ineligible_reason = d.pop("ineligible_reason", UNSET)

        _available_reject_reasons = d.pop("available_reject_reasons", UNSET)
        available_reject_reasons: list[AvailableRejectReason] | Unset = UNSET
        if _available_reject_reasons is not UNSET:
            available_reject_reasons = []
            for available_reject_reasons_item_data in _available_reject_reasons:
                available_reject_reasons_item = AvailableRejectReason.from_dict(available_reject_reasons_item_data)

                available_reject_reasons.append(available_reject_reasons_item)

        _partial_refund_amount_range = d.pop("partial_refund_amount_range", UNSET)
        partial_refund_amount_range: (
            GetAvailableReviewDecisionsResponseDataLineItemDecisionPartialRefundAmountRange | Unset
        )
        if isinstance(_partial_refund_amount_range, Unset):
            partial_refund_amount_range = UNSET
        else:
            partial_refund_amount_range = (
                GetAvailableReviewDecisionsResponseDataLineItemDecisionPartialRefundAmountRange.from_dict(
                    _partial_refund_amount_range
                )
            )

        get_available_review_decisions_response_data_line_item_decision = cls(
            decision=decision,
            eligible=eligible,
            ineligible_code=ineligible_code,
            ineligible_reason=ineligible_reason,
            available_reject_reasons=available_reject_reasons,
            partial_refund_amount_range=partial_refund_amount_range,
        )

        get_available_review_decisions_response_data_line_item_decision.additional_properties = d
        return get_available_review_decisions_response_data_line_item_decision

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
