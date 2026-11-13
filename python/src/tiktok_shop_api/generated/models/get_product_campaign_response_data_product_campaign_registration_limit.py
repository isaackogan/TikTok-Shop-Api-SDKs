from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetProductCampaignResponseDataProductCampaignRegistrationLimit")



@_attrs_define
class GetProductCampaignResponseDataProductCampaignRegistrationLimit:
    """ 
        Attributes:
            has_limit (bool | Unset): true: The shop has a quota limit. false: No limit applies, including exemptions.
                Omitted if the business quota conclusion is undetermined. Query failures still return an API error.
            is_limit_reached (bool | Unset): Always returned when has_limit=true and equals remaining_count==0. Always false
                when has_limit=false. Omitted when has_limit is omitted.
            limit_count (int | Unset): Always returned when has_limit=true. Nonnegative product quota applicable to the
                shop; otherwise omitted.
            remaining_count (int | Unset): Always returned when has_limit=true; equals max(limit_count-used_count, 0).
                Otherwise omitted. Zero must not be used to represent an unknown value.
            used_count (int | Unset): Always returned when has_limit=true. Nonnegative product slots consumed under the
                quota rules, not cumulative registrations; otherwise omitted.
     """

    has_limit: bool | Unset = UNSET
    is_limit_reached: bool | Unset = UNSET
    limit_count: int | Unset = UNSET
    remaining_count: int | Unset = UNSET
    used_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        has_limit = self.has_limit

        is_limit_reached = self.is_limit_reached

        limit_count = self.limit_count

        remaining_count = self.remaining_count

        used_count = self.used_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if has_limit is not UNSET:
            field_dict["has_limit"] = has_limit
        if is_limit_reached is not UNSET:
            field_dict["is_limit_reached"] = is_limit_reached
        if limit_count is not UNSET:
            field_dict["limit_count"] = limit_count
        if remaining_count is not UNSET:
            field_dict["remaining_count"] = remaining_count
        if used_count is not UNSET:
            field_dict["used_count"] = used_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        has_limit = d.pop("has_limit", UNSET)

        is_limit_reached = d.pop("is_limit_reached", UNSET)

        limit_count = d.pop("limit_count", UNSET)

        remaining_count = d.pop("remaining_count", UNSET)

        used_count = d.pop("used_count", UNSET)

        get_product_campaign_response_data_product_campaign_registration_limit = cls(
            has_limit=has_limit,
            is_limit_reached=is_limit_reached,
            limit_count=limit_count,
            remaining_count=remaining_count,
            used_count=used_count,
        )


        get_product_campaign_response_data_product_campaign_registration_limit.additional_properties = d
        return get_product_campaign_response_data_product_campaign_registration_limit

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
