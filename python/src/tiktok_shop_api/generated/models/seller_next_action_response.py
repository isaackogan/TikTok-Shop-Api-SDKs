from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SellerNextActionResponse")


@_attrs_define
class SellerNextActionResponse:
    """
    Attributes:
        action (str | Unset): Seller's next action.
            Available values:
            - `SELLER_RESPOND_REFUND`
            - `SELLER_RESPOND_RETURN`
            - `SELLER_RESPOND_RECEIVE_PACKAGE`
            - `SELLER_RESPOND_REPLACEMENT`
        deadline (int | Unset): The deadline for the seller to perform the specified action, as a Unix timestamp in
            seconds.
    """

    action: str | Unset = UNSET
    deadline: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        deadline = self.deadline

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if deadline is not UNSET:
            field_dict["deadline"] = deadline

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = d.pop("action", UNSET)

        deadline = d.pop("deadline", UNSET)

        seller_next_action_response = cls(
            action=action,
            deadline=deadline,
        )

        seller_next_action_response.additional_properties = d
        return seller_next_action_response

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
