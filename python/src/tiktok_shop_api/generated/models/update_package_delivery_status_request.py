from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.update_package_delivery_status_request_package import UpdatePackageDeliveryStatusRequestPackage


T = TypeVar("T", bound="UpdatePackageDeliveryStatusRequest")


@_attrs_define
class UpdatePackageDeliveryStatusRequest:
    """
    Attributes:
        packages (list[UpdatePackageDeliveryStatusRequestPackage]): The packages to update. Provide at least one
            package.
    """

    packages: list[UpdatePackageDeliveryStatusRequestPackage]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        packages = []
        for packages_item_data in self.packages:
            packages_item = packages_item_data.to_dict()
            packages.append(packages_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "packages": packages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_package_delivery_status_request_package import (
            UpdatePackageDeliveryStatusRequestPackage,  # noqa: PLC0415
        )

        d = dict(src_dict)
        packages = []
        _packages = d.pop("packages")
        for packages_item_data in _packages:
            packages_item = UpdatePackageDeliveryStatusRequestPackage.from_dict(packages_item_data)

            packages.append(packages_item)

        update_package_delivery_status_request = cls(
            packages=packages,
        )

        update_package_delivery_status_request.additional_properties = d
        return update_package_delivery_status_request

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
