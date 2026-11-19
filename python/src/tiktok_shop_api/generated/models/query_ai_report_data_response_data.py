from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.query_ai_report_data_response_data_column import QueryAIReportDataResponseDataColumn
  from ..models.query_ai_report_data_response_data_row import QueryAIReportDataResponseDataRow





T = TypeVar("T", bound="QueryAIReportDataResponseData")



@_attrs_define
class QueryAIReportDataResponseData:
    """ 
        Attributes:
            next_page_token (str): Pass this token as page_token to retrieve the next page. An empty string means there are
                no more results.
            columns (list[QueryAIReportDataResponseDataColumn] | Unset): Definitions of the returned columns, including
                their codes, display names, roles and value types.
            end_date (datetime.date | Unset): Last date included in this query, in the shop timezone.
            rows (list[QueryAIReportDataResponseDataRow] | Unset): Result rows; an empty list means no matching data.
            start_date (datetime.date | Unset): First date included in this query, in the shop timezone.
            total_count (int | Unset): Total number of matching results across all pages. Returned when the total is
                available.
     """

    next_page_token: str
    columns: list[QueryAIReportDataResponseDataColumn] | Unset = UNSET
    end_date: datetime.date | Unset = UNSET
    rows: list[QueryAIReportDataResponseDataRow] | Unset = UNSET
    start_date: datetime.date | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.query_ai_report_data_response_data_column import QueryAIReportDataResponseDataColumn # noqa: PLC0415
        from ..models.query_ai_report_data_response_data_row import QueryAIReportDataResponseDataRow # noqa: PLC0415
        next_page_token = self.next_page_token

        columns: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.columns, Unset):
            columns = []
            for columns_item_data in self.columns:
                columns_item = columns_item_data.to_dict()
                columns.append(columns_item)



        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        rows: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rows, Unset):
            rows = []
            for rows_item_data in self.rows:
                rows_item = rows_item_data.to_dict()
                rows.append(rows_item)



        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        total_count = self.total_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "next_page_token": next_page_token,
        })
        if columns is not UNSET:
            field_dict["columns"] = columns
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if rows is not UNSET:
            field_dict["rows"] = rows
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.query_ai_report_data_response_data_column import QueryAIReportDataResponseDataColumn # noqa: PLC0415
        from ..models.query_ai_report_data_response_data_row import QueryAIReportDataResponseDataRow # noqa: PLC0415
        d = dict(src_dict)
        next_page_token = d.pop("next_page_token")

        _columns = d.pop("columns", UNSET)
        columns: list[QueryAIReportDataResponseDataColumn] | Unset = UNSET
        if _columns is not UNSET:
            columns = []
            for columns_item_data in _columns:
                columns_item = QueryAIReportDataResponseDataColumn.from_dict(columns_item_data)



                columns.append(columns_item)


        _end_date = d.pop("end_date", UNSET)
        end_date: datetime.date | Unset
        if isinstance(_end_date,  Unset):
            end_date = UNSET
        else:
            end_date = datetime.date.fromisoformat(_end_date)




        _rows = d.pop("rows", UNSET)
        rows: list[QueryAIReportDataResponseDataRow] | Unset = UNSET
        if _rows is not UNSET:
            rows = []
            for rows_item_data in _rows:
                rows_item = QueryAIReportDataResponseDataRow.from_dict(rows_item_data)



                rows.append(rows_item)


        _start_date = d.pop("start_date", UNSET)
        start_date: datetime.date | Unset
        if isinstance(_start_date,  Unset):
            start_date = UNSET
        else:
            start_date = datetime.date.fromisoformat(_start_date)




        total_count = d.pop("total_count", UNSET)

        query_ai_report_data_response_data = cls(
            next_page_token=next_page_token,
            columns=columns,
            end_date=end_date,
            rows=rows,
            start_date=start_date,
            total_count=total_count,
        )


        query_ai_report_data_response_data.additional_properties = d
        return query_ai_report_data_response_data

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
