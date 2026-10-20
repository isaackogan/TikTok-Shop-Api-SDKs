from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UpcomingAuthorizationExpirationWebhookData")



@_attrs_define
class UpcomingAuthorizationExpirationWebhookData:
    """ 
        Attributes:
            message (str | Unset):
            expiration_time (str | Unset):
     """

    message: str | Unset = UNSET
    expiration_time: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        message = self.message

        expiration_time = self.expiration_time


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if message is not UNSET:
            field_dict["message"] = message
        if expiration_time is not UNSET:
            field_dict["expiration_time"] = expiration_time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message", UNSET)

        expiration_time = d.pop("expiration_time", UNSET)

        upcoming_authorization_expiration_webhook_data = cls(
            message=message,
            expiration_time=expiration_time,
        )


        upcoming_authorization_expiration_webhook_data.additional_properties = d
        return upcoming_authorization_expiration_webhook_data

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
