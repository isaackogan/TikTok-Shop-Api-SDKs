from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_order_customs_requirements_response_data_order_clearance_list import GetOrderCustomsRequirementsResponseDataOrderClearanceList





T = TypeVar("T", bound="GetOrderCustomsRequirementsResponseData")



@_attrs_define
class GetOrderCustomsRequirementsResponseData:
    """ 
        Attributes:
            order_clearance_list (list[GetOrderCustomsRequirementsResponseDataOrderClearanceList] | Unset): clearance info
                of this order
     """

    order_clearance_list: list[GetOrderCustomsRequirementsResponseDataOrderClearanceList] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_order_customs_requirements_response_data_order_clearance_list import GetOrderCustomsRequirementsResponseDataOrderClearanceList # noqa: PLC0415
        order_clearance_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.order_clearance_list, Unset):
            order_clearance_list = []
            for order_clearance_list_item_data in self.order_clearance_list:
                order_clearance_list_item = order_clearance_list_item_data.to_dict()
                order_clearance_list.append(order_clearance_list_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if order_clearance_list is not UNSET:
            field_dict["order_clearance_list"] = order_clearance_list

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_order_customs_requirements_response_data_order_clearance_list import GetOrderCustomsRequirementsResponseDataOrderClearanceList # noqa: PLC0415
        d = dict(src_dict)
        _order_clearance_list = d.pop("order_clearance_list", UNSET)
        order_clearance_list: list[GetOrderCustomsRequirementsResponseDataOrderClearanceList] | Unset = UNSET
        if _order_clearance_list is not UNSET:
            order_clearance_list = []
            for order_clearance_list_item_data in _order_clearance_list:
                order_clearance_list_item = GetOrderCustomsRequirementsResponseDataOrderClearanceList.from_dict(order_clearance_list_item_data)



                order_clearance_list.append(order_clearance_list_item)


        get_order_customs_requirements_response_data = cls(
            order_clearance_list=order_clearance_list,
        )


        get_order_customs_requirements_response_data.additional_properties = d
        return get_order_customs_requirements_response_data

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
