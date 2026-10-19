from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.remove_promotion_activity_products_response_data_status import (
    RemovePromotionActivityProductsResponseDataStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RemovePromotionActivityProductsResponseData")


@_attrs_define
class RemovePromotionActivityProductsResponseData:
    """
    Attributes:
        activity_id (str | Unset): A unique ID that identifies activities.
        status (RemovePromotionActivityProductsResponseDataStatus | Unset): Activity status.
            Possible values:
            - DRAFT: Promotion activities with this status are not available to TikTok users.
            - NOT_START: Promotion activities with this status are not available to TikTok users until the set activity
            start time.
            - ONGOING: Promotion activities with this status are available to TikTok users.
            - EXPIRED: Promotion activities with this status are not available to TikTok users because it has expired.
            - DEACTIVATED: The activity has been deactivated by the seller and is not available to TikTok users.
            - NOT_EFFECTIVE:  The activity is terminated by the platform and is not available to TikTok users.
        update_time (int | Unset): The time when the response was generated, as a Unix timestamp in seconds (UTC).
    """

    activity_id: str | Unset = UNSET
    status: RemovePromotionActivityProductsResponseDataStatus | Unset = UNSET
    update_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activity_id = self.activity_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        update_time = self.update_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if activity_id is not UNSET:
            field_dict["activity_id"] = activity_id
        if status is not UNSET:
            field_dict["status"] = status
        if update_time is not UNSET:
            field_dict["update_time"] = update_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        activity_id = d.pop("activity_id", UNSET)

        _status = d.pop("status", UNSET)
        status: RemovePromotionActivityProductsResponseDataStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RemovePromotionActivityProductsResponseDataStatus(_status)

        update_time = d.pop("update_time", UNSET)

        remove_promotion_activity_products_response_data = cls(
            activity_id=activity_id,
            status=status,
            update_time=update_time,
        )

        remove_promotion_activity_products_response_data.additional_properties = d
        return remove_promotion_activity_products_response_data

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
