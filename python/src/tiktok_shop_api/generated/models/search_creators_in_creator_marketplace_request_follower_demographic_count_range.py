from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SearchCreatorsInCreatorMarketplaceRequestFollowerDemographicCountRange")



@_attrs_define
class SearchCreatorsInCreatorMarketplaceRequestFollowerDemographicCountRange:
    """ 
        Attributes:
            count_ge (int | Unset): The minimum value of follower count.
                The value passed in must be greater than or equal to 0
            count_le (int | Unset): The maximum value of follower count.
                - Generally, a value greater than or equal to 0 needs to be passed. If a value less than 0 is passed, it means
                that the field will not be filtered.
     """

    count_ge: int | Unset = UNSET
    count_le: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        count_ge = self.count_ge

        count_le = self.count_le


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if count_ge is not UNSET:
            field_dict["count_ge"] = count_ge
        if count_le is not UNSET:
            field_dict["count_le"] = count_le

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count_ge = d.pop("count_ge", UNSET)

        count_le = d.pop("count_le", UNSET)

        search_creators_in_creator_marketplace_request_follower_demographic_count_range = cls(
            count_ge=count_ge,
            count_le=count_le,
        )


        search_creators_in_creator_marketplace_request_follower_demographic_count_range.additional_properties = d
        return search_creators_in_creator_marketplace_request_follower_demographic_count_range

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
