from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.batch_ship_packages_request_package import BatchShipPackagesRequestPackage





T = TypeVar("T", bound="BatchShipPackagesRequest")



@_attrs_define
class BatchShipPackagesRequest:
    """ 
        Attributes:
            packages (list[BatchShipPackagesRequestPackage]): Input list of packages you would like to batch ship.
     """

    packages: list[BatchShipPackagesRequestPackage]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.batch_ship_packages_request_package import BatchShipPackagesRequestPackage # noqa: PLC0415
        packages = []
        for packages_item_data in self.packages:
            packages_item = packages_item_data.to_dict()
            packages.append(packages_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "packages": packages,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.batch_ship_packages_request_package import BatchShipPackagesRequestPackage # noqa: PLC0415
        d = dict(src_dict)
        packages = []
        _packages = d.pop("packages")
        for packages_item_data in (_packages):
            packages_item = BatchShipPackagesRequestPackage.from_dict(packages_item_data)



            packages.append(packages_item)


        batch_ship_packages_request = cls(
            packages=packages,
        )


        batch_ship_packages_request.additional_properties = d
        return batch_ship_packages_request

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
