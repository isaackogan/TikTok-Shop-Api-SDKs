from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.confirm_order_split_request_splittable_groups_v2_order_line_list import ConfirmOrderSplitRequestSplittableGroupsV2OrderLineList





T = TypeVar("T", bound="ConfirmOrderSplitRequestSplittableGroupsV2")



@_attrs_define
class ConfirmOrderSplitRequestSplittableGroupsV2:
    """ 
        Attributes:
            id (str | Unset): A developer-defined identifier for this split group. The response returns the same value in
                `splittable_group_id` to correlate the group with its newly created package.
            order_line_list (list[ConfirmOrderSplitRequestSplittableGroupsV2OrderLineList] | Unset): This new parameter is
                completely backward compatible with the previous oder_line_items_ids field and in addition this supports bundle
                order splitting, use the sub items accordingly
     """

    id: str | Unset = UNSET
    order_line_list: list[ConfirmOrderSplitRequestSplittableGroupsV2OrderLineList] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.confirm_order_split_request_splittable_groups_v2_order_line_list import ConfirmOrderSplitRequestSplittableGroupsV2OrderLineList # noqa: PLC0415
        id = self.id

        order_line_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.order_line_list, Unset):
            order_line_list = []
            for order_line_list_item_data in self.order_line_list:
                order_line_list_item = order_line_list_item_data.to_dict()
                order_line_list.append(order_line_list_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if order_line_list is not UNSET:
            field_dict["order_line_list"] = order_line_list

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.confirm_order_split_request_splittable_groups_v2_order_line_list import ConfirmOrderSplitRequestSplittableGroupsV2OrderLineList # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _order_line_list = d.pop("order_line_list", UNSET)
        order_line_list: list[ConfirmOrderSplitRequestSplittableGroupsV2OrderLineList] | Unset = UNSET
        if _order_line_list is not UNSET:
            order_line_list = []
            for order_line_list_item_data in _order_line_list:
                order_line_list_item = ConfirmOrderSplitRequestSplittableGroupsV2OrderLineList.from_dict(order_line_list_item_data)



                order_line_list.append(order_line_list_item)


        confirm_order_split_request_splittable_groups_v2 = cls(
            id=id,
            order_line_list=order_line_list,
        )


        confirm_order_split_request_splittable_groups_v2.additional_properties = d
        return confirm_order_split_request_splittable_groups_v2

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
