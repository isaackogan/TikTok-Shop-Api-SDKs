from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetProductCampaignResponseDataProductCampaignShopParticipationRegistrationStatistic")



@_attrs_define
class GetProductCampaignResponseDataProductCampaignShopParticipationRegistrationStatistic:
    """ 
        Attributes:
            approved_count (int | Unset): Number of products whose current registrations are approved. Not the number of
                products currently effective in the campaign.
            expired_count (int | Unset): Number of products whose current registrations are no longer effective.
            join_failed_count (int | Unset): Number of products whose participation failed during execution after approval.
            registered_count (int | Unset): Number of products with submitted or confirmed registrations, including
                subsequent rejection, invalidation, and withdrawal outcomes.
            rejected_count (int | Unset): Number of products whose current registration reviews were rejected.
            scheduled_count (int | Unset): Number of products assigned a campaign schedule. May overlap with the approved
                count.
            under_review_count (int | Unset): Number of products whose registrations are still under review.
            withdrawal_under_review_count (int | Unset): Number of products whose withdrawal requests are still under
                review.
     """

    approved_count: int | Unset = UNSET
    expired_count: int | Unset = UNSET
    join_failed_count: int | Unset = UNSET
    registered_count: int | Unset = UNSET
    rejected_count: int | Unset = UNSET
    scheduled_count: int | Unset = UNSET
    under_review_count: int | Unset = UNSET
    withdrawal_under_review_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        approved_count = self.approved_count

        expired_count = self.expired_count

        join_failed_count = self.join_failed_count

        registered_count = self.registered_count

        rejected_count = self.rejected_count

        scheduled_count = self.scheduled_count

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
        if join_failed_count is not UNSET:
            field_dict["join_failed_count"] = join_failed_count
        if registered_count is not UNSET:
            field_dict["registered_count"] = registered_count
        if rejected_count is not UNSET:
            field_dict["rejected_count"] = rejected_count
        if scheduled_count is not UNSET:
            field_dict["scheduled_count"] = scheduled_count
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

        join_failed_count = d.pop("join_failed_count", UNSET)

        registered_count = d.pop("registered_count", UNSET)

        rejected_count = d.pop("rejected_count", UNSET)

        scheduled_count = d.pop("scheduled_count", UNSET)

        under_review_count = d.pop("under_review_count", UNSET)

        withdrawal_under_review_count = d.pop("withdrawal_under_review_count", UNSET)

        get_product_campaign_response_data_product_campaign_shop_participation_registration_statistic = cls(
            approved_count=approved_count,
            expired_count=expired_count,
            join_failed_count=join_failed_count,
            registered_count=registered_count,
            rejected_count=rejected_count,
            scheduled_count=scheduled_count,
            under_review_count=under_review_count,
            withdrawal_under_review_count=withdrawal_under_review_count,
        )


        get_product_campaign_response_data_product_campaign_shop_participation_registration_statistic.additional_properties = d
        return get_product_campaign_response_data_product_campaign_shop_participation_registration_statistic

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
