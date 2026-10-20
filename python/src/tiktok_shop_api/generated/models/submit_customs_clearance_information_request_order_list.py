from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.submit_customs_clearance_information_request_order_list_item_list import SubmitCustomsClearanceInformationRequestOrderListItemList





T = TypeVar("T", bound="SubmitCustomsClearanceInformationRequestOrderList")



@_attrs_define
class SubmitCustomsClearanceInformationRequestOrderList:
    """ 
        Attributes:
            order_id (str): TikTok Shop order ID
            item_list (list[SubmitCustomsClearanceInformationRequestOrderListItemList] | Unset): List of customs clearance
                entries for order lines. Within the same order, explicit order_line_id values must be unique.
     """

    order_id: str
    item_list: list[SubmitCustomsClearanceInformationRequestOrderListItemList] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.submit_customs_clearance_information_request_order_list_item_list import SubmitCustomsClearanceInformationRequestOrderListItemList # noqa: PLC0415
        order_id = self.order_id

        item_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.item_list, Unset):
            item_list = []
            for item_list_item_data in self.item_list:
                item_list_item = item_list_item_data.to_dict()
                item_list.append(item_list_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "order_id": order_id,
        })
        if item_list is not UNSET:
            field_dict["item_list"] = item_list

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.submit_customs_clearance_information_request_order_list_item_list import SubmitCustomsClearanceInformationRequestOrderListItemList # noqa: PLC0415
        d = dict(src_dict)
        order_id = d.pop("order_id")

        _item_list = d.pop("item_list", UNSET)
        item_list: list[SubmitCustomsClearanceInformationRequestOrderListItemList] | Unset = UNSET
        if _item_list is not UNSET:
            item_list = []
            for item_list_item_data in _item_list:
                item_list_item = SubmitCustomsClearanceInformationRequestOrderListItemList.from_dict(item_list_item_data)



                item_list.append(item_list_item)


        submit_customs_clearance_information_request_order_list = cls(
            order_id=order_id,
            item_list=item_list,
        )


        submit_customs_clearance_information_request_order_list.additional_properties = d
        return submit_customs_clearance_information_request_order_list

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
