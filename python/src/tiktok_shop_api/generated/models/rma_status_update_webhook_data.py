from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RMAStatusUpdateWebhookData")


@_attrs_define
class RMAStatusUpdateWebhookData:
    """
    Attributes:
        rma_id (str | Unset): Unique identifier of the RMA.
        aftersales_request_id (str | Unset): Parent aftersales request identifier.
        return_role (str | Unset): Role that initiated the return flow. Possible enumerations:

             * `BUYER`
             * `SELLER`
        rma_status (str | Unset): Current RMA status. Possible enumerations:

             * `INIT` = The RMA has been created
             * `AWAITING_BUYER_SHIPPED` = Awaiting buyer's action to ship the return package with carrier
             * `RETURN_IN_TRANSIT` = Buyer has shipped the return and is in transit to the sellers destination warehouse
             * `PENDING_PACKAGE_REVIEW` = The return package has been delivered and is pending seller package review. The
            seller has **2-4 business days** **SLA** to respond with a refund review/decision. Please refer to the latest
            seller academy document.
             * `PACKAGE_REVIEW_COMPLETED` = The package review lifecycle is complete, and the RMA refund has either been
            approved or rejected.
        rma_request_create_time (int | Unset): Creation time of the RMA in Unix seconds.
        rma_request_update_time (int | Unset): Last update time of the RMA in Unix seconds.
    """

    rma_id: str | Unset = UNSET
    aftersales_request_id: str | Unset = UNSET
    return_role: str | Unset = UNSET
    rma_status: str | Unset = UNSET
    rma_request_create_time: int | Unset = UNSET
    rma_request_update_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rma_id = self.rma_id

        aftersales_request_id = self.aftersales_request_id

        return_role = self.return_role

        rma_status = self.rma_status

        rma_request_create_time = self.rma_request_create_time

        rma_request_update_time = self.rma_request_update_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rma_id is not UNSET:
            field_dict["rma_id"] = rma_id
        if aftersales_request_id is not UNSET:
            field_dict["aftersales_request_id"] = aftersales_request_id
        if return_role is not UNSET:
            field_dict["return_role"] = return_role
        if rma_status is not UNSET:
            field_dict["rma_status"] = rma_status
        if rma_request_create_time is not UNSET:
            field_dict["rma_request_create_time"] = rma_request_create_time
        if rma_request_update_time is not UNSET:
            field_dict["rma_request_update_time"] = rma_request_update_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rma_id = d.pop("rma_id", UNSET)

        aftersales_request_id = d.pop("aftersales_request_id", UNSET)

        return_role = d.pop("return_role", UNSET)

        rma_status = d.pop("rma_status", UNSET)

        rma_request_create_time = d.pop("rma_request_create_time", UNSET)

        rma_request_update_time = d.pop("rma_request_update_time", UNSET)

        rma_status_update_webhook_data = cls(
            rma_id=rma_id,
            aftersales_request_id=aftersales_request_id,
            return_role=return_role,
            rma_status=rma_status,
            rma_request_create_time=rma_request_create_time,
            rma_request_update_time=rma_request_update_time,
        )

        rma_status_update_webhook_data.additional_properties = d
        return rma_status_update_webhook_data

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
