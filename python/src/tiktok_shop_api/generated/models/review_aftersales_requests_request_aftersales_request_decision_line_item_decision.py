from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.review_aftersales_requests_request_aftersales_request_decision_line_item_decision_action import (
    ReviewAftersalesRequestsRequestAftersalesRequestDecisionLineItemDecisionAction,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.review_aftersales_requests_request_aftersales_request_decision_line_item_decision_alternative_solution_detail import (
        ReviewAftersalesRequestsRequestAftersalesRequestDecisionLineItemDecisionAlternativeSolutionDetail,
    )
    from ..models.review_aftersales_requests_request_aftersales_request_decision_line_item_decision_line_item import (
        ReviewAftersalesRequestsRequestAftersalesRequestDecisionLineItemDecisionLineItem,
    )
    from ..models.review_aftersales_requests_request_aftersales_request_decision_line_item_decision_reason import (
        ReviewAftersalesRequestsRequestAftersalesRequestDecisionLineItemDecisionReason,
    )


T = TypeVar("T", bound="ReviewAftersalesRequestsRequestAftersalesRequestDecisionLineItemDecision")


@_attrs_define
class ReviewAftersalesRequestsRequestAftersalesRequestDecisionLineItemDecision:
    """
    Attributes:
        line_items (list[ReviewAftersalesRequestsRequestAftersalesRequestDecisionLineItemDecisionLineItem]): Line items
            for which this decision applies. Decision details apply to each line item individually (e.g. a partial refund
            amount of $1.00 for 3 line items will result in a total partial refund amount of $3.00).
        action (ReviewAftersalesRequestsRequestAftersalesRequestDecisionLineItemDecisionAction): Action/decision to be
            applied.
            Possible values:
            - `APPROVE_REQUEST`
            - `APPROVE_RETURN_PACKAGE`
            - `REJECT_REQUEST`
            - `REJECT_RETURN_PACKAGE`
            - `REFUND_INSTEAD`
            - `OFFER_PARTIAL_REFUND`
            - `OFFER_PARTIAL_REFUND_AFTER_RECEIVING_PKG`
        alternative_solution_details
            (ReviewAftersalesRequestsRequestAftersalesRequestDecisionLineItemDecisionAlternativeSolutionDetail | Unset):
        reason (ReviewAftersalesRequestsRequestAftersalesRequestDecisionLineItemDecisionReason | Unset):
    """

    line_items: list[ReviewAftersalesRequestsRequestAftersalesRequestDecisionLineItemDecisionLineItem]
    action: ReviewAftersalesRequestsRequestAftersalesRequestDecisionLineItemDecisionAction
    alternative_solution_details: (
        ReviewAftersalesRequestsRequestAftersalesRequestDecisionLineItemDecisionAlternativeSolutionDetail | Unset
    ) = UNSET
    reason: ReviewAftersalesRequestsRequestAftersalesRequestDecisionLineItemDecisionReason | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        line_items = []
        for line_items_item_data in self.line_items:
            line_items_item = line_items_item_data.to_dict()
            line_items.append(line_items_item)

        action = self.action.value

        alternative_solution_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.alternative_solution_details, Unset):
            alternative_solution_details = self.alternative_solution_details.to_dict()

        reason: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "line_items": line_items,
                "action": action,
            }
        )
        if alternative_solution_details is not UNSET:
            field_dict["alternative_solution_details"] = alternative_solution_details
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.review_aftersales_requests_request_aftersales_request_decision_line_item_decision_alternative_solution_detail import (
            ReviewAftersalesRequestsRequestAftersalesRequestDecisionLineItemDecisionAlternativeSolutionDetail,  # noqa: PLC0415
        )
        from ..models.review_aftersales_requests_request_aftersales_request_decision_line_item_decision_line_item import (
            ReviewAftersalesRequestsRequestAftersalesRequestDecisionLineItemDecisionLineItem,  # noqa: PLC0415
        )
        from ..models.review_aftersales_requests_request_aftersales_request_decision_line_item_decision_reason import (
            ReviewAftersalesRequestsRequestAftersalesRequestDecisionLineItemDecisionReason,  # noqa: PLC0415
        )

        d = dict(src_dict)
        line_items = []
        _line_items = d.pop("line_items")
        for line_items_item_data in _line_items:
            line_items_item = (
                ReviewAftersalesRequestsRequestAftersalesRequestDecisionLineItemDecisionLineItem.from_dict(
                    line_items_item_data
                )
            )

            line_items.append(line_items_item)

        action = ReviewAftersalesRequestsRequestAftersalesRequestDecisionLineItemDecisionAction(d.pop("action"))

        _alternative_solution_details = d.pop("alternative_solution_details", UNSET)
        alternative_solution_details: (
            ReviewAftersalesRequestsRequestAftersalesRequestDecisionLineItemDecisionAlternativeSolutionDetail | Unset
        )
        if isinstance(_alternative_solution_details, Unset):
            alternative_solution_details = UNSET
        else:
            alternative_solution_details = ReviewAftersalesRequestsRequestAftersalesRequestDecisionLineItemDecisionAlternativeSolutionDetail.from_dict(
                _alternative_solution_details
            )

        _reason = d.pop("reason", UNSET)
        reason: ReviewAftersalesRequestsRequestAftersalesRequestDecisionLineItemDecisionReason | Unset
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = ReviewAftersalesRequestsRequestAftersalesRequestDecisionLineItemDecisionReason.from_dict(_reason)

        review_aftersales_requests_request_aftersales_request_decision_line_item_decision = cls(
            line_items=line_items,
            action=action,
            alternative_solution_details=alternative_solution_details,
            reason=reason,
        )

        review_aftersales_requests_request_aftersales_request_decision_line_item_decision.additional_properties = d
        return review_aftersales_requests_request_aftersales_request_decision_line_item_decision

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
