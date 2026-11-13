from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="Agreement")



@_attrs_define
class Agreement:
    """ 
        Attributes:
            is_confirmation_required (bool | Unset): Whether agreement confirmation is required before entering the
                registration flow. Omission means unknown.
            sign_status (str | Unset): The shop's agreement signing status. Omission means unknown. Signing does not
                establish that other registration conditions are met.
                The shop's campaign agreement signing status.
                - NO_SIGN_REQUIRED: Signing is not required.
                - PENDING_TO_SIGN: Awaiting signature.
                - SIGNED: Signed.
     """

    is_confirmation_required: bool | Unset = UNSET
    sign_status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        is_confirmation_required = self.is_confirmation_required

        sign_status = self.sign_status


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if is_confirmation_required is not UNSET:
            field_dict["is_confirmation_required"] = is_confirmation_required
        if sign_status is not UNSET:
            field_dict["sign_status"] = sign_status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_confirmation_required = d.pop("is_confirmation_required", UNSET)

        sign_status = d.pop("sign_status", UNSET)

        agreement = cls(
            is_confirmation_required=is_confirmation_required,
            sign_status=sign_status,
        )


        agreement.additional_properties = d
        return agreement

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
