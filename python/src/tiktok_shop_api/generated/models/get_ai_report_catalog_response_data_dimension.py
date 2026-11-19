from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_ai_report_catalog_response_data_detail_field_value import GetAIReportCatalogResponseDataDetailFieldValue





T = TypeVar("T", bound="GetAIReportCatalogResponseDataDimension")



@_attrs_define
class GetAIReportCatalogResponseDataDimension:
    """ 
        Attributes:
            code (str | Unset): Dimension code to use in group_dimensions or filters[].code, according to the query rules.
            description (str | Unset): Business meaning of this dimension.
            name (str | Unset): Display name of this dimension.
            values (list[GetAIReportCatalogResponseDataDetailFieldValue] | Unset): Fixed filter options for this dimension,
                such as LIVE, VIDEO and PRODUCT_CARD for content_type. Use option.value in filters[].values. Use Search AI
                Report Dimension Options to find products, Creators and other entities.
     """

    code: str | Unset = UNSET
    description: str | Unset = UNSET
    name: str | Unset = UNSET
    values: list[GetAIReportCatalogResponseDataDetailFieldValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_ai_report_catalog_response_data_detail_field_value import GetAIReportCatalogResponseDataDetailFieldValue # noqa: PLC0415
        code = self.code

        description = self.description

        name = self.name

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

        _values = d.pop("values", UNSET)
        values: list[GetAIReportCatalogResponseDataDetailFieldValue] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = GetAIReportCatalogResponseDataDetailFieldValue.from_dict(values_item_data)



                values.append(values_item)


        get_ai_report_catalog_response_data_dimension = cls(
            code=code,
            description=description,
            name=name,
            values=values,
        )


        get_ai_report_catalog_response_data_dimension.additional_properties = d
        return get_ai_report_catalog_response_data_dimension

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
