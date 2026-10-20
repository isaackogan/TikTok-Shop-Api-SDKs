from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.review_a_sample_application_request_reject_reason import ReviewASampleApplicationRequestRejectReason
from ..models.review_a_sample_application_request_review_result import ReviewASampleApplicationRequestReviewResult
from ..types import UNSET, Unset






T = TypeVar("T", bound="ReviewASampleApplicationRequest")



@_attrs_define
class ReviewASampleApplicationRequest:
    """ 
        Attributes:
            review_result (ReviewASampleApplicationRequestReviewResult): The review action to take on the sample
                application. Possible values:
                - APPROVE: Approves the sample application.
                - REJECT: Rejects the sample application.
            reject_reason (ReviewASampleApplicationRequestRejectReason | Unset): The reason why a seller rejected a
                creator's sample application. The possible enumerated values are:
                - NOT_MATCH: The creator does not meet the seller's collaboration requirements.
                - OFFLINE: The product has been taken offline.
                - OUT_OF_STOCK: The product is temporarily out of stock.
                - OTHER: Any other reason not covered by the above categories.
                Required if the review_result is set to REJECT
                This field allows the seller to specify the reason for rejecting a sample application, providing clarity to the
                creator regarding the rejection.
     """

    review_result: ReviewASampleApplicationRequestReviewResult
    reject_reason: ReviewASampleApplicationRequestRejectReason | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        review_result = self.review_result.value

        reject_reason: str | Unset = UNSET
        if not isinstance(self.reject_reason, Unset):
            reject_reason = self.reject_reason.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "review_result": review_result,
        })
        if reject_reason is not UNSET:
            field_dict["reject_reason"] = reject_reason

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        review_result = ReviewASampleApplicationRequestReviewResult(d.pop("review_result"))




        _reject_reason = d.pop("reject_reason", UNSET)
        reject_reason: ReviewASampleApplicationRequestRejectReason | Unset
        if isinstance(_reject_reason,  Unset):
            reject_reason = UNSET
        else:
            reject_reason = ReviewASampleApplicationRequestRejectReason(_reject_reason)




        review_a_sample_application_request = cls(
            review_result=review_result,
            reject_reason=reject_reason,
        )


        review_a_sample_application_request.additional_properties = d
        return review_a_sample_application_request

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
