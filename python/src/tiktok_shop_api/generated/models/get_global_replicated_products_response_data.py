from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_global_replicated_products_response_data_replicated_product import (
        GetGlobalReplicatedProductsResponseDataReplicatedProduct,
    )


T = TypeVar("T", bound="GetGlobalReplicatedProductsResponseData")


@_attrs_define
class GetGlobalReplicatedProductsResponseData:
    """
    Attributes:
        replicated_products (list[GetGlobalReplicatedProductsResponseDataReplicatedProduct] | Unset): The product
            replicas associated with the requested product in other markets. The requested source product is excluded.
            Returns an empty array when no other associated replica is found.
    """

    replicated_products: list[GetGlobalReplicatedProductsResponseDataReplicatedProduct] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        replicated_products: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.replicated_products, Unset):
            replicated_products = []
            for replicated_products_item_data in self.replicated_products:
                replicated_products_item = replicated_products_item_data.to_dict()
                replicated_products.append(replicated_products_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if replicated_products is not UNSET:
            field_dict["replicated_products"] = replicated_products

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_global_replicated_products_response_data_replicated_product import (
            GetGlobalReplicatedProductsResponseDataReplicatedProduct,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _replicated_products = d.pop("replicated_products", UNSET)
        replicated_products: list[GetGlobalReplicatedProductsResponseDataReplicatedProduct] | Unset = UNSET
        if _replicated_products is not UNSET:
            replicated_products = []
            for replicated_products_item_data in _replicated_products:
                replicated_products_item = GetGlobalReplicatedProductsResponseDataReplicatedProduct.from_dict(
                    replicated_products_item_data
                )

                replicated_products.append(replicated_products_item)

        get_global_replicated_products_response_data = cls(
            replicated_products=replicated_products,
        )

        get_global_replicated_products_response_data.additional_properties = d
        return get_global_replicated_products_response_data

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
