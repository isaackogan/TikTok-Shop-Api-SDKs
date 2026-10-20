from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_external_order_references_response_data_external_order_line_item import GetExternalOrderReferencesResponseDataExternalOrderLineItem





T = TypeVar("T", bound="ExternalOrder")



@_attrs_define
class ExternalOrder:
    """ 
        Attributes:
            id (str | Unset): Order ID in your OMS.
            platform (str | Unset): The alias of your OMS.
            line_items (list[GetExternalOrderReferencesResponseDataExternalOrderLineItem] | Unset): Line item references
                between the external order and TikTok Shop.
     """

    id: str | Unset = UNSET
    platform: str | Unset = UNSET
    line_items: list[GetExternalOrderReferencesResponseDataExternalOrderLineItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_external_order_references_response_data_external_order_line_item import GetExternalOrderReferencesResponseDataExternalOrderLineItem # noqa: PLC0415
        id = self.id

        platform = self.platform

        line_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.line_items, Unset):
            line_items = []
            for line_items_item_data in self.line_items:
                line_items_item = line_items_item_data.to_dict()
                line_items.append(line_items_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if platform is not UNSET:
            field_dict["platform"] = platform
        if line_items is not UNSET:
            field_dict["line_items"] = line_items

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_external_order_references_response_data_external_order_line_item import GetExternalOrderReferencesResponseDataExternalOrderLineItem # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        platform = d.pop("platform", UNSET)

        _line_items = d.pop("line_items", UNSET)
        line_items: list[GetExternalOrderReferencesResponseDataExternalOrderLineItem] | Unset = UNSET
        if _line_items is not UNSET:
            line_items = []
            for line_items_item_data in _line_items:
                line_items_item = GetExternalOrderReferencesResponseDataExternalOrderLineItem.from_dict(line_items_item_data)



                line_items.append(line_items_item)


        external_order = cls(
            id=id,
            platform=platform,
            line_items=line_items,
        )


        external_order.additional_properties = d
        return external_order

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
