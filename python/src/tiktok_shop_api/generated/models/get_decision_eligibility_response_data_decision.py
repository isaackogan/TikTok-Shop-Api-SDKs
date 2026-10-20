from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.available_reject_reason import AvailableRejectReason


T = TypeVar("T", bound="GetDecisionEligibilityResponseDataDecision")


@_attrs_define
class GetDecisionEligibilityResponseDataDecision:
    """
    Attributes:
        decision (str | Unset): One eligibility result for one evaluated seller decision. Possible Values:
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
            -`ISSUE_EXCHANGE_REFUND`
        eligible (bool | Unset): Whether this seller decision is currently eligible for the specified aftersales
            request. `true` means eligible; `false` means ineligible.
        ineligible_code (int | Unset): The reason code for an ineligible decision. This field is returned when eligible
            is false.
        ineligible_reason (str | Unset): The reason for an ineligible decision. This field is returned when eligible is
            false.
        available_reject_reasons (list[AvailableRejectReason] | Unset): The reject reasons available for an eligible
            reject decision. Each reason includes a name and localized display text.
    """

    decision: str | Unset = UNSET
    eligible: bool | Unset = UNSET
    ineligible_code: int | Unset = UNSET
    ineligible_reason: str | Unset = UNSET
    available_reject_reasons: list[AvailableRejectReason] | Unset = UNSET
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.available_reject_reason import AvailableRejectReason  # noqa: PLC0415

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

        get_decision_eligibility_response_data_decision = cls(
            decision=decision,
            eligible=eligible,
            ineligible_code=ineligible_code,
            ineligible_reason=ineligible_reason,
            available_reject_reasons=available_reject_reasons,
        )

        get_decision_eligibility_response_data_decision.additional_properties = d
        return get_decision_eligibility_response_data_decision

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
