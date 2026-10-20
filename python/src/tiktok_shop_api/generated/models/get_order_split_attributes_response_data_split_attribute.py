from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_order_split_attributes_response_data_split_attribute_must_split_reason import GetOrderSplitAttributesResponseDataSplitAttributeMustSplitReason





T = TypeVar("T", bound="GetOrderSplitAttributesResponseDataSplitAttribute")



@_attrs_define
class GetOrderSplitAttributesResponseDataSplitAttribute:
    """ 
        Attributes:
            order_id (str | Unset): TikTok Shop order ID.
            can_split (bool | Unset): Whether an order can be split:
                - `true`: The order can be split into multiple packages.
                - `false`: The order cannot be split into multiple packages.
            reason (str | Unset): The reason why the order cannot be split. Only return this field when `can_split = false`.
            must_split (bool | Unset): Whether an order must be split:
                - true: The order must be split into multiple packages.
                - false: The order does not have to be split into multiple packages.
            must_split_reasons (list[GetOrderSplitAttributesResponseDataSplitAttributeMustSplitReason] | Unset): The reason
                why the order must be split. Only return this field when must_split = true.
     """

    order_id: str | Unset = UNSET
    can_split: bool | Unset = UNSET
    reason: str | Unset = UNSET
    must_split: bool | Unset = UNSET
    must_split_reasons: list[GetOrderSplitAttributesResponseDataSplitAttributeMustSplitReason] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_order_split_attributes_response_data_split_attribute_must_split_reason import GetOrderSplitAttributesResponseDataSplitAttributeMustSplitReason # noqa: PLC0415
        order_id = self.order_id

        can_split = self.can_split

        reason = self.reason

        must_split = self.must_split

        must_split_reasons: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.must_split_reasons, Unset):
            must_split_reasons = []
            for must_split_reasons_item_data in self.must_split_reasons:
                must_split_reasons_item = must_split_reasons_item_data.to_dict()
                must_split_reasons.append(must_split_reasons_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if can_split is not UNSET:
            field_dict["can_split"] = can_split
        if reason is not UNSET:
            field_dict["reason"] = reason
        if must_split is not UNSET:
            field_dict["must_split"] = must_split
        if must_split_reasons is not UNSET:
            field_dict["must_split_reasons"] = must_split_reasons

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_order_split_attributes_response_data_split_attribute_must_split_reason import GetOrderSplitAttributesResponseDataSplitAttributeMustSplitReason # noqa: PLC0415
        d = dict(src_dict)
        order_id = d.pop("order_id", UNSET)

        can_split = d.pop("can_split", UNSET)

        reason = d.pop("reason", UNSET)

        must_split = d.pop("must_split", UNSET)

        _must_split_reasons = d.pop("must_split_reasons", UNSET)
        must_split_reasons: list[GetOrderSplitAttributesResponseDataSplitAttributeMustSplitReason] | Unset = UNSET
        if _must_split_reasons is not UNSET:
            must_split_reasons = []
            for must_split_reasons_item_data in _must_split_reasons:
                must_split_reasons_item = GetOrderSplitAttributesResponseDataSplitAttributeMustSplitReason.from_dict(must_split_reasons_item_data)



                must_split_reasons.append(must_split_reasons_item)


        get_order_split_attributes_response_data_split_attribute = cls(
            order_id=order_id,
            can_split=can_split,
            reason=reason,
            must_split=must_split,
            must_split_reasons=must_split_reasons,
        )


        get_order_split_attributes_response_data_split_attribute.additional_properties = d
        return get_order_split_attributes_response_data_split_attribute

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
