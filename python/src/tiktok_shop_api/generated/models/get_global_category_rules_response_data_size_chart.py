from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetGlobalCategoryRulesResponseDataSizeChart")


@_attrs_define
class GetGlobalCategoryRulesResponseDataSizeChart:
    """
    Attributes:
        is_supported (bool | Unset): A flag to indicate whether size charts are supported.

            **Note**: If size charts are not supported, even if you provide a size chart when creating or editing a product,
            the size chart will not be saved.
        is_required (bool | Unset): A flag to indicate whether a size chart is required.
    """

    is_supported: bool | Unset = UNSET
    is_required: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_supported = self.is_supported

        is_required = self.is_required

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_supported is not UNSET:
            field_dict["is_supported"] = is_supported
        if is_required is not UNSET:
            field_dict["is_required"] = is_required

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_supported = d.pop("is_supported", UNSET)

        is_required = d.pop("is_required", UNSET)

        get_global_category_rules_response_data_size_chart = cls(
            is_supported=is_supported,
            is_required=is_required,
        )

        get_global_category_rules_response_data_size_chart.additional_properties = d
        return get_global_category_rules_response_data_size_chart

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
