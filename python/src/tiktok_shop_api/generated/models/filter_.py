from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.creator import Creator





T = TypeVar("T", bound="Filter")



@_attrs_define
class Filter:
    """ 
        Attributes:
            code (str): Catalog code of the filter target. Currently this must be a dimensions[].code from the catalog;
                metric filters are not supported. For author_id, supply creators; for other dimensions, supply values.
            creators (list[Creator] | Unset): Creators to include when code is author_id. Each entry contains a
                creator_open_id returned to this application. Do not also supply values.
            operator (str | Unset): Filter operator. IN: Include records whose field value is in values, or whose Creator is
                in creators. Currently only IN is supported. Defaults to IN when omitted.
            type_ (str | Unset): Filter target type. DIMENSION: Filter a dimension. Currently only DIMENSION is supported.
                Defaults to DIMENSION when omitted.
            values (list[str] | Unset): Values to include for this dimension. Use dimensions[].values[].value from the
                catalog or options[].value from dimension candidate search. For author_id, use creators instead.
     """

    code: str
    creators: list[Creator] | Unset = UNSET
    operator: str | Unset = UNSET
    type_: str | Unset = UNSET
    values: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.creator import Creator # noqa: PLC0415
        code = self.code

        creators: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.creators, Unset):
            creators = []
            for creators_item_data in self.creators:
                creators_item = creators_item_data.to_dict()
                creators.append(creators_item)



        operator = self.operator

        type_ = self.type_

        values: list[str] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = self.values




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "code": code,
        })
        if creators is not UNSET:
            field_dict["creators"] = creators
        if operator is not UNSET:
            field_dict["operator"] = operator
        if type_ is not UNSET:
            field_dict["type"] = type_
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.creator import Creator # noqa: PLC0415
        d = dict(src_dict)
        code = d.pop("code")

        _creators = d.pop("creators", UNSET)
        creators: list[Creator] | Unset = UNSET
        if _creators is not UNSET:
            creators = []
            for creators_item_data in _creators:
                creators_item = Creator.from_dict(creators_item_data)



                creators.append(creators_item)


        operator = d.pop("operator", UNSET)

        type_ = d.pop("type", UNSET)

        values = cast(list[str], d.pop("values", UNSET))


        filter_ = cls(
            code=code,
            creators=creators,
            operator=operator,
            type_=type_,
            values=values,
        )


        filter_.additional_properties = d
        return filter_

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
