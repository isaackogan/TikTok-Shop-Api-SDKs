from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_affiliate_partner_campaign_product_list_response_data_product_sku_information_list_base_price import (
        GetAffiliatePartnerCampaignProductListResponseDataProductSkuInformationListBasePrice,
    )
    from ..models.get_affiliate_partner_campaign_product_list_response_data_product_sku_information_list_inventory import (
        GetAffiliatePartnerCampaignProductListResponseDataProductSkuInformationListInventory,
    )
    from ..models.get_affiliate_partner_campaign_product_list_response_data_product_sku_information_list_property import (
        GetAffiliatePartnerCampaignProductListResponseDataProductSkuInformationListProperty,
    )
    from ..models.get_affiliate_partner_campaign_product_list_response_data_product_sku_information_list_region_price import (
        GetAffiliatePartnerCampaignProductListResponseDataProductSkuInformationListRegionPrice,
    )


T = TypeVar("T", bound="GetAffiliatePartnerCampaignProductListResponseDataProductSkuInformationList")


@_attrs_define
class GetAffiliatePartnerCampaignProductListResponseDataProductSkuInformationList:
    """
    Attributes:
        sku_name (str | Unset): The name of the sku
        sku_id (str | Unset): The id of the sku
        inventory (GetAffiliatePartnerCampaignProductListResponseDataProductSkuInformationListInventory | Unset):
        base_price (GetAffiliatePartnerCampaignProductListResponseDataProductSkuInformationListBasePrice | Unset):
        region_prices (list[GetAffiliatePartnerCampaignProductListResponseDataProductSkuInformationListRegionPrice] |
            Unset): region prices
        properties (list[GetAffiliatePartnerCampaignProductListResponseDataProductSkuInformationListProperty] | Unset):
            The properties of the sku
    """

    sku_name: str | Unset = UNSET
    sku_id: str | Unset = UNSET
    inventory: GetAffiliatePartnerCampaignProductListResponseDataProductSkuInformationListInventory | Unset = UNSET
    base_price: GetAffiliatePartnerCampaignProductListResponseDataProductSkuInformationListBasePrice | Unset = UNSET
    region_prices: (
        list[GetAffiliatePartnerCampaignProductListResponseDataProductSkuInformationListRegionPrice] | Unset
    ) = UNSET
    properties: list[GetAffiliatePartnerCampaignProductListResponseDataProductSkuInformationListProperty] | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sku_name = self.sku_name

        sku_id = self.sku_id

        inventory: dict[str, Any] | Unset = UNSET
        if not isinstance(self.inventory, Unset):
            inventory = self.inventory.to_dict()

        base_price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.base_price, Unset):
            base_price = self.base_price.to_dict()

        region_prices: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.region_prices, Unset):
            region_prices = []
            for region_prices_item_data in self.region_prices:
                region_prices_item = region_prices_item_data.to_dict()
                region_prices.append(region_prices_item)

        properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()
                properties.append(properties_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sku_name is not UNSET:
            field_dict["sku_name"] = sku_name
        if sku_id is not UNSET:
            field_dict["sku_id"] = sku_id
        if inventory is not UNSET:
            field_dict["inventory"] = inventory
        if base_price is not UNSET:
            field_dict["base_price"] = base_price
        if region_prices is not UNSET:
            field_dict["region_prices"] = region_prices
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_affiliate_partner_campaign_product_list_response_data_product_sku_information_list_base_price import (
            GetAffiliatePartnerCampaignProductListResponseDataProductSkuInformationListBasePrice,  # noqa: PLC0415
        )
        from ..models.get_affiliate_partner_campaign_product_list_response_data_product_sku_information_list_inventory import (
            GetAffiliatePartnerCampaignProductListResponseDataProductSkuInformationListInventory,  # noqa: PLC0415
        )
        from ..models.get_affiliate_partner_campaign_product_list_response_data_product_sku_information_list_property import (
            GetAffiliatePartnerCampaignProductListResponseDataProductSkuInformationListProperty,  # noqa: PLC0415
        )
        from ..models.get_affiliate_partner_campaign_product_list_response_data_product_sku_information_list_region_price import (
            GetAffiliatePartnerCampaignProductListResponseDataProductSkuInformationListRegionPrice,  # noqa: PLC0415
        )

        d = dict(src_dict)
        sku_name = d.pop("sku_name", UNSET)

        sku_id = d.pop("sku_id", UNSET)

        _inventory = d.pop("inventory", UNSET)
        inventory: GetAffiliatePartnerCampaignProductListResponseDataProductSkuInformationListInventory | Unset
        if isinstance(_inventory, Unset):
            inventory = UNSET
        else:
            inventory = GetAffiliatePartnerCampaignProductListResponseDataProductSkuInformationListInventory.from_dict(
                _inventory
            )

        _base_price = d.pop("base_price", UNSET)
        base_price: GetAffiliatePartnerCampaignProductListResponseDataProductSkuInformationListBasePrice | Unset
        if isinstance(_base_price, Unset):
            base_price = UNSET
        else:
            base_price = GetAffiliatePartnerCampaignProductListResponseDataProductSkuInformationListBasePrice.from_dict(
                _base_price
            )

        _region_prices = d.pop("region_prices", UNSET)
        region_prices: (
            list[GetAffiliatePartnerCampaignProductListResponseDataProductSkuInformationListRegionPrice] | Unset
        ) = UNSET
        if _region_prices is not UNSET:
            region_prices = []
            for region_prices_item_data in _region_prices:
                region_prices_item = (
                    GetAffiliatePartnerCampaignProductListResponseDataProductSkuInformationListRegionPrice.from_dict(
                        region_prices_item_data
                    )
                )

                region_prices.append(region_prices_item)

        _properties = d.pop("properties", UNSET)
        properties: (
            list[GetAffiliatePartnerCampaignProductListResponseDataProductSkuInformationListProperty] | Unset
        ) = UNSET
        if _properties is not UNSET:
            properties = []
            for properties_item_data in _properties:
                properties_item = (
                    GetAffiliatePartnerCampaignProductListResponseDataProductSkuInformationListProperty.from_dict(
                        properties_item_data
                    )
                )

                properties.append(properties_item)

        get_affiliate_partner_campaign_product_list_response_data_product_sku_information_list = cls(
            sku_name=sku_name,
            sku_id=sku_id,
            inventory=inventory,
            base_price=base_price,
            region_prices=region_prices,
            properties=properties,
        )

        get_affiliate_partner_campaign_product_list_response_data_product_sku_information_list.additional_properties = d
        return get_affiliate_partner_campaign_product_list_response_data_product_sku_information_list

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
