from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetAffiliatePartnerCampaignProductListResponseDataProductSkuInformationListInventory")


@_attrs_define
class GetAffiliatePartnerCampaignProductListResponseDataProductSkuInformationListInventory:
    """
    Attributes:
        available_quantity (str | Unset): The total SKU quantity available in the warehouse.
    """

    available_quantity: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        available_quantity = self.available_quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if available_quantity is not UNSET:
            field_dict["available_quantity"] = available_quantity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        available_quantity = d.pop("available_quantity", UNSET)

        get_affiliate_partner_campaign_product_list_response_data_product_sku_information_list_inventory = cls(
            available_quantity=available_quantity,
        )

        get_affiliate_partner_campaign_product_list_response_data_product_sku_information_list_inventory.additional_properties = d
        return get_affiliate_partner_campaign_product_list_response_data_product_sku_information_list_inventory

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
