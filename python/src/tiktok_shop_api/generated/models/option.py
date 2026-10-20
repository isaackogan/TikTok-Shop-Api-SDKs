from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.option_children import OptionChildren





T = TypeVar("T", bound="Option")



@_attrs_define
class Option:
    """ 
        Attributes:
            id (str | Unset): Option id
            name (str | Unset): The option name.
            option_children (list[OptionChildren] | Unset): Children option detail list, used if the option has sub option
                choices
     """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    option_children: list[OptionChildren] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.option_children import OptionChildren # noqa: PLC0415
        id = self.id

        name = self.name

        option_children: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.option_children, Unset):
            option_children = []
            for option_children_item_data in self.option_children:
                option_children_item = option_children_item_data.to_dict()
                option_children.append(option_children_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if option_children is not UNSET:
            field_dict["option_children"] = option_children

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.option_children import OptionChildren # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _option_children = d.pop("option_children", UNSET)
        option_children: list[OptionChildren] | Unset = UNSET
        if _option_children is not UNSET:
            option_children = []
            for option_children_item_data in _option_children:
                option_children_item = OptionChildren.from_dict(option_children_item_data)



                option_children.append(option_children_item)


        option = cls(
            id=id,
            name=name,
            option_children=option_children,
        )


        option.additional_properties = d
        return option

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
