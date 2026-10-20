from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetFBTWarehouseListResponseDataWarehouseLogisticsService")



@_attrs_define
class GetFBTWarehouseListResponseDataWarehouseLogisticsService:
    """ 
        Attributes:
            id (str | Unset): The identifier for logistics service in TikTok Shop system.
            name (str | Unset): The logistics service name.
            subscribed (bool | Unset): A flag indicating whether the logistic service is subscribed.
                True: Subscribed.
                False: Not subscribed.
     """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    subscribed: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        subscribed = self.subscribed


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if subscribed is not UNSET:
            field_dict["subscribed"] = subscribed

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        subscribed = d.pop("subscribed", UNSET)

        get_fbt_warehouse_list_response_data_warehouse_logistics_service = cls(
            id=id,
            name=name,
            subscribed=subscribed,
        )


        get_fbt_warehouse_list_response_data_warehouse_logistics_service.additional_properties = d
        return get_fbt_warehouse_list_response_data_warehouse_logistics_service

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
