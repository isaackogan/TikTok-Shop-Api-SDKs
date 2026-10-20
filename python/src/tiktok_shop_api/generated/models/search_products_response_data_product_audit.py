from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchProductsResponseDataProductAudit")


@_attrs_define
class SearchProductsResponseDataProductAudit:
    """
    Attributes:
        status (str | Unset): The product audit status.
            Possible values:
            - NONE: The product is not applicable for audit as it is still in a draft, frozen, or deactivated state.
            - AUDITING: The product is currently being audited.
            - FAILED: The product failed the audit, or the audit was cancelled.
            - PRE_APPROVED: The product has passed the audit but is not yet listed due to pending prerequisites.
            - APPROVED: The product passed the audit and has been listed on the platform.
        pre_approved_reasons (list[str] | Unset): The reason why the product is pre-approved.
            Applicable only if `audit.status=PRE_APPROVED`, otherwise returns an empty array.
            Possible values:
            - KYC_PENDING: The seller's onboarding (KYC - Know Your Customer information) is incomplete or awaiting
            processing.
            - RESTRICTED_CATEGORY_PENDING: The product is in a restricted category, and category approval is still pending.
            To request access, submit an application through the Qualification Center on TikTok Shop Seller Center.
            Applicable only for the US market.
    """

    status: str | Unset = UNSET
    pre_approved_reasons: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        pre_approved_reasons: list[str] | Unset = UNSET
        if not isinstance(self.pre_approved_reasons, Unset):
            pre_approved_reasons = self.pre_approved_reasons

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if pre_approved_reasons is not UNSET:
            field_dict["pre_approved_reasons"] = pre_approved_reasons

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = d.pop("status", UNSET)

        pre_approved_reasons = cast(list[str], d.pop("pre_approved_reasons", UNSET))

        search_products_response_data_product_audit = cls(
            status=status,
            pre_approved_reasons=pre_approved_reasons,
        )

        search_products_response_data_product_audit.additional_properties = d
        return search_products_response_data_product_audit

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
