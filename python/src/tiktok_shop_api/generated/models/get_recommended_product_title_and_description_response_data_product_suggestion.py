from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_recommended_product_title_and_description_response_data_product_suggestion_item import (
        GetRecommendedProductTitleAndDescriptionResponseDataProductSuggestionItem,
    )


T = TypeVar("T", bound="GetRecommendedProductTitleAndDescriptionResponseDataProductSuggestion")


@_attrs_define
class GetRecommendedProductTitleAndDescriptionResponseDataProductSuggestion:
    """
    Attributes:
        field (str | Unset): The applicable product field.
            Possible values:
            - TITLE
            - DESCRIPTION
        items (list[GetRecommendedProductTitleAndDescriptionResponseDataProductSuggestionItem] | Unset): The list of
            optimized text.
    """

    field: str | Unset = UNSET
    items: list[GetRecommendedProductTitleAndDescriptionResponseDataProductSuggestionItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field = self.field

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field is not UNSET:
            field_dict["field"] = field
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_recommended_product_title_and_description_response_data_product_suggestion_item import (
            GetRecommendedProductTitleAndDescriptionResponseDataProductSuggestionItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        field = d.pop("field", UNSET)

        _items = d.pop("items", UNSET)
        items: list[GetRecommendedProductTitleAndDescriptionResponseDataProductSuggestionItem] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = GetRecommendedProductTitleAndDescriptionResponseDataProductSuggestionItem.from_dict(
                    items_item_data
                )

                items.append(items_item)

        get_recommended_product_title_and_description_response_data_product_suggestion = cls(
            field=field,
            items=items,
        )

        get_recommended_product_title_and_description_response_data_product_suggestion.additional_properties = d
        return get_recommended_product_title_and_description_response_data_product_suggestion

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
