from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_size_charts_response_data_size_chart_size_chart_data_size_chart_data_table_row_cell import (
        SearchSizeChartsResponseDataSizeChartSizeChartDataSizeChartDataTableRowCell,
    )


T = TypeVar("T", bound="SearchSizeChartsResponseDataSizeChartSizeChartDataSizeChartDataTableRow")


@_attrs_define
class SearchSizeChartsResponseDataSizeChartSizeChartDataSizeChartDataTableRow:
    """
    Attributes:
        cells (list[SearchSizeChartsResponseDataSizeChartSizeChartDataSizeChartDataTableRowCell] | Unset): Cells aligned
            by index with table.headers.
    """

    cells: list[SearchSizeChartsResponseDataSizeChartSizeChartDataSizeChartDataTableRowCell] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cells: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cells, Unset):
            cells = []
            for cells_item_data in self.cells:
                cells_item = cells_item_data.to_dict()
                cells.append(cells_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cells is not UNSET:
            field_dict["cells"] = cells

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_size_charts_response_data_size_chart_size_chart_data_size_chart_data_table_row_cell import (
            SearchSizeChartsResponseDataSizeChartSizeChartDataSizeChartDataTableRowCell,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _cells = d.pop("cells", UNSET)
        cells: list[SearchSizeChartsResponseDataSizeChartSizeChartDataSizeChartDataTableRowCell] | Unset = UNSET
        if _cells is not UNSET:
            cells = []
            for cells_item_data in _cells:
                cells_item = SearchSizeChartsResponseDataSizeChartSizeChartDataSizeChartDataTableRowCell.from_dict(
                    cells_item_data
                )

                cells.append(cells_item)

        search_size_charts_response_data_size_chart_size_chart_data_size_chart_data_table_row = cls(
            cells=cells,
        )

        search_size_charts_response_data_size_chart_size_chart_data_size_chart_data_table_row.additional_properties = d
        return search_size_charts_response_data_size_chart_size_chart_data_size_chart_data_table_row

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
