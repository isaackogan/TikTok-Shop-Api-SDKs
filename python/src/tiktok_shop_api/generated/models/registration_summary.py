from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.registration_block_reason import RegistrationBlockReason





T = TypeVar("T", bound="RegistrationSummary")



@_attrs_define
class RegistrationSummary:
    """ 
        Attributes:
            is_eligible (bool | Unset): Whether the shop meets campaign eligibility requirements. Omitted if no definite
                conclusion is available. Does not establish final registration availability.
            registration_block_reasons (list[RegistrationBlockReason] | Unset): Confirmed registration-blocking reasons for
                the shop. [] means there are explicitly no blocking reasons; omission means unknown. An omitted message does not
                change the meaning of an existing reason code.
     """

    is_eligible: bool | Unset = UNSET
    registration_block_reasons: list[RegistrationBlockReason] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.registration_block_reason import RegistrationBlockReason # noqa: PLC0415
        is_eligible = self.is_eligible

        registration_block_reasons: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.registration_block_reasons, Unset):
            registration_block_reasons = []
            for registration_block_reasons_item_data in self.registration_block_reasons:
                registration_block_reasons_item = registration_block_reasons_item_data.to_dict()
                registration_block_reasons.append(registration_block_reasons_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if is_eligible is not UNSET:
            field_dict["is_eligible"] = is_eligible
        if registration_block_reasons is not UNSET:
            field_dict["registration_block_reasons"] = registration_block_reasons

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.registration_block_reason import RegistrationBlockReason # noqa: PLC0415
        d = dict(src_dict)
        is_eligible = d.pop("is_eligible", UNSET)

        _registration_block_reasons = d.pop("registration_block_reasons", UNSET)
        registration_block_reasons: list[RegistrationBlockReason] | Unset = UNSET
        if _registration_block_reasons is not UNSET:
            registration_block_reasons = []
            for registration_block_reasons_item_data in _registration_block_reasons:
                registration_block_reasons_item = RegistrationBlockReason.from_dict(registration_block_reasons_item_data)



                registration_block_reasons.append(registration_block_reasons_item)


        registration_summary = cls(
            is_eligible=is_eligible,
            registration_block_reasons=registration_block_reasons,
        )


        registration_summary.additional_properties = d
        return registration_summary

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
