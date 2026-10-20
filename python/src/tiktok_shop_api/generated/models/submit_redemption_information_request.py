from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.submit_redemption_information_request_order_info_list import (
        SubmitRedemptionInformationRequestOrderInfoList,
    )


T = TypeVar("T", bound="SubmitRedemptionInformationRequest")


@_attrs_define
class SubmitRedemptionInformationRequest:
    """
    Attributes:
        order_id (str): TikTok Shop order ID.
        order_info_list (list[SubmitRedemptionInformationRequestOrderInfoList]): Order line items for which to submit
            redemption information. Include at least one item. Each `order_line_id` must belong to the order specified by
            `order_id` and must appear only once in the list.
    """

    order_id: str
    order_info_list: list[SubmitRedemptionInformationRequestOrderInfoList]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_id = self.order_id

        order_info_list = []
        for order_info_list_item_data in self.order_info_list:
            order_info_list_item = order_info_list_item_data.to_dict()
            order_info_list.append(order_info_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "order_id": order_id,
                "order_info_list": order_info_list,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.submit_redemption_information_request_order_info_list import (
            SubmitRedemptionInformationRequestOrderInfoList,  # noqa: PLC0415
        )

        d = dict(src_dict)
        order_id = d.pop("order_id")

        order_info_list = []
        _order_info_list = d.pop("order_info_list")
        for order_info_list_item_data in _order_info_list:
            order_info_list_item = SubmitRedemptionInformationRequestOrderInfoList.from_dict(order_info_list_item_data)

            order_info_list.append(order_info_list_item)

        submit_redemption_information_request = cls(
            order_id=order_id,
            order_info_list=order_info_list,
        )

        submit_redemption_information_request.additional_properties = d
        return submit_redemption_information_request

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
