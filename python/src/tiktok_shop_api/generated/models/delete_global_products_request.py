from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeleteGlobalProductsRequest")


@_attrs_define
class DeleteGlobalProductsRequest:
    """
    Attributes:
        global_product_ids (list[str]): The global product IDs to delete.
            Max number of IDs: 20
    """

    global_product_ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        global_product_ids = self.global_product_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "global_product_ids": global_product_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        global_product_ids = cast(list[str], d.pop("global_product_ids"))

        delete_global_products_request = cls(
            global_product_ids=global_product_ids,
        )

        delete_global_products_request.additional_properties = d
        return delete_global_products_request

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
