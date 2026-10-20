from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdatePromotionActivityResponseData")


@_attrs_define
class UpdatePromotionActivityResponseData:
    """
    Attributes:
        activity_id (str | Unset): A unique ID that identifies different activities.
        title (str | Unset): Activity name set by the seller. Returned on successful fixed-price, direct-discount,
            flash-sale, BMSM, GWP, and BXGY updates. Not returned on successful shipping-discount updates.
        update_time (int | Unset): Last update time as a Unix timestamp in seconds.
    """

    activity_id: str | Unset = UNSET
    title: str | Unset = UNSET
    update_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activity_id = self.activity_id

        title = self.title

        update_time = self.update_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if activity_id is not UNSET:
            field_dict["activity_id"] = activity_id
        if title is not UNSET:
            field_dict["title"] = title
        if update_time is not UNSET:
            field_dict["update_time"] = update_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        activity_id = d.pop("activity_id", UNSET)

        title = d.pop("title", UNSET)

        update_time = d.pop("update_time", UNSET)

        update_promotion_activity_response_data = cls(
            activity_id=activity_id,
            title=title,
            update_time=update_time,
        )

        update_promotion_activity_response_data.additional_properties = d
        return update_promotion_activity_response_data

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
