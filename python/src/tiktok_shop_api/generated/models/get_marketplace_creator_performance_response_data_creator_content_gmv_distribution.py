from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetMarketplaceCreatorPerformanceResponseDataCreatorContentGmvDistribution")



@_attrs_define
class GetMarketplaceCreatorPerformanceResponseDataCreatorContentGmvDistribution:
    """ 
        Attributes:
            content_type (str | Unset): The content type. This an enumerated type with values:
                - VIDEO
                - LIVE
                - SHOWCASE
            value (str | Unset): The proportion of the creator's GMV attributed to this content type, expressed as a decimal
                from `0` to `1` (for example, `0.3035` = 30.35%).
     """

    content_type: str | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        content_type = self.content_type

        value = self.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content_type = d.pop("content_type", UNSET)

        value = d.pop("value", UNSET)

        get_marketplace_creator_performance_response_data_creator_content_gmv_distribution = cls(
            content_type=content_type,
            value=value,
        )


        get_marketplace_creator_performance_response_data_creator_content_gmv_distribution.additional_properties = d
        return get_marketplace_creator_performance_response_data_creator_content_gmv_distribution

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
