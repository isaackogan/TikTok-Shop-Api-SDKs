from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="GetCampaignProductPerformanceListResponseDataCampaignProductStatisticCampaignProductDetailProductThumbnail",
)


@_attrs_define
class GetCampaignProductPerformanceListResponseDataCampaignProductStatisticCampaignProductDetailProductThumbnail:
    """
    Attributes:
        uri (str | Unset): The URI of the product thumbnail image.
        url_list (list[str] | Unset): A list of URLs for the product thumbnail image.
    """

    uri: str | Unset = UNSET
    url_list: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uri = self.uri

        url_list: list[str] | Unset = UNSET
        if not isinstance(self.url_list, Unset):
            url_list = self.url_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uri is not UNSET:
            field_dict["uri"] = uri
        if url_list is not UNSET:
            field_dict["url_list"] = url_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uri = d.pop("uri", UNSET)

        url_list = cast(list[str], d.pop("url_list", UNSET))

        get_campaign_product_performance_list_response_data_campaign_product_statistic_campaign_product_detail_product_thumbnail = cls(
            uri=uri,
            url_list=url_list,
        )

        get_campaign_product_performance_list_response_data_campaign_product_statistic_campaign_product_detail_product_thumbnail.additional_properties = d
        return get_campaign_product_performance_list_response_data_campaign_product_statistic_campaign_product_detail_product_thumbnail

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
