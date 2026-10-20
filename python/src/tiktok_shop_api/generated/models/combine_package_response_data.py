from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.batch_ship_packages_response_data_error import BatchShipPackagesResponseDataError
  from ..models.package import Package





T = TypeVar("T", bound="CombinePackageResponseData")



@_attrs_define
class CombinePackageResponseData:
    """ 
        Attributes:
            packages (list[Package] | Unset): Return list of successfully combined packages.
            errors (list[BatchShipPackagesResponseDataError] | Unset): The errors returned for packages that could not be
                combined.
     """

    packages: list[Package] | Unset = UNSET
    errors: list[BatchShipPackagesResponseDataError] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.batch_ship_packages_response_data_error import BatchShipPackagesResponseDataError # noqa: PLC0415
        from ..models.package import Package # noqa: PLC0415
        packages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.packages, Unset):
            packages = []
            for packages_item_data in self.packages:
                packages_item = packages_item_data.to_dict()
                packages.append(packages_item)



        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if packages is not UNSET:
            field_dict["packages"] = packages
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.batch_ship_packages_response_data_error import BatchShipPackagesResponseDataError # noqa: PLC0415
        from ..models.package import Package # noqa: PLC0415
        d = dict(src_dict)
        _packages = d.pop("packages", UNSET)
        packages: list[Package] | Unset = UNSET
        if _packages is not UNSET:
            packages = []
            for packages_item_data in _packages:
                packages_item = Package.from_dict(packages_item_data)



                packages.append(packages_item)


        _errors = d.pop("errors", UNSET)
        errors: list[BatchShipPackagesResponseDataError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = BatchShipPackagesResponseDataError.from_dict(errors_item_data)



                errors.append(errors_item)


        combine_package_response_data = cls(
            packages=packages,
            errors=errors,
        )


        combine_package_response_data.additional_properties = d
        return combine_package_response_data

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
