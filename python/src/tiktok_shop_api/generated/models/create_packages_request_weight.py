from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_packages_request_weight_unit import CreatePackagesRequestWeightUnit

T = TypeVar("T", bound="CreatePackagesRequestWeight")


@_attrs_define
class CreatePackagesRequestWeight:
    """
    Attributes:
        value (str): The numerical value of the package weight.
        unit (CreatePackagesRequestWeightUnit): The unit of measurement for the package weight.

            Available values:
            - `GRAM`
            - `POUND`
    """

    value: str
    unit: CreatePackagesRequestWeightUnit
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        unit = self.unit.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
                "unit": unit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value")

        unit = CreatePackagesRequestWeightUnit(d.pop("unit"))

        create_packages_request_weight = cls(
            value=value,
            unit=unit,
        )

        create_packages_request_weight.additional_properties = d
        return create_packages_request_weight

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
