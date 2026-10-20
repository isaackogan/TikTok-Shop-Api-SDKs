from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_products_for_compliance_auditing_response_data_product import (
        SearchProductsForComplianceAuditingResponseDataProduct,
    )


T = TypeVar("T", bound="SearchProductsForComplianceAuditingResponseData")


@_attrs_define
class SearchProductsForComplianceAuditingResponseData:
    """
    Attributes:
        next_page_token (str | Unset): The opaque token returned for a subsequent page. When this value is non-empty,
            pass it in the next request's `page_token`.
        total_count (int | Unset): The total number of products selected by the active mode. For direct product-ID
            lookup, this is the number of product IDs used for the lookup. For shop search, this is the total number of
            products matching the seller, product-title, category, and brand filters.
        products (list[SearchProductsForComplianceAuditingResponseDataProduct] | Unset): Product information
    """

    next_page_token: str | Unset = UNSET
    total_count: int | Unset = UNSET
    products: list[SearchProductsForComplianceAuditingResponseDataProduct] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        next_page_token = self.next_page_token

        total_count = self.total_count

        products: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.products, Unset):
            products = []
            for products_item_data in self.products:
                products_item = products_item_data.to_dict()
                products.append(products_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if products is not UNSET:
            field_dict["products"] = products

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_products_for_compliance_auditing_response_data_product import (
            SearchProductsForComplianceAuditingResponseDataProduct,  # noqa: PLC0415
        )

        d = dict(src_dict)
        next_page_token = d.pop("next_page_token", UNSET)

        total_count = d.pop("total_count", UNSET)

        _products = d.pop("products", UNSET)
        products: list[SearchProductsForComplianceAuditingResponseDataProduct] | Unset = UNSET
        if _products is not UNSET:
            products = []
            for products_item_data in _products:
                products_item = SearchProductsForComplianceAuditingResponseDataProduct.from_dict(products_item_data)

                products.append(products_item)

        search_products_for_compliance_auditing_response_data = cls(
            next_page_token=next_page_token,
            total_count=total_count,
            products=products,
        )

        search_products_for_compliance_auditing_response_data.additional_properties = d
        return search_products_for_compliance_auditing_response_data

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
