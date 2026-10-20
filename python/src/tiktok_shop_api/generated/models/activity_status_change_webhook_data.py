from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ActivityStatusChangeWebhookData")



@_attrs_define
class ActivityStatusChangeWebhookData:
    """ 
        Attributes:
            activity_id (str | Unset): The ID of the promotion activity.
            update_time (int | Unset): The time when the status changed, represented as a Unix timestamp (seconds).
            activity_type (str | Unset): The type of the promotion activity. Possible values are:

                 * `FIXED_PRICE`
                 * `DIRECT_DISCOUNT`
                 * `SHIPPING_DISCOUNT`
                 * `BUY_MORE_SAVE_MORE`
                 * `FLASHSALE` (Only available in SEA markets: SG, TH, ID, MY, PH, VN)
            product_level (str | Unset): Activity product dimension, values are:

                 * `PRODUCT`
                 * `VARIATION`
                 * `SHOP`
            status (str | Unset): The current status of the promotion activity. Possible values are:

                 * `ONGOING`
                 * `EXPIRED`
                 * `DEACTIVATED`
     """

    activity_id: str | Unset = UNSET
    update_time: int | Unset = UNSET
    activity_type: str | Unset = UNSET
    product_level: str | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        activity_id = self.activity_id

        update_time = self.update_time

        activity_type = self.activity_type

        product_level = self.product_level

        status = self.status


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if activity_id is not UNSET:
            field_dict["activity_id"] = activity_id
        if update_time is not UNSET:
            field_dict["update_time"] = update_time
        if activity_type is not UNSET:
            field_dict["activity_type"] = activity_type
        if product_level is not UNSET:
            field_dict["product_level"] = product_level
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        activity_id = d.pop("activity_id", UNSET)

        update_time = d.pop("update_time", UNSET)

        activity_type = d.pop("activity_type", UNSET)

        product_level = d.pop("product_level", UNSET)

        status = d.pop("status", UNSET)

        activity_status_change_webhook_data = cls(
            activity_id=activity_id,
            update_time=update_time,
            activity_type=activity_type,
            product_level=product_level,
            status=status,
        )


        activity_status_change_webhook_data.additional_properties = d
        return activity_status_change_webhook_data

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
