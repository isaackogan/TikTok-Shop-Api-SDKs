from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_product_response_data_audit_failed_reason_listing_platform import (
    GetProductResponseDataAuditFailedReasonListingPlatform,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetProductResponseDataAuditFailedReason")


@_attrs_define
class GetProductResponseDataAuditFailedReason:
    """
    Attributes:
        listing_platform (GetProductResponseDataAuditFailedReasonListingPlatform | Unset): The platform for listing the
            product.
            Possible values:
            - TIKTOK_SHOP
            - TOKOPEDIA
        position (str | Unset): The audit failure reason name.
        reasons (list[str] | Unset): A brief reason for failing TikTok Shop audit.
        suggestions (list[str] | Unset): A detailed explanation of the reason for failure.
    """

    listing_platform: GetProductResponseDataAuditFailedReasonListingPlatform | Unset = UNSET
    position: str | Unset = UNSET
    reasons: list[str] | Unset = UNSET
    suggestions: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        listing_platform: str | Unset = UNSET
        if not isinstance(self.listing_platform, Unset):
            listing_platform = self.listing_platform.value

        position = self.position

        reasons: list[str] | Unset = UNSET
        if not isinstance(self.reasons, Unset):
            reasons = self.reasons

        suggestions: list[str] | Unset = UNSET
        if not isinstance(self.suggestions, Unset):
            suggestions = self.suggestions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if listing_platform is not UNSET:
            field_dict["listing_platform"] = listing_platform
        if position is not UNSET:
            field_dict["position"] = position
        if reasons is not UNSET:
            field_dict["reasons"] = reasons
        if suggestions is not UNSET:
            field_dict["suggestions"] = suggestions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _listing_platform = d.pop("listing_platform", UNSET)
        listing_platform: GetProductResponseDataAuditFailedReasonListingPlatform | Unset
        if isinstance(_listing_platform, Unset):
            listing_platform = UNSET
        else:
            listing_platform = GetProductResponseDataAuditFailedReasonListingPlatform(_listing_platform)

        position = d.pop("position", UNSET)

        reasons = cast(list[str], d.pop("reasons", UNSET))

        suggestions = cast(list[str], d.pop("suggestions", UNSET))

        get_product_response_data_audit_failed_reason = cls(
            listing_platform=listing_platform,
            position=position,
            reasons=reasons,
            suggestions=suggestions,
        )

        get_product_response_data_audit_failed_reason.additional_properties = d
        return get_product_response_data_audit_failed_reason

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
