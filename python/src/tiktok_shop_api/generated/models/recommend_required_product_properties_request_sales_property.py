from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.recommend_required_product_properties_request_sales_property_value import (
        RecommendRequiredProductPropertiesRequestSalesPropertyValue,
    )


T = TypeVar("T", bound="RecommendRequiredProductPropertiesRequestSalesProperty")


@_attrs_define
class RecommendRequiredProductPropertiesRequestSalesProperty:
    """
    Attributes:
        id (str): ID of the sales property.
        values (list[RecommendRequiredProductPropertiesRequestSalesPropertyValue]): Existing values selected for the
            sales property.
    """

    id: str
    values: list[RecommendRequiredProductPropertiesRequestSalesPropertyValue]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        values = []
        for values_item_data in self.values:
            values_item = values_item_data.to_dict()
            values.append(values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "values": values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.recommend_required_product_properties_request_sales_property_value import (
            RecommendRequiredProductPropertiesRequestSalesPropertyValue,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id")

        values = []
        _values = d.pop("values")
        for values_item_data in _values:
            values_item = RecommendRequiredProductPropertiesRequestSalesPropertyValue.from_dict(values_item_data)

            values.append(values_item)

        recommend_required_product_properties_request_sales_property = cls(
            id=id,
            values=values,
        )

        recommend_required_product_properties_request_sales_property.additional_properties = d
        return recommend_required_product_properties_request_sales_property

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
