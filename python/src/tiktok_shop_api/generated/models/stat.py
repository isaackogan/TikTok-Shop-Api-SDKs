from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="Stat")



@_attrs_define
class Stat:
    """ 
        Attributes:
            customers (str | Unset): Reported customer count for this item in the selected reporting window, represented as
                a string.
            gmv_range (str | Unset): Formatted gross merchandise value (GMV) band for this item. Positive values use 50-unit
                bands separated by " ~ "; nonpositive values are shown as a formatted zero. Currency formatting uses the shop's
                region and currency information where available.
            orders (str | Unset): Reported order count for this item in the selected reporting window, represented as a
                string.
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

        stat = cls(
            customers=customers,
            gmv_range=gmv_range,
            orders=orders,
        )


        stat.additional_properties = d
        return stat

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
