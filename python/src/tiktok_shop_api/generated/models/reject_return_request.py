from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.reject_return_request_decision import RejectReturnRequestDecision
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.partial_refund_amount import PartialRefundAmount
  from ..models.reject_cancellation_request_image import RejectCancellationRequestImage





T = TypeVar("T", bound="RejectReturnRequest")



@_attrs_define
class RejectReturnRequest:
    """ 
        Attributes:
            decision (RejectReturnRequestDecision): Seller's decision for the request, available values:
                - `REJECT_REFUND`: seller reject a refund-only request
                - `REJECT_RETURN`: seller reject the initial return-and-refund request
                - `REJECT_RECEIVED_PACKAGE`: seller reject return-and-refund request after the buyer has already shipped or
                handed over the item.
                - `REJECT_REPLACEMENT`: seller reject replacement request
                - `OFFER_PARTIAL_REFUND_AFTER_RECEIVING_PKG`: seller offer partial refund regarding to the package item quality
                check
            reject_reason (str): Seller's reason for rejecting the aftersales request. For
                `OFFER_PARTIAL_REFUND_AFTER_RECEIVING_PKG`, first call Get Review Decision (`GET
                /return_refund/202606/review_decision`) for the same aftersales request: pass this request's `return_id` as
                `return_or_cancel_id` and set `check_decisions` to `OFFER_PARTIAL_REFUND_AFTER_RECEIVING_PKG`. In the response,
                select the `data.line_items[]` entry for the affected return line item, then select its `decisions[]` entry
                whose `decision` is `OFFER_PARTIAL_REFUND_AFTER_RECEIVING_PKG`, and submit one of that decision's
                `available_reject_reasons[].name` values in this field. For other decisions, use the [Get Decision
                Eligibility](https://partner.tiktokshop.com/docv2/page/69844a11eeba77049695c7f6) endpoint to retrieve the
                currently available rejection options for the same request and submit the returned rejection reason name.
                **Note**: Available decisions and rejection reasons depend on the current request status, so retrieve
                eligibility again before calling this API.
            comment (str | Unset): Seller's comment about the rejection decision. For
                `OFFER_PARTIAL_REFUND_AFTER_RECEIVING_PKG`, the comment must not exceed 500 characters.
            images (list[RejectCancellationRequestImage] | Unset): Images provided by the seller to support the decision.
                For `OFFER_PARTIAL_REFUND_AFTER_RECEIVING_PKG`, a maximum of 6 images is allowed.
            partial_refund_amount (PartialRefundAmount | Unset):
     """

    decision: RejectReturnRequestDecision
    reject_reason: str
    comment: str | Unset = UNSET
    images: list[RejectCancellationRequestImage] | Unset = UNSET
    partial_refund_amount: PartialRefundAmount | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.partial_refund_amount import PartialRefundAmount # noqa: PLC0415
        from ..models.reject_cancellation_request_image import RejectCancellationRequestImage # noqa: PLC0415
        decision = self.decision.value

        reject_reason = self.reject_reason

        comment = self.comment

        images: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)



        partial_refund_amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.partial_refund_amount, Unset):
            partial_refund_amount = self.partial_refund_amount.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "decision": decision,
            "reject_reason": reject_reason,
        })
        if comment is not UNSET:
            field_dict["comment"] = comment
        if images is not UNSET:
            field_dict["images"] = images
        if partial_refund_amount is not UNSET:
            field_dict["partial_refund_amount"] = partial_refund_amount

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.partial_refund_amount import PartialRefundAmount # noqa: PLC0415
        from ..models.reject_cancellation_request_image import RejectCancellationRequestImage # noqa: PLC0415
        d = dict(src_dict)
        decision = RejectReturnRequestDecision(d.pop("decision"))




        reject_reason = d.pop("reject_reason")

        comment = d.pop("comment", UNSET)

        _images = d.pop("images", UNSET)
        images: list[RejectCancellationRequestImage] | Unset = UNSET
        if _images is not UNSET:
            images = []
            for images_item_data in _images:
                images_item = RejectCancellationRequestImage.from_dict(images_item_data)



                images.append(images_item)


        _partial_refund_amount = d.pop("partial_refund_amount", UNSET)
        partial_refund_amount: PartialRefundAmount | Unset
        if isinstance(_partial_refund_amount,  Unset):
            partial_refund_amount = UNSET
        else:
            partial_refund_amount = PartialRefundAmount.from_dict(_partial_refund_amount)




        reject_return_request = cls(
            decision=decision,
            reject_reason=reject_reason,
            comment=comment,
            images=images,
            partial_refund_amount=partial_refund_amount,
        )


        reject_return_request.additional_properties = d
        return reject_return_request

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
