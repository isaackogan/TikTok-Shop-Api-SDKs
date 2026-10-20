from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_products_seo_words_response_data_product import GetProductsSEOWordsResponseDataProduct


T = TypeVar("T", bound="GetProductsSEOWordsResponseData")


@_attrs_define
class GetProductsSEOWordsResponseData:
    """
    Attributes:
        products (list[GetProductsSEOWordsResponseDataProduct] | Unset): The requested products for which SEO keyword
            suggestions were returned. Products without returned suggestions are omitted. When no suggestions are returned,
            `products` may be omitted or returned as an empty list.
    """

    products: list[GetProductsSEOWordsResponseDataProduct] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        products: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.products, Unset):
            products = []
            for products_item_data in self.products:
                products_item = products_item_data.to_dict()
                products.append(products_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if products is not UNSET:
            field_dict["products"] = products

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_products_seo_words_response_data_product import (
            GetProductsSEOWordsResponseDataProduct,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _products = d.pop("products", UNSET)
        products: list[GetProductsSEOWordsResponseDataProduct] | Unset = UNSET
        if _products is not UNSET:
            products = []
            for products_item_data in _products:
                products_item = GetProductsSEOWordsResponseDataProduct.from_dict(products_item_data)

                products.append(products_item)

        get_products_seo_words_response_data = cls(
            products=products,
        )

        get_products_seo_words_response_data.additional_properties = d
        return get_products_seo_words_response_data

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
