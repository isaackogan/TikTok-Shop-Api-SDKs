from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.creator_search_sample_application_fulfillments_request_fulfillment_statuses_item import (
    CreatorSearchSampleApplicationFulfillmentsRequestFulfillmentStatusesItem,
)

T = TypeVar("T", bound="CreatorSearchSampleApplicationFulfillmentsRequest")


@_attrs_define
class CreatorSearchSampleApplicationFulfillmentsRequest:
    """
    Attributes:
        fulfillment_statuses (list[CreatorSearchSampleApplicationFulfillmentsRequestFulfillmentStatusesItem]): A list of
            fulfillment statuses. The response is filtered to include sample fulfillments with the `status` field set to one
            of the specified values. The possible values are:
            - PENDING: The creator has not yet fulfilled the content creation obligation.
            - ONGOING: Fulfillment is in progress; content has been created and is being evaluated against criteria.
            - SUCCEED: Fulfillment has been successfully completed; the content meets the required standards.
            - FAILED: Fulfillment failed; the content did not meet the required standards.
            - OVERDUE: Fulfillment is overdue; the creator did not meet the deadline.
            - SUSPEND: Fulfillment has been suspended.
            - CANCELLED: Fulfillment has been cancelled, either by the creator or due to operational reasons.
            - EXEMPTED: The creator is exempt from the fulfillment obligation.
    """

    fulfillment_statuses: list[CreatorSearchSampleApplicationFulfillmentsRequestFulfillmentStatusesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fulfillment_statuses = []
        for fulfillment_statuses_item_data in self.fulfillment_statuses:
            fulfillment_statuses_item = fulfillment_statuses_item_data.value
            fulfillment_statuses.append(fulfillment_statuses_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fulfillment_statuses": fulfillment_statuses,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fulfillment_statuses = []
        _fulfillment_statuses = d.pop("fulfillment_statuses")
        for fulfillment_statuses_item_data in _fulfillment_statuses:
            fulfillment_statuses_item = CreatorSearchSampleApplicationFulfillmentsRequestFulfillmentStatusesItem(
                fulfillment_statuses_item_data
            )

            fulfillment_statuses.append(fulfillment_statuses_item)

        creator_search_sample_application_fulfillments_request = cls(
            fulfillment_statuses=fulfillment_statuses,
        )

        creator_search_sample_application_fulfillments_request.additional_properties = d
        return creator_search_sample_application_fulfillments_request

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
