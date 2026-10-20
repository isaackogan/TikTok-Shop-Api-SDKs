from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_creator_marketplace_advanced_search_filters_response_data_data_option_list import (
        GetCreatorMarketplaceAdvancedSearchFiltersResponseDataDataOptionList,
    )
    from ..models.get_creator_marketplace_advanced_search_filters_response_data_data_sorter import (
        GetCreatorMarketplaceAdvancedSearchFiltersResponseDataDataSorter,
    )


T = TypeVar("T", bound="GetCreatorMarketplaceAdvancedSearchFiltersResponseDataData")


@_attrs_define
class GetCreatorMarketplaceAdvancedSearchFiltersResponseDataData:
    """
    Attributes:
        option_list (list[GetCreatorMarketplaceAdvancedSearchFiltersResponseDataDataOptionList] | Unset): Creator
            Marketplace Advanced Filter Option List. If we return an empty object, it means this filter is not currently
            supported by your account or region.
        sorters (list[GetCreatorMarketplaceAdvancedSearchFiltersResponseDataDataSorter] | Unset): The available sorting
            options for Creator Marketplace search results.
    """

    option_list: list[GetCreatorMarketplaceAdvancedSearchFiltersResponseDataDataOptionList] | Unset = UNSET
    sorters: list[GetCreatorMarketplaceAdvancedSearchFiltersResponseDataDataSorter] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        option_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.option_list, Unset):
            option_list = []
            for option_list_item_data in self.option_list:
                option_list_item = option_list_item_data.to_dict()
                option_list.append(option_list_item)

        sorters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sorters, Unset):
            sorters = []
            for sorters_item_data in self.sorters:
                sorters_item = sorters_item_data.to_dict()
                sorters.append(sorters_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if option_list is not UNSET:
            field_dict["option_list"] = option_list
        if sorters is not UNSET:
            field_dict["sorters"] = sorters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_creator_marketplace_advanced_search_filters_response_data_data_option_list import (
            GetCreatorMarketplaceAdvancedSearchFiltersResponseDataDataOptionList,  # noqa: PLC0415
        )
        from ..models.get_creator_marketplace_advanced_search_filters_response_data_data_sorter import (
            GetCreatorMarketplaceAdvancedSearchFiltersResponseDataDataSorter,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _option_list = d.pop("option_list", UNSET)
        option_list: list[GetCreatorMarketplaceAdvancedSearchFiltersResponseDataDataOptionList] | Unset = UNSET
        if _option_list is not UNSET:
            option_list = []
            for option_list_item_data in _option_list:
                option_list_item = GetCreatorMarketplaceAdvancedSearchFiltersResponseDataDataOptionList.from_dict(
                    option_list_item_data
                )

                option_list.append(option_list_item)

        _sorters = d.pop("sorters", UNSET)
        sorters: list[GetCreatorMarketplaceAdvancedSearchFiltersResponseDataDataSorter] | Unset = UNSET
        if _sorters is not UNSET:
            sorters = []
            for sorters_item_data in _sorters:
                sorters_item = GetCreatorMarketplaceAdvancedSearchFiltersResponseDataDataSorter.from_dict(
                    sorters_item_data
                )

                sorters.append(sorters_item)

        get_creator_marketplace_advanced_search_filters_response_data_data = cls(
            option_list=option_list,
            sorters=sorters,
        )

        get_creator_marketplace_advanced_search_filters_response_data_data.additional_properties = d
        return get_creator_marketplace_advanced_search_filters_response_data_data

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
