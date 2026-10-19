from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RemoveShowcaseProductsRequest")


@_attrs_define
class RemoveShowcaseProductsRequest:
    """
    Attributes:
        product_ids (list[str]): The product IDs to remove from the creator's showcase. Specify at least one product ID.
            The maximum number of products to delete at once is 200.
    """

    product_ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_ids = self.product_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "product_ids": product_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_ids = cast(list[str], d.pop("product_ids"))

        remove_showcase_products_request = cls(
            product_ids=product_ids,
        )

        remove_showcase_products_request.additional_properties = d
        return remove_showcase_products_request

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
