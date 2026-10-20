from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_shop_skpp_summary_response_data_shop_summary import GetShopSKPPSummaryResponseDataShopSummary


T = TypeVar("T", bound="GetShopSKPPSummaryResponseData")


@_attrs_define
class GetShopSKPPSummaryResponseData:
    """
    Attributes:
        shop_summary (GetShopSKPPSummaryResponseDataShopSummary | Unset):
    """

    shop_summary: GetShopSKPPSummaryResponseDataShopSummary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shop_summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shop_summary, Unset):
            shop_summary = self.shop_summary.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shop_summary is not UNSET:
            field_dict["shop_summary"] = shop_summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shop_skpp_summary_response_data_shop_summary import (
            GetShopSKPPSummaryResponseDataShopSummary,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _shop_summary = d.pop("shop_summary", UNSET)
        shop_summary: GetShopSKPPSummaryResponseDataShopSummary | Unset
        if isinstance(_shop_summary, Unset):
            shop_summary = UNSET
        else:
            shop_summary = GetShopSKPPSummaryResponseDataShopSummary.from_dict(_shop_summary)

        get_shop_skpp_summary_response_data = cls(
            shop_summary=shop_summary,
        )

        get_shop_skpp_summary_response_data.additional_properties = d
        return get_shop_skpp_summary_response_data

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
