from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_family_product import ProductFamilyProduct


T = TypeVar("T", bound="ProductFamily")


@_attrs_define
class ProductFamily:
    """
    Attributes:
        id (str | Unset): The product family ID.
        products (list[ProductFamilyProduct] | Unset): A list of products that belong to the family.
    """

    id: str | Unset = UNSET
    products: list[ProductFamilyProduct] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        products: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.products, Unset):
            products = []
            for products_item_data in self.products:
                products_item = products_item_data.to_dict()
                products.append(products_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if products is not UNSET:
            field_dict["products"] = products

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.product_family_product import ProductFamilyProduct  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _products = d.pop("products", UNSET)
        products: list[ProductFamilyProduct] | Unset = UNSET
        if _products is not UNSET:
            products = []
            for products_item_data in _products:
                products_item = ProductFamilyProduct.from_dict(products_item_data)

                products.append(products_item)

        product_family = cls(
            id=id,
            products=products,
        )

        product_family.additional_properties = d
        return product_family

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
