from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.search_creators_in_creator_marketplace_request_advanced_filter_option_list import SearchCreatorsInCreatorMarketplaceRequestAdvancedFilterOptionList





T = TypeVar("T", bound="SearchCreatorsInCreatorMarketplaceRequestAdvancedFilter")



@_attrs_define
class SearchCreatorsInCreatorMarketplaceRequestAdvancedFilter:
    """ 
        Attributes:
            content_preference_type (list[str] | Unset): Content preference type. e.g.
                -VIDEO
                -LIVE
            eligible_flat_fee (bool | Unset): Creator is eligible for flat fee invitation, only available in US local seller
            option_list (list[SearchCreatorsInCreatorMarketplaceRequestAdvancedFilterOptionList] | Unset): Creator
                Marketplace Advanced Filter Option List. Please use "Get Seller Search  Creator Marketplace Advanced
                Filters"(https://partner.tiktokshop.com/docv2/page/get-seller-search-creator-marketplace-advanced-filters) get
                available options for you first
            sorter_algorithm_id (str | Unset): Sorter algorithm id. Please use "Get Seller Search  Creator Marketplace
                Advanced Filters"(https://partner.tiktokshop.com/docv2/page/get-seller-search-creator-marketplace-advanced-
                filters) get available sorter algorithm for you first. Default is 1(default sorter)
     """

    content_preference_type: list[str] | Unset = UNSET
    eligible_flat_fee: bool | Unset = UNSET
    option_list: list[SearchCreatorsInCreatorMarketplaceRequestAdvancedFilterOptionList] | Unset = UNSET
    sorter_algorithm_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.search_creators_in_creator_marketplace_request_advanced_filter_option_list import SearchCreatorsInCreatorMarketplaceRequestAdvancedFilterOptionList # noqa: PLC0415
        content_preference_type: list[str] | Unset = UNSET
        if not isinstance(self.content_preference_type, Unset):
            content_preference_type = self.content_preference_type



        eligible_flat_fee = self.eligible_flat_fee

        option_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.option_list, Unset):
            option_list = []
            for option_list_item_data in self.option_list:
                option_list_item = option_list_item_data.to_dict()
                option_list.append(option_list_item)



        sorter_algorithm_id = self.sorter_algorithm_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if content_preference_type is not UNSET:
            field_dict["content_preference_type"] = content_preference_type
        if eligible_flat_fee is not UNSET:
            field_dict["eligible_flat_fee"] = eligible_flat_fee
        if option_list is not UNSET:
            field_dict["option_list"] = option_list
        if sorter_algorithm_id is not UNSET:
            field_dict["sorter_algorithm_id"] = sorter_algorithm_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_creators_in_creator_marketplace_request_advanced_filter_option_list import SearchCreatorsInCreatorMarketplaceRequestAdvancedFilterOptionList # noqa: PLC0415
        d = dict(src_dict)
        content_preference_type = cast(list[str], d.pop("content_preference_type", UNSET))


        eligible_flat_fee = d.pop("eligible_flat_fee", UNSET)

        _option_list = d.pop("option_list", UNSET)
        option_list: list[SearchCreatorsInCreatorMarketplaceRequestAdvancedFilterOptionList] | Unset = UNSET
        if _option_list is not UNSET:
            option_list = []
            for option_list_item_data in _option_list:
                option_list_item = SearchCreatorsInCreatorMarketplaceRequestAdvancedFilterOptionList.from_dict(option_list_item_data)



                option_list.append(option_list_item)


        sorter_algorithm_id = d.pop("sorter_algorithm_id", UNSET)

        search_creators_in_creator_marketplace_request_advanced_filter = cls(
            content_preference_type=content_preference_type,
            eligible_flat_fee=eligible_flat_fee,
            option_list=option_list,
            sorter_algorithm_id=sorter_algorithm_id,
        )


        search_creators_in_creator_marketplace_request_advanced_filter.additional_properties = d
        return search_creators_in_creator_marketplace_request_advanced_filter

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
