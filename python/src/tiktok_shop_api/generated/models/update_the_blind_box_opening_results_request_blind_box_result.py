from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UpdateTheBlindBoxOpeningResultsRequestBlindBoxResult")



@_attrs_define
class UpdateTheBlindBoxOpeningResultsRequestBlindBoxResult:
    """ 
        Attributes:
            order_line_id (str | Unset): The TikTok Shop line item ID for the blind box in the specified order.
            blind_result_product_id (str | Unset): The TikTok Shop product ID revealed by opening the blind box.
            blind_result_sku_id (str | Unset): The TikTok Shop SKU ID revealed by opening the blind box.
            blind_open_time (int | Unset): Unix timestamp in milliseconds indicating when the blind box was opened.
     """

    order_line_id: str | Unset = UNSET
    blind_result_product_id: str | Unset = UNSET
    blind_result_sku_id: str | Unset = UNSET
    blind_open_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        order_line_id = self.order_line_id

        blind_result_product_id = self.blind_result_product_id

        blind_result_sku_id = self.blind_result_sku_id

        blind_open_time = self.blind_open_time


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if order_line_id is not UNSET:
            field_dict["order_line_id"] = order_line_id
        if blind_result_product_id is not UNSET:
            field_dict["blind_result_product_id"] = blind_result_product_id
        if blind_result_sku_id is not UNSET:
            field_dict["blind_result_sku_id"] = blind_result_sku_id
        if blind_open_time is not UNSET:
            field_dict["blind_open_time"] = blind_open_time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order_line_id = d.pop("order_line_id", UNSET)

        blind_result_product_id = d.pop("blind_result_product_id", UNSET)

        blind_result_sku_id = d.pop("blind_result_sku_id", UNSET)

        blind_open_time = d.pop("blind_open_time", UNSET)

        update_the_blind_box_opening_results_request_blind_box_result = cls(
            order_line_id=order_line_id,
            blind_result_product_id=blind_result_product_id,
            blind_result_sku_id=blind_result_sku_id,
            blind_open_time=blind_open_time,
        )


        update_the_blind_box_opening_results_request_blind_box_result.additional_properties = d
        return update_the_blind_box_opening_results_request_blind_box_result

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
