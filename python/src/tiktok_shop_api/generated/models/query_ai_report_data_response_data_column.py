from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="QueryAIReportDataResponseDataColumn")



@_attrs_define
class QueryAIReportDataResponseDataColumn:
    """ 
        Attributes:
            code (str | Unset): Catalog code used by row cells.
            kind (str | Unset): Role of this column. DIMENSION: row values are in dimensions. METRIC: row values are in
                metrics. DETAIL: row values are in detail_fields.
            name (str | Unset): Name to display for this column.
            value_type (datetime.datetime | Unset): Format of the returned value. Current types: CURRENCY — Monetary value;
                read currency in the query result for its currency code; DATETIME — UTC date-time string in RFC 3339 format;
                DECIMAL — Decimal value represented as a string; DURATION — Duration; the metric or detail field description
                specifies its unit; ENUM — Coded value; read the field definition or candidate values for its meaning; INT —
                Integer value represented as a string; RATIO — Raw ratio: 0.1234 represents 12.34%; STRING — Text value. New
                types may be added.
     """

    code: str | Unset = UNSET
    kind: str | Unset = UNSET
    name: str | Unset = UNSET
    value_type: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        code = self.code

        kind = self.kind

        name = self.name

        value_type: str | Unset = UNSET
        if not isinstance(self.value_type, Unset):
            value_type = self.value_type.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if code is not UNSET:
            field_dict["code"] = code
        if kind is not UNSET:
            field_dict["kind"] = kind
        if name is not UNSET:
            field_dict["name"] = name
        if value_type is not UNSET:
            field_dict["value_type"] = value_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        kind = d.pop("kind", UNSET)

        name = d.pop("name", UNSET)

        _value_type = d.pop("value_type", UNSET)
        value_type: datetime.datetime | Unset
        if isinstance(_value_type,  Unset):
            value_type = UNSET
        else:
            value_type = datetime.datetime.fromisoformat(_value_type)




        query_ai_report_data_response_data_column = cls(
            code=code,
            kind=kind,
            name=name,
            value_type=value_type,
        )


        query_ai_report_data_response_data_column.additional_properties = d
        return query_ai_report_data_response_data_column

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
