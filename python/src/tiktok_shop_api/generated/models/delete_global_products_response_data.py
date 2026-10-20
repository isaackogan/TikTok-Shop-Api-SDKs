from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.delete_global_products_response_data_error import DeleteGlobalProductsResponseDataError





T = TypeVar("T", bound="DeleteGlobalProductsResponseData")



@_attrs_define
class DeleteGlobalProductsResponseData:
    """ 
        Attributes:
            errors (list[DeleteGlobalProductsResponseDataError] | Unset): The errors for individual global products that
                could not be deleted. Check this list even when the top-level `code` is `0`.
     """

    errors: list[DeleteGlobalProductsResponseDataError] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.delete_global_products_response_data_error import DeleteGlobalProductsResponseDataError # noqa: PLC0415
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
        from ..models.delete_global_products_response_data_error import DeleteGlobalProductsResponseDataError # noqa: PLC0415
        d = dict(src_dict)
        _errors = d.pop("errors", UNSET)
        errors: list[DeleteGlobalProductsResponseDataError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = DeleteGlobalProductsResponseDataError.from_dict(errors_item_data)



                errors.append(errors_item)


        delete_global_products_response_data = cls(
            errors=errors,
        )


        delete_global_products_response_data.additional_properties = d
        return delete_global_products_response_data

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
