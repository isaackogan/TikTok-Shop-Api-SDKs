from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.product_tag_operation_product_tag import ProductTagOperationProductTag

T = TypeVar("T", bound="ProductTagOperation")


@_attrs_define
class ProductTagOperation:
    """
    Attributes:
        product_tag (ProductTagOperationProductTag): Possible values: AUCTION
        enable (bool): Whether to enable the specified product tag. Set to `true` to enable the `AUCTION` tag or `false`
            to disable it.
    """

    product_tag: ProductTagOperationProductTag
    enable: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_tag = self.product_tag.value

        enable = self.enable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "product_tag": product_tag,
                "enable": enable,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_tag = ProductTagOperationProductTag(d.pop("product_tag"))

        enable = d.pop("enable")

        product_tag_operation = cls(
            product_tag=product_tag,
            enable=enable,
        )

        product_tag_operation.additional_properties = d
        return product_tag_operation

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
