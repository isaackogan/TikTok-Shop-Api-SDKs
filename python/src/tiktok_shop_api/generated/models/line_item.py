from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="LineItem")



@_attrs_define
class LineItem:
    """ 
        Attributes:
            return_line_item_id (str | Unset): Unique identifier for this item in the return. In the case of virtual bundle,
                this is corresponds to the id of the original parent item bundle.
            sub_return_line_item_id (str | Unset): Unique identifier for this item in the return. In the case of virtual
                bundle, this is corresponds to the id of the current child item being returned.
            sku_id (str | Unset): SKU identifier associated with this item (for product details).
            main_order_id (str | Unset): Identifier of the associated main (forward) order.
            sku_return_request_id (str | Unset): Identifier of the associated SKU-level, sub return request.
     """

    return_line_item_id: str | Unset = UNSET
    sub_return_line_item_id: str | Unset = UNSET
    sku_id: str | Unset = UNSET
    main_order_id: str | Unset = UNSET
    sku_return_request_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        return_line_item_id = self.return_line_item_id

        sub_return_line_item_id = self.sub_return_line_item_id

        sku_id = self.sku_id

        main_order_id = self.main_order_id

        sku_return_request_id = self.sku_return_request_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if return_line_item_id is not UNSET:
            field_dict["return_line_item_id"] = return_line_item_id
        if sub_return_line_item_id is not UNSET:
            field_dict["sub_return_line_item_id"] = sub_return_line_item_id
        if sku_id is not UNSET:
            field_dict["sku_id"] = sku_id
        if main_order_id is not UNSET:
            field_dict["main_order_id"] = main_order_id
        if sku_return_request_id is not UNSET:
            field_dict["sku_return_request_id"] = sku_return_request_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        return_line_item_id = d.pop("return_line_item_id", UNSET)

        sub_return_line_item_id = d.pop("sub_return_line_item_id", UNSET)

        sku_id = d.pop("sku_id", UNSET)

        main_order_id = d.pop("main_order_id", UNSET)

        sku_return_request_id = d.pop("sku_return_request_id", UNSET)

        line_item = cls(
            return_line_item_id=return_line_item_id,
            sub_return_line_item_id=sub_return_line_item_id,
            sku_id=sku_id,
            main_order_id=main_order_id,
            sku_return_request_id=sku_return_request_id,
        )


        line_item.additional_properties = d
        return line_item

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
