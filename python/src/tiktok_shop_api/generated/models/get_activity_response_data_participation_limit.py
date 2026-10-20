from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetActivityResponseDataParticipationLimit")


@_attrs_define
class GetActivityResponseDataParticipationLimit:
    """
    Attributes:
        type_ (str | Unset): Determines whether the promotion activity limits the number of times each buyer can receive
            its benefit. e.g.:
            - `BUYER_NO_LIMIT`: No limit for buyer​s. Buyers can benefit from this promotion across multiple orders.
            - `BUYER_LIMIT_ONLY_ONE`: Buyers can benefit from this promotion activity for no more than one order.
            ​Default: `BUYER_NO_LIMIT`
    """

    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        get_activity_response_data_participation_limit = cls(
            type_=type_,
        )

        get_activity_response_data_participation_limit.additional_properties = d
        return get_activity_response_data_participation_limit

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
