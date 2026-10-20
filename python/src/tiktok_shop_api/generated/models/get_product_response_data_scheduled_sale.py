from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetProductResponseDataScheduledSale")



@_attrs_define
class GetProductResponseDataScheduledSale:
    """ 
        Attributes:
            is_enabled_scheduled_sale (bool | Unset): Whether scheduled listing is enabled for this product.
            schedule_sale_time (int | Unset): The stored scheduled listing time, expressed as a Unix timestamp in
                milliseconds.
     """

    is_enabled_scheduled_sale: bool | Unset = UNSET
    schedule_sale_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        is_enabled_scheduled_sale = self.is_enabled_scheduled_sale

        schedule_sale_time = self.schedule_sale_time


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if is_enabled_scheduled_sale is not UNSET:
            field_dict["is_enabled_scheduled_sale"] = is_enabled_scheduled_sale
        if schedule_sale_time is not UNSET:
            field_dict["schedule_sale_time"] = schedule_sale_time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_enabled_scheduled_sale = d.pop("is_enabled_scheduled_sale", UNSET)

        schedule_sale_time = d.pop("schedule_sale_time", UNSET)

        get_product_response_data_scheduled_sale = cls(
            is_enabled_scheduled_sale=is_enabled_scheduled_sale,
            schedule_sale_time=schedule_sale_time,
        )


        get_product_response_data_scheduled_sale.additional_properties = d
        return get_product_response_data_scheduled_sale

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
