from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_recommended_product_title_and_description_response_data_product_suggestion import GetRecommendedProductTitleAndDescriptionResponseDataProductSuggestion





T = TypeVar("T", bound="GetRecommendedProductTitleAndDescriptionResponseDataProduct")



@_attrs_define
class GetRecommendedProductTitleAndDescriptionResponseDataProduct:
    """ 
        Attributes:
            id (str | Unset): The product ID.
            suggestions (list[GetRecommendedProductTitleAndDescriptionResponseDataProductSuggestion] | Unset): The
                suggestions for each product field.
     """

    id: str | Unset = UNSET
    suggestions: list[GetRecommendedProductTitleAndDescriptionResponseDataProductSuggestion] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_recommended_product_title_and_description_response_data_product_suggestion import GetRecommendedProductTitleAndDescriptionResponseDataProductSuggestion # noqa: PLC0415
        id = self.id

        suggestions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.suggestions, Unset):
            suggestions = []
            for suggestions_item_data in self.suggestions:
                suggestions_item = suggestions_item_data.to_dict()
                suggestions.append(suggestions_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if suggestions is not UNSET:
            field_dict["suggestions"] = suggestions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_recommended_product_title_and_description_response_data_product_suggestion import GetRecommendedProductTitleAndDescriptionResponseDataProductSuggestion # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _suggestions = d.pop("suggestions", UNSET)
        suggestions: list[GetRecommendedProductTitleAndDescriptionResponseDataProductSuggestion] | Unset = UNSET
        if _suggestions is not UNSET:
            suggestions = []
            for suggestions_item_data in _suggestions:
                suggestions_item = GetRecommendedProductTitleAndDescriptionResponseDataProductSuggestion.from_dict(suggestions_item_data)



                suggestions.append(suggestions_item)


        get_recommended_product_title_and_description_response_data_product = cls(
            id=id,
            suggestions=suggestions,
        )


        get_recommended_product_title_and_description_response_data_product.additional_properties = d
        return get_recommended_product_title_and_description_response_data_product

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
