from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckProductListingResponseDataListingQuality")


@_attrs_define
class CheckProductListingResponseDataListingQuality:
    """
    Attributes:
        current_tier (str | Unset): The current quality tier of this product listing. The quality tier of a product
            listing depends on the quality of the content in its product fields such as the title, image, attributes etc.

            Possible values:
            - POOR
            - FAIR
            - GOOD
            - EXCELLENT

            **Note**: Available only for the US market.
        remaining_recommendations (int | Unset): The remaining number of recommendations (see `diagnosis_results`) that
            must be implemented for the product to reach the highest tier.

            **Note**:
            - To reach the highest tier, you must implement all recommendations listed in `diagnosis_results`.
            - Available only for the US market.
    """

    current_tier: str | Unset = UNSET
    remaining_recommendations: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_tier = self.current_tier

        remaining_recommendations = self.remaining_recommendations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_tier is not UNSET:
            field_dict["current_tier"] = current_tier
        if remaining_recommendations is not UNSET:
            field_dict["remaining_recommendations"] = remaining_recommendations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        current_tier = d.pop("current_tier", UNSET)

        remaining_recommendations = d.pop("remaining_recommendations", UNSET)

        check_product_listing_response_data_listing_quality = cls(
            current_tier=current_tier,
            remaining_recommendations=remaining_recommendations,
        )

        check_product_listing_response_data_listing_quality.additional_properties = d
        return check_product_listing_response_data_listing_quality

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
