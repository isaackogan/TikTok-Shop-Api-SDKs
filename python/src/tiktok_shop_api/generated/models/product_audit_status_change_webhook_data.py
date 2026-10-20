from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.product_audit_status_change_webhook_data_audit import ProductAuditStatusChangeWebhookDataAudit
  from ..models.product_audit_status_change_webhook_data_integrated_platform_status import ProductAuditStatusChangeWebhookDataIntegratedPlatformStatus





T = TypeVar("T", bound="ProductAuditStatusChangeWebhookData")



@_attrs_define
class ProductAuditStatusChangeWebhookData:
    """ 
        Attributes:
            product_id (int | Unset): The ID of the product.
            audit (ProductAuditStatusChangeWebhookDataAudit | Unset):
            integrated_platform_statuses (ProductAuditStatusChangeWebhookDataIntegratedPlatformStatus | Unset):
            update_time (int | Unset): The time when the status changed, represented as a Unix timestamp (seconds).
     """

    product_id: int | Unset = UNSET
    audit: ProductAuditStatusChangeWebhookDataAudit | Unset = UNSET
    integrated_platform_statuses: ProductAuditStatusChangeWebhookDataIntegratedPlatformStatus | Unset = UNSET
    update_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.product_audit_status_change_webhook_data_audit import ProductAuditStatusChangeWebhookDataAudit # noqa: PLC0415
        from ..models.product_audit_status_change_webhook_data_integrated_platform_status import ProductAuditStatusChangeWebhookDataIntegratedPlatformStatus # noqa: PLC0415
        product_id = self.product_id

        audit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.audit, Unset):
            audit = self.audit.to_dict()

        integrated_platform_statuses: dict[str, Any] | Unset = UNSET
        if not isinstance(self.integrated_platform_statuses, Unset):
            integrated_platform_statuses = self.integrated_platform_statuses.to_dict()

        update_time = self.update_time


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if audit is not UNSET:
            field_dict["audit"] = audit
        if integrated_platform_statuses is not UNSET:
            field_dict["integrated_platform_statuses"] = integrated_platform_statuses
        if update_time is not UNSET:
            field_dict["update_time"] = update_time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.product_audit_status_change_webhook_data_audit import ProductAuditStatusChangeWebhookDataAudit # noqa: PLC0415
        from ..models.product_audit_status_change_webhook_data_integrated_platform_status import ProductAuditStatusChangeWebhookDataIntegratedPlatformStatus # noqa: PLC0415
        d = dict(src_dict)
        product_id = d.pop("product_id", UNSET)

        _audit = d.pop("audit", UNSET)
        audit: ProductAuditStatusChangeWebhookDataAudit | Unset
        if isinstance(_audit,  Unset):
            audit = UNSET
        else:
            audit = ProductAuditStatusChangeWebhookDataAudit.from_dict(_audit)




        _integrated_platform_statuses = d.pop("integrated_platform_statuses", UNSET)
        integrated_platform_statuses: ProductAuditStatusChangeWebhookDataIntegratedPlatformStatus | Unset
        if isinstance(_integrated_platform_statuses,  Unset):
            integrated_platform_statuses = UNSET
        else:
            integrated_platform_statuses = ProductAuditStatusChangeWebhookDataIntegratedPlatformStatus.from_dict(_integrated_platform_statuses)




        update_time = d.pop("update_time", UNSET)

        product_audit_status_change_webhook_data = cls(
            product_id=product_id,
            audit=audit,
            integrated_platform_statuses=integrated_platform_statuses,
            update_time=update_time,
        )


        product_audit_status_change_webhook_data.additional_properties = d
        return product_audit_status_change_webhook_data

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
