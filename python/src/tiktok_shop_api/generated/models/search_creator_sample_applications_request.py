from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SearchCreatorSampleApplicationsRequest")



@_attrs_define
class SearchCreatorSampleApplicationsRequest:
    """ 
        Attributes:
            application_statuses (list[str] | Unset): Filter sample applications by status.
                The possible enumerated values are:
                - PENDING: The sample application is waiting for the seller's review.
                - AWAITING_SHIPMENT: The application is approved, and the seller needs to ship the sample.
                - SHIPPED: The sample has been shipped by the seller and is waiting for the creator to receive the package.
                - CONTENT_PENDING: The creator has received the sample package and is expected to create content.
                - REJECT_CANCELLED: The sample application has been rejected by the seller.
                - OVERDUE_CANCELLED: The sample application has expired due to being overdue.
                - UNFULFILL_CANCELLED: The creator did not fulfill the commitment to create content within the agreed timeframe.
                - FULFILLMENT_SUSPEND: The application fulfillment was paused because the product could not be promoted.
                - DEL_OPEN_COLLAB: Open collaboration has been deleted.
                - SELLER_NOT_SHIP_CANCELLED: The seller did not ship the sample within the required timeframe.
                - WITHDRAW_CANCELLED: The creator withdrew the sample application before the seller approved it.
                - UNFULFILLABLE_CANCELLED: The application was cancelled due to reasons beyond the creator's control, making it
                impossible to create content.
                - OPS_CANCELLED: The application was manually cancelled by operations staff.
                - OPS_FAILED: The application was marked as failed by operations staff.
                - OPS_ COMPLETED: The application was manually marked as completed by operations staff.
                - COMPLETED: The application is complete, and the creator has posted the content.
                - TO_BE_POST: The creator has not posted a video or LIVE for this sample.
                - POST_IN_REVIEW: The creator has posted a video or LIVE that has not yet satisfied the fulfillment
                requirements.
                - POST_FAILED: The creator posted a video or LIVE but deleted it before completing sample fulfillment.
                - CANCELED: The sample application has been canceled.
                This field allows for tracking the status of a sample application throughout its lifecycle, providing visibility
                into each stage of the process for sellers and creators.
     """

    application_statuses: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        application_statuses: list[str] | Unset = UNSET
        if not isinstance(self.application_statuses, Unset):
            application_statuses = self.application_statuses




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if application_statuses is not UNSET:
            field_dict["application_statuses"] = application_statuses

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        application_statuses = cast(list[str], d.pop("application_statuses", UNSET))


        search_creator_sample_applications_request = cls(
            application_statuses=application_statuses,
        )


        search_creator_sample_applications_request.additional_properties = d
        return search_creator_sample_applications_request

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
