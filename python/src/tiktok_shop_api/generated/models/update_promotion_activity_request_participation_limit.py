from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdatePromotionActivityRequestParticipationLimit")


@_attrs_define
class UpdatePromotionActivityRequestParticipationLimit:
    """
    Attributes:
        type_ (str): Determines whether the promotion limits how many orders each buyer can receive the benefit from.
            - `BUYER_NO_LIMIT`: Buyers can receive the benefit across multiple orders.
            - `BUYER_LIMIT_ONLY_ONE`: Each buyer can receive the benefit for no more than one order.
    """

    type_: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        update_promotion_activity_request_participation_limit = cls(
            type_=type_,
        )

        update_promotion_activity_request_participation_limit.additional_properties = d
        return update_promotion_activity_request_participation_limit

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
