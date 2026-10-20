from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.confirm_package_shipment_request_package_weight_unit import ConfirmPackageShipmentRequestPackageWeightUnit
from ..types import UNSET, Unset






T = TypeVar("T", bound="ConfirmPackageShipmentRequestPackageWeight")



@_attrs_define
class ConfirmPackageShipmentRequestPackageWeight:
    """ 
        Attributes:
            value (int | Unset): Package weight. Must be greater than or equal to `0`.
            unit (ConfirmPackageShipmentRequestPackageWeightUnit | Unset): Package weight unit
                Possible values:
                - KILOGRAM
                - GRAM
                - MILLIGRAM
                - POUND
                - OUNCE
     """

    value: int | Unset = UNSET
    unit: ConfirmPackageShipmentRequestPackageWeightUnit | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        value = self.value

        unit: str | Unset = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if value is not UNSET:
            field_dict["value"] = value
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value", UNSET)

        _unit = d.pop("unit", UNSET)
        unit: ConfirmPackageShipmentRequestPackageWeightUnit | Unset
        if isinstance(_unit,  Unset):
            unit = UNSET
        else:
            unit = ConfirmPackageShipmentRequestPackageWeightUnit(_unit)




        confirm_package_shipment_request_package_weight = cls(
            value=value,
            unit=unit,
        )


        confirm_package_shipment_request_package_weight.additional_properties = d
        return confirm_package_shipment_request_package_weight

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
