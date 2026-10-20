from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdatePromotionActivityProductsResponseData")


@_attrs_define
class UpdatePromotionActivityProductsResponseData:
    """
    Attributes:
        activity_id (str | Unset): A unique ID that identifies different activities.
        title (str | Unset): Activity name set by the merchant.
        update_time (int | Unset): The time when the response was generated, as a Unix timestamp in seconds (UTC).
        status (str | Unset): Activity status.
            Possible values:
            - DRAFT: Promotion activities with this status are not available to TikTok users.
            - NOT_START: Promotion activities with this status are not available to TikTok users until the set activity
            start time.
            - ONGOING: Promotion activities with this status are available to TikTok users.
            - EXPIRED: Promotion activities with this status are not available to TikTok users because it has expired.
            - DEACTIVATED: The activity has been deactivated by the seller and is not available to TikTok users.
            - NOT_EFFECTIVE:  The activity is terminated by the platform and is not available to TikTok users.
        total_count (int | Unset): The number of items in this request.
            When `product_level==PRODUCT`, this is the number of products. When `product_level==VARIATION`, this is the
            total number of SKUs across all products. When `product_level==SHOP`, this value is `0`. IDs in
            `benefit_product_ids` and `exclude_product_ids` are not included.
    """

    activity_id: str | Unset = UNSET
    title: str | Unset = UNSET
    update_time: int | Unset = UNSET
    status: str | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activity_id = self.activity_id

        title = self.title

        update_time = self.update_time

        status = self.status

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if activity_id is not UNSET:
            field_dict["activity_id"] = activity_id
        if title is not UNSET:
            field_dict["title"] = title
        if update_time is not UNSET:
            field_dict["update_time"] = update_time
        if status is not UNSET:
            field_dict["status"] = status
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        activity_id = d.pop("activity_id", UNSET)

        title = d.pop("title", UNSET)

        update_time = d.pop("update_time", UNSET)

        status = d.pop("status", UNSET)

        total_count = d.pop("total_count", UNSET)

        update_promotion_activity_products_response_data = cls(
            activity_id=activity_id,
            title=title,
            update_time=update_time,
            status=status,
            total_count=total_count,
        )

        update_promotion_activity_products_response_data.additional_properties = d
        return update_promotion_activity_products_response_data

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
