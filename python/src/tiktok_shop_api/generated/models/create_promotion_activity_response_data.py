from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatePromotionActivityResponseData")


@_attrs_define
class CreatePromotionActivityResponseData:
    """
    Attributes:
        activity_id (str | Unset): On success, the ID of the created activity. Use it as `activity_id` when adding
            products or SKUs with [Update Activity
            Product](https://partner.tiktokshop.com/docv2/page/650d32c42aaa3602b86ccb5c).
        create_time (int | Unset): The time when the activity was created.
        update_time (int | Unset): The time when the activity was last updated.
        status (str | Unset): Possible values:
            - DRAFT: Promotion activities with this status are not available to TikTok users.
            - NOT_START: Promotion activities with this status are not available to TikTok users until the set activity
            start time.
            - ONGOING: Promotion activities with this status are available to TikTok users.
            - EXPIRED: Promotion activities with this status are not available to TikTok users because it has expired.
            - DEACTIVATED: The activity has been deactivated by the seller and is not available to TikTok users.
            - NOT_EFFECTIVE:  The activity is terminated by the platform and is not available to TikTok users.
    """

    activity_id: str | Unset = UNSET
    create_time: int | Unset = UNSET
    update_time: int | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activity_id = self.activity_id

        create_time = self.create_time

        update_time = self.update_time

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if activity_id is not UNSET:
            field_dict["activity_id"] = activity_id
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if update_time is not UNSET:
            field_dict["update_time"] = update_time
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        activity_id = d.pop("activity_id", UNSET)

        create_time = d.pop("create_time", UNSET)

        update_time = d.pop("update_time", UNSET)

        status = d.pop("status", UNSET)

        create_promotion_activity_response_data = cls(
            activity_id=activity_id,
            create_time=create_time,
            update_time=update_time,
            status=status,
        )

        create_promotion_activity_response_data.additional_properties = d
        return create_promotion_activity_response_data

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
