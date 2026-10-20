from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetShopProductPerformanceDetailResponseDataPerformanceRating")


@_attrs_define
class GetShopProductPerformanceDetailResponseDataPerformanceRating:
    """
    Attributes:
        stars (str | Unset): Rating star bucket.
            Possible values:
            - 1_STAR: One-star rating.
            - 2_STAR: Two-star rating.
            - 3_STAR: Three-star rating.
            - 4_STAR: Four-star rating.
            - 5_STAR: Five-star rating.
        count (int | Unset): Number of reviews in the corresponding rating.
        percentage (str | Unset): Share of all product reviews in the corresponding rating bucket. The value is the
            bucket's review count divided by the total product review count and is returned as a decimal from 0 to 1,
            rounded to four decimal places. For example, `0.23` means 23%.
    """

    stars: str | Unset = UNSET
    count: int | Unset = UNSET
    percentage: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stars = self.stars

        count = self.count

        percentage = self.percentage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stars is not UNSET:
            field_dict["stars"] = stars
        if count is not UNSET:
            field_dict["count"] = count
        if percentage is not UNSET:
            field_dict["percentage"] = percentage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        stars = d.pop("stars", UNSET)

        count = d.pop("count", UNSET)

        percentage = d.pop("percentage", UNSET)

        get_shop_product_performance_detail_response_data_performance_rating = cls(
            stars=stars,
            count=count,
            percentage=percentage,
        )

        get_shop_product_performance_detail_response_data_performance_rating.additional_properties = d
        return get_shop_product_performance_detail_response_data_performance_rating

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
