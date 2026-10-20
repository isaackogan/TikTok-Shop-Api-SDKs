from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SendEngagementMessageResponseDataErrorDetail")



@_attrs_define
class SendEngagementMessageResponseDataErrorDetail:
    """ 
        Attributes:
            buyer_email (str | Unset): The anonymized buyer email address associated with the error.
     """

    buyer_email: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        buyer_email = self.buyer_email


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if buyer_email is not UNSET:
            field_dict["buyer_email"] = buyer_email

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        buyer_email = d.pop("buyer_email", UNSET)

        send_engagement_message_response_data_error_detail = cls(
            buyer_email=buyer_email,
        )


        send_engagement_message_response_data_error_detail.additional_properties = d
        return send_engagement_message_response_data_error_detail

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
