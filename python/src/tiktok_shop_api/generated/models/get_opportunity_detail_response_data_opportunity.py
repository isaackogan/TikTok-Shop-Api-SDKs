from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_opportunity_detail_response_data_opportunity_basic_info import (
        GetOpportunityDetailResponseDataOpportunityBasicInfo,
    )
    from ..models.get_opportunity_detail_response_data_opportunity_content_data import (
        GetOpportunityDetailResponseDataOpportunityContentData,
    )
    from ..models.get_opportunity_detail_response_data_opportunity_listing_criteria import (
        GetOpportunityDetailResponseDataOpportunityListingCriteria,
    )
    from ..models.get_opportunity_detail_response_data_opportunity_market_data import (
        GetOpportunityDetailResponseDataOpportunityMarketData,
    )


T = TypeVar("T", bound="GetOpportunityDetailResponseDataOpportunity")


@_attrs_define
class GetOpportunityDetailResponseDataOpportunity:
    """
    Attributes:
        id (str | Unset): Unique ID of the opportunity
        action_type (str | Unset): The recommended action.
            Possible values:
            - LIST_SAME: List the same product.
            - LIST_SIMILAR: List a similar product.
        listing_criteria (GetOpportunityDetailResponseDataOpportunityListingCriteria | Unset):
        content_data (GetOpportunityDetailResponseDataOpportunityContentData | Unset):
        market_data (GetOpportunityDetailResponseDataOpportunityMarketData | Unset):
        basic_info (GetOpportunityDetailResponseDataOpportunityBasicInfo | Unset):
    """

    id: str | Unset = UNSET
    action_type: str | Unset = UNSET
    listing_criteria: GetOpportunityDetailResponseDataOpportunityListingCriteria | Unset = UNSET
    content_data: GetOpportunityDetailResponseDataOpportunityContentData | Unset = UNSET
    market_data: GetOpportunityDetailResponseDataOpportunityMarketData | Unset = UNSET
    basic_info: GetOpportunityDetailResponseDataOpportunityBasicInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        action_type = self.action_type

        listing_criteria: dict[str, Any] | Unset = UNSET
        if not isinstance(self.listing_criteria, Unset):
            listing_criteria = self.listing_criteria.to_dict()

        content_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.content_data, Unset):
            content_data = self.content_data.to_dict()

        market_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.market_data, Unset):
            market_data = self.market_data.to_dict()

        basic_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.basic_info, Unset):
            basic_info = self.basic_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if action_type is not UNSET:
            field_dict["action_type"] = action_type
        if listing_criteria is not UNSET:
            field_dict["listing_criteria"] = listing_criteria
        if content_data is not UNSET:
            field_dict["content_data"] = content_data
        if market_data is not UNSET:
            field_dict["market_data"] = market_data
        if basic_info is not UNSET:
            field_dict["basic_info"] = basic_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_opportunity_detail_response_data_opportunity_basic_info import (
            GetOpportunityDetailResponseDataOpportunityBasicInfo,  # noqa: PLC0415
        )
        from ..models.get_opportunity_detail_response_data_opportunity_content_data import (
            GetOpportunityDetailResponseDataOpportunityContentData,  # noqa: PLC0415
        )
        from ..models.get_opportunity_detail_response_data_opportunity_listing_criteria import (
            GetOpportunityDetailResponseDataOpportunityListingCriteria,  # noqa: PLC0415
        )
        from ..models.get_opportunity_detail_response_data_opportunity_market_data import (
            GetOpportunityDetailResponseDataOpportunityMarketData,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        action_type = d.pop("action_type", UNSET)

        _listing_criteria = d.pop("listing_criteria", UNSET)
        listing_criteria: GetOpportunityDetailResponseDataOpportunityListingCriteria | Unset
        if isinstance(_listing_criteria, Unset):
            listing_criteria = UNSET
        else:
            listing_criteria = GetOpportunityDetailResponseDataOpportunityListingCriteria.from_dict(_listing_criteria)

        _content_data = d.pop("content_data", UNSET)
        content_data: GetOpportunityDetailResponseDataOpportunityContentData | Unset
        if isinstance(_content_data, Unset):
            content_data = UNSET
        else:
            content_data = GetOpportunityDetailResponseDataOpportunityContentData.from_dict(_content_data)

        _market_data = d.pop("market_data", UNSET)
        market_data: GetOpportunityDetailResponseDataOpportunityMarketData | Unset
        if isinstance(_market_data, Unset):
            market_data = UNSET
        else:
            market_data = GetOpportunityDetailResponseDataOpportunityMarketData.from_dict(_market_data)

        _basic_info = d.pop("basic_info", UNSET)
        basic_info: GetOpportunityDetailResponseDataOpportunityBasicInfo | Unset
        if isinstance(_basic_info, Unset):
            basic_info = UNSET
        else:
            basic_info = GetOpportunityDetailResponseDataOpportunityBasicInfo.from_dict(_basic_info)

        get_opportunity_detail_response_data_opportunity = cls(
            id=id,
            action_type=action_type,
            listing_criteria=listing_criteria,
            content_data=content_data,
            market_data=market_data,
            basic_info=basic_info,
        )

        get_opportunity_detail_response_data_opportunity.additional_properties = d
        return get_opportunity_detail_response_data_opportunity

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
