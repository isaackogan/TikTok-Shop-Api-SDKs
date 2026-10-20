from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateTargetCollaborationResponseDataUpdateFailedAddProduct")


@_attrs_define
class UpdateTargetCollaborationResponseDataUpdateFailedAddProduct:
    """
    Attributes:
        id (str | Unset): The product identifier.
        commission_rate (int | Unset): The desired commission rate for the target collaboration. The desired commission
            rate is expressed in hundredths of a percent. For example, 3587 is a commission rate of 35.87%. This value must
            be a minimum of 1000.
    """

    id: str | Unset = UNSET
    commission_rate: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        commission_rate = self.commission_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if commission_rate is not UNSET:
            field_dict["commission_rate"] = commission_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        commission_rate = d.pop("commission_rate", UNSET)

        update_target_collaboration_response_data_update_failed_add_product = cls(
            id=id,
            commission_rate=commission_rate,
        )

        update_target_collaboration_response_data_update_failed_add_product.additional_properties = d
        return update_target_collaboration_response_data_update_failed_add_product

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
