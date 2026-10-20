from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_size_charts_request_size_chart_mode import SearchSizeChartsRequestSizeChartMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchSizeChartsRequest")


@_attrs_define
class SearchSizeChartsRequest:
    """
    Attributes:
        ids (list[str] | Unset): Filter size charts by size chart template IDs.
            Max: 50 IDs
        keyword (str | Unset): Filter size charts by size chart template name or by key words in the template name.
            Keyword searches do not return PRODUCT_SCOPED size charts because they do not have a template name.
            If both ids and keyword are provided, ids takes priority.
        size_chart_mode (SearchSizeChartsRequestSizeChartMode | Unset): Filter size charts by usage mode. Possible
            values: REUSABLE_TEMPLATE: A size chart template that can be reused across multiple products. PRODUCT_SCOPED: A
            size chart created for and used by a single product. If omitted, the existing search behavior is preserved.
    """

    ids: list[str] | Unset = UNSET
    keyword: str | Unset = UNSET
    size_chart_mode: SearchSizeChartsRequestSizeChartMode | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ids: list[str] | Unset = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids

        keyword = self.keyword

        size_chart_mode: str | Unset = UNSET
        if not isinstance(self.size_chart_mode, Unset):
            size_chart_mode = self.size_chart_mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ids is not UNSET:
            field_dict["ids"] = ids
        if keyword is not UNSET:
            field_dict["keyword"] = keyword
        if size_chart_mode is not UNSET:
            field_dict["size_chart_mode"] = size_chart_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ids = cast(list[str], d.pop("ids", UNSET))

        keyword = d.pop("keyword", UNSET)

        _size_chart_mode = d.pop("size_chart_mode", UNSET)
        size_chart_mode: SearchSizeChartsRequestSizeChartMode | Unset
        if isinstance(_size_chart_mode, Unset):
            size_chart_mode = UNSET
        else:
            size_chart_mode = SearchSizeChartsRequestSizeChartMode(_size_chart_mode)

        search_size_charts_request = cls(
            ids=ids,
            keyword=keyword,
            size_chart_mode=size_chart_mode,
        )

        search_size_charts_request.additional_properties = d
        return search_size_charts_request

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
