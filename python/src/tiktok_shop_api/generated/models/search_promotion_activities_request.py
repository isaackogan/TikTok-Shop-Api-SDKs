from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_promotion_activities_request_activity_type import SearchPromotionActivitiesRequestActivityType
from ..models.search_promotion_activities_request_status import SearchPromotionActivitiesRequestStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchPromotionActivitiesRequest")


@_attrs_define
class SearchPromotionActivitiesRequest:
    """
    Attributes:
        status (SearchPromotionActivitiesRequestStatus | Unset): Filter activities by status. If omitted, activities
            with `NOT_START`, `ONGOING`, `EXPIRED`, or `DEACTIVATED` status are returned. Possible values:
            - `NOT_START`: The activity is not available to TikTok users until its start time.
            - `ONGOING`: The activity is available to TikTok users.
            - `EXPIRED`: The activity is no longer available because it has expired.
            - `DEACTIVATED`: The activity was deactivated by the seller and is not available to TikTok users.
        activity_title (str | Unset): Activity title key words. No fuzzy matching.
        page_size (int | Unset): Number of activities to return per page. Range: 0 to 100. If omitted or set to 0, the
            effective page size is 10.
        page_token (str | Unset): Specify the value for the page. Use `""` for the first page.
        activity_type (SearchPromotionActivitiesRequestActivityType | Unset): The type of promotion activity to return.
            If `activity_type` is omitted, activities of all supported types are returned. Possible values:
            - `FIXED_PRICE`: Product discount activity with a fixed price.
            - `DIRECT_DISCOUNT`: Product discount activity with a percentage off.
            - `FLASHSALE`: Flash sale activity.
            - `SHIPPING_DISCOUNT`: Shipping fee discount activity.
            - `BUY_MORE_SAVE_MORE`: Buy More Save More activity.
            - `GIFT_WITH_PURCHASE`: Gift With Purchase activity.
            - `BUY_X_GET_Y`: Buy X Get Y activity.
    """

    status: SearchPromotionActivitiesRequestStatus | Unset = UNSET
    activity_title: str | Unset = UNSET
    page_size: int | Unset = UNSET
    page_token: str | Unset = UNSET
    activity_type: SearchPromotionActivitiesRequestActivityType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        activity_title = self.activity_title

        page_size = self.page_size

        page_token = self.page_token

        activity_type: str | Unset = UNSET
        if not isinstance(self.activity_type, Unset):
            activity_type = self.activity_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if activity_title is not UNSET:
            field_dict["activity_title"] = activity_title
        if page_size is not UNSET:
            field_dict["page_size"] = page_size
        if page_token is not UNSET:
            field_dict["page_token"] = page_token
        if activity_type is not UNSET:
            field_dict["activity_type"] = activity_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: SearchPromotionActivitiesRequestStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SearchPromotionActivitiesRequestStatus(_status)

        activity_title = d.pop("activity_title", UNSET)

        page_size = d.pop("page_size", UNSET)

        page_token = d.pop("page_token", UNSET)

        _activity_type = d.pop("activity_type", UNSET)
        activity_type: SearchPromotionActivitiesRequestActivityType | Unset
        if isinstance(_activity_type, Unset):
            activity_type = UNSET
        else:
            activity_type = SearchPromotionActivitiesRequestActivityType(_activity_type)

        search_promotion_activities_request = cls(
            status=status,
            activity_title=activity_title,
            page_size=page_size,
            page_token=page_token,
            activity_type=activity_type,
        )

        search_promotion_activities_request.additional_properties = d
        return search_promotion_activities_request

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
