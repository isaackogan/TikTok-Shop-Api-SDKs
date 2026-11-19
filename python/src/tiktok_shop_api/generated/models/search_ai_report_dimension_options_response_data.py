from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.search_ai_report_dimension_options_response_data_option import SearchAIReportDimensionOptionsResponseDataOption





T = TypeVar("T", bound="SearchAIReportDimensionOptionsResponseData")



@_attrs_define
class SearchAIReportDimensionOptionsResponseData:
    """ 
        Attributes:
            next_page_token (str): For entity candidates, pass a nonempty token as page_token to retrieve the next page. An
                empty string means there are no more results. Fixed attribute options always return an empty token because the
                complete list is returned together.
            dimension_code (str | Unset): Dimension code these options belong to. Use it as filters[].code when building a
                query.
            options (list[SearchAIReportDimensionOptionsResponseDataOption] | Unset): Filter values for the requested
                dimension. Fixed attribute options contain the complete configured list regardless of page_size; entity options
                contain the current page. Use a non-Creator option value in filters[].values, or a Creator option creator in
                filters[].creators. An unknown Creator without an identity cannot be selected as a Creator filter.
            total_count (int | Unset): Total number of matching results across all pages. Returned when the total is
                available.
     """

    next_page_token: str
    dimension_code: str | Unset = UNSET
    options: list[SearchAIReportDimensionOptionsResponseDataOption] | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.search_ai_report_dimension_options_response_data_option import SearchAIReportDimensionOptionsResponseDataOption # noqa: PLC0415
        next_page_token = self.next_page_token

        dimension_code = self.dimension_code

        options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)



        total_count = self.total_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "next_page_token": next_page_token,
        })
        if dimension_code is not UNSET:
            field_dict["dimension_code"] = dimension_code
        if options is not UNSET:
            field_dict["options"] = options
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_ai_report_dimension_options_response_data_option import SearchAIReportDimensionOptionsResponseDataOption # noqa: PLC0415
        d = dict(src_dict)
        next_page_token = d.pop("next_page_token")

        dimension_code = d.pop("dimension_code", UNSET)

        _options = d.pop("options", UNSET)
        options: list[SearchAIReportDimensionOptionsResponseDataOption] | Unset = UNSET
        if _options is not UNSET:
            options = []
            for options_item_data in _options:
                options_item = SearchAIReportDimensionOptionsResponseDataOption.from_dict(options_item_data)



                options.append(options_item)


        total_count = d.pop("total_count", UNSET)

        search_ai_report_dimension_options_response_data = cls(
            next_page_token=next_page_token,
            dimension_code=dimension_code,
            options=options,
            total_count=total_count,
        )


        search_ai_report_dimension_options_response_data.additional_properties = d
        return search_ai_report_dimension_options_response_data

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
