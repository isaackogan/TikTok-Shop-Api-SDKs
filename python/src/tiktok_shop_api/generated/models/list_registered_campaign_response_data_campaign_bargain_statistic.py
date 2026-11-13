from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ListRegisteredCampaignResponseDataCampaignBargainStatistic")



@_attrs_define
class ListRegisteredCampaignResponseDataCampaignBargainStatistic:
    """ 
        Attributes:
            promotion_rejected_count (int | Unset): Number of rejected subsidy plans, not rejected product registrations.
            promotion_to_be_set_count (int | Unset): Number awaiting subsidy plan configuration.
            promotion_under_review_count (int | Unset): Number of subsidy plans under review, independent of standard
                registration review counts.
            under_review_count (int | Unset): Number of products under review in the negotiation process, not standard
                registrations awaiting review.
     """

    promotion_rejected_count: int | Unset = UNSET
    promotion_to_be_set_count: int | Unset = UNSET
    promotion_under_review_count: int | Unset = UNSET
    under_review_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        promotion_rejected_count = self.promotion_rejected_count

        promotion_to_be_set_count = self.promotion_to_be_set_count

        promotion_under_review_count = self.promotion_under_review_count

        under_review_count = self.under_review_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if promotion_rejected_count is not UNSET:
            field_dict["promotion_rejected_count"] = promotion_rejected_count
        if promotion_to_be_set_count is not UNSET:
            field_dict["promotion_to_be_set_count"] = promotion_to_be_set_count
        if promotion_under_review_count is not UNSET:
            field_dict["promotion_under_review_count"] = promotion_under_review_count
        if under_review_count is not UNSET:
            field_dict["under_review_count"] = under_review_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        promotion_rejected_count = d.pop("promotion_rejected_count", UNSET)

        promotion_to_be_set_count = d.pop("promotion_to_be_set_count", UNSET)

        promotion_under_review_count = d.pop("promotion_under_review_count", UNSET)

        under_review_count = d.pop("under_review_count", UNSET)

        list_registered_campaign_response_data_campaign_bargain_statistic = cls(
            promotion_rejected_count=promotion_rejected_count,
            promotion_to_be_set_count=promotion_to_be_set_count,
            promotion_under_review_count=promotion_under_review_count,
            under_review_count=under_review_count,
        )


        list_registered_campaign_response_data_campaign_bargain_statistic.additional_properties = d
        return list_registered_campaign_response_data_campaign_bargain_statistic

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
