from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.update_global_inventory_request_global_sku import UpdateGlobalInventoryRequestGlobalSku





T = TypeVar("T", bound="UpdateGlobalInventoryRequest")



@_attrs_define
class UpdateGlobalInventoryRequest:
    """ 
        Attributes:
            global_skus (list[UpdateGlobalInventoryRequestGlobalSku]): A non-empty list of global SKUs whose inventory
                quantities you want to set.
     """

    global_skus: list[UpdateGlobalInventoryRequestGlobalSku]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_global_inventory_request_global_sku import UpdateGlobalInventoryRequestGlobalSku # noqa: PLC0415
        global_skus = []
        for global_skus_item_data in self.global_skus:
            global_skus_item = global_skus_item_data.to_dict()
            global_skus.append(global_skus_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "global_skus": global_skus,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_global_inventory_request_global_sku import UpdateGlobalInventoryRequestGlobalSku # noqa: PLC0415
        d = dict(src_dict)
        global_skus = []
        _global_skus = d.pop("global_skus")
        for global_skus_item_data in (_global_skus):
            global_skus_item = UpdateGlobalInventoryRequestGlobalSku.from_dict(global_skus_item_data)



            global_skus.append(global_skus_item)


        update_global_inventory_request = cls(
            global_skus=global_skus,
        )


        update_global_inventory_request.additional_properties = d
        return update_global_inventory_request

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
