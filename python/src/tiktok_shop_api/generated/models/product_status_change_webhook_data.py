from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ProductStatusChangeWebhookData")



@_attrs_define
class ProductStatusChangeWebhookData:
    """ 
        Attributes:
            product_id (int | Unset): The identification of a TikTok Shop product
            status (str | Unset): Product audit status, with possible values:

                 * PRODUCT_FIRST_PASS_REVIEW
                 * PRODUCT_STATUS_CHANGED
                 * PRODUCT_AUDIT_FAILURE
            suspended_reason (str | Unset): The reason a product audit was rejected or frozen
            update_time (int | Unset): The time when the status changed, represented as a Unix timestamp (seconds).
     """

    product_id: int | Unset = UNSET
    status: str | Unset = UNSET
    suspended_reason: str | Unset = UNSET
    update_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        status = self.status

        suspended_reason = self.suspended_reason

        update_time = self.update_time


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if status is not UNSET:
            field_dict["status"] = status
        if suspended_reason is not UNSET:
            field_dict["suspended_reason"] = suspended_reason
        if update_time is not UNSET:
            field_dict["update_time"] = update_time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_id = d.pop("product_id", UNSET)

        status = d.pop("status", UNSET)

        suspended_reason = d.pop("suspended_reason", UNSET)

        update_time = d.pop("update_time", UNSET)

        product_status_change_webhook_data = cls(
            product_id=product_id,
            status=status,
            suspended_reason=suspended_reason,
            update_time=update_time,
        )


        product_status_change_webhook_data.additional_properties = d
        return product_status_change_webhook_data

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
