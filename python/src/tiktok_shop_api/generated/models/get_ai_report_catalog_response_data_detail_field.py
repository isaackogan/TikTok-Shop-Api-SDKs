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
  from ..models.get_ai_report_catalog_response_data_detail_field_value import GetAIReportCatalogResponseDataDetailFieldValue





T = TypeVar("T", bound="GetAIReportCatalogResponseDataDetailField")



@_attrs_define
class GetAIReportCatalogResponseDataDetailField:
    """ 
        Attributes:
            code (str | Unset): Detail field code to include in the request detail_fields.
            description (str | Unset): Business meaning of this detail field.
            name (str | Unset): Display name of this detail field.
            value_type (datetime.datetime | Unset): Format of the returned value. Current types: CURRENCY — Monetary value;
                read currency in the query result for its currency code; DATETIME — UTC date-time string in RFC 3339 format;
                DECIMAL — Decimal value represented as a string; DURATION — Duration; the metric or detail field description
                specifies its unit; ENUM — Coded value; read the field definition or candidate values for its meaning; INT —
                Integer value represented as a string; RATIO — Raw ratio: 0.1234 represents 12.34%; STRING — Text value. New
                types may be added.
            values (list[GetAIReportCatalogResponseDataDetailFieldValue] | Unset): Fixed values defined for this detail
                field, when configured. Each entry provides a value and its display information.
     """

    code: str | Unset = UNSET
    description: str | Unset = UNSET
    name: str | Unset = UNSET
    value_type: datetime.datetime | Unset = UNSET
    values: list[GetAIReportCatalogResponseDataDetailFieldValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_ai_report_catalog_response_data_detail_field_value import GetAIReportCatalogResponseDataDetailFieldValue # noqa: PLC0415
        code = self.code

        description = self.description

        name = self.name

        value_type: str | Unset = UNSET
        if not isinstance(self.value_type, Unset):
            value_type = self.value_type.isoformat()

        values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if code is not UNSET:
            field_dict["code"] = code
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if value_type is not UNSET:
            field_dict["value_type"] = value_type
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_ai_report_catalog_response_data_detail_field_value import GetAIReportCatalogResponseDataDetailFieldValue # noqa: PLC0415
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        _value_type = d.pop("value_type", UNSET)
        value_type: datetime.datetime | Unset
        if isinstance(_value_type,  Unset):
            value_type = UNSET
        else:
            value_type = datetime.datetime.fromisoformat(_value_type)




        _values = d.pop("values", UNSET)
        values: list[GetAIReportCatalogResponseDataDetailFieldValue] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = GetAIReportCatalogResponseDataDetailFieldValue.from_dict(values_item_data)



                values.append(values_item)


        get_ai_report_catalog_response_data_detail_field = cls(
            code=code,
            description=description,
            name=name,
            value_type=value_type,
            values=values,
        )


        get_ai_report_catalog_response_data_detail_field.additional_properties = d
        return get_ai_report_catalog_response_data_detail_field

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
