from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_shop_products_response_data_product import GetShopProductsResponseDataProduct


T = TypeVar("T", bound="GetShopProductsResponseData")


@_attrs_define
class GetShopProductsResponseData:
    """
    Attributes:
        products (list[GetShopProductsResponseDataProduct] | Unset): The searched product list. It will be empty when
            there are no search results.
        total_count (int | Unset): The total number of products that meet the query conditions.
        next_page_token (str | Unset): An opaque token used to retrieve the next page. Pass it as `page_token` in the
            next request. It is empty when there are no more products to retrieve.
    """

    products: list[GetShopProductsResponseDataProduct] | Unset = UNSET
    total_count: int | Unset = UNSET
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        products: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.products, Unset):
            products = []
            for products_item_data in self.products:
                products_item = products_item_data.to_dict()
                products.append(products_item)

        total_count = self.total_count

        next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if products is not UNSET:
            field_dict["products"] = products
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shop_products_response_data_product import GetShopProductsResponseDataProduct  # noqa: PLC0415

        d = dict(src_dict)
        _products = d.pop("products", UNSET)
        products: list[GetShopProductsResponseDataProduct] | Unset = UNSET
        if _products is not UNSET:
            products = []
            for products_item_data in _products:
                products_item = GetShopProductsResponseDataProduct.from_dict(products_item_data)

                products.append(products_item)

        total_count = d.pop("total_count", UNSET)

        next_page_token = d.pop("next_page_token", UNSET)

        get_shop_products_response_data = cls(
            products=products,
            total_count=total_count,
            next_page_token=next_page_token,
        )

        get_shop_products_response_data.additional_properties = d
        return get_shop_products_response_data

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
