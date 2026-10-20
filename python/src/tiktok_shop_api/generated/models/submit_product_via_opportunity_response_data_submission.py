from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SubmitProductViaOpportunityResponseDataSubmission")



@_attrs_define
class SubmitProductViaOpportunityResponseDataSubmission:
    """ 
        Attributes:
            id (str | Unset): Unique ID of this submission record. Use for tracking review status.
            opportunity_id (str | Unset): The opportunity ID this submission is linked to.
            product_id (str | Unset): The submitted product ID.
            status (str | Unset): APPROVED, UNDER_REVIEW, REJECTED are supported.
                Initial submission status: PENDING_REVIEW.
            submit_time (int | Unset): The submission time as a Unix timestamp in seconds (UTC).
            rejection_reason (str | Unset): the reason when the status is REJECTED
     """

    id: str | Unset = UNSET
    opportunity_id: str | Unset = UNSET
    product_id: str | Unset = UNSET
    status: str | Unset = UNSET
    submit_time: int | Unset = UNSET
    rejection_reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        opportunity_id = self.opportunity_id

        product_id = self.product_id

        status = self.status

        submit_time = self.submit_time

        rejection_reason = self.rejection_reason


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if opportunity_id is not UNSET:
            field_dict["opportunity_id"] = opportunity_id
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if status is not UNSET:
            field_dict["status"] = status
        if submit_time is not UNSET:
            field_dict["submit_time"] = submit_time
        if rejection_reason is not UNSET:
            field_dict["rejection_reason"] = rejection_reason

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        opportunity_id = d.pop("opportunity_id", UNSET)

        product_id = d.pop("product_id", UNSET)

        status = d.pop("status", UNSET)

        submit_time = d.pop("submit_time", UNSET)

        rejection_reason = d.pop("rejection_reason", UNSET)

        submit_product_via_opportunity_response_data_submission = cls(
            id=id,
            opportunity_id=opportunity_id,
            product_id=product_id,
            status=status,
            submit_time=submit_time,
            rejection_reason=rejection_reason,
        )


        submit_product_via_opportunity_response_data_submission.additional_properties = d
        return submit_product_via_opportunity_response_data_submission

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
