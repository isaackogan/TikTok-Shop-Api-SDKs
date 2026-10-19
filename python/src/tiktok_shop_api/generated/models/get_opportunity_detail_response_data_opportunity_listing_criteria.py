from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetOpportunityDetailResponseDataOpportunityListingCriteria")


@_attrs_define
class GetOpportunityDetailResponseDataOpportunityListingCriteria:
    """
    Attributes:
        product_brand (str | Unset): Requirement for product brand.
        product_category (str | Unset): Requirement for product category.
        product_status (str | Unset): Requirement for product status : LIVE / DRAFT
        keywords (str | Unset): A comma-separated list of keywords that must be included in the product's title,
            attributes, description, or other applicable content.
    """

    product_brand: str | Unset = UNSET
    product_category: str | Unset = UNSET
    product_status: str | Unset = UNSET
    keywords: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_brand = self.product_brand

        product_category = self.product_category

        product_status = self.product_status

        keywords = self.keywords

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_brand is not UNSET:
            field_dict["product_brand"] = product_brand
        if product_category is not UNSET:
            field_dict["product_category"] = product_category
        if product_status is not UNSET:
            field_dict["product_status"] = product_status
        if keywords is not UNSET:
            field_dict["keywords"] = keywords

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_brand = d.pop("product_brand", UNSET)

        product_category = d.pop("product_category", UNSET)

        product_status = d.pop("product_status", UNSET)

        keywords = d.pop("keywords", UNSET)

        get_opportunity_detail_response_data_opportunity_listing_criteria = cls(
            product_brand=product_brand,
            product_category=product_category,
            product_status=product_status,
            keywords=keywords,
        )

        get_opportunity_detail_response_data_opportunity_listing_criteria.additional_properties = d
        return get_opportunity_detail_response_data_opportunity_listing_criteria

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
