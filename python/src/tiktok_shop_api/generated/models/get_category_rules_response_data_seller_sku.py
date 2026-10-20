from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCategoryRulesResponseDataSellerSku")


@_attrs_define
class GetCategoryRulesResponseDataSellerSku:
    """
    Attributes:
        is_required (bool | Unset): A flag to indicate whether a Seller SKU is required when creating or editing a
            product in this category. When required, the Seller SKU must be 6 to 50 characters long and can contain only
            letters, digits, hyphens (-) and underscores (_).
    """

    is_required: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_required = self.is_required

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_required is not UNSET:
            field_dict["is_required"] = is_required

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_required = d.pop("is_required", UNSET)

        get_category_rules_response_data_seller_sku = cls(
            is_required=is_required,
        )

        get_category_rules_response_data_seller_sku.additional_properties = d
        return get_category_rules_response_data_seller_sku

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
