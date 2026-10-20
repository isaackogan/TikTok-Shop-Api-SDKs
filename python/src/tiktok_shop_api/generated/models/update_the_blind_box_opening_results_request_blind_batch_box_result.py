from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_the_blind_box_opening_results_request_blind_batch_box_result_blind_box_order_line_list import UpdateTheBlindBoxOpeningResultsRequestBlindBatchBoxResultBlindBoxOrderLineList





T = TypeVar("T", bound="UpdateTheBlindBoxOpeningResultsRequestBlindBatchBoxResult")



@_attrs_define
class UpdateTheBlindBoxOpeningResultsRequestBlindBatchBoxResult:
    """ 
        Attributes:
            order_line_id (str | Unset): The TikTok Shop line item ID of the blind box in the specified order to which this
                batch unboxing result belongs.
            blind_box_order_line_list (list[UpdateTheBlindBoxOpeningResultsRequestBlindBatchBoxResultBlindBoxOrderLineList]
                | Unset): Unboxing results for line items under orders. on batch box version
     """

    order_line_id: str | Unset = UNSET
    blind_box_order_line_list: list[UpdateTheBlindBoxOpeningResultsRequestBlindBatchBoxResultBlindBoxOrderLineList] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_the_blind_box_opening_results_request_blind_batch_box_result_blind_box_order_line_list import UpdateTheBlindBoxOpeningResultsRequestBlindBatchBoxResultBlindBoxOrderLineList # noqa: PLC0415
        order_line_id = self.order_line_id

        blind_box_order_line_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.blind_box_order_line_list, Unset):
            blind_box_order_line_list = []
            for blind_box_order_line_list_item_data in self.blind_box_order_line_list:
                blind_box_order_line_list_item = blind_box_order_line_list_item_data.to_dict()
                blind_box_order_line_list.append(blind_box_order_line_list_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if order_line_id is not UNSET:
            field_dict["order_line_id"] = order_line_id
        if blind_box_order_line_list is not UNSET:
            field_dict["blind_box_order_line_list"] = blind_box_order_line_list

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_the_blind_box_opening_results_request_blind_batch_box_result_blind_box_order_line_list import UpdateTheBlindBoxOpeningResultsRequestBlindBatchBoxResultBlindBoxOrderLineList # noqa: PLC0415
        d = dict(src_dict)
        order_line_id = d.pop("order_line_id", UNSET)

        _blind_box_order_line_list = d.pop("blind_box_order_line_list", UNSET)
        blind_box_order_line_list: list[UpdateTheBlindBoxOpeningResultsRequestBlindBatchBoxResultBlindBoxOrderLineList] | Unset = UNSET
        if _blind_box_order_line_list is not UNSET:
            blind_box_order_line_list = []
            for blind_box_order_line_list_item_data in _blind_box_order_line_list:
                blind_box_order_line_list_item = UpdateTheBlindBoxOpeningResultsRequestBlindBatchBoxResultBlindBoxOrderLineList.from_dict(blind_box_order_line_list_item_data)



                blind_box_order_line_list.append(blind_box_order_line_list_item)


        update_the_blind_box_opening_results_request_blind_batch_box_result = cls(
            order_line_id=order_line_id,
            blind_box_order_line_list=blind_box_order_line_list,
        )


        update_the_blind_box_opening_results_request_blind_batch_box_result.additional_properties = d
        return update_the_blind_box_opening_results_request_blind_batch_box_result

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
