from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="InventorySearchRequest")



@_attrs_define
class InventorySearchRequest:
    """ 
        Attributes:
            product_ids (list[str] | Unset): A list of product IDs used to search for inventory information.
                Max IDs: 100
            sku_ids (list[str] | Unset): A list of SKU IDs used to search for inventory information.
                Max IDs: 600

                **Note**: If both `sku_ids` and `product_ids` are passed, `sku_ids` will take precedence.
     """

    product_ids: list[str] | Unset = UNSET
    sku_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        product_ids: list[str] | Unset = UNSET
        if not isinstance(self.product_ids, Unset):
            product_ids = self.product_ids



        sku_ids: list[str] | Unset = UNSET
        if not isinstance(self.sku_ids, Unset):
            sku_ids = self.sku_ids




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if product_ids is not UNSET:
            field_dict["product_ids"] = product_ids
        if sku_ids is not UNSET:
            field_dict["sku_ids"] = sku_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_ids = cast(list[str], d.pop("product_ids", UNSET))


        sku_ids = cast(list[str], d.pop("sku_ids", UNSET))


        inventory_search_request = cls(
            product_ids=product_ids,
            sku_ids=sku_ids,
        )


        inventory_search_request.additional_properties = d
        return inventory_search_request

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
