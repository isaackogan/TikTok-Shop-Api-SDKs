from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="Metric")



@_attrs_define
class Metric:
    """ 
        Attributes:
            customers (str | Unset): Customer count for this entity within the selected audience, scope and analysis window,
                represented as a string.
            gmv_range (str | Unset): Formatted gross merchandise value (GMV) range for this entity, using the shop's
                currency. Zero is represented as a formatted zero rather than a range. Positive GMV is grouped into 50-unit
                bands in the shop's local currency. The formatted value is returned without conversion to another currency.
            orders (str | Unset): Order count for this entity within the selected audience, scope and analysis window,
                represented as a string.
     """

    customers: str | Unset = UNSET
    gmv_range: str | Unset = UNSET
    orders: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        customers = self.customers

        gmv_range = self.gmv_range

        orders = self.orders


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if customers is not UNSET:
            field_dict["customers"] = customers
        if gmv_range is not UNSET:
            field_dict["gmv_range"] = gmv_range
        if orders is not UNSET:
            field_dict["orders"] = orders

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        customers = d.pop("customers", UNSET)

        gmv_range = d.pop("gmv_range", UNSET)

        orders = d.pop("orders", UNSET)

        metric = cls(
            customers=customers,
            gmv_range=gmv_range,
            orders=orders,
        )


        metric.additional_properties = d
        return metric

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
