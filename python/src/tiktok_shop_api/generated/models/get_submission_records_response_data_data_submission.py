from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GetSubmissionRecordsResponseDataDataSubmission")



@_attrs_define
class GetSubmissionRecordsResponseDataDataSubmission:
    """ 
        Attributes:
            id (str | Unset): Unique ID of this submission.
            opportunity_id (str | Unset): The opportunity ID this submission is linked to.
            opportunity_title (str | Unset): Opportunity title for reference.
            status (str | Unset): Current status: PENDING_REVIEW / APPROVED / REJECTED
            product_id (str | Unset): The submitted product ID.
            product_name (str | Unset): Product name for reference.
            submit_time (int | Unset): The time when the product was submitted, expressed as a Unix timestamp in seconds.
            review_time (int | Unset): Review completion timestamp
            rejection_reason (None | str | Unset): Rejection reason if status is REJECTED. Null otherwise.
            product_orders (int | Unset): The total number of units sold for the product in the last 30 days.
            product_pv (int | Unset): The product page view count for the last 30 days.
     """

    id: str | Unset = UNSET
    opportunity_id: str | Unset = UNSET
    opportunity_title: str | Unset = UNSET
    status: str | Unset = UNSET
    product_id: str | Unset = UNSET
    product_name: str | Unset = UNSET
    submit_time: int | Unset = UNSET
    review_time: int | Unset = UNSET
    rejection_reason: None | str | Unset = UNSET
    product_orders: int | Unset = UNSET
    product_pv: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        opportunity_id = self.opportunity_id

        opportunity_title = self.opportunity_title

        status = self.status

        product_id = self.product_id

        product_name = self.product_name

        submit_time = self.submit_time

        review_time = self.review_time

        rejection_reason: None | str | Unset
        if isinstance(self.rejection_reason, Unset):
            rejection_reason = UNSET
        else:
            rejection_reason = self.rejection_reason

        product_orders = self.product_orders

        product_pv = self.product_pv


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if opportunity_id is not UNSET:
            field_dict["opportunity_id"] = opportunity_id
        if opportunity_title is not UNSET:
            field_dict["opportunity_title"] = opportunity_title
        if status is not UNSET:
            field_dict["status"] = status
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if product_name is not UNSET:
            field_dict["product_name"] = product_name
        if submit_time is not UNSET:
            field_dict["submit_time"] = submit_time
        if review_time is not UNSET:
            field_dict["review_time"] = review_time
        if rejection_reason is not UNSET:
            field_dict["rejection_reason"] = rejection_reason
        if product_orders is not UNSET:
            field_dict["product_orders"] = product_orders
        if product_pv is not UNSET:
            field_dict["product_pv"] = product_pv

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        opportunity_id = d.pop("opportunity_id", UNSET)

        opportunity_title = d.pop("opportunity_title", UNSET)

        status = d.pop("status", UNSET)

        product_id = d.pop("product_id", UNSET)

        product_name = d.pop("product_name", UNSET)

        submit_time = d.pop("submit_time", UNSET)

        review_time = d.pop("review_time", UNSET)

        def _parse_rejection_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rejection_reason = _parse_rejection_reason(d.pop("rejection_reason", UNSET))


        product_orders = d.pop("product_orders", UNSET)

        product_pv = d.pop("product_pv", UNSET)

        get_submission_records_response_data_data_submission = cls(
            id=id,
            opportunity_id=opportunity_id,
            opportunity_title=opportunity_title,
            status=status,
            product_id=product_id,
            product_name=product_name,
            submit_time=submit_time,
            review_time=review_time,
            rejection_reason=rejection_reason,
            product_orders=product_orders,
            product_pv=product_pv,
        )


        get_submission_records_response_data_data_submission.additional_properties = d
        return get_submission_records_response_data_data_submission

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
