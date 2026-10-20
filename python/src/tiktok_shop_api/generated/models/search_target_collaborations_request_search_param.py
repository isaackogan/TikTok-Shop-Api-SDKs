from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.search_target_collaborations_request_search_param_keyword_type import SearchTargetCollaborationsRequestSearchParamKeywordType






T = TypeVar("T", bound="SearchTargetCollaborationsRequestSearchParam")



@_attrs_define
class SearchTargetCollaborationsRequestSearchParam:
    """ 
        Attributes:
            keyword_type (SearchTargetCollaborationsRequestSearchParamKeywordType): Type of value provided in keyword.
                Possible values:
                - PRODUCT_ID: Search for a specific product ID.
                - PRODUCT_NAME: Fuzzy-search by product name.
                - TARGET_COLLABORATION_ID: Search for a specific target collaboration ID.
                - TARGET_COLLABORATION_NAME: Fuzzy-search by target collaboration name.
            keyword (str): The value to search for, interpreted according to keyword_type.
     """

    keyword_type: SearchTargetCollaborationsRequestSearchParamKeywordType
    keyword: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        keyword_type = self.keyword_type.value

        keyword = self.keyword


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "keyword_type": keyword_type,
            "keyword": keyword,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        keyword_type = SearchTargetCollaborationsRequestSearchParamKeywordType(d.pop("keyword_type"))




        keyword = d.pop("keyword")

        search_target_collaborations_request_search_param = cls(
            keyword_type=keyword_type,
            keyword=keyword,
        )


        search_target_collaborations_request_search_param.additional_properties = d
        return search_target_collaborations_request_search_param

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
