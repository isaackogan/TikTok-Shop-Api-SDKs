from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SubmitRedemptionInformationResponseDataOrderStatus")



@_attrs_define
class SubmitRedemptionInformationResponseDataOrderStatus:
    """ 
        Attributes:
            order_line_id (str | Unset): Line order id, same as the input line order id.
            status_code (int | Unset): Callback status of this line order id. A none zero code represent a failure callback.
     """

    order_line_id: str | Unset = UNSET
    status_code: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        order_line_id = self.order_line_id

        status_code = self.status_code


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if order_line_id is not UNSET:
            field_dict["order_line_id"] = order_line_id
        if status_code is not UNSET:
            field_dict["status_code"] = status_code

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order_line_id = d.pop("order_line_id", UNSET)

        status_code = d.pop("status_code", UNSET)

        submit_redemption_information_response_data_order_status = cls(
            order_line_id=order_line_id,
            status_code=status_code,
        )


        submit_redemption_information_response_data_order_status.additional_properties = d
        return submit_redemption_information_response_data_order_status

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
