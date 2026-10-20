from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProductLinkInfo")


@_attrs_define
class ProductLinkInfo:
    """
    Attributes:
        product_id (str): Use product_id to bind the product with the video.
            The product_id from [Get Shop Products](https://api/affiliate_creator/202509/shop_products) or [Get Showcase
            Products](https://api/affiliate_creator/202405/showcases/products)
        title (str): The title to be shown on the product anchor. Anchor title should be shorter than 30 characters.
            Titles may be rejected for punctuation, emoji, or offensive language.
    """

    product_id: str
    title: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "product_id": product_id,
                "title": title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_id = d.pop("product_id")

        title = d.pop("title")

        product_link_info = cls(
            product_id=product_id,
            title=title,
        )

        product_link_info.additional_properties = d
        return product_link_info

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
