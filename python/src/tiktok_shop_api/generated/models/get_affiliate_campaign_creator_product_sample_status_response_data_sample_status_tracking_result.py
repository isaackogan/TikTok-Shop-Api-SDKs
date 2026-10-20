from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetAffiliateCampaignCreatorProductSampleStatusResponseDataSampleStatusTrackingResult")


@_attrs_define
class GetAffiliateCampaignCreatorProductSampleStatusResponseDataSampleStatusTrackingResult:
    """
    Attributes:
        tracking_event_update_date (str | Unset): The date at which the tracking event was last updated, in Unix epoch
            format.
        tracking_event_description (str | Unset): The title of the tracking event.
            - THE_PACKAGE_HAS_BEEN_DELIVERED
            - OUT_FOR_DELIVERY
            - ORDER_PACKED_AND_READY_FOR_DROP_OFF_AT_CARRIERS_FACILITY
            - ORDER_PLACED
        tracking_event_description_extended (str | Unset): More information about the tracking event
    """

    tracking_event_update_date: str | Unset = UNSET
    tracking_event_description: str | Unset = UNSET
    tracking_event_description_extended: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tracking_event_update_date = self.tracking_event_update_date

        tracking_event_description = self.tracking_event_description

        tracking_event_description_extended = self.tracking_event_description_extended

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tracking_event_update_date is not UNSET:
            field_dict["tracking_event_update_date"] = tracking_event_update_date
        if tracking_event_description is not UNSET:
            field_dict["tracking_event_description"] = tracking_event_description
        if tracking_event_description_extended is not UNSET:
            field_dict["tracking_event_description_extended"] = tracking_event_description_extended

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tracking_event_update_date = d.pop("tracking_event_update_date", UNSET)

        tracking_event_description = d.pop("tracking_event_description", UNSET)

        tracking_event_description_extended = d.pop("tracking_event_description_extended", UNSET)

        get_affiliate_campaign_creator_product_sample_status_response_data_sample_status_tracking_result = cls(
            tracking_event_update_date=tracking_event_update_date,
            tracking_event_description=tracking_event_description,
            tracking_event_description_extended=tracking_event_description_extended,
        )

        get_affiliate_campaign_creator_product_sample_status_response_data_sample_status_tracking_result.additional_properties = d
        return get_affiliate_campaign_creator_product_sample_status_response_data_sample_status_tracking_result

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
