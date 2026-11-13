from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetLivestreamCampaignResponseDataLivestreamCampaignSessionStatistic")



@_attrs_define
class GetLivestreamCampaignResponseDataLivestreamCampaignSessionStatistic:
    """ 
        Attributes:
            approved_count (int | Unset): Number of approved registration records.
            expired_count (int | Unset): Number of registration records that are no longer effective.
            rejected_count (int | Unset): Number of rejected registration records.
            total_count (int | Unset): Total registered livestream sessions, not actual livestream broadcasts.
            under_review_count (int | Unset): Number of registration records under review.
            withdrawal_under_review_count (int | Unset): Number of registration records with withdrawal under review.
     """

    approved_count: int | Unset = UNSET
    expired_count: int | Unset = UNSET
    rejected_count: int | Unset = UNSET
    total_count: int | Unset = UNSET
    under_review_count: int | Unset = UNSET
    withdrawal_under_review_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        approved_count = self.approved_count

        expired_count = self.expired_count

        rejected_count = self.rejected_count

        total_count = self.total_count

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
        if rejected_count is not UNSET:
            field_dict["rejected_count"] = rejected_count
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
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

        rejected_count = d.pop("rejected_count", UNSET)

        total_count = d.pop("total_count", UNSET)

        under_review_count = d.pop("under_review_count", UNSET)

        withdrawal_under_review_count = d.pop("withdrawal_under_review_count", UNSET)

        get_livestream_campaign_response_data_livestream_campaign_session_statistic = cls(
            approved_count=approved_count,
            expired_count=expired_count,
            rejected_count=rejected_count,
            total_count=total_count,
            under_review_count=under_review_count,
            withdrawal_under_review_count=withdrawal_under_review_count,
        )


        get_livestream_campaign_response_data_livestream_campaign_session_statistic.additional_properties = d
        return get_livestream_campaign_response_data_livestream_campaign_session_statistic

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
