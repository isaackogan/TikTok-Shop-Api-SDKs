from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_open_collaborations_request_keyword_type import SearchOpenCollaborationsRequestKeywordType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchOpenCollaborationsRequest")


@_attrs_define
class SearchOpenCollaborationsRequest:
    """
    Attributes:
        keyword_type (SearchOpenCollaborationsRequestKeywordType | Unset): Specifies the type of value in `keyword`. To
            filter open collaborations by product name or product ID, provide `keyword_type` and `keyword` together.
            Possible values:
            - `PRODUCT_ID`: Search for open collaboration information for the specified product ID.
            - `PRODUCT_NAME`: Fuzzy-search open collaboration information by related product names.
        keyword (str | Unset): Search based on the product name or product ID. Pass in the appropriate value based on
            the keyword_type above.
        top_level_category_id (str | Unset): Filter products by a first-level category ID.
            The value of `top_level_category_id` must be greater than 0.
    """

    keyword_type: SearchOpenCollaborationsRequestKeywordType | Unset = UNSET
    keyword: str | Unset = UNSET
    top_level_category_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        keyword_type: str | Unset = UNSET
        if not isinstance(self.keyword_type, Unset):
            keyword_type = self.keyword_type.value

        keyword = self.keyword

        top_level_category_id = self.top_level_category_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if keyword_type is not UNSET:
            field_dict["keyword_type"] = keyword_type
        if keyword is not UNSET:
            field_dict["keyword"] = keyword
        if top_level_category_id is not UNSET:
            field_dict["top_level_category_id"] = top_level_category_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _keyword_type = d.pop("keyword_type", UNSET)
        keyword_type: SearchOpenCollaborationsRequestKeywordType | Unset
        if isinstance(_keyword_type, Unset):
            keyword_type = UNSET
        else:
            keyword_type = SearchOpenCollaborationsRequestKeywordType(_keyword_type)

        keyword = d.pop("keyword", UNSET)

        top_level_category_id = d.pop("top_level_category_id", UNSET)

        search_open_collaborations_request = cls(
            keyword_type=keyword_type,
            keyword=keyword,
            top_level_category_id=top_level_category_id,
        )

        search_open_collaborations_request.additional_properties = d
        return search_open_collaborations_request

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
