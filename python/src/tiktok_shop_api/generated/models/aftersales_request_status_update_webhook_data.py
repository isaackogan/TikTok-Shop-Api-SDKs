from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.aftersales_request_status_update_webhook_data_aftersales_request_status import (
    AftersalesRequestStatusUpdateWebhookDataAftersalesRequestStatus,
)
from ..models.aftersales_request_status_update_webhook_data_return_role import (
    AftersalesRequestStatusUpdateWebhookDataReturnRole,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AftersalesRequestStatusUpdateWebhookData")


@_attrs_define
class AftersalesRequestStatusUpdateWebhookData:
    """
    Attributes:
        aftersales_request_id (str | Unset): Unique identifier of the aftersales request.
        return_role (AftersalesRequestStatusUpdateWebhookDataReturnRole | Unset): Role that initiated the return flow.
            Possible enumerations:

             * `BUYER`
             * `SELLER`
        aftersales_request_status (AftersalesRequestStatusUpdateWebhookDataAftersalesRequestStatus | Unset): Current
            aftersales request status. Possible enumerations:

             * `PENDING_REQUEST_REVIEW`
             * `REQUEST_REVIEW_COMPLETED`
        aftersales_request_create_time (int | Unset): Creation time of the aftersales request in Unix seconds.
        aftersales_request_update_time (int | Unset): Last update time of the aftersales request in Unix seconds.
    """

    aftersales_request_id: str | Unset = UNSET
    return_role: AftersalesRequestStatusUpdateWebhookDataReturnRole | Unset = UNSET
    aftersales_request_status: AftersalesRequestStatusUpdateWebhookDataAftersalesRequestStatus | Unset = UNSET
    aftersales_request_create_time: int | Unset = UNSET
    aftersales_request_update_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aftersales_request_id = self.aftersales_request_id

        return_role: str | Unset = UNSET
        if not isinstance(self.return_role, Unset):
            return_role = self.return_role.value

        aftersales_request_status: str | Unset = UNSET
        if not isinstance(self.aftersales_request_status, Unset):
            aftersales_request_status = self.aftersales_request_status.value

        aftersales_request_create_time = self.aftersales_request_create_time

        aftersales_request_update_time = self.aftersales_request_update_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aftersales_request_id is not UNSET:
            field_dict["aftersales_request_id"] = aftersales_request_id
        if return_role is not UNSET:
            field_dict["return_role"] = return_role
        if aftersales_request_status is not UNSET:
            field_dict["aftersales_request_status"] = aftersales_request_status
        if aftersales_request_create_time is not UNSET:
            field_dict["aftersales_request_create_time"] = aftersales_request_create_time
        if aftersales_request_update_time is not UNSET:
            field_dict["aftersales_request_update_time"] = aftersales_request_update_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        aftersales_request_id = d.pop("aftersales_request_id", UNSET)

        _return_role = d.pop("return_role", UNSET)
        return_role: AftersalesRequestStatusUpdateWebhookDataReturnRole | Unset
        if isinstance(_return_role, Unset):
            return_role = UNSET
        else:
            return_role = AftersalesRequestStatusUpdateWebhookDataReturnRole(_return_role)

        _aftersales_request_status = d.pop("aftersales_request_status", UNSET)
        aftersales_request_status: AftersalesRequestStatusUpdateWebhookDataAftersalesRequestStatus | Unset
        if isinstance(_aftersales_request_status, Unset):
            aftersales_request_status = UNSET
        else:
            aftersales_request_status = AftersalesRequestStatusUpdateWebhookDataAftersalesRequestStatus(
                _aftersales_request_status
            )

        aftersales_request_create_time = d.pop("aftersales_request_create_time", UNSET)

        aftersales_request_update_time = d.pop("aftersales_request_update_time", UNSET)

        aftersales_request_status_update_webhook_data = cls(
            aftersales_request_id=aftersales_request_id,
            return_role=return_role,
            aftersales_request_status=aftersales_request_status,
            aftersales_request_create_time=aftersales_request_create_time,
            aftersales_request_update_time=aftersales_request_update_time,
        )

        aftersales_request_status_update_webhook_data.additional_properties = d
        return aftersales_request_status_update_webhook_data

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
