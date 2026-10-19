from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.creator_search_sample_application_fulfillments_response_data_fulfillment_bound_product_status import (
    CreatorSearchSampleApplicationFulfillmentsResponseDataFulfillmentBoundProductStatus,
)
from ..models.creator_search_sample_application_fulfillments_response_data_fulfillment_sample_application_type import (
    CreatorSearchSampleApplicationFulfillmentsResponseDataFulfillmentSampleApplicationType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatorSearchSampleApplicationFulfillmentsResponseDataFulfillment")


@_attrs_define
class CreatorSearchSampleApplicationFulfillmentsResponseDataFulfillment:
    """
    Attributes:
        id (str | Unset): The fulfillment identifier.
        shop_id (str | Unset): The TikTok Shop identifier.
        application_id (str | Unset): The sample application identifier.
        sample_application_type (CreatorSearchSampleApplicationFulfillmentsResponseDataFulfillmentSampleApplicationType
            | Unset): The type of the sample application. Possible values:
            - FREE_SAMPLE
            - SAMPLE_COUPON
            - SAMPLE_CAMPAIGN
            - PLATFORM_FREE_SAMPLE
            - REFUNDABLE_SAMPLE
            - UNSPECIFIED
        product_id (str | Unset): The product identifier.
        expiration_time (int | Unset): Fulfillment deadline timestamp.
            Usually the value is  `{you_receiving_sample_time} + 14Days`. But if you apply for fulfillment suspension, the
            value is `{you_receiving_sample_time} + 14Days + total_suspend_duration`.
        total_suspend_duration (int | Unset): The duration you applied for fulfillment suspension in seconds.
        status (str | Unset): The fulfillment status.This is an enumerated type with values:
            - PENDING: The creator has not yet fulfilled the content creation obligation.
            - ONGOING: Fulfillment is in progress; content has been created and is being evaluated against criteria.
            - SUCCEED: Fulfillment has been successfully completed; the content meets the required standards.
            - FAILED: Fulfillment failed; the content did not meet the required standards.
            - OVERDUE: Fulfillment is overdue; the creator did not meet the deadline.SUSPEND: Fulfillment has been
            suspended.
            - CANCELLED: Fulfillment has been cancelled, either by the creator or due to operational reasons.
            - EXEMPTED: The creator is exempt from the fulfillment obligation.
        bound_product_status (CreatorSearchSampleApplicationFulfillmentsResponseDataFulfillmentBoundProductStatus |
            Unset): The promotion status of the product associated with the fulfillment. Possible values:
            - UNKNOWN: The product's promotion status is unknown.
            - LIVE: The product is available for promotion.
            - OUT_OF_STOCK: The product is out of stock.
            - SELLER_DEACTIVATE: The product has been deactivated by the seller.
            - PLATFORM_DEACTIVATE: The product has been deactivated by the platform.
            - NO_PLAN: There is no valid plan available for the creator to promote the product.
            - PERMANENT_DELETED: The product has been permanently deleted and is no longer available.
    """

    id: str | Unset = UNSET
    shop_id: str | Unset = UNSET
    application_id: str | Unset = UNSET
    sample_application_type: (
        CreatorSearchSampleApplicationFulfillmentsResponseDataFulfillmentSampleApplicationType | Unset
    ) = UNSET
    product_id: str | Unset = UNSET
    expiration_time: int | Unset = UNSET
    total_suspend_duration: int | Unset = UNSET
    status: str | Unset = UNSET
    bound_product_status: (
        CreatorSearchSampleApplicationFulfillmentsResponseDataFulfillmentBoundProductStatus | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        shop_id = self.shop_id

        application_id = self.application_id

        sample_application_type: str | Unset = UNSET
        if not isinstance(self.sample_application_type, Unset):
            sample_application_type = self.sample_application_type.value

        product_id = self.product_id

        expiration_time = self.expiration_time

        total_suspend_duration = self.total_suspend_duration

        status = self.status

        bound_product_status: str | Unset = UNSET
        if not isinstance(self.bound_product_status, Unset):
            bound_product_status = self.bound_product_status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if shop_id is not UNSET:
            field_dict["shop_id"] = shop_id
        if application_id is not UNSET:
            field_dict["application_id"] = application_id
        if sample_application_type is not UNSET:
            field_dict["sample_application_type"] = sample_application_type
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
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

        shop_id = d.pop("shop_id", UNSET)

        application_id = d.pop("application_id", UNSET)

        _sample_application_type = d.pop("sample_application_type", UNSET)
        sample_application_type: (
            CreatorSearchSampleApplicationFulfillmentsResponseDataFulfillmentSampleApplicationType | Unset
        )
        if isinstance(_sample_application_type, Unset):
            sample_application_type = UNSET
        else:
            sample_application_type = (
                CreatorSearchSampleApplicationFulfillmentsResponseDataFulfillmentSampleApplicationType(
                    _sample_application_type
                )
            )

        product_id = d.pop("product_id", UNSET)

        expiration_time = d.pop("expiration_time", UNSET)

        total_suspend_duration = d.pop("total_suspend_duration", UNSET)

        status = d.pop("status", UNSET)

        _bound_product_status = d.pop("bound_product_status", UNSET)
        bound_product_status: (
            CreatorSearchSampleApplicationFulfillmentsResponseDataFulfillmentBoundProductStatus | Unset
        )
        if isinstance(_bound_product_status, Unset):
            bound_product_status = UNSET
        else:
            bound_product_status = CreatorSearchSampleApplicationFulfillmentsResponseDataFulfillmentBoundProductStatus(
                _bound_product_status
            )

        creator_search_sample_application_fulfillments_response_data_fulfillment = cls(
            id=id,
            shop_id=shop_id,
            application_id=application_id,
            sample_application_type=sample_application_type,
            product_id=product_id,
            expiration_time=expiration_time,
            total_suspend_duration=total_suspend_duration,
            status=status,
            bound_product_status=bound_product_status,
        )

        creator_search_sample_application_fulfillments_response_data_fulfillment.additional_properties = d
        return creator_search_sample_application_fulfillments_response_data_fulfillment

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
