from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.product_audit_status_change_webhook_data_integrated_platform_status_platform import (
    ProductAuditStatusChangeWebhookDataIntegratedPlatformStatusPlatform,
)
from ..models.product_audit_status_change_webhook_data_integrated_platform_status_status import (
    ProductAuditStatusChangeWebhookDataIntegratedPlatformStatusStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProductAuditStatusChangeWebhookDataIntegratedPlatformStatus")


@_attrs_define
class ProductAuditStatusChangeWebhookDataIntegratedPlatformStatus:
    """
    Attributes:
        platform (ProductAuditStatusChangeWebhookDataIntegratedPlatformStatusPlatform | Unset): The integrated platform
            name.
             Possible values:

             * TOKOPEDIA.
        status (ProductAuditStatusChangeWebhookDataIntegratedPlatformStatusStatus | Unset): The product audit status.
             Possible values:

             * NONE: The product is not applicable for audit because it has not been submitted for listing on this platform,
            or it is in a draft, frozen, or deactivated state.
             * AUDITING: The product is currently being audited.
             * FAILED: The product failed the audit or the audit was cancelled.
             * APPROVED: The product passed the audit and has been listed on the platform.
    """

    platform: ProductAuditStatusChangeWebhookDataIntegratedPlatformStatusPlatform | Unset = UNSET
    status: ProductAuditStatusChangeWebhookDataIntegratedPlatformStatusStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platform: str | Unset = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if platform is not UNSET:
            field_dict["platform"] = platform
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _platform = d.pop("platform", UNSET)
        platform: ProductAuditStatusChangeWebhookDataIntegratedPlatformStatusPlatform | Unset
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = ProductAuditStatusChangeWebhookDataIntegratedPlatformStatusPlatform(_platform)

        _status = d.pop("status", UNSET)
        status: ProductAuditStatusChangeWebhookDataIntegratedPlatformStatusStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ProductAuditStatusChangeWebhookDataIntegratedPlatformStatusStatus(_status)

        product_audit_status_change_webhook_data_integrated_platform_status = cls(
            platform=platform,
            status=status,
        )

        product_audit_status_change_webhook_data_integrated_platform_status.additional_properties = d
        return product_audit_status_change_webhook_data_integrated_platform_status

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
