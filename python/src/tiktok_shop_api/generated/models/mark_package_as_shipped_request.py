from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.confirm_order_split_request_splittable_groups_v2_order_line_list import (
        ConfirmOrderSplitRequestSplittableGroupsV2OrderLineList,
    )
    from ..models.shipping_info_list import ShippingInfoList


T = TypeVar("T", bound="MarkPackageAsShippedRequest")


@_attrs_define
class MarkPackageAsShippedRequest:
    """
    Attributes:
        order_line_list (list[ConfirmOrderSplitRequestSplittableGroupsV2OrderLineList] | Unset): This new parameter is
            completely backward compatible with the previous oder_line_items_ids field and in addition this supports bundle
            order splitting, use the sub items accordingly
        shipping_info_list (list[ShippingInfoList] | Unset): "Only supports uploading multiple tracking numbers for
            split-shipment in 3PL single item scenarios (non-virtual bundle) (This function is only support for whitelist
            sellers； If you are not on the allowlist, it is recommended to contact AM to apply)
            For other scenarios, only one tracking number can be uploaded at a time."
    """

    order_line_list: list[ConfirmOrderSplitRequestSplittableGroupsV2OrderLineList] | Unset = UNSET
    shipping_info_list: list[ShippingInfoList] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_line_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.order_line_list, Unset):
            order_line_list = []
            for order_line_list_item_data in self.order_line_list:
                order_line_list_item = order_line_list_item_data.to_dict()
                order_line_list.append(order_line_list_item)

        shipping_info_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.shipping_info_list, Unset):
            shipping_info_list = []
            for shipping_info_list_item_data in self.shipping_info_list:
                shipping_info_list_item = shipping_info_list_item_data.to_dict()
                shipping_info_list.append(shipping_info_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_line_list is not UNSET:
            field_dict["order_line_list"] = order_line_list
        if shipping_info_list is not UNSET:
            field_dict["shipping_info_list"] = shipping_info_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.confirm_order_split_request_splittable_groups_v2_order_line_list import (
            ConfirmOrderSplitRequestSplittableGroupsV2OrderLineList,  # noqa: PLC0415
        )
        from ..models.shipping_info_list import ShippingInfoList  # noqa: PLC0415

        d = dict(src_dict)
        _order_line_list = d.pop("order_line_list", UNSET)
        order_line_list: list[ConfirmOrderSplitRequestSplittableGroupsV2OrderLineList] | Unset = UNSET
        if _order_line_list is not UNSET:
            order_line_list = []
            for order_line_list_item_data in _order_line_list:
                order_line_list_item = ConfirmOrderSplitRequestSplittableGroupsV2OrderLineList.from_dict(
                    order_line_list_item_data
                )

                order_line_list.append(order_line_list_item)

        _shipping_info_list = d.pop("shipping_info_list", UNSET)
        shipping_info_list: list[ShippingInfoList] | Unset = UNSET
        if _shipping_info_list is not UNSET:
            shipping_info_list = []
            for shipping_info_list_item_data in _shipping_info_list:
                shipping_info_list_item = ShippingInfoList.from_dict(shipping_info_list_item_data)

                shipping_info_list.append(shipping_info_list_item)

        mark_package_as_shipped_request = cls(
            order_line_list=order_line_list,
            shipping_info_list=shipping_info_list,
        )

        mark_package_as_shipped_request.additional_properties = d
        return mark_package_as_shipped_request

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
