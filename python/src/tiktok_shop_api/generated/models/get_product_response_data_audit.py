from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_product_response_data_audit_not_submitted_reasons_item import (
    GetProductResponseDataAuditNotSubmittedReasonsItem,
)
from ..models.get_product_response_data_audit_pre_approved_reasons_item import (
    GetProductResponseDataAuditPreApprovedReasonsItem,
)
from ..models.get_product_response_data_audit_status import GetProductResponseDataAuditStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetProductResponseDataAudit")


@_attrs_define
class GetProductResponseDataAudit:
    """
    Attributes:
        pre_approved_reasons (list[GetProductResponseDataAuditPreApprovedReasonsItem] | Unset): The reason why the
            product is pre-approved.
            Applicable only if `audit.status=PRE_APPROVED`, otherwise returns an empty array.

            Possible values:
            - KYC_PENDING: The seller's onboarding (KYC - Know Your Customer information) is incomplete or awaiting
            processing.
            - RESTRICTED_CATEGORY_PENDING: The product is in a restricted category, and category approval is still pending.
            To request access, submit an application through the Qualification Center on TikTok Shop Seller Center.
            Applicable only for the US market.
        status (GetProductResponseDataAuditStatus | Unset): The product audit status.
            Possible values:
            - NONE: The product is not applicable for audit because it has not been submitted for listing on this platform,
            or it is in a draft, frozen, or deactivated state.
            - AUDITING: The product is currently being audited.
            - FAILED: The product failed the audit, or the audit was cancelled.
            - PRE_APPROVED: The product has passed the audit but is not yet listed due to pending prerequisites. Refer to
            `pre_approved_reasons` for the prerequisites.
            - APPROVED: The product passed the audit and has been listed on the platform.
        not_submitted_reasons (list[GetProductResponseDataAuditNotSubmittedReasonsItem] | Unset): The reasons why the
            product has not been submitted for TikTok Shop audit.
            Applicable only when `audit.status=NONE` and the product cannot be submitted for audit because the shop has not
            met one or more listing prerequisites; otherwise, an empty array is returned.

            Possible values:
            - PAYMENT_ACCOUNT_NOT_LINKED: No payment account is linked to the shop.
            - SHOP_INACTIVE: The shop is inactive.
            - W8_NOT_CONFIGURED: The required W-8 tax information has not been provided for the shop. Applicable only to US
            shops.
    """

    pre_approved_reasons: list[GetProductResponseDataAuditPreApprovedReasonsItem] | Unset = UNSET
    status: GetProductResponseDataAuditStatus | Unset = UNSET
    not_submitted_reasons: list[GetProductResponseDataAuditNotSubmittedReasonsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pre_approved_reasons: list[str] | Unset = UNSET
        if not isinstance(self.pre_approved_reasons, Unset):
            pre_approved_reasons = []
            for pre_approved_reasons_item_data in self.pre_approved_reasons:
                pre_approved_reasons_item = pre_approved_reasons_item_data.value
                pre_approved_reasons.append(pre_approved_reasons_item)

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        not_submitted_reasons: list[str] | Unset = UNSET
        if not isinstance(self.not_submitted_reasons, Unset):
            not_submitted_reasons = []
            for not_submitted_reasons_item_data in self.not_submitted_reasons:
                not_submitted_reasons_item = not_submitted_reasons_item_data.value
                not_submitted_reasons.append(not_submitted_reasons_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pre_approved_reasons is not UNSET:
            field_dict["pre_approved_reasons"] = pre_approved_reasons
        if status is not UNSET:
            field_dict["status"] = status
        if not_submitted_reasons is not UNSET:
            field_dict["not_submitted_reasons"] = not_submitted_reasons

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _pre_approved_reasons = d.pop("pre_approved_reasons", UNSET)
        pre_approved_reasons: list[GetProductResponseDataAuditPreApprovedReasonsItem] | Unset = UNSET
        if _pre_approved_reasons is not UNSET:
            pre_approved_reasons = []
            for pre_approved_reasons_item_data in _pre_approved_reasons:
                pre_approved_reasons_item = GetProductResponseDataAuditPreApprovedReasonsItem(
                    pre_approved_reasons_item_data
                )

                pre_approved_reasons.append(pre_approved_reasons_item)

        _status = d.pop("status", UNSET)
        status: GetProductResponseDataAuditStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = GetProductResponseDataAuditStatus(_status)

        _not_submitted_reasons = d.pop("not_submitted_reasons", UNSET)
        not_submitted_reasons: list[GetProductResponseDataAuditNotSubmittedReasonsItem] | Unset = UNSET
        if _not_submitted_reasons is not UNSET:
            not_submitted_reasons = []
            for not_submitted_reasons_item_data in _not_submitted_reasons:
                not_submitted_reasons_item = GetProductResponseDataAuditNotSubmittedReasonsItem(
                    not_submitted_reasons_item_data
                )

                not_submitted_reasons.append(not_submitted_reasons_item)

        get_product_response_data_audit = cls(
            pre_approved_reasons=pre_approved_reasons,
            status=status,
            not_submitted_reasons=not_submitted_reasons,
        )

        get_product_response_data_audit.additional_properties = d
        return get_product_response_data_audit

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
