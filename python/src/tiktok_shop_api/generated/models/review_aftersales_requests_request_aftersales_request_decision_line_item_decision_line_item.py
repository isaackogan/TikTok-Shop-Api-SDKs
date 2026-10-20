from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ReviewAftersalesRequestsRequestAftersalesRequestDecisionLineItemDecisionLineItem")



@_attrs_define
class ReviewAftersalesRequestsRequestAftersalesRequestDecisionLineItemDecisionLineItem:
    """ 
        Attributes:
            return_line_item_id (str): Unique identifier for this item in the return. In the case of virtual bundle, this
                corresponds to the id of the original parent item bundle.
            sub_return_line_item_id (str | Unset): Unique identifier for this item in the return. In the case of virtual
                bundle, this corresponds to the id of the current child item being returned.
     """

    return_line_item_id: str
    sub_return_line_item_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        return_line_item_id = self.return_line_item_id

        sub_return_line_item_id = self.sub_return_line_item_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "return_line_item_id": return_line_item_id,
        })
        if sub_return_line_item_id is not UNSET:
            field_dict["sub_return_line_item_id"] = sub_return_line_item_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        return_line_item_id = d.pop("return_line_item_id")

        sub_return_line_item_id = d.pop("sub_return_line_item_id", UNSET)

        review_aftersales_requests_request_aftersales_request_decision_line_item_decision_line_item = cls(
            return_line_item_id=return_line_item_id,
            sub_return_line_item_id=sub_return_line_item_id,
        )


        review_aftersales_requests_request_aftersales_request_decision_line_item_decision_line_item.additional_properties = d
        return review_aftersales_requests_request_aftersales_request_decision_line_item_decision_line_item

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
