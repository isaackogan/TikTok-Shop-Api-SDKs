from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_decision_eligibility_response_data_decision import GetDecisionEligibilityResponseDataDecision





T = TypeVar("T", bound="GetDecisionEligibilityResponseData")



@_attrs_define
class GetDecisionEligibilityResponseData:
    """ 
        Attributes:
            decisions (list[GetDecisionEligibilityResponseDataDecision] | Unset): The seller-decision eligibility results
                for the specified aftersales request.
     """

    decisions: list[GetDecisionEligibilityResponseDataDecision] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_decision_eligibility_response_data_decision import GetDecisionEligibilityResponseDataDecision # noqa: PLC0415
        decisions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.decisions, Unset):
            decisions = []
            for decisions_item_data in self.decisions:
                decisions_item = decisions_item_data.to_dict()
                decisions.append(decisions_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if decisions is not UNSET:
            field_dict["decisions"] = decisions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_decision_eligibility_response_data_decision import GetDecisionEligibilityResponseDataDecision # noqa: PLC0415
        d = dict(src_dict)
        _decisions = d.pop("decisions", UNSET)
        decisions: list[GetDecisionEligibilityResponseDataDecision] | Unset = UNSET
        if _decisions is not UNSET:
            decisions = []
            for decisions_item_data in _decisions:
                decisions_item = GetDecisionEligibilityResponseDataDecision.from_dict(decisions_item_data)



                decisions.append(decisions_item)


        get_decision_eligibility_response_data = cls(
            decisions=decisions,
        )


        get_decision_eligibility_response_data.additional_properties = d
        return get_decision_eligibility_response_data

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
