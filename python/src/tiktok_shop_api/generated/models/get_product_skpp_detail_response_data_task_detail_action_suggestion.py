from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetProductSKPPDetailResponseDataTaskDetailActionSuggestion")



@_attrs_define
class GetProductSKPPDetailResponseDataTaskDetailActionSuggestion:
    """ 
        Attributes:
            score_increase (int | Unset): SKPP points added to total_score when this action is completed; for tiered
                actions, the maximum tier.
            url (str | Unset): Link to the Seller Center page that completes the action.
     """

    score_increase: int | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        score_increase = self.score_increase

        url = self.url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if score_increase is not UNSET:
            field_dict["score_increase"] = score_increase
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        score_increase = d.pop("score_increase", UNSET)

        url = d.pop("url", UNSET)

        get_product_skpp_detail_response_data_task_detail_action_suggestion = cls(
            score_increase=score_increase,
            url=url,
        )


        get_product_skpp_detail_response_data_task_detail_action_suggestion.additional_properties = d
        return get_product_skpp_detail_response_data_task_detail_action_suggestion

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
