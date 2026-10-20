from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.submit_product_via_opportunity_response_data_submission import (
        SubmitProductViaOpportunityResponseDataSubmission,
    )


T = TypeVar("T", bound="SubmitProductViaOpportunityResponseData")


@_attrs_define
class SubmitProductViaOpportunityResponseData:
    """
    Attributes:
        submission (SubmitProductViaOpportunityResponseDataSubmission | Unset):
    """

    submission: SubmitProductViaOpportunityResponseDataSubmission | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        submission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.submission, Unset):
            submission = self.submission.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if submission is not UNSET:
            field_dict["submission"] = submission

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.submit_product_via_opportunity_response_data_submission import (
            SubmitProductViaOpportunityResponseDataSubmission,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _submission = d.pop("submission", UNSET)
        submission: SubmitProductViaOpportunityResponseDataSubmission | Unset
        if isinstance(_submission, Unset):
            submission = UNSET
        else:
            submission = SubmitProductViaOpportunityResponseDataSubmission.from_dict(_submission)

        submit_product_via_opportunity_response_data = cls(
            submission=submission,
        )

        submit_product_via_opportunity_response_data.additional_properties = d
        return submit_product_via_opportunity_response_data

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
