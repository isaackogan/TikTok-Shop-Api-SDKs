from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_global_category_rules_response_data_manufacturer_optional_regions_item import (
    GetGlobalCategoryRulesResponseDataManufacturerOptionalRegionsItem,
)
from ..models.get_global_category_rules_response_data_manufacturer_required_regions_item import (
    GetGlobalCategoryRulesResponseDataManufacturerRequiredRegionsItem,
)
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
        optional_regions (list[GetGlobalCategoryRulesResponseDataManufacturerOptionalRegionsItem] | Unset): The markets
            where the manufacturer is optional.
            Possible values:
            - DE: Germany
            - ES: Spain
            - FR: France
            - IT: Italy
            - IE: Ireland
        required_regions (list[GetGlobalCategoryRulesResponseDataManufacturerRequiredRegionsItem] | Unset): The markets
            where the manufacturer is required.
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
    optional_regions: list[GetGlobalCategoryRulesResponseDataManufacturerOptionalRegionsItem] | Unset = UNSET
    required_regions: list[GetGlobalCategoryRulesResponseDataManufacturerRequiredRegionsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_required = self.is_required

        optional_regions: list[str] | Unset = UNSET
        if not isinstance(self.optional_regions, Unset):
            optional_regions = []
            for optional_regions_item_data in self.optional_regions:
                optional_regions_item = optional_regions_item_data.value
                optional_regions.append(optional_regions_item)

        required_regions: list[str] | Unset = UNSET
        if not isinstance(self.required_regions, Unset):
            required_regions = []
            for required_regions_item_data in self.required_regions:
                required_regions_item = required_regions_item_data.value
                required_regions.append(required_regions_item)

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

        _optional_regions = d.pop("optional_regions", UNSET)
        optional_regions: list[GetGlobalCategoryRulesResponseDataManufacturerOptionalRegionsItem] | Unset = UNSET
        if _optional_regions is not UNSET:
            optional_regions = []
            for optional_regions_item_data in _optional_regions:
                optional_regions_item = GetGlobalCategoryRulesResponseDataManufacturerOptionalRegionsItem(
                    optional_regions_item_data
                )

                optional_regions.append(optional_regions_item)

        _required_regions = d.pop("required_regions", UNSET)
        required_regions: list[GetGlobalCategoryRulesResponseDataManufacturerRequiredRegionsItem] | Unset = UNSET
        if _required_regions is not UNSET:
            required_regions = []
            for required_regions_item_data in _required_regions:
                required_regions_item = GetGlobalCategoryRulesResponseDataManufacturerRequiredRegionsItem(
                    required_regions_item_data
                )

                required_regions.append(required_regions_item)

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
