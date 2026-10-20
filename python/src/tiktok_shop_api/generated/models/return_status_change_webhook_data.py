from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ReturnStatusChangeWebhookData")



@_attrs_define
class ReturnStatusChangeWebhookData:
    """ 
        Attributes:
            order_id (str | Unset): The identification of a TikTok Shop order
            return_role (str | Unset): Return or refund request user, with possible values:

                 * BUYER
                 * SELLER
                 * SYSTEM
            return_type (str | Unset): The return or refund request type, with possible values:

                 * REFUND
                 * REPLACEMENT
                 * RETURN_AND_REFUND
            return_status (str | Unset): The return status for a request, with possible values:

                 * AWAITING_BUYER_SHIP
                 * BUYER_SHIPPED_ITEM
                 * REFUND_OR_RETURN_REQUEST_REJECT
                 * REJECT_RECEIVE_PACKAGE
                 * REPLACEMENT_REQUEST_CANCEL
                 * REPLACEMENT_REQUEST_COMPLETE
                 * REPLACEMENT_REQUEST_PENDING
                 * REPLACEMENT_REQUEST_REFUND_SUCCESS
                 * REPLACEMENT_REQUEST_REJECT
                 * RETURN_OR_REFUND_REQUEST_CANCEL
                 * RETURN_OR_REFUND_REQUEST_COMPLETE
                 * RETURN_OR_REFUND_REQUEST_PENDING
                 * RETURN_OR_REFUND_REQUEST_SUCCESS
            return_id (str | Unset): The identifier of a specific return
            create_time (int | Unset): The time when the request was created.
            update_time (int | Unset): The time when return order status update, represented as a Unix timestamp (seconds).
     """

    order_id: str | Unset = UNSET
    return_role: str | Unset = UNSET
    return_type: str | Unset = UNSET
    return_status: str | Unset = UNSET
    return_id: str | Unset = UNSET
    create_time: int | Unset = UNSET
    update_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        order_id = self.order_id

        return_role = self.return_role

        return_type = self.return_type

        return_status = self.return_status

        return_id = self.return_id

        create_time = self.create_time

        update_time = self.update_time


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if return_role is not UNSET:
            field_dict["return_role"] = return_role
        if return_type is not UNSET:
            field_dict["return_type"] = return_type
        if return_status is not UNSET:
            field_dict["return_status"] = return_status
        if return_id is not UNSET:
            field_dict["return_id"] = return_id
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if update_time is not UNSET:
            field_dict["update_time"] = update_time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order_id = d.pop("order_id", UNSET)

        return_role = d.pop("return_role", UNSET)

        return_type = d.pop("return_type", UNSET)

        return_status = d.pop("return_status", UNSET)

        return_id = d.pop("return_id", UNSET)

        create_time = d.pop("create_time", UNSET)

        update_time = d.pop("update_time", UNSET)

        return_status_change_webhook_data = cls(
            order_id=order_id,
            return_role=return_role,
            return_type=return_type,
            return_status=return_status,
            return_id=return_id,
            create_time=create_time,
            update_time=update_time,
        )


        return_status_change_webhook_data.additional_properties = d
        return return_status_change_webhook_data

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
