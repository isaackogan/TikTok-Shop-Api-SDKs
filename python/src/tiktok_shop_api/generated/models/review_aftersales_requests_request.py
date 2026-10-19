from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.review_aftersales_requests_request_aftersales_request_decision import (
        ReviewAftersalesRequestsRequestAftersalesRequestDecision,
    )


T = TypeVar("T", bound="ReviewAftersalesRequestsRequest")


@_attrs_define
class ReviewAftersalesRequestsRequest:
    """
    Attributes:
        aftersales_request_decisions (list[ReviewAftersalesRequestsRequestAftersalesRequestDecision] | Unset): Decisions
            to apply to aftersales requests.
    """

    aftersales_request_decisions: list[ReviewAftersalesRequestsRequestAftersalesRequestDecision] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aftersales_request_decisions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.aftersales_request_decisions, Unset):
            aftersales_request_decisions = []
            for aftersales_request_decisions_item_data in self.aftersales_request_decisions:
                aftersales_request_decisions_item = aftersales_request_decisions_item_data.to_dict()
                aftersales_request_decisions.append(aftersales_request_decisions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aftersales_request_decisions is not UNSET:
            field_dict["aftersales_request_decisions"] = aftersales_request_decisions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.review_aftersales_requests_request_aftersales_request_decision import (
            ReviewAftersalesRequestsRequestAftersalesRequestDecision,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _aftersales_request_decisions = d.pop("aftersales_request_decisions", UNSET)
        aftersales_request_decisions: list[ReviewAftersalesRequestsRequestAftersalesRequestDecision] | Unset = UNSET
        if _aftersales_request_decisions is not UNSET:
            aftersales_request_decisions = []
            for aftersales_request_decisions_item_data in _aftersales_request_decisions:
                aftersales_request_decisions_item = ReviewAftersalesRequestsRequestAftersalesRequestDecision.from_dict(
                    aftersales_request_decisions_item_data
                )

                aftersales_request_decisions.append(aftersales_request_decisions_item)

        review_aftersales_requests_request = cls(
            aftersales_request_decisions=aftersales_request_decisions,
        )

        review_aftersales_requests_request.additional_properties = d
        return review_aftersales_requests_request

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
