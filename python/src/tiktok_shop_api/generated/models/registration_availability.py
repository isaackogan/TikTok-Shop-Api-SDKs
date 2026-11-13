from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.reason import Reason





T = TypeVar("T", bound="RegistrationAvailability")



@_attrs_define
class RegistrationAvailability:
    """ 
        Attributes:
            can_register (bool | Unset): Always returned. True when all applicable registration-period, campaign-status,
                eligibility, conflict, participation, quota, ongoing-operation, and agreement-acceptance checks have passed, are
                exempt, or do not apply. False when a registration blocker is confirmed; see reasons. A fee information dialog
                alone does not constitute an unaccepted required agreement.
            reasons (list[Reason] | Unset): Always returned. Empty when can_register is true; contains at least one
                confirmed blocker when can_register is false. Use can_register as the decision rather than inferring permission
                from an empty list. Necessary query failures return an API error.
     """

    can_register: bool | Unset = UNSET
    reasons: list[Reason] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.reason import Reason # noqa: PLC0415
        can_register = self.can_register

        reasons: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.reasons, Unset):
            reasons = []
            for reasons_item_data in self.reasons:
                reasons_item = reasons_item_data.to_dict()
                reasons.append(reasons_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if can_register is not UNSET:
            field_dict["can_register"] = can_register
        if reasons is not UNSET:
            field_dict["reasons"] = reasons

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reason import Reason # noqa: PLC0415
        d = dict(src_dict)
        can_register = d.pop("can_register", UNSET)

        _reasons = d.pop("reasons", UNSET)
        reasons: list[Reason] | Unset = UNSET
        if _reasons is not UNSET:
            reasons = []
            for reasons_item_data in _reasons:
                reasons_item = Reason.from_dict(reasons_item_data)



                reasons.append(reasons_item)


        registration_availability = cls(
            can_register=can_register,
            reasons=reasons,
        )


        registration_availability.additional_properties = d
        return registration_availability

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
