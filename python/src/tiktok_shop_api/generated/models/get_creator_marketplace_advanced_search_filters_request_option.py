from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_creator_marketplace_advanced_search_filters_request_option_option_type import (
    GetCreatorMarketplaceAdvancedSearchFiltersRequestOptionOptionType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCreatorMarketplaceAdvancedSearchFiltersRequestOption")


@_attrs_define
class GetCreatorMarketplaceAdvancedSearchFiltersRequestOption:
    """
    Attributes:
        option_type (GetCreatorMarketplaceAdvancedSearchFiltersRequestOptionOptionType | Unset): Filter option type to
            retrieve. Possible values:
            - `OPTION_VERTICAL_PRO`: Category Pro, a label for creators who regularly post about one product category and
            generated most of their sales in that category during the past 60 days.
            - `OPTION_LANGUAGE`: Creator language.
            - `OPTION_CREATOR_LEVEL`: Creator level based on GMV. The definition varies by country and is maintained by the
            TikTok Shop Creator team.
            - `OPTION_SORTER`: Available creator-search sorting options, returned in `sorters`.
            - `OPTION_BRAND`: Creator brand information. This value is not supported in DE, FR, IT, ES, IE, or JP.
    """

    option_type: GetCreatorMarketplaceAdvancedSearchFiltersRequestOptionOptionType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        option_type: str | Unset = UNSET
        if not isinstance(self.option_type, Unset):
            option_type = self.option_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if option_type is not UNSET:
            field_dict["option_type"] = option_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _option_type = d.pop("option_type", UNSET)
        option_type: GetCreatorMarketplaceAdvancedSearchFiltersRequestOptionOptionType | Unset
        if isinstance(_option_type, Unset):
            option_type = UNSET
        else:
            option_type = GetCreatorMarketplaceAdvancedSearchFiltersRequestOptionOptionType(_option_type)

        get_creator_marketplace_advanced_search_filters_request_option = cls(
            option_type=option_type,
        )

        get_creator_marketplace_advanced_search_filters_request_option.additional_properties = d
        return get_creator_marketplace_advanced_search_filters_request_option

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
