from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.add_external_order_references_request_order_external_order import AddExternalOrderReferencesRequestOrderExternalOrder





T = TypeVar("T", bound="AddExternalOrderReferencesRequestOrder")



@_attrs_define
class AddExternalOrderReferencesRequestOrder:
    """ 
        Attributes:
            id (str): The unique identifier for a TikTok Shop order.
            external_order (AddExternalOrderReferencesRequestOrderExternalOrder):
     """

    id: str
    external_order: AddExternalOrderReferencesRequestOrderExternalOrder
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.add_external_order_references_request_order_external_order import AddExternalOrderReferencesRequestOrderExternalOrder # noqa: PLC0415
        id = self.id

        external_order = self.external_order.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "external_order": external_order,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_external_order_references_request_order_external_order import AddExternalOrderReferencesRequestOrderExternalOrder # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id")

        external_order = AddExternalOrderReferencesRequestOrderExternalOrder.from_dict(d.pop("external_order"))




        add_external_order_references_request_order = cls(
            id=id,
            external_order=external_order,
        )


        add_external_order_references_request_order.additional_properties = d
        return add_external_order_references_request_order

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
