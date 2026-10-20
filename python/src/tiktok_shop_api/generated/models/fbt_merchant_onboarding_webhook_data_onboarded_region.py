from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FBTMerchantOnboardingWebhookDataOnboardedRegion")


@_attrs_define
class FBTMerchantOnboardingWebhookDataOnboardedRegion:
    """
    Attributes:
        region_code (str | Unset): Onboarded FBT region code.
    """

    region_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        region_code = self.region_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if region_code is not UNSET:
            field_dict["region_code"] = region_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        region_code = d.pop("region_code", UNSET)

        fbt_merchant_onboarding_webhook_data_onboarded_region = cls(
            region_code=region_code,
        )

        fbt_merchant_onboarding_webhook_data_onboarded_region.additional_properties = d
        return fbt_merchant_onboarding_webhook_data_onboarded_region

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
