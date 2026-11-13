from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="RegistrationBlockReason")



@_attrs_define
class RegistrationBlockReason:
    """ 
        Attributes:
            code (str | Unset): Always returned when the object exists. UNKNOWN means an unclassified blocking reason
                exists.
                Livestream campaign registration-blocking reason.
                - UNKNOWN: An unclassified registration-blocking reason exists. Must not be treated as no blocker.
                - INELIGIBLE: Campaign eligibility requirements are not met.
                - NOT_IN_DESIGNATED_SHOP: Outside the designated shop scope.
                - REGISTRATION_HAS_CLOSED: Registration has closed.
                - SHOP_NOT_ACTIVE: The shop is not operating normally.
                - NOT_IN_REGISTRATION_DATE: Outside the registration period.
                - NOT_IN_DESIGNATED_CREATOR: Outside the designated account scope. No account list or identifiers are returned.
                - NOT_ALLOW_REGISTER: Registration is explicitly prohibited by business rules.
                - NOT_ALLOW_REGISTER_ON_SELLER_APP: Registration through the seller mobile app is not supported. Does not mean
                registration is unavailable through all channels.
                - NOT_BIND_ACCOUNT_ID: The shop has no linked account.
                - ALL_BIND_ACCOUNT_NOT_ALLOW_REGISTER: None of the linked accounts meets registration requirements.
                - CAMPAIGN_DEACTIVATE: The campaign is deactivated.
                - MAX_SESSIONS_PER_ACCOUNT_REACHED: The livestream competition's per-account registration session limit has been
                reached.
            message (str | Unset): Localized reason message visible to the shop. Omitted if unavailable; never an empty
                string.
     """

    code: str | Unset = UNSET
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        message = d.pop("message", UNSET)

        registration_block_reason = cls(
            code=code,
            message=message,
        )


        registration_block_reason.additional_properties = d
        return registration_block_reason

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
