from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchSizeChartsResponseDataSizeChartSizeChartDataSizeChartDataTableHeader")


@_attrs_define
class SearchSizeChartsResponseDataSizeChartSizeChartDataSizeChartDataTableHeader:
    """
    Attributes:
        name (str | Unset): Header display name.
        id (str | Unset): Standard size-system ID or measurement key.
    """

    name: str | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        id = d.pop("id", UNSET)

        search_size_charts_response_data_size_chart_size_chart_data_size_chart_data_table_header = cls(
            name=name,
            id=id,
        )

        search_size_charts_response_data_size_chart_size_chart_data_size_chart_data_table_header.additional_properties = d
        return search_size_charts_response_data_size_chart_size_chart_data_size_chart_data_table_header

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
