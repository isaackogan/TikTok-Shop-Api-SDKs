from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_size_charts_response_data_size_chart_size_chart_data_size_chart_data_table_header import (
        SearchSizeChartsResponseDataSizeChartSizeChartDataSizeChartDataTableHeader,
    )
    from ..models.search_size_charts_response_data_size_chart_size_chart_data_size_chart_data_table_row import (
        SearchSizeChartsResponseDataSizeChartSizeChartDataSizeChartDataTableRow,
    )


T = TypeVar("T", bound="SearchSizeChartsResponseDataSizeChartSizeChartDataSizeChartDataTable")


@_attrs_define
class SearchSizeChartsResponseDataSizeChartSizeChartDataSizeChartDataTable:
    """
    Attributes:
        headers (list[SearchSizeChartsResponseDataSizeChartSizeChartDataSizeChartDataTableHeader] | Unset): Ordered
            header definitions.
        rows (list[SearchSizeChartsResponseDataSizeChartSizeChartDataSizeChartDataTableRow] | Unset): Rows of the size
            chart.
    """

    headers: list[SearchSizeChartsResponseDataSizeChartSizeChartDataSizeChartDataTableHeader] | Unset = UNSET
    rows: list[SearchSizeChartsResponseDataSizeChartSizeChartDataSizeChartDataTableRow] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        headers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = []
            for headers_item_data in self.headers:
                headers_item = headers_item_data.to_dict()
                headers.append(headers_item)

        rows: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rows, Unset):
            rows = []
            for rows_item_data in self.rows:
                rows_item = rows_item_data.to_dict()
                rows.append(rows_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if headers is not UNSET:
            field_dict["headers"] = headers
        if rows is not UNSET:
            field_dict["rows"] = rows

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_size_charts_response_data_size_chart_size_chart_data_size_chart_data_table_header import (
            SearchSizeChartsResponseDataSizeChartSizeChartDataSizeChartDataTableHeader,  # noqa: PLC0415
        )
        from ..models.search_size_charts_response_data_size_chart_size_chart_data_size_chart_data_table_row import (
            SearchSizeChartsResponseDataSizeChartSizeChartDataSizeChartDataTableRow,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _headers = d.pop("headers", UNSET)
        headers: list[SearchSizeChartsResponseDataSizeChartSizeChartDataSizeChartDataTableHeader] | Unset = UNSET
        if _headers is not UNSET:
            headers = []
            for headers_item_data in _headers:
                headers_item = SearchSizeChartsResponseDataSizeChartSizeChartDataSizeChartDataTableHeader.from_dict(
                    headers_item_data
                )

                headers.append(headers_item)

        _rows = d.pop("rows", UNSET)
        rows: list[SearchSizeChartsResponseDataSizeChartSizeChartDataSizeChartDataTableRow] | Unset = UNSET
        if _rows is not UNSET:
            rows = []
            for rows_item_data in _rows:
                rows_item = SearchSizeChartsResponseDataSizeChartSizeChartDataSizeChartDataTableRow.from_dict(
                    rows_item_data
                )

                rows.append(rows_item)

        search_size_charts_response_data_size_chart_size_chart_data_size_chart_data_table = cls(
            headers=headers,
            rows=rows,
        )

        search_size_charts_response_data_size_chart_size_chart_data_size_chart_data_table.additional_properties = d
        return search_size_charts_response_data_size_chart_size_chart_data_size_chart_data_table

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
