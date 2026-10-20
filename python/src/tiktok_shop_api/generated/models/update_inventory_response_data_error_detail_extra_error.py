from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UpdateInventoryResponseDataErrorDetailExtraError")



@_attrs_define
class UpdateInventoryResponseDataErrorDetailExtraError:
    """ 
        Attributes:
            warehouse_id (str | Unset): The ID of the warehouse  where the error occurred.
            code (int | Unset): The secondary error code.
            message (str | Unset): The secondary error message.
     """

    warehouse_id: str | Unset = UNSET
    code: int | Unset = UNSET
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        warehouse_id = self.warehouse_id

        code = self.code

        message = self.message


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if warehouse_id is not UNSET:
            field_dict["warehouse_id"] = warehouse_id
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        warehouse_id = d.pop("warehouse_id", UNSET)

        code = d.pop("code", UNSET)

        message = d.pop("message", UNSET)

        update_inventory_response_data_error_detail_extra_error = cls(
            warehouse_id=warehouse_id,
            code=code,
            message=message,
        )


        update_inventory_response_data_error_detail_extra_error.additional_properties = d
        return update_inventory_response_data_error_detail_extra_error

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
