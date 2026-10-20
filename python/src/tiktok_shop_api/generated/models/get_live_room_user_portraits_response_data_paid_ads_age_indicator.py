from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetLiveRoomUserPortraitsResponseDataPaidAdsAgeIndicator")



@_attrs_define
class GetLiveRoomUserPortraitsResponseDataPaidAdsAgeIndicator:
    """ 
        Attributes:
            type_ (str | Unset): The type of paid advertisement age indicator.
                USER_PORTRAIT_AGE_LESS_THAN_15: Users whose age is less than 15.
                USER_PORTRAIT_AGE_MORE_THAN_34: Users whose age is more than 34.
                USER_PORTRAIT_AGE_MORE_THAN_55: Users whose age is more than 55.
                USER_PORTRAIT_AGE_13_TO_17: Users whose age is between 13 and 17.
                USER_PORTRAIT_AGE_15_TO_17: Users whose age is between 15 and 17.
                USER_PORTRAIT_AGE_18_TO_24: Users whose age is between 18 and 24.
                USER_PORTRAIT_AGE_25_TO_34: Users whose age is between 25 and 34.
                USER_PORTRAIT_AGE_35_TO_44: Users whose age is between 35 and 44.
                USER_PORTRAIT_AGE_45_TO_54: Users whose age is between 45 and 54.
            value (str | Unset): The count for the corresponding paid-advertising age indicator.
     """

    type_: str | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        value = self.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        value = d.pop("value", UNSET)

        get_live_room_user_portraits_response_data_paid_ads_age_indicator = cls(
            type_=type_,
            value=value,
        )


        get_live_room_user_portraits_response_data_paid_ads_age_indicator.additional_properties = d
        return get_live_room_user_portraits_response_data_paid_ads_age_indicator

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
