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





T = TypeVar("T", bound="ShopEligibility")



@_attrs_define
class ShopEligibility:
    """ 
        Attributes:
            is_eligible (bool | Unset): true: All applicable eligibility checks pass, including exemptions. false: A blocker
                is confirmed. Omitted if no business conclusion is available; this does not indicate a query failure or
                establish that any product is eligible.
            reasons (list[Reason] | Unset): Always returned. [] when the conclusion is true, confirmed reasons when false,
                and [] when the conclusion is undetermined.
     """

    is_eligible: bool | Unset = UNSET
    reasons: list[Reason] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.reason import Reason # noqa: PLC0415
        is_eligible = self.is_eligible

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
        if is_eligible is not UNSET:
            field_dict["is_eligible"] = is_eligible
        if reasons is not UNSET:
            field_dict["reasons"] = reasons

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reason import Reason # noqa: PLC0415
        d = dict(src_dict)
        is_eligible = d.pop("is_eligible", UNSET)

        _reasons = d.pop("reasons", UNSET)
        reasons: list[Reason] | Unset = UNSET
        if _reasons is not UNSET:
            reasons = []
            for reasons_item_data in _reasons:
                reasons_item = Reason.from_dict(reasons_item_data)



                reasons.append(reasons_item)


        shop_eligibility = cls(
            is_eligible=is_eligible,
            reasons=reasons,
        )


        shop_eligibility.additional_properties = d
        return shop_eligibility

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
