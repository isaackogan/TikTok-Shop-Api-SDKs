from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ListRegisteredCampaignResponseDataCampaignRegistrationStatistic")



@_attrs_define
class ListRegisteredCampaignResponseDataCampaignRegistrationStatistic:
    """ 
        Attributes:
            approved_count (int | Unset): Registrations currently approved. Not the number with effective benefits.
            expired_count (int | Unset): Registrations currently no longer effective. Not limited to campaigns that ended as
                scheduled.
            registered_count (int | Unset): Total registrations for product, livestream, or short video campaigns, including
                rejected and no longer effective registrations. Omitted for shop campaigns.
            rejected_count (int | Unset): Registrations currently rejected.
            scheduled_count (int | Unset): Scheduled product count, applicable only to product campaigns. Omitted for other
                types. Must not be added to approved_count.
            suspended_count (int | Unset): Paused registration record count, applicable only to shop campaigns. Omitted for
                other types.
            under_review_count (int | Unset): Registrations currently under review. Not the number awaiting seller
                confirmation.
            withdrawal_under_review_count (int | Unset): Withdrawal requests under review. Does not mean withdrawal is
                complete.
     """

    approved_count: int | Unset = UNSET
    expired_count: int | Unset = UNSET
    registered_count: int | Unset = UNSET
    rejected_count: int | Unset = UNSET
    scheduled_count: int | Unset = UNSET
    suspended_count: int | Unset = UNSET
    under_review_count: int | Unset = UNSET
    withdrawal_under_review_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        approved_count = self.approved_count

        expired_count = self.expired_count

        registered_count = self.registered_count

        rejected_count = self.rejected_count

        scheduled_count = self.scheduled_count

        suspended_count = self.suspended_count

        under_review_count = self.under_review_count

        withdrawal_under_review_count = self.withdrawal_under_review_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if approved_count is not UNSET:
            field_dict["approved_count"] = approved_count
        if expired_count is not UNSET:
            field_dict["expired_count"] = expired_count
        if registered_count is not UNSET:
            field_dict["registered_count"] = registered_count
        if rejected_count is not UNSET:
            field_dict["rejected_count"] = rejected_count
        if scheduled_count is not UNSET:
            field_dict["scheduled_count"] = scheduled_count
        if suspended_count is not UNSET:
            field_dict["suspended_count"] = suspended_count
        if under_review_count is not UNSET:
            field_dict["under_review_count"] = under_review_count
        if withdrawal_under_review_count is not UNSET:
            field_dict["withdrawal_under_review_count"] = withdrawal_under_review_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        approved_count = d.pop("approved_count", UNSET)

        expired_count = d.pop("expired_count", UNSET)

        registered_count = d.pop("registered_count", UNSET)

        rejected_count = d.pop("rejected_count", UNSET)

        scheduled_count = d.pop("scheduled_count", UNSET)

        suspended_count = d.pop("suspended_count", UNSET)

        under_review_count = d.pop("under_review_count", UNSET)

        withdrawal_under_review_count = d.pop("withdrawal_under_review_count", UNSET)

        list_registered_campaign_response_data_campaign_registration_statistic = cls(
            approved_count=approved_count,
            expired_count=expired_count,
            registered_count=registered_count,
            rejected_count=rejected_count,
            scheduled_count=scheduled_count,
            suspended_count=suspended_count,
            under_review_count=under_review_count,
            withdrawal_under_review_count=withdrawal_under_review_count,
        )


        list_registered_campaign_response_data_campaign_registration_statistic.additional_properties = d
        return list_registered_campaign_response_data_campaign_registration_statistic

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
