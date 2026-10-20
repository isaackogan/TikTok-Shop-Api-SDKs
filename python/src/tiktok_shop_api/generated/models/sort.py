from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.sort_sort_field import SortSortField
from ..models.sort_sort_order import SortSortOrder
from ..types import UNSET, Unset






T = TypeVar("T", bound="Sort")



@_attrs_define
class Sort:
    """ 
        Attributes:
            sort_field (SortSortField | Unset): Name of the field used for sorting.
                Possible values:
                - `CREATE_TIME`
                - `UPDATE_TIME`
            sort_order (SortSortOrder | Unset): Sort direction.
                Possible values:
                - `ASC`
                - `DESC`
     """

    sort_field: SortSortField | Unset = UNSET
    sort_order: SortSortOrder | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        sort_field: str | Unset = UNSET
        if not isinstance(self.sort_field, Unset):
            sort_field = self.sort_field.value


        sort_order: str | Unset = UNSET
        if not isinstance(self.sort_order, Unset):
            sort_order = self.sort_order.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if sort_field is not UNSET:
            field_dict["sort_field"] = sort_field
        if sort_order is not UNSET:
            field_dict["sort_order"] = sort_order

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _sort_field = d.pop("sort_field", UNSET)
        sort_field: SortSortField | Unset
        if isinstance(_sort_field,  Unset):
            sort_field = UNSET
        else:
            sort_field = SortSortField(_sort_field)




        _sort_order = d.pop("sort_order", UNSET)
        sort_order: SortSortOrder | Unset
        if isinstance(_sort_order,  Unset):
            sort_order = UNSET
        else:
            sort_order = SortSortOrder(_sort_order)




        sort = cls(
            sort_field=sort_field,
            sort_order=sort_order,
        )


        sort.additional_properties = d
        return sort

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
