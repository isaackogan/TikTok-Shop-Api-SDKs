from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.submit_customs_clearance_information_request_order_list import SubmitCustomsClearanceInformationRequestOrderList





T = TypeVar("T", bound="SubmitCustomsClearanceInformationRequest")



@_attrs_define
class SubmitCustomsClearanceInformationRequest:
    """ 
        Attributes:
            order_list (list[SubmitCustomsClearanceInformationRequestOrderList] | Unset): List of orders for which to submit
                customs clearance information. Maximum: 100 orders per request.
     """

    order_list: list[SubmitCustomsClearanceInformationRequestOrderList] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.submit_customs_clearance_information_request_order_list import SubmitCustomsClearanceInformationRequestOrderList # noqa: PLC0415
        order_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.order_list, Unset):
            order_list = []
            for order_list_item_data in self.order_list:
                order_list_item = order_list_item_data.to_dict()
                order_list.append(order_list_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if order_list is not UNSET:
            field_dict["order_list"] = order_list

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.submit_customs_clearance_information_request_order_list import SubmitCustomsClearanceInformationRequestOrderList # noqa: PLC0415
        d = dict(src_dict)
        _order_list = d.pop("order_list", UNSET)
        order_list: list[SubmitCustomsClearanceInformationRequestOrderList] | Unset = UNSET
        if _order_list is not UNSET:
            order_list = []
            for order_list_item_data in _order_list:
                order_list_item = SubmitCustomsClearanceInformationRequestOrderList.from_dict(order_list_item_data)



                order_list.append(order_list_item)


        submit_customs_clearance_information_request = cls(
            order_list=order_list,
        )


        submit_customs_clearance_information_request.additional_properties = d
        return submit_customs_clearance_information_request

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
