from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_product_skpp_detail_response_data_reward_claim_condition import (
        GetProductSKPPDetailResponseDataRewardClaimCondition,
    )


T = TypeVar("T", bound="GetProductSKPPDetailResponseDataReward")


@_attrs_define
class GetProductSKPPDetailResponseDataReward:
    """
    Attributes:
        reward_type (str | Unset): Possible values: ADS_CREDIT / TOP_CREATOR_MATCHMAKING / SHOPTAB_PV /
            BIG_PROMOTION_CAMPAIGN / OFF_PLATFORM_BESTSELLER_ADS_CREDIT.
        title (str | Unset): Localized reward name, resolved from the shared Seller-Center content by the request
            locale.
        status (str | Unset): Possible values: NOT_GRANTED / PENDING / AVAILABLE
        ad_credit_claim_status (str | Unset): Ad-credit-only sub-status, returned only when reward_type = ADS_CREDIT and
            status = AVAILABLE. Possible values: UNCLAIMED (eligible, not yet claimed) / CLAIMED (claimed).
        value (str | Unset): Granted amount/quantity; currency-typed values lead with the currency symbol.
        claim_conditions (list[GetProductSKPPDetailResponseDataRewardClaimCondition] | Unset): Thresholds to unlock the
            reward; used by ADS_CREDIT.
        campaign_id (str | Unset): Returned only for reward_type = BIG_PROMOTION_CAMPAIGN.
    """

    reward_type: str | Unset = UNSET
    title: str | Unset = UNSET
    status: str | Unset = UNSET
    ad_credit_claim_status: str | Unset = UNSET
    value: str | Unset = UNSET
    claim_conditions: list[GetProductSKPPDetailResponseDataRewardClaimCondition] | Unset = UNSET
    campaign_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reward_type = self.reward_type

        title = self.title

        status = self.status

        ad_credit_claim_status = self.ad_credit_claim_status

        value = self.value

        claim_conditions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.claim_conditions, Unset):
            claim_conditions = []
            for claim_conditions_item_data in self.claim_conditions:
                claim_conditions_item = claim_conditions_item_data.to_dict()
                claim_conditions.append(claim_conditions_item)

        campaign_id = self.campaign_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reward_type is not UNSET:
            field_dict["reward_type"] = reward_type
        if title is not UNSET:
            field_dict["title"] = title
        if status is not UNSET:
            field_dict["status"] = status
        if ad_credit_claim_status is not UNSET:
            field_dict["ad_credit_claim_status"] = ad_credit_claim_status
        if value is not UNSET:
            field_dict["value"] = value
        if claim_conditions is not UNSET:
            field_dict["claim_conditions"] = claim_conditions
        if campaign_id is not UNSET:
            field_dict["campaign_id"] = campaign_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_product_skpp_detail_response_data_reward_claim_condition import (
            GetProductSKPPDetailResponseDataRewardClaimCondition,  # noqa: PLC0415
        )

        d = dict(src_dict)
        reward_type = d.pop("reward_type", UNSET)

        title = d.pop("title", UNSET)

        status = d.pop("status", UNSET)

        ad_credit_claim_status = d.pop("ad_credit_claim_status", UNSET)

        value = d.pop("value", UNSET)

        _claim_conditions = d.pop("claim_conditions", UNSET)
        claim_conditions: list[GetProductSKPPDetailResponseDataRewardClaimCondition] | Unset = UNSET
        if _claim_conditions is not UNSET:
            claim_conditions = []
            for claim_conditions_item_data in _claim_conditions:
                claim_conditions_item = GetProductSKPPDetailResponseDataRewardClaimCondition.from_dict(
                    claim_conditions_item_data
                )

                claim_conditions.append(claim_conditions_item)

        campaign_id = d.pop("campaign_id", UNSET)

        get_product_skpp_detail_response_data_reward = cls(
            reward_type=reward_type,
            title=title,
            status=status,
            ad_credit_claim_status=ad_credit_claim_status,
            value=value,
            claim_conditions=claim_conditions,
            campaign_id=campaign_id,
        )

        get_product_skpp_detail_response_data_reward.additional_properties = d
        return get_product_skpp_detail_response_data_reward

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
