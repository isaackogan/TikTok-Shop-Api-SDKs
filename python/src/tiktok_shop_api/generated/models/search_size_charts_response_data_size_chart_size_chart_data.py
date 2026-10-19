from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_size_charts_response_data_size_chart_size_chart_data_size_chart_data import (
        SearchSizeChartsResponseDataSizeChartSizeChartDataSizeChartData,
    )


T = TypeVar("T", bound="SearchSizeChartsResponseDataSizeChartSizeChartData")


@_attrs_define
class SearchSizeChartsResponseDataSizeChartSizeChartData:
    """
    Attributes:
        locale (str | Unset): The language of the size chart table.
        size_chart_data (SearchSizeChartsResponseDataSizeChartSizeChartDataSizeChartData | Unset):
    """

    locale: str | Unset = UNSET
    size_chart_data: SearchSizeChartsResponseDataSizeChartSizeChartDataSizeChartData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        locale = self.locale

        size_chart_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.size_chart_data, Unset):
            size_chart_data = self.size_chart_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if locale is not UNSET:
            field_dict["locale"] = locale
        if size_chart_data is not UNSET:
            field_dict["size_chart_data"] = size_chart_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_size_charts_response_data_size_chart_size_chart_data_size_chart_data import (
            SearchSizeChartsResponseDataSizeChartSizeChartDataSizeChartData,  # noqa: PLC0415
        )

        d = dict(src_dict)
        locale = d.pop("locale", UNSET)

        _size_chart_data = d.pop("size_chart_data", UNSET)
        size_chart_data: SearchSizeChartsResponseDataSizeChartSizeChartDataSizeChartData | Unset
        if isinstance(_size_chart_data, Unset):
            size_chart_data = UNSET
        else:
            size_chart_data = SearchSizeChartsResponseDataSizeChartSizeChartDataSizeChartData.from_dict(
                _size_chart_data
            )

        search_size_charts_response_data_size_chart_size_chart_data = cls(
            locale=locale,
            size_chart_data=size_chart_data,
        )

        search_size_charts_response_data_size_chart_size_chart_data.additional_properties = d
        return search_size_charts_response_data_size_chart_size_chart_data

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
