from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ConfirmOrderSplitResponseDataPackage")



@_attrs_define
class ConfirmOrderSplitResponseDataPackage:
    """ 
        Attributes:
            splittable_group_id (str | Unset): The developer-defined `id` of the corresponding group from
                `splittable_groups` or `splittable_groups_v2` in the request.
            id (str | Unset): Package ID after success split. Use this new package ID to call [Ship Package
                API](https://partner.tiktokshop.com/docv2/page/650aa4f1defece02be6e7cb1?external_id=650aa4f1defece02be6e7cb1) to
                ship the package.
     """

    splittable_group_id: str | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        splittable_group_id = self.splittable_group_id

        id = self.id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if splittable_group_id is not UNSET:
            field_dict["splittable_group_id"] = splittable_group_id
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        splittable_group_id = d.pop("splittable_group_id", UNSET)

        id = d.pop("id", UNSET)

        confirm_order_split_response_data_package = cls(
            splittable_group_id=splittable_group_id,
            id=id,
        )


        confirm_order_split_response_data_package.additional_properties = d
        return confirm_order_split_response_data_package

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
