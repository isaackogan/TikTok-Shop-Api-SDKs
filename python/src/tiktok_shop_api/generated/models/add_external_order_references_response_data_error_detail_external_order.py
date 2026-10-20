from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddExternalOrderReferencesResponseDataErrorDetailExternalOrder")


@_attrs_define
class AddExternalOrderReferencesResponseDataErrorDetailExternalOrder:
    """
    Attributes:
        id (str | Unset): The corresponding order ID in your OMS.
        platform (str | Unset): The alias of your OMS.
    """

    id: str | Unset = UNSET
    platform: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        platform = self.platform

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if platform is not UNSET:
            field_dict["platform"] = platform

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        platform = d.pop("platform", UNSET)

        add_external_order_references_response_data_error_detail_external_order = cls(
            id=id,
            platform=platform,
        )

        add_external_order_references_response_data_error_detail_external_order.additional_properties = d
        return add_external_order_references_response_data_error_detail_external_order

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
