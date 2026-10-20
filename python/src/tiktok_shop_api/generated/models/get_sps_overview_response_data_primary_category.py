from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetSPSOverviewResponseDataPrimaryCategory")



@_attrs_define
class GetSPSOverviewResponseDataPrimaryCategory:
    """ 
        Attributes:
            category_id (str | Unset): The primary category ID.
            category_name (str | Unset): The primary category name.
     """

    category_id: str | Unset = UNSET
    category_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        category_id = self.category_id

        category_name = self.category_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if category_id is not UNSET:
            field_dict["category_id"] = category_id
        if category_name is not UNSET:
            field_dict["category_name"] = category_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category_id = d.pop("category_id", UNSET)

        category_name = d.pop("category_name", UNSET)

        get_sps_overview_response_data_primary_category = cls(
            category_id=category_id,
            category_name=category_name,
        )


        get_sps_overview_response_data_primary_category.additional_properties = d
        return get_sps_overview_response_data_primary_category

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
