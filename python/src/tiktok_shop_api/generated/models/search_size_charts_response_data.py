from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.search_size_charts_response_data_size_chart import SearchSizeChartsResponseDataSizeChart





T = TypeVar("T", bound="SearchSizeChartsResponseData")



@_attrs_define
class SearchSizeChartsResponseData:
    """ 
        Attributes:
            size_chart (list[SearchSizeChartsResponseDataSizeChart] | Unset): The list of size charts that meet the query
                conditions.
            next_page_token (str | Unset): An opaque token used to retrieve the next page of a paginated result set. If this
                value is non-empty, pass it in the `page_token` parameter of the next request. An empty value means there are no
                more results.
            total_count (int | Unset): The number of size charts that meet the query conditions.
     """

    size_chart: list[SearchSizeChartsResponseDataSizeChart] | Unset = UNSET
    next_page_token: str | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.search_size_charts_response_data_size_chart import SearchSizeChartsResponseDataSizeChart # noqa: PLC0415
        size_chart: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.size_chart, Unset):
            size_chart = []
            for size_chart_item_data in self.size_chart:
                size_chart_item = size_chart_item_data.to_dict()
                size_chart.append(size_chart_item)



        next_page_token = self.next_page_token

        total_count = self.total_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if size_chart is not UNSET:
            field_dict["size_chart"] = size_chart
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_size_charts_response_data_size_chart import SearchSizeChartsResponseDataSizeChart # noqa: PLC0415
        d = dict(src_dict)
        _size_chart = d.pop("size_chart", UNSET)
        size_chart: list[SearchSizeChartsResponseDataSizeChart] | Unset = UNSET
        if _size_chart is not UNSET:
            size_chart = []
            for size_chart_item_data in _size_chart:
                size_chart_item = SearchSizeChartsResponseDataSizeChart.from_dict(size_chart_item_data)



                size_chart.append(size_chart_item)


        next_page_token = d.pop("next_page_token", UNSET)

        total_count = d.pop("total_count", UNSET)

        search_size_charts_response_data = cls(
            size_chart=size_chart,
            next_page_token=next_page_token,
            total_count=total_count,
        )


        search_size_charts_response_data.additional_properties = d
        return search_size_charts_response_data

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
