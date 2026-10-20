from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.option import Option





T = TypeVar("T", bound="GetCreatorMarketplaceAdvancedSearchFiltersResponseDataDataOptionList")



@_attrs_define
class GetCreatorMarketplaceAdvancedSearchFiltersResponseDataDataOptionList:
    """ 
        Attributes:
            option_type (str | Unset): The requested filter option type represented by this entry.
            options (list[Option] | Unset): The available values for this filter option type.
     """

    option_type: str | Unset = UNSET
    options: list[Option] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.option import Option # noqa: PLC0415
        option_type = self.option_type

        options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if option_type is not UNSET:
            field_dict["option_type"] = option_type
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.option import Option # noqa: PLC0415
        d = dict(src_dict)
        option_type = d.pop("option_type", UNSET)

        _options = d.pop("options", UNSET)
        options: list[Option] | Unset = UNSET
        if _options is not UNSET:
            options = []
            for options_item_data in _options:
                options_item = Option.from_dict(options_item_data)



                options.append(options_item)


        get_creator_marketplace_advanced_search_filters_response_data_data_option_list = cls(
            option_type=option_type,
            options=options,
        )


        get_creator_marketplace_advanced_search_filters_response_data_data_option_list.additional_properties = d
        return get_creator_marketplace_advanced_search_filters_response_data_data_option_list

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
