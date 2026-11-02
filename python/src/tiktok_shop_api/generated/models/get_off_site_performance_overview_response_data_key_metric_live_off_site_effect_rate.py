from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetOffSitePerformanceOverviewResponseDataKeyMetricLiveOffSiteEffectRate")



@_attrs_define
class GetOffSitePerformanceOverviewResponseDataKeyMetricLiveOffSiteEffectRate:
    """ 
        Attributes:
            affiliate_account_rate (str | Unset): Off-site GMV divided by TikTok Shop GMV for LIVE content from affiliate
                accounts in the selected report week.
            linked_account_rate (str | Unset): Off-site GMV divided by TikTok Shop GMV for LIVE content from linked accounts
                in the selected report week.
            overall_rate (str | Unset): Off-site GMV divided by TikTok Shop GMV for LIVE content in the selected report
                week.
     """

    affiliate_account_rate: str | Unset = UNSET
    linked_account_rate: str | Unset = UNSET
    overall_rate: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        affiliate_account_rate = self.affiliate_account_rate

        linked_account_rate = self.linked_account_rate

        overall_rate = self.overall_rate


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if affiliate_account_rate is not UNSET:
            field_dict["affiliate_account_rate"] = affiliate_account_rate
        if linked_account_rate is not UNSET:
            field_dict["linked_account_rate"] = linked_account_rate
        if overall_rate is not UNSET:
            field_dict["overall_rate"] = overall_rate

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        affiliate_account_rate = d.pop("affiliate_account_rate", UNSET)

        linked_account_rate = d.pop("linked_account_rate", UNSET)

        overall_rate = d.pop("overall_rate", UNSET)

        get_off_site_performance_overview_response_data_key_metric_live_off_site_effect_rate = cls(
            affiliate_account_rate=affiliate_account_rate,
            linked_account_rate=linked_account_rate,
            overall_rate=overall_rate,
        )


        get_off_site_performance_overview_response_data_key_metric_live_off_site_effect_rate.additional_properties = d
        return get_off_site_performance_overview_response_data_key_metric_live_off_site_effect_rate

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
