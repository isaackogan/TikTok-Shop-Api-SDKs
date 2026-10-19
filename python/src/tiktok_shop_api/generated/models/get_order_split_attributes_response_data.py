from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_order_split_attributes_response_data_split_attribute import (
        GetOrderSplitAttributesResponseDataSplitAttribute,
    )


T = TypeVar("T", bound="GetOrderSplitAttributesResponseData")


@_attrs_define
class GetOrderSplitAttributesResponseData:
    """
    Attributes:
        split_attributes (list[GetOrderSplitAttributesResponseDataSplitAttribute] | Unset): Split-eligibility results
            for the evaluated TikTok Shop orders. Each result identifies an order and indicates whether it can be split; it
            may also include a reason when splitting is not allowed and mandatory package-splitting limits when applicable.
    """

    split_attributes: list[GetOrderSplitAttributesResponseDataSplitAttribute] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        split_attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.split_attributes, Unset):
            split_attributes = []
            for split_attributes_item_data in self.split_attributes:
                split_attributes_item = split_attributes_item_data.to_dict()
                split_attributes.append(split_attributes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if split_attributes is not UNSET:
            field_dict["split_attributes"] = split_attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_order_split_attributes_response_data_split_attribute import (
            GetOrderSplitAttributesResponseDataSplitAttribute,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _split_attributes = d.pop("split_attributes", UNSET)
        split_attributes: list[GetOrderSplitAttributesResponseDataSplitAttribute] | Unset = UNSET
        if _split_attributes is not UNSET:
            split_attributes = []
            for split_attributes_item_data in _split_attributes:
                split_attributes_item = GetOrderSplitAttributesResponseDataSplitAttribute.from_dict(
                    split_attributes_item_data
                )

                split_attributes.append(split_attributes_item)

        get_order_split_attributes_response_data = cls(
            split_attributes=split_attributes,
        )

        get_order_split_attributes_response_data.additional_properties = d
        return get_order_split_attributes_response_data

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
