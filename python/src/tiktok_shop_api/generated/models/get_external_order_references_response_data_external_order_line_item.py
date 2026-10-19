from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetExternalOrderReferencesResponseDataExternalOrderLineItem")


@_attrs_define
class GetExternalOrderReferencesResponseDataExternalOrderLineItem:
    """
    Attributes:
        id (str | Unset): Line item ID in your OMS.
        origin_id (str | Unset): Line item ID in TikTok Shop.
    """

    id: str | Unset = UNSET
    origin_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        origin_id = self.origin_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if origin_id is not UNSET:
            field_dict["origin_id"] = origin_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        origin_id = d.pop("origin_id", UNSET)

        get_external_order_references_response_data_external_order_line_item = cls(
            id=id,
            origin_id=origin_id,
        )

        get_external_order_references_response_data_external_order_line_item.additional_properties = d
        return get_external_order_references_response_data_external_order_line_item

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
