from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.value import Value





T = TypeVar("T", bound="ProductAttribute")



@_attrs_define
class ProductAttribute:
    """ 
        Attributes:
            id (str): The ID of the product attribute, retrieved from the [Get Attributes
                API](https://partner.tiktokshop.com/docv2/page/6509c5784a0bb702c0561cc8).
            values (list[Value]): A list of selectable values for the product attribute.

                **Note**: Provide either a built-in ID or a custom name; if both are provided, the ID takes priority.
     """

    id: str
    values: list[Value]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.value import Value # noqa: PLC0415
        id = self.id

        values = []
        for values_item_data in self.values:
            values_item = values_item_data.to_dict()
            values.append(values_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "values": values,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.value import Value # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id")

        values = []
        _values = d.pop("values")
        for values_item_data in (_values):
            values_item = Value.from_dict(values_item_data)



            values.append(values_item)


        product_attribute = cls(
            id=id,
            values=values,
        )


        product_attribute.additional_properties = d
        return product_attribute

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
