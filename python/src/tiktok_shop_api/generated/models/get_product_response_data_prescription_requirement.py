from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetProductResponseDataPrescriptionRequirement")


@_attrs_define
class GetProductResponseDataPrescriptionRequirement:
    """
    Attributes:
        needs_prescription (bool | Unset): A flag to indicate whether a prescription is required to purchase this
            pharmacy product.
    """

    needs_prescription: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        needs_prescription = self.needs_prescription

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if needs_prescription is not UNSET:
            field_dict["needs_prescription"] = needs_prescription

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        needs_prescription = d.pop("needs_prescription", UNSET)

        get_product_response_data_prescription_requirement = cls(
            needs_prescription=needs_prescription,
        )

        get_product_response_data_prescription_requirement.additional_properties = d
        return get_product_response_data_prescription_requirement

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
