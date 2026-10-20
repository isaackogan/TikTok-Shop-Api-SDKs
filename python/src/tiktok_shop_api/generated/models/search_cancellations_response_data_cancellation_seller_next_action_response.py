from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchCancellationsResponseDataCancellationSellerNextActionResponse")


@_attrs_define
class SearchCancellationsResponseDataCancellationSellerNextActionResponse:
    """
    Attributes:
        action (str | Unset): **Optional.** For buyer-initiated cancellation requests that still require seller
            handling, the action value is `SELLER_RESPOND_BUYER_CANCEL`.
        deadline (int | Unset): Unix timestamp in seconds indicating the deadline for the seller to perform the next
            action.
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

        search_cancellations_response_data_cancellation_seller_next_action_response = cls(
            action=action,
            deadline=deadline,
        )

        search_cancellations_response_data_cancellation_seller_next_action_response.additional_properties = d
        return search_cancellations_response_data_cancellation_seller_next_action_response

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
