from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="GetAIReportCatalogResponseDataMetric")



@_attrs_define
class GetAIReportCatalogResponseDataMetric:
    """ 
        Attributes:
            category (str | Unset): Category used to organize the metric catalog. TRANSACTIONS: sales and transaction
                metrics. TRAFFIC_EFFICIENCY: traffic and conversion efficiency metrics. Query rules determine which metrics can
                be combined.
            code (str | Unset): Metric code to include in the request metric_codes.
            description (str | Unset): What the metric measures and how it is calculated.
            formula (str | Unset): Formula explaining how this metric is calculated. Returned when a formula is configured.
            name (str | Unset): Display name of this metric.
            value_type (datetime.datetime | Unset): Format of the returned value. Current types: CURRENCY — Monetary value;
                read currency in the query result for its currency code; DATETIME — UTC date-time string in RFC 3339 format;
                DECIMAL — Decimal value represented as a string; DURATION — Duration; the metric or detail field description
                specifies its unit; ENUM — Coded value; read the field definition or candidate values for its meaning; INT —
                Integer value represented as a string; RATIO — Raw ratio: 0.1234 represents 12.34%; STRING — Text value. New
                types may be added.
     """

    category: str | Unset = UNSET
    code: str | Unset = UNSET
    description: str | Unset = UNSET
    formula: str | Unset = UNSET
    name: str | Unset = UNSET
    value_type: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        category = self.category

        code = self.code

        description = self.description

        formula = self.formula

        name = self.name

        value_type: str | Unset = UNSET
        if not isinstance(self.value_type, Unset):
            value_type = self.value_type.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if category is not UNSET:
            field_dict["category"] = category
        if code is not UNSET:
            field_dict["code"] = code
        if description is not UNSET:
            field_dict["description"] = description
        if formula is not UNSET:
            field_dict["formula"] = formula
        if name is not UNSET:
            field_dict["name"] = name
        if value_type is not UNSET:
            field_dict["value_type"] = value_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = d.pop("category", UNSET)

        code = d.pop("code", UNSET)

        description = d.pop("description", UNSET)

        formula = d.pop("formula", UNSET)

        name = d.pop("name", UNSET)

        _value_type = d.pop("value_type", UNSET)
        value_type: datetime.datetime | Unset
        if isinstance(_value_type,  Unset):
            value_type = UNSET
        else:
            value_type = datetime.datetime.fromisoformat(_value_type)




        get_ai_report_catalog_response_data_metric = cls(
            category=category,
            code=code,
            description=description,
            formula=formula,
            name=name,
            value_type=value_type,
        )


        get_ai_report_catalog_response_data_metric.additional_properties = d
        return get_ai_report_catalog_response_data_metric

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
