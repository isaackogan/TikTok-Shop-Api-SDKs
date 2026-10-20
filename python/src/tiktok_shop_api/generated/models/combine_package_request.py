from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.combine_package_request_combinable_package import CombinePackageRequestCombinablePackage


T = TypeVar("T", bound="CombinePackageRequest")


@_attrs_define
class CombinePackageRequest:
    """
    Attributes:
        combinable_packages (list[CombinePackageRequestCombinablePackage]): The packages to combine. Provide at least
            one package. Each item identifies a package and can specify the order IDs to include.
    """

    combinable_packages: list[CombinePackageRequestCombinablePackage]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        combinable_packages = []
        for combinable_packages_item_data in self.combinable_packages:
            combinable_packages_item = combinable_packages_item_data.to_dict()
            combinable_packages.append(combinable_packages_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "combinable_packages": combinable_packages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.combine_package_request_combinable_package import (
            CombinePackageRequestCombinablePackage,  # noqa: PLC0415
        )

        d = dict(src_dict)
        combinable_packages = []
        _combinable_packages = d.pop("combinable_packages")
        for combinable_packages_item_data in _combinable_packages:
            combinable_packages_item = CombinePackageRequestCombinablePackage.from_dict(combinable_packages_item_data)

            combinable_packages.append(combinable_packages_item)

        combine_package_request = cls(
            combinable_packages=combinable_packages,
        )

        combine_package_request.additional_properties = d
        return combine_package_request

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
