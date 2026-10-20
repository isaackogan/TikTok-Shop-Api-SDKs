from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetGlobalCategoryRulesResponseDataManufacturer")


@_attrs_define
class GetGlobalCategoryRulesResponseDataManufacturer:
    """
    Attributes:
        is_required (bool | Unset): A flag to indicate whether the manufacturer is required for **all EU markets**.
            - true: The manufacturer is required in all EU markets.
            - false: The manufacturer is required only in some EU markets. Refer to `required_regions` and
            `optional_regions` for details.
        optional_regions (list[str] | Unset): The markets where the manufacturer is optional.
            Possible values:
            - DE: Germany
            - ES: Spain
            - FR: France
            - IT: Italy
            - IE: Ireland
        required_regions (list[str] | Unset): The markets where the manufacturer is required.
            Possible values:
            - AT: Austria
            - BE: Belgium
            - CZ: Czechia
            - DE: Germany
            - ES: Spain
            - FR: France
            - GR: Greece
            - HU: Hungary
            - IE: Ireland
            - IT: Italy
            - NL: Netherlands
            - PL: Poland
            - PT: Portugal
    """

    is_required: bool | Unset = UNSET
    optional_regions: list[str] | Unset = UNSET
    required_regions: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_required = self.is_required

        optional_regions: list[str] | Unset = UNSET
        if not isinstance(self.optional_regions, Unset):
            optional_regions = self.optional_regions

        required_regions: list[str] | Unset = UNSET
        if not isinstance(self.required_regions, Unset):
            required_regions = self.required_regions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_required is not UNSET:
            field_dict["is_required"] = is_required
        if optional_regions is not UNSET:
            field_dict["optional_regions"] = optional_regions
        if required_regions is not UNSET:
            field_dict["required_regions"] = required_regions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_required = d.pop("is_required", UNSET)

        optional_regions = cast(list[str], d.pop("optional_regions", UNSET))

        required_regions = cast(list[str], d.pop("required_regions", UNSET))

        get_global_category_rules_response_data_manufacturer = cls(
            is_required=is_required,
            optional_regions=optional_regions,
            required_regions=required_regions,
        )

        get_global_category_rules_response_data_manufacturer.additional_properties = d
        return get_global_category_rules_response_data_manufacturer

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
