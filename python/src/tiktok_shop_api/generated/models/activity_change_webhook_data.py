from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_change_webhook_data_product_remove_list import ActivityChangeWebhookDataProductRemoveList
    from ..models.activity_change_webhook_data_product_update_list import ActivityChangeWebhookDataProductUpdateList


T = TypeVar("T", bound="ActivityChangeWebhookData")


@_attrs_define
class ActivityChangeWebhookData:
    """
    Attributes:
        activity_id (str | Unset): The ID of the promotion activity.
        update_time (int | Unset): The time when the status changed, represented as a Unix timestamp (seconds).
        change_type (str | Unset): The type of activity changes.

             * CREATE
             * UPDATE
             * DEACTIVATE
        product_update_list (ActivityChangeWebhookDataProductUpdateList | Unset):
        product_remove_list (ActivityChangeWebhookDataProductRemoveList | Unset):
    """

    activity_id: str | Unset = UNSET
    update_time: int | Unset = UNSET
    change_type: str | Unset = UNSET
    product_update_list: ActivityChangeWebhookDataProductUpdateList | Unset = UNSET
    product_remove_list: ActivityChangeWebhookDataProductRemoveList | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activity_id = self.activity_id

        update_time = self.update_time

        change_type = self.change_type

        product_update_list: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product_update_list, Unset):
            product_update_list = self.product_update_list.to_dict()

        product_remove_list: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product_remove_list, Unset):
            product_remove_list = self.product_remove_list.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if activity_id is not UNSET:
            field_dict["activity_id"] = activity_id
        if update_time is not UNSET:
            field_dict["update_time"] = update_time
        if change_type is not UNSET:
            field_dict["change_type"] = change_type
        if product_update_list is not UNSET:
            field_dict["product_update_list"] = product_update_list
        if product_remove_list is not UNSET:
            field_dict["product_remove_list"] = product_remove_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_change_webhook_data_product_remove_list import (
            ActivityChangeWebhookDataProductRemoveList,  # noqa: PLC0415
        )
        from ..models.activity_change_webhook_data_product_update_list import (
            ActivityChangeWebhookDataProductUpdateList,  # noqa: PLC0415
        )

        d = dict(src_dict)
        activity_id = d.pop("activity_id", UNSET)

        update_time = d.pop("update_time", UNSET)

        change_type = d.pop("change_type", UNSET)

        _product_update_list = d.pop("product_update_list", UNSET)
        product_update_list: ActivityChangeWebhookDataProductUpdateList | Unset
        if isinstance(_product_update_list, Unset):
            product_update_list = UNSET
        else:
            product_update_list = ActivityChangeWebhookDataProductUpdateList.from_dict(_product_update_list)

        _product_remove_list = d.pop("product_remove_list", UNSET)
        product_remove_list: ActivityChangeWebhookDataProductRemoveList | Unset
        if isinstance(_product_remove_list, Unset):
            product_remove_list = UNSET
        else:
            product_remove_list = ActivityChangeWebhookDataProductRemoveList.from_dict(_product_remove_list)

        activity_change_webhook_data = cls(
            activity_id=activity_id,
            update_time=update_time,
            change_type=change_type,
            product_update_list=product_update_list,
            product_remove_list=product_remove_list,
        )

        activity_change_webhook_data.additional_properties = d
        return activity_change_webhook_data

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
