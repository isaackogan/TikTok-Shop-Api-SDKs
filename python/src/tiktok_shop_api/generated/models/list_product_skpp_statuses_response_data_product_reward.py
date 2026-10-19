from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListProductSKPPStatusesResponseDataProductReward")


@_attrs_define
class ListProductSKPPStatusesResponseDataProductReward:
    """
    Attributes:
        reward_type (str | Unset): Possible values: ADS_CREDIT / TOP_CREATOR_MATCHMAKING / SHOPTAB_PV.
        status (str | Unset): Possible values: NOT_GRANTED (below threshold, locked) / PENDING (qualified, not yet
            granted) / AVAILABLE (granted).
        value (str | Unset): Granted amount/quantity; present only when status = AVAILABLE. Currency-typed (ADS_CREDIT)
            leads with the currency symbol (e.g. $15); count-typed (TOP_CREATOR_MATCHMAKING, SHOPTAB_PV) are bare numbers.
        ad_credit_claim_status (str | Unset): Ad-credit-only sub-status, returned only when reward_type = ADS_CREDIT and
            status = AVAILABLE. Possible values: UNCLAIMED (eligible, not yet claimed) / CLAIMED (claimed). Ad credit must
            be claimed manually.
    """

    reward_type: str | Unset = UNSET
    status: str | Unset = UNSET
    value: str | Unset = UNSET
    ad_credit_claim_status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reward_type = self.reward_type

        status = self.status

        value = self.value

        ad_credit_claim_status = self.ad_credit_claim_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reward_type is not UNSET:
            field_dict["reward_type"] = reward_type
        if status is not UNSET:
            field_dict["status"] = status
        if value is not UNSET:
            field_dict["value"] = value
        if ad_credit_claim_status is not UNSET:
            field_dict["ad_credit_claim_status"] = ad_credit_claim_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reward_type = d.pop("reward_type", UNSET)

        status = d.pop("status", UNSET)

        value = d.pop("value", UNSET)

        ad_credit_claim_status = d.pop("ad_credit_claim_status", UNSET)

        list_product_skpp_statuses_response_data_product_reward = cls(
            reward_type=reward_type,
            status=status,
            value=value,
            ad_credit_claim_status=ad_credit_claim_status,
        )

        list_product_skpp_statuses_response_data_product_reward.additional_properties = d
        return list_product_skpp_statuses_response_data_product_reward

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
