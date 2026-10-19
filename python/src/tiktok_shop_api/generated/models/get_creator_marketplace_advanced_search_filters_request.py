from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_creator_marketplace_advanced_search_filters_request_option import (
        GetCreatorMarketplaceAdvancedSearchFiltersRequestOption,
    )


T = TypeVar("T", bound="GetCreatorMarketplaceAdvancedSearchFiltersRequest")


@_attrs_define
class GetCreatorMarketplaceAdvancedSearchFiltersRequest:
    """
    Attributes:
        options (list[GetCreatorMarketplaceAdvancedSearchFiltersRequestOption] | Unset): The filter option types to
            retrieve. If this field is omitted or empty, both `option_list` and `sorters` are returned as empty arrays.
    """

    options: list[GetCreatorMarketplaceAdvancedSearchFiltersRequestOption] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_creator_marketplace_advanced_search_filters_request_option import (
            GetCreatorMarketplaceAdvancedSearchFiltersRequestOption,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _options = d.pop("options", UNSET)
        options: list[GetCreatorMarketplaceAdvancedSearchFiltersRequestOption] | Unset = UNSET
        if _options is not UNSET:
            options = []
            for options_item_data in _options:
                options_item = GetCreatorMarketplaceAdvancedSearchFiltersRequestOption.from_dict(options_item_data)

                options.append(options_item)

        get_creator_marketplace_advanced_search_filters_request = cls(
            options=options,
        )

        get_creator_marketplace_advanced_search_filters_request.additional_properties = d
        return get_creator_marketplace_advanced_search_filters_request

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
