from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_creator_target_collaborations_request_keyword_type import (
    SearchCreatorTargetCollaborationsRequestKeywordType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchCreatorTargetCollaborationsRequest")


@_attrs_define
class SearchCreatorTargetCollaborationsRequest:
    """
    Attributes:
        shop_id (str): The TikTok Shop identifier.
        keyword_type (SearchCreatorTargetCollaborationsRequestKeywordType | Unset): The type of value specified in
            `keyword`. Provide `keyword` and `keyword_type` together to filter by ID or name. Omit both fields to search
            without an ID or name filter. Possible values:
            - `TARGET_COLLABORATIONS_ID`: Match by target collaboration ID and return matching collaborations in the `LIVE`,
            `EXPIRED`, `DELETED`, or `ENDED` state.
            - `TARGET_COLLABORATIONS_NAME`: Match by target collaboration name and return matching collaborations in the
            `LIVE` state only.
        keyword (str | Unset): The target collaboration ID or name to search for, as specified by `keyword_type`. For
            `TARGET_COLLABORATIONS_ID`, provide a base-10 integer. For `TARGET_COLLABORATIONS_NAME`, provide a value shorter
            than 500 bytes.
    """

    shop_id: str
    keyword_type: SearchCreatorTargetCollaborationsRequestKeywordType | Unset = UNSET
    keyword: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shop_id = self.shop_id

        keyword_type: str | Unset = UNSET
        if not isinstance(self.keyword_type, Unset):
            keyword_type = self.keyword_type.value

        keyword = self.keyword

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "shop_id": shop_id,
            }
        )
        if keyword_type is not UNSET:
            field_dict["keyword_type"] = keyword_type
        if keyword is not UNSET:
            field_dict["keyword"] = keyword

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        shop_id = d.pop("shop_id")

        _keyword_type = d.pop("keyword_type", UNSET)
        keyword_type: SearchCreatorTargetCollaborationsRequestKeywordType | Unset
        if isinstance(_keyword_type, Unset):
            keyword_type = UNSET
        else:
            keyword_type = SearchCreatorTargetCollaborationsRequestKeywordType(_keyword_type)

        keyword = d.pop("keyword", UNSET)

        search_creator_target_collaborations_request = cls(
            shop_id=shop_id,
            keyword_type=keyword_type,
            keyword=keyword,
        )

        search_creator_target_collaborations_request.additional_properties = d
        return search_creator_target_collaborations_request

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
