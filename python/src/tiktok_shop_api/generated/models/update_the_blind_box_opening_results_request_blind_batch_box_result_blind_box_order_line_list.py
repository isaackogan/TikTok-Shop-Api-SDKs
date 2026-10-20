from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_the_blind_box_opening_results_request_blind_batch_box_result_blind_box_order_line_list_product_type import (
    UpdateTheBlindBoxOpeningResultsRequestBlindBatchBoxResultBlindBoxOrderLineListProductType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateTheBlindBoxOpeningResultsRequestBlindBatchBoxResultBlindBoxOrderLineList")


@_attrs_define
class UpdateTheBlindBoxOpeningResultsRequestBlindBatchBoxResultBlindBoxOrderLineList:
    """
    Attributes:
        blind_result_product_id (str | Unset): The TikTok Shop product ID revealed for this item in the batch unboxing
            result.
        blind_result_sku_id (str | Unset): The TikTok Shop SKU ID revealed for this item in the batch unboxing result.
        blind_open_time (int | Unset): Unix timestamp in milliseconds indicating when the blind box was opened.
        product_type (UpdateTheBlindBoxOpeningResultsRequestBlindBatchBoxResultBlindBoxOrderLineListProductType |
            Unset): Unboxing product type.
            Possible values:
            - `NORMAL`: A normal unboxed product.
            - `GIFT`: A gift unboxed product.
    """

    blind_result_product_id: str | Unset = UNSET
    blind_result_sku_id: str | Unset = UNSET
    blind_open_time: int | Unset = UNSET
    product_type: UpdateTheBlindBoxOpeningResultsRequestBlindBatchBoxResultBlindBoxOrderLineListProductType | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        blind_result_product_id = self.blind_result_product_id

        blind_result_sku_id = self.blind_result_sku_id

        blind_open_time = self.blind_open_time

        product_type: str | Unset = UNSET
        if not isinstance(self.product_type, Unset):
            product_type = self.product_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if blind_result_product_id is not UNSET:
            field_dict["blind_result_product_id"] = blind_result_product_id
        if blind_result_sku_id is not UNSET:
            field_dict["blind_result_sku_id"] = blind_result_sku_id
        if blind_open_time is not UNSET:
            field_dict["blind_open_time"] = blind_open_time
        if product_type is not UNSET:
            field_dict["product_type"] = product_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        blind_result_product_id = d.pop("blind_result_product_id", UNSET)

        blind_result_sku_id = d.pop("blind_result_sku_id", UNSET)

        blind_open_time = d.pop("blind_open_time", UNSET)

        _product_type = d.pop("product_type", UNSET)
        product_type: UpdateTheBlindBoxOpeningResultsRequestBlindBatchBoxResultBlindBoxOrderLineListProductType | Unset
        if isinstance(_product_type, Unset):
            product_type = UNSET
        else:
            product_type = UpdateTheBlindBoxOpeningResultsRequestBlindBatchBoxResultBlindBoxOrderLineListProductType(
                _product_type
            )

        update_the_blind_box_opening_results_request_blind_batch_box_result_blind_box_order_line_list = cls(
            blind_result_product_id=blind_result_product_id,
            blind_result_sku_id=blind_result_sku_id,
            blind_open_time=blind_open_time,
            product_type=product_type,
        )

        update_the_blind_box_opening_results_request_blind_batch_box_result_blind_box_order_line_list.additional_properties = d
        return update_the_blind_box_opening_results_request_blind_batch_box_result_blind_box_order_line_list

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
