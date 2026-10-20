from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BatchShipPackagesResponseDataErrorDetail")


@_attrs_define
class BatchShipPackagesResponseDataErrorDetail:
    """
    Attributes:
        package_id (str | Unset): Package ID.
    """

    package_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        package_id = self.package_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if package_id is not UNSET:
            field_dict["package_id"] = package_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        package_id = d.pop("package_id", UNSET)

        batch_ship_packages_response_data_error_detail = cls(
            package_id=package_id,
        )

        batch_ship_packages_response_data_error_detail.additional_properties = d
        return batch_ship_packages_response_data_error_detail

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
