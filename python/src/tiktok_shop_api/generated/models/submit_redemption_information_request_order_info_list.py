from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.submit_redemption_information_request_order_info_list_redeem_info import SubmitRedemptionInformationRequestOrderInfoListRedeemInfo





T = TypeVar("T", bound="SubmitRedemptionInformationRequestOrderInfoList")



@_attrs_define
class SubmitRedemptionInformationRequestOrderInfoList:
    """ 
        Attributes:
            order_line_id (str): The unique identifier of the order line item.
            redeem_info (SubmitRedemptionInformationRequestOrderInfoListRedeemInfo):
            source_unique_id (str | Unset): Optional, a unique id related to the order line in the caller system
     """

    order_line_id: str
    redeem_info: SubmitRedemptionInformationRequestOrderInfoListRedeemInfo
    source_unique_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.submit_redemption_information_request_order_info_list_redeem_info import SubmitRedemptionInformationRequestOrderInfoListRedeemInfo # noqa: PLC0415
        order_line_id = self.order_line_id

        redeem_info = self.redeem_info.to_dict()

        source_unique_id = self.source_unique_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "order_line_id": order_line_id,
            "redeem_info": redeem_info,
        })
        if source_unique_id is not UNSET:
            field_dict["source_unique_id"] = source_unique_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.submit_redemption_information_request_order_info_list_redeem_info import SubmitRedemptionInformationRequestOrderInfoListRedeemInfo # noqa: PLC0415
        d = dict(src_dict)
        order_line_id = d.pop("order_line_id")

        redeem_info = SubmitRedemptionInformationRequestOrderInfoListRedeemInfo.from_dict(d.pop("redeem_info"))




        source_unique_id = d.pop("source_unique_id", UNSET)

        submit_redemption_information_request_order_info_list = cls(
            order_line_id=order_line_id,
            redeem_info=redeem_info,
            source_unique_id=source_unique_id,
        )


        submit_redemption_information_request_order_info_list.additional_properties = d
        return submit_redemption_information_request_order_info_list

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
