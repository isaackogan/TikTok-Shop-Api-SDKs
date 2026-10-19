from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_coupon_list_response_data_coupon import SearchCouponListResponseDataCoupon


T = TypeVar("T", bound="SearchCouponListResponseData")


@_attrs_define
class SearchCouponListResponseData:
    """
    Attributes:
        total_count (int | Unset): Total number of coupon records matching the supplied filters. This value can be
            greater than the number of entries in coupons.
        next_page_token (str | Unset): Cursor for the next page. If this field is present and non-empty, pass its value
            as `page_token` in the next request. Stop pagination when this field is absent or empty.
        coupons (list[SearchCouponListResponseDataCoupon] | Unset): The list of coupons matching the search criteria.
    """

    total_count: int | Unset = UNSET
    next_page_token: str | Unset = UNSET
    coupons: list[SearchCouponListResponseDataCoupon] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_count = self.total_count

        next_page_token = self.next_page_token

        coupons: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.coupons, Unset):
            coupons = []
            for coupons_item_data in self.coupons:
                coupons_item = coupons_item_data.to_dict()
                coupons.append(coupons_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token
        if coupons is not UNSET:
            field_dict["coupons"] = coupons

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_coupon_list_response_data_coupon import SearchCouponListResponseDataCoupon  # noqa: PLC0415

        d = dict(src_dict)
        total_count = d.pop("total_count", UNSET)

        next_page_token = d.pop("next_page_token", UNSET)

        _coupons = d.pop("coupons", UNSET)
        coupons: list[SearchCouponListResponseDataCoupon] | Unset = UNSET
        if _coupons is not UNSET:
            coupons = []
            for coupons_item_data in _coupons:
                coupons_item = SearchCouponListResponseDataCoupon.from_dict(coupons_item_data)

                coupons.append(coupons_item)

        search_coupon_list_response_data = cls(
            total_count=total_count,
            next_page_token=next_page_token,
            coupons=coupons,
        )

        search_coupon_list_response_data.additional_properties = d
        return search_coupon_list_response_data

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
