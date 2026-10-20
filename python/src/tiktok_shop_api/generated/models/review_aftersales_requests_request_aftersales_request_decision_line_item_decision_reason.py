from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.review_aftersales_requests_request_aftersales_request_decision_line_item_decision_reason_media import ReviewAftersalesRequestsRequestAftersalesRequestDecisionLineItemDecisionReasonMedia





T = TypeVar("T", bound="ReviewAftersalesRequestsRequestAftersalesRequestDecisionLineItemDecisionReason")



@_attrs_define
class ReviewAftersalesRequestsRequestAftersalesRequestDecisionLineItemDecisionReason:
    """ 
        Attributes:
            reason_id (str | Unset): Seller's reason for rejecting the aftersales request. Use the [Get Review
                Decision](https://partner.tiktokshop.com/docv2/page/get-review-decision-202606) endpoint to retrieve the
                currently available rejection options for the same request, and submit the returned rejection reason name in
                this field.
                **Note**: The available decisions and rejection reasons can change depending on the current request status, so
                fetch eligibility again before calling this API.
            text (str | Unset): Additional explanation for the decision.
            media (ReviewAftersalesRequestsRequestAftersalesRequestDecisionLineItemDecisionReasonMedia | Unset):
     """

    reason_id: str | Unset = UNSET
    text: str | Unset = UNSET
    media: ReviewAftersalesRequestsRequestAftersalesRequestDecisionLineItemDecisionReasonMedia | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.review_aftersales_requests_request_aftersales_request_decision_line_item_decision_reason_media import ReviewAftersalesRequestsRequestAftersalesRequestDecisionLineItemDecisionReasonMedia # noqa: PLC0415
        reason_id = self.reason_id

        text = self.text

        media: dict[str, Any] | Unset = UNSET
        if not isinstance(self.media, Unset):
            media = self.media.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if reason_id is not UNSET:
            field_dict["reason_id"] = reason_id
        if text is not UNSET:
            field_dict["text"] = text
        if media is not UNSET:
            field_dict["media"] = media

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.review_aftersales_requests_request_aftersales_request_decision_line_item_decision_reason_media import ReviewAftersalesRequestsRequestAftersalesRequestDecisionLineItemDecisionReasonMedia # noqa: PLC0415
        d = dict(src_dict)
        reason_id = d.pop("reason_id", UNSET)

        text = d.pop("text", UNSET)

        _media = d.pop("media", UNSET)
        media: ReviewAftersalesRequestsRequestAftersalesRequestDecisionLineItemDecisionReasonMedia | Unset
        if isinstance(_media,  Unset):
            media = UNSET
        else:
            media = ReviewAftersalesRequestsRequestAftersalesRequestDecisionLineItemDecisionReasonMedia.from_dict(_media)




        review_aftersales_requests_request_aftersales_request_decision_line_item_decision_reason = cls(
            reason_id=reason_id,
            text=text,
            media=media,
        )


        review_aftersales_requests_request_aftersales_request_decision_line_item_decision_reason.additional_properties = d
        return review_aftersales_requests_request_aftersales_request_decision_line_item_decision_reason

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
