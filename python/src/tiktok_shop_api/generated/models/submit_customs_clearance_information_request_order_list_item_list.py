from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.submit_customs_clearance_information_request_order_list_item_list_item_detail import (
        SubmitCustomsClearanceInformationRequestOrderListItemListItemDetail,
    )


T = TypeVar("T", bound="SubmitCustomsClearanceInformationRequestOrderListItemList")


@_attrs_define
class SubmitCustomsClearanceInformationRequestOrderListItemList:
    """
    Attributes:
        order_line_id (str | Unset): Sub order ID; order_line_id and sku_id should not be both empty.
        sku_id (str | Unset): SKU ID; order_line_id and sku_id should not be both empty.
        item_detail (list[SubmitCustomsClearanceInformationRequestOrderListItemListItemDetail] | Unset): List of SKU-
            level customs clearance details for the order line.
    """

    order_line_id: str | Unset = UNSET
    sku_id: str | Unset = UNSET
    item_detail: list[SubmitCustomsClearanceInformationRequestOrderListItemListItemDetail] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_line_id = self.order_line_id

        sku_id = self.sku_id

        item_detail: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.item_detail, Unset):
            item_detail = []
            for item_detail_item_data in self.item_detail:
                item_detail_item = item_detail_item_data.to_dict()
                item_detail.append(item_detail_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_line_id is not UNSET:
            field_dict["order_line_id"] = order_line_id
        if sku_id is not UNSET:
            field_dict["sku_id"] = sku_id
        if item_detail is not UNSET:
            field_dict["item_detail"] = item_detail

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.submit_customs_clearance_information_request_order_list_item_list_item_detail import (
            SubmitCustomsClearanceInformationRequestOrderListItemListItemDetail,  # noqa: PLC0415
        )

        d = dict(src_dict)
        order_line_id = d.pop("order_line_id", UNSET)

        sku_id = d.pop("sku_id", UNSET)

        _item_detail = d.pop("item_detail", UNSET)
        item_detail: list[SubmitCustomsClearanceInformationRequestOrderListItemListItemDetail] | Unset = UNSET
        if _item_detail is not UNSET:
            item_detail = []
            for item_detail_item_data in _item_detail:
                item_detail_item = SubmitCustomsClearanceInformationRequestOrderListItemListItemDetail.from_dict(
                    item_detail_item_data
                )

                item_detail.append(item_detail_item)

        submit_customs_clearance_information_request_order_list_item_list = cls(
            order_line_id=order_line_id,
            sku_id=sku_id,
            item_detail=item_detail,
        )

        submit_customs_clearance_information_request_order_list_item_list.additional_properties = d
        return submit_customs_clearance_information_request_order_list_item_list

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
