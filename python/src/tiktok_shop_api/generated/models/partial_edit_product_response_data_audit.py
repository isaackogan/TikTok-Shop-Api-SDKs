from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.partial_edit_product_response_data_audit_status import PartialEditProductResponseDataAuditStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="PartialEditProductResponseDataAudit")


@_attrs_define
class PartialEditProductResponseDataAudit:
    """
    Attributes:
        status (PartialEditProductResponseDataAuditStatus | Unset): The product audit status.
            Possible values:
            - NONE: The product is not applicable for audit because it has not been submitted for listing on this platform,
            or it is in a draft, frozen, or deactivated state.
            - AUDITING: The product is currently being audited.
            - APPROVED: If you only edited the `price` or `inventory` fields of an approved product, the product remains
            approved and the edits are immediately published on the platform.
    """

    status: PartialEditProductResponseDataAuditStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: PartialEditProductResponseDataAuditStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PartialEditProductResponseDataAuditStatus(_status)

        partial_edit_product_response_data_audit = cls(
            status=status,
        )

        partial_edit_product_response_data_audit.additional_properties = d
        return partial_edit_product_response_data_audit

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
