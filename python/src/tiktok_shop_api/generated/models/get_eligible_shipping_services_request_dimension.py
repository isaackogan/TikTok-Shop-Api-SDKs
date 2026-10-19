from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetEligibleShippingServicesRequestDimension")


@_attrs_define
class GetEligibleShippingServicesRequestDimension:
    """
    Attributes:
        length (str): The length of the package. The length, width, height must be passed together.
        width (str): The width of the package. The length, width, height must be passed together.
        height (str): The height of the package. The length, width, height must be passed together.
        unit (str): The unit of measurement for the package dimensions.
            - CM
            - INCH
    """

    length: str
    width: str
    height: str
    unit: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        length = self.length

        width = self.width

        height = self.height

        unit = self.unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "length": length,
                "width": width,
                "height": height,
                "unit": unit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        length = d.pop("length")

        width = d.pop("width")

        height = d.pop("height")

        unit = d.pop("unit")

        get_eligible_shipping_services_request_dimension = cls(
            length=length,
            width=width,
            height=height,
            unit=unit,
        )

        get_eligible_shipping_services_request_dimension.additional_properties = d
        return get_eligible_shipping_services_request_dimension

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
