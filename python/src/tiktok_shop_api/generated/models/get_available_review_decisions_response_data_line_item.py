from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_available_review_decisions_response_data_line_item_decision import GetAvailableReviewDecisionsResponseDataLineItemDecision





T = TypeVar("T", bound="GetAvailableReviewDecisionsResponseDataLineItem")



@_attrs_define
class GetAvailableReviewDecisionsResponseDataLineItem:
    """ 
        Attributes:
            return_line_item_id (str | Unset): Unique identifier for this item in the return. In the case of virtual bundle,
                this corresponds to the id of the original parent item bundle.
            sub_return_line_item_id (str | Unset): Unique identifier for this item in the return. In the case of virtual
                bundle, this corresponds to the id of the current child item being returned.
            decisions (list[GetAvailableReviewDecisionsResponseDataLineItemDecision] | Unset): The list of candidate review
                decisions for this line item.
     """

    return_line_item_id: str | Unset = UNSET
    sub_return_line_item_id: str | Unset = UNSET
    decisions: list[GetAvailableReviewDecisionsResponseDataLineItemDecision] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_available_review_decisions_response_data_line_item_decision import GetAvailableReviewDecisionsResponseDataLineItemDecision # noqa: PLC0415
        return_line_item_id = self.return_line_item_id

        sub_return_line_item_id = self.sub_return_line_item_id

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
        if return_line_item_id is not UNSET:
            field_dict["return_line_item_id"] = return_line_item_id
        if sub_return_line_item_id is not UNSET:
            field_dict["sub_return_line_item_id"] = sub_return_line_item_id
        if decisions is not UNSET:
            field_dict["decisions"] = decisions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_available_review_decisions_response_data_line_item_decision import GetAvailableReviewDecisionsResponseDataLineItemDecision # noqa: PLC0415
        d = dict(src_dict)
        return_line_item_id = d.pop("return_line_item_id", UNSET)

        sub_return_line_item_id = d.pop("sub_return_line_item_id", UNSET)

        _decisions = d.pop("decisions", UNSET)
        decisions: list[GetAvailableReviewDecisionsResponseDataLineItemDecision] | Unset = UNSET
        if _decisions is not UNSET:
            decisions = []
            for decisions_item_data in _decisions:
                decisions_item = GetAvailableReviewDecisionsResponseDataLineItemDecision.from_dict(decisions_item_data)



                decisions.append(decisions_item)


        get_available_review_decisions_response_data_line_item = cls(
            return_line_item_id=return_line_item_id,
            sub_return_line_item_id=sub_return_line_item_id,
            decisions=decisions,
        )


        get_available_review_decisions_response_data_line_item.additional_properties = d
        return get_available_review_decisions_response_data_line_item

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
