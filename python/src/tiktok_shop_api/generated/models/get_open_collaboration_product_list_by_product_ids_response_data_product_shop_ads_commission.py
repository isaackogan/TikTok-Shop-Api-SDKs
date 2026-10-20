from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetOpenCollaborationProductListByProductIdsResponseDataProductShopAdsCommission")



@_attrs_define
class GetOpenCollaborationProductListByProductIdsResponseDataProductShopAdsCommission:
    """ 
        Attributes:
            rate (int | Unset): The Shop Ads commission rate for this product, multiplied by 10,000. The range is 100 to
                8,000. For example, 3,000 represents 30.00% and 3,555 represents 35.55%.
     """

    rate: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        rate = self.rate


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if rate is not UNSET:
            field_dict["rate"] = rate

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rate = d.pop("rate", UNSET)

        get_open_collaboration_product_list_by_product_ids_response_data_product_shop_ads_commission = cls(
            rate=rate,
        )


        get_open_collaboration_product_list_by_product_ids_response_data_product_shop_ads_commission.additional_properties = d
        return get_open_collaboration_product_list_by_product_ids_response_data_product_shop_ads_commission

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
