from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_marketplace_creator_performance_response_data_creator import (
        GetMarketplaceCreatorPerformanceResponseDataCreator,
    )


T = TypeVar("T", bound="GetMarketplaceCreatorPerformanceResponseData")


@_attrs_define
class GetMarketplaceCreatorPerformanceResponseData:
    """
    Attributes:
        creator (GetMarketplaceCreatorPerformanceResponseDataCreator | Unset):
    """

    creator: GetMarketplaceCreatorPerformanceResponseDataCreator | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        creator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if creator is not UNSET:
            field_dict["creator"] = creator

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_marketplace_creator_performance_response_data_creator import (
            GetMarketplaceCreatorPerformanceResponseDataCreator,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _creator = d.pop("creator", UNSET)
        creator: GetMarketplaceCreatorPerformanceResponseDataCreator | Unset
        if isinstance(_creator, Unset):
            creator = UNSET
        else:
            creator = GetMarketplaceCreatorPerformanceResponseDataCreator.from_dict(_creator)

        get_marketplace_creator_performance_response_data = cls(
            creator=creator,
        )

        get_marketplace_creator_performance_response_data.additional_properties = d
        return get_marketplace_creator_performance_response_data

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
