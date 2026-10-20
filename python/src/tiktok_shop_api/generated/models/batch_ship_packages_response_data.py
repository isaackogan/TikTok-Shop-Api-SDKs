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





T = TypeVar("T", bound="BatchShipPackagesResponseData")



@_attrs_define
class BatchShipPackagesResponseData:
    """ 
        Attributes:
            errors (list[BatchShipPackagesResponseDataError] | Unset): Package-specific errors for packages that could not
                be shipped. Check this list even when the top-level response `code` is `0`.
     """

    errors: list[BatchShipPackagesResponseDataError] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.batch_ship_packages_response_data_error import BatchShipPackagesResponseDataError # noqa: PLC0415
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
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.batch_ship_packages_response_data_error import BatchShipPackagesResponseDataError # noqa: PLC0415
        d = dict(src_dict)
        _errors = d.pop("errors", UNSET)
        errors: list[BatchShipPackagesResponseDataError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = BatchShipPackagesResponseDataError.from_dict(errors_item_data)



                errors.append(errors_item)


        batch_ship_packages_response_data = cls(
            errors=errors,
        )


        batch_ship_packages_response_data.additional_properties = d
        return batch_ship_packages_response_data

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
