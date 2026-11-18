from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="DeleteShopMaterialResponseData")



@_attrs_define
class DeleteShopMaterialResponseData:
    """ 
        Attributes:
            failed_reason (str | Unset): The failure reason when `is_deleted` is `false`.
            is_deleted (bool | Unset): Whether the requested material deletion succeeded.
     """

    failed_reason: str | Unset = UNSET
    is_deleted: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        failed_reason = self.failed_reason

        is_deleted = self.is_deleted


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if failed_reason is not UNSET:
            field_dict["failed_reason"] = failed_reason
        if is_deleted is not UNSET:
            field_dict["is_deleted"] = is_deleted

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        failed_reason = d.pop("failed_reason", UNSET)

        is_deleted = d.pop("is_deleted", UNSET)

        delete_shop_material_response_data = cls(
            failed_reason=failed_reason,
            is_deleted=is_deleted,
        )


        delete_shop_material_response_data.additional_properties = d
        return delete_shop_material_response_data

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
