from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.confirm_package_shipment_request_package import ConfirmPackageShipmentRequestPackage





T = TypeVar("T", bound="ConfirmPackageShipmentRequest")



@_attrs_define
class ConfirmPackageShipmentRequest:
    """ 
        Attributes:
            warehouse_provider_id (str): The unique warehouse provider ID assigned by TikTok Shop. The value must represent
                a positive base-10 integer.
            packages (list[ConfirmPackageShipmentRequestPackage]): List of packages to confirm. Provide at least one
                package.
     """

    warehouse_provider_id: str
    packages: list[ConfirmPackageShipmentRequestPackage]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.confirm_package_shipment_request_package import ConfirmPackageShipmentRequestPackage # noqa: PLC0415
        warehouse_provider_id = self.warehouse_provider_id

        packages = []
        for packages_item_data in self.packages:
            packages_item = packages_item_data.to_dict()
            packages.append(packages_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "warehouse_provider_id": warehouse_provider_id,
            "packages": packages,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.confirm_package_shipment_request_package import ConfirmPackageShipmentRequestPackage # noqa: PLC0415
        d = dict(src_dict)
        warehouse_provider_id = d.pop("warehouse_provider_id")

        packages = []
        _packages = d.pop("packages")
        for packages_item_data in (_packages):
            packages_item = ConfirmPackageShipmentRequestPackage.from_dict(packages_item_data)



            packages.append(packages_item)


        confirm_package_shipment_request = cls(
            warehouse_provider_id=warehouse_provider_id,
            packages=packages,
        )


        confirm_package_shipment_request.additional_properties = d
        return confirm_package_shipment_request

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
