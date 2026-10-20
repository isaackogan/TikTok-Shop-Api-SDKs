from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCategoryRulesResponseDataSizeChartMeasurementAndOptionOption")


@_attrs_define
class GetCategoryRulesResponseDataSizeChartMeasurementAndOptionOption:
    """
    Attributes:
        name (str | Unset): Localized measurement name resolved using the request locale.
        id (str | Unset): Platform-defined standard measurement ID, for example size_chart_option_bust. Use this ID as
            table.headers[].id for the corresponding standard measurement.
        role (str | Unset): Possible values: KEY: a key category measurement; RECOMMEND: a useful recommended
            measurement.
        unit (str | Unset): Possible values: NONE: no unit conversion; LENGTH: length values such as cm or in; WEIGHT:
            weight values such as kg or lb; HEIGHT: person-height values such as cm or ft/in.
        metric_value_range (list[str] | Unset): Allowed metric range in [minimum, maximum] order.
        imperial_value_range (list[str] | Unset): Allowed imperial range in [minimum, maximum] order.
    """

    name: str | Unset = UNSET
    id: str | Unset = UNSET
    role: str | Unset = UNSET
    unit: str | Unset = UNSET
    metric_value_range: list[str] | Unset = UNSET
    imperial_value_range: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        id = self.id

        role = self.role

        unit = self.unit

        metric_value_range: list[str] | Unset = UNSET
        if not isinstance(self.metric_value_range, Unset):
            metric_value_range = self.metric_value_range

        imperial_value_range: list[str] | Unset = UNSET
        if not isinstance(self.imperial_value_range, Unset):
            imperial_value_range = self.imperial_value_range

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if id is not UNSET:
            field_dict["id"] = id
        if role is not UNSET:
            field_dict["role"] = role
        if unit is not UNSET:
            field_dict["unit"] = unit
        if metric_value_range is not UNSET:
            field_dict["metric_value_range"] = metric_value_range
        if imperial_value_range is not UNSET:
            field_dict["imperial_value_range"] = imperial_value_range

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        id = d.pop("id", UNSET)

        role = d.pop("role", UNSET)

        unit = d.pop("unit", UNSET)

        metric_value_range = cast(list[str], d.pop("metric_value_range", UNSET))

        imperial_value_range = cast(list[str], d.pop("imperial_value_range", UNSET))

        get_category_rules_response_data_size_chart_measurement_and_option_option = cls(
            name=name,
            id=id,
            role=role,
            unit=unit,
            metric_value_range=metric_value_range,
            imperial_value_range=imperial_value_range,
        )

        get_category_rules_response_data_size_chart_measurement_and_option_option.additional_properties = d
        return get_category_rules_response_data_size_chart_measurement_and_option_option

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
