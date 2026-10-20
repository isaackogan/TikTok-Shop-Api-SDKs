from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_product_skpp_detail_response_data_task_detail_action_suggestion import GetProductSKPPDetailResponseDataTaskDetailActionSuggestion





T = TypeVar("T", bound="GetProductSKPPDetailResponseDataTaskDetail")



@_attrs_define
class GetProductSKPPDetailResponseDataTaskDetail:
    """ 
        Attributes:
            category (str | Unset): Key for the scoring category.
                Possible values:
                - COMMISSION_RATE
                - FULFILMENT
                - PRICING
                - FREE_SHIPING
                - FOLLOWER_BENEFITS
                - SAMPLING
                - ADS_SPEND
                - STOCK
                - SHOPPABLE_VIDEOS
                - INFORMATION_QUALITY
                - CRM_HOSTING
            name (str | Unset): Localized category name, resolved from category via the shared content by the request
                locale.
            current_value (str | Unset): Current value of this dimension's metric (e.g. current price, commission rate,
                free-shipping status).
            target_value (str | Unset): The threshold this dimension must reach to pass. It uses the same unit as
                `current_value` and may include a leading comparison operator, such as `≥` or `≤`, to show the required
                direction.
            passed (bool | Unset): Whether this dimension meets its target_value.
            action_suggestions (list[GetProductSKPPDetailResponseDataTaskDetailActionSuggestion] | Unset): Suggested actions
                to complete this task; returned only when passed = false. A task may have multiple suggestions.
     """

    category: str | Unset = UNSET
    name: str | Unset = UNSET
    current_value: str | Unset = UNSET
    target_value: str | Unset = UNSET
    passed: bool | Unset = UNSET
    action_suggestions: list[GetProductSKPPDetailResponseDataTaskDetailActionSuggestion] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_product_skpp_detail_response_data_task_detail_action_suggestion import GetProductSKPPDetailResponseDataTaskDetailActionSuggestion # noqa: PLC0415
        category = self.category

        name = self.name

        current_value = self.current_value

        target_value = self.target_value

        passed = self.passed

        action_suggestions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.action_suggestions, Unset):
            action_suggestions = []
            for action_suggestions_item_data in self.action_suggestions:
                action_suggestions_item = action_suggestions_item_data.to_dict()
                action_suggestions.append(action_suggestions_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if category is not UNSET:
            field_dict["category"] = category
        if name is not UNSET:
            field_dict["name"] = name
        if current_value is not UNSET:
            field_dict["current_value"] = current_value
        if target_value is not UNSET:
            field_dict["target_value"] = target_value
        if passed is not UNSET:
            field_dict["passed"] = passed
        if action_suggestions is not UNSET:
            field_dict["action_suggestions"] = action_suggestions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_product_skpp_detail_response_data_task_detail_action_suggestion import GetProductSKPPDetailResponseDataTaskDetailActionSuggestion # noqa: PLC0415
        d = dict(src_dict)
        category = d.pop("category", UNSET)

        name = d.pop("name", UNSET)

        current_value = d.pop("current_value", UNSET)

        target_value = d.pop("target_value", UNSET)

        passed = d.pop("passed", UNSET)

        _action_suggestions = d.pop("action_suggestions", UNSET)
        action_suggestions: list[GetProductSKPPDetailResponseDataTaskDetailActionSuggestion] | Unset = UNSET
        if _action_suggestions is not UNSET:
            action_suggestions = []
            for action_suggestions_item_data in _action_suggestions:
                action_suggestions_item = GetProductSKPPDetailResponseDataTaskDetailActionSuggestion.from_dict(action_suggestions_item_data)



                action_suggestions.append(action_suggestions_item)


        get_product_skpp_detail_response_data_task_detail = cls(
            category=category,
            name=name,
            current_value=current_value,
            target_value=target_value,
            passed=passed,
            action_suggestions=action_suggestions,
        )


        get_product_skpp_detail_response_data_task_detail.additional_properties = d
        return get_product_skpp_detail_response_data_task_detail

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
