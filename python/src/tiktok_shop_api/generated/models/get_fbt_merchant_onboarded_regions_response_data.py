from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_fbt_merchant_onboarded_regions_response_data_onboarded_region import GetFBTMerchantOnboardedRegionsResponseDataOnboardedRegion





T = TypeVar("T", bound="GetFBTMerchantOnboardedRegionsResponseData")



@_attrs_define
class GetFBTMerchantOnboardedRegionsResponseData:
    """ 
        Attributes:
            onboarded_regions (list[GetFBTMerchantOnboardedRegionsResponseDataOnboardedRegion] | Unset): A list of countries
                or regions where the merchant is onboarded and can conduct business in the Fulfilled by TikTok system. If seller
                is not onboarded, `data` will be empty.
     """

    onboarded_regions: list[GetFBTMerchantOnboardedRegionsResponseDataOnboardedRegion] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_fbt_merchant_onboarded_regions_response_data_onboarded_region import GetFBTMerchantOnboardedRegionsResponseDataOnboardedRegion # noqa: PLC0415
        onboarded_regions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.onboarded_regions, Unset):
            onboarded_regions = []
            for onboarded_regions_item_data in self.onboarded_regions:
                onboarded_regions_item = onboarded_regions_item_data.to_dict()
                onboarded_regions.append(onboarded_regions_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if onboarded_regions is not UNSET:
            field_dict["onboarded_regions"] = onboarded_regions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_fbt_merchant_onboarded_regions_response_data_onboarded_region import GetFBTMerchantOnboardedRegionsResponseDataOnboardedRegion # noqa: PLC0415
        d = dict(src_dict)
        _onboarded_regions = d.pop("onboarded_regions", UNSET)
        onboarded_regions: list[GetFBTMerchantOnboardedRegionsResponseDataOnboardedRegion] | Unset = UNSET
        if _onboarded_regions is not UNSET:
            onboarded_regions = []
            for onboarded_regions_item_data in _onboarded_regions:
                onboarded_regions_item = GetFBTMerchantOnboardedRegionsResponseDataOnboardedRegion.from_dict(onboarded_regions_item_data)



                onboarded_regions.append(onboarded_regions_item)


        get_fbt_merchant_onboarded_regions_response_data = cls(
            onboarded_regions=onboarded_regions,
        )


        get_fbt_merchant_onboarded_regions_response_data.additional_properties = d
        return get_fbt_merchant_onboarded_regions_response_data

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
