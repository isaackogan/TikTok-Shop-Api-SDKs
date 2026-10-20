from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchCouponListRequest")


@_attrs_define
class SearchCouponListRequest:
    """
    Attributes:
        status (list[str] | Unset): Coupon's promotion status.
            Values:
            - `NOT_START`: Not available to TikTok users until the coupon's configured start time.
            - `ONGOING`: Available to TikTok users.
            - `EXPIRED`: Not available to TikTok users because it has expired.
            - `DEACTIVATED`: Deactivated by the seller and is not available to TikTok users.
        title_keyword (str | Unset): Keywords in coupon titles to search for. The UTF-8 byte length must be from 1 to
            100. Fuzzy matching is not supported.
        display_type (list[str] | Unset): The display type of coupons.
            Values:
            - `REGULAR`: Regular coupons which are displayed to TikTok users across all display locations available in TTS,
            including PLPs, PDPs, TikTok Videos, LIVE Rooms, Creator Showcases, and may be shared via TTS Customer Support
            instant messages. Includes coupons which target select customer segments.
            - `LIVE`: Coupons which are only displayed to TikTok users in LIVE Rooms.
            - `CREATOR_EXCLUSIVE`: Coupons that can be claimed through the display channels of the specified creator, such
            as their LIVE Rooms, and their Creator Showcase.
            - `CHAT`: Exclusive coupons that may be sent to customers via TTS customer support chat messages, but are not
            displayed in other display locations.
            - `PROMO_CODE`: Promo codes do not have dedicated display locations on TikTok, but may be shared with customers
            in LIVEs, in TikTok videos, or other social media platforms. They can be claimed by customers entering a claim
            code at checkout or by customers that use a custom promo code landing page URL.
    """

    status: list[str] | Unset = UNSET
    title_keyword: str | Unset = UNSET
    display_type: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: list[str] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        title_keyword = self.title_keyword

        display_type: list[str] | Unset = UNSET
        if not isinstance(self.display_type, Unset):
            display_type = self.display_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if title_keyword is not UNSET:
            field_dict["title_keyword"] = title_keyword
        if display_type is not UNSET:
            field_dict["display_type"] = display_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = cast(list[str], d.pop("status", UNSET))

        title_keyword = d.pop("title_keyword", UNSET)

        display_type = cast(list[str], d.pop("display_type", UNSET))

        search_coupon_list_request = cls(
            status=status,
            title_keyword=title_keyword,
            display_type=display_type,
        )

        search_coupon_list_request.additional_properties = d
        return search_coupon_list_request

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
