from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchCreatorSampleApplicationsResponseDataSampleApplicationCreatorFulfillment")


@_attrs_define
class SearchCreatorSampleApplicationsResponseDataSampleApplicationCreatorFulfillment:
    """
    Attributes:
        id (str | Unset): Fulfillment ID.
        expiration_time (int | Unset): Fulfillment deadline timestamp, in seconds.
        total_suspend_duration (int | Unset): Total suspension duration for fulfillment, in seconds.
        status (str | Unset): Fulfillment status, It indicates the current status of the fulfillment process. The
            possible values are:
            - PENDING: The creator is yet to fulfill the content creation obligation.
            - ONGOING: Fulfillment is in progress; content has been created and is being evaluated against criteria.
            - SUCCEED: Fulfillment has been successfully completed; the content meets the required standards.
            - FAILED: Fulfillment failed; the content did not meet the required standards.
            - OVERDUE: Fulfillment is overdue; the creator did not meet the deadline.
            - SUSPEND: Fulfillment has been suspended.
            - CANCELLED: Fulfillment has been cancelled, either by the creator or due to operational reasons.
            - EXEMPTED: The creator has been exempted from the fulfillment obligation.
        bound_product_status (str | Unset): Represents the marketing status of a product associated with a fulfillment
            order. It indicates whether the product is available for marketing and fulfillment. The possible values are:
            - UNKNOWN: The marketing status of the product is unknown.
            - LIVE: The product is available and can be used for fulfillment.
            - OUT_OF_STOCK: The product is out of stock and cannot be fulfilled.
            - SELLER_DEACTIVATE: The product has been deactivated by the seller.
            - PLATFORM_DEACTIVATE: The product has been deactivated by the platform.
            - NO_PLAN: There is no valid plan available for the creator to market the product.
            - PERMANENT_DELETED: The product has been permanently deleted and is no longer available.
            This field helps sellers and creators understand the current status of products associated with fulfillment
            orders, ensuring that all parties are aware of the availability and marketing status of the products involved in
            sample applications and collaborations.
    """

    id: str | Unset = UNSET
    expiration_time: int | Unset = UNSET
    total_suspend_duration: int | Unset = UNSET
    status: str | Unset = UNSET
    bound_product_status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        expiration_time = self.expiration_time

        total_suspend_duration = self.total_suspend_duration

        status = self.status

        bound_product_status = self.bound_product_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if expiration_time is not UNSET:
            field_dict["expiration_time"] = expiration_time
        if total_suspend_duration is not UNSET:
            field_dict["total_suspend_duration"] = total_suspend_duration
        if status is not UNSET:
            field_dict["status"] = status
        if bound_product_status is not UNSET:
            field_dict["bound_product_status"] = bound_product_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        expiration_time = d.pop("expiration_time", UNSET)

        total_suspend_duration = d.pop("total_suspend_duration", UNSET)

        status = d.pop("status", UNSET)

        bound_product_status = d.pop("bound_product_status", UNSET)

        search_creator_sample_applications_response_data_sample_application_creator_fulfillment = cls(
            id=id,
            expiration_time=expiration_time,
            total_suspend_duration=total_suspend_duration,
            status=status,
            bound_product_status=bound_product_status,
        )

        search_creator_sample_applications_response_data_sample_application_creator_fulfillment.additional_properties = d
        return search_creator_sample_applications_response_data_sample_application_creator_fulfillment

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
