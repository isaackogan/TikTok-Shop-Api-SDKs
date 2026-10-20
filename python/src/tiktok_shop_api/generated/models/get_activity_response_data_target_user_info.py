from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetActivityResponseDataTargetUserInfo")


@_attrs_define
class GetActivityResponseDataTargetUserInfo:
    """
    Attributes:
        user_type (str | Unset): The targeted user type.
            Possible values:
            - `ALL_USER`
            - `SHOP_NEW_CUSTOMER`
            - `SHOP_EXISTING_CUSTOMER`
            - `SHOP_REPEAT_CUSTOMER`
            - `SHOP_ABANDONED_CHECKOUTS_CUSTOMER`
    """

    user_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_type = self.user_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_type is not UNSET:
            field_dict["user_type"] = user_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_type = d.pop("user_type", UNSET)

        get_activity_response_data_target_user_info = cls(
            user_type=user_type,
        )

        get_activity_response_data_target_user_info.additional_properties = d
        return get_activity_response_data_target_user_info

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
