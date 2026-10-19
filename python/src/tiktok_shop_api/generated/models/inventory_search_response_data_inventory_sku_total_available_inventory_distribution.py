from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inventory_search_response_data_inventory_sku_total_available_inventory_distribution_campaign_inventory import (
        InventorySearchResponseDataInventorySkuTotalAvailableInventoryDistributionCampaignInventory,
    )
    from ..models.inventory_search_response_data_inventory_sku_total_available_inventory_distribution_creator_inventory import (
        InventorySearchResponseDataInventorySkuTotalAvailableInventoryDistributionCreatorInventory,
    )
    from ..models.inventory_search_response_data_inventory_sku_total_available_inventory_distribution_in_shop_inventory import (
        InventorySearchResponseDataInventorySkuTotalAvailableInventoryDistributionInShopInventory,
    )


T = TypeVar("T", bound="InventorySearchResponseDataInventorySkuTotalAvailableInventoryDistribution")


@_attrs_define
class InventorySearchResponseDataInventorySkuTotalAvailableInventoryDistribution:
    """
    Attributes:
        campaign_inventory
            (list[InventorySearchResponseDataInventorySkuTotalAvailableInventoryDistributionCampaignInventory] | Unset):
            Inventory that is allocated to a specific campaign.
        creator_inventory
            (list[InventorySearchResponseDataInventorySkuTotalAvailableInventoryDistributionCreatorInventory] | Unset):
            Inventory that is allocated to TikTok creators.
        in_shop_inventory (InventorySearchResponseDataInventorySkuTotalAvailableInventoryDistributionInShopInventory |
            Unset):
    """

    campaign_inventory: (
        list[InventorySearchResponseDataInventorySkuTotalAvailableInventoryDistributionCampaignInventory] | Unset
    ) = UNSET
    creator_inventory: (
        list[InventorySearchResponseDataInventorySkuTotalAvailableInventoryDistributionCreatorInventory] | Unset
    ) = UNSET
    in_shop_inventory: (
        InventorySearchResponseDataInventorySkuTotalAvailableInventoryDistributionInShopInventory | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        campaign_inventory: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.campaign_inventory, Unset):
            campaign_inventory = []
            for campaign_inventory_item_data in self.campaign_inventory:
                campaign_inventory_item = campaign_inventory_item_data.to_dict()
                campaign_inventory.append(campaign_inventory_item)

        creator_inventory: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.creator_inventory, Unset):
            creator_inventory = []
            for creator_inventory_item_data in self.creator_inventory:
                creator_inventory_item = creator_inventory_item_data.to_dict()
                creator_inventory.append(creator_inventory_item)

        in_shop_inventory: dict[str, Any] | Unset = UNSET
        if not isinstance(self.in_shop_inventory, Unset):
            in_shop_inventory = self.in_shop_inventory.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if campaign_inventory is not UNSET:
            field_dict["campaign_inventory"] = campaign_inventory
        if creator_inventory is not UNSET:
            field_dict["creator_inventory"] = creator_inventory
        if in_shop_inventory is not UNSET:
            field_dict["in_shop_inventory"] = in_shop_inventory

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inventory_search_response_data_inventory_sku_total_available_inventory_distribution_campaign_inventory import (
            InventorySearchResponseDataInventorySkuTotalAvailableInventoryDistributionCampaignInventory,  # noqa: PLC0415
        )
        from ..models.inventory_search_response_data_inventory_sku_total_available_inventory_distribution_creator_inventory import (
            InventorySearchResponseDataInventorySkuTotalAvailableInventoryDistributionCreatorInventory,  # noqa: PLC0415
        )
        from ..models.inventory_search_response_data_inventory_sku_total_available_inventory_distribution_in_shop_inventory import (
            InventorySearchResponseDataInventorySkuTotalAvailableInventoryDistributionInShopInventory,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _campaign_inventory = d.pop("campaign_inventory", UNSET)
        campaign_inventory: (
            list[InventorySearchResponseDataInventorySkuTotalAvailableInventoryDistributionCampaignInventory] | Unset
        ) = UNSET
        if _campaign_inventory is not UNSET:
            campaign_inventory = []
            for campaign_inventory_item_data in _campaign_inventory:
                campaign_inventory_item = InventorySearchResponseDataInventorySkuTotalAvailableInventoryDistributionCampaignInventory.from_dict(
                    campaign_inventory_item_data
                )

                campaign_inventory.append(campaign_inventory_item)

        _creator_inventory = d.pop("creator_inventory", UNSET)
        creator_inventory: (
            list[InventorySearchResponseDataInventorySkuTotalAvailableInventoryDistributionCreatorInventory] | Unset
        ) = UNSET
        if _creator_inventory is not UNSET:
            creator_inventory = []
            for creator_inventory_item_data in _creator_inventory:
                creator_inventory_item = InventorySearchResponseDataInventorySkuTotalAvailableInventoryDistributionCreatorInventory.from_dict(
                    creator_inventory_item_data
                )

                creator_inventory.append(creator_inventory_item)

        _in_shop_inventory = d.pop("in_shop_inventory", UNSET)
        in_shop_inventory: (
            InventorySearchResponseDataInventorySkuTotalAvailableInventoryDistributionInShopInventory | Unset
        )
        if isinstance(_in_shop_inventory, Unset):
            in_shop_inventory = UNSET
        else:
            in_shop_inventory = (
                InventorySearchResponseDataInventorySkuTotalAvailableInventoryDistributionInShopInventory.from_dict(
                    _in_shop_inventory
                )
            )

        inventory_search_response_data_inventory_sku_total_available_inventory_distribution = cls(
            campaign_inventory=campaign_inventory,
            creator_inventory=creator_inventory,
            in_shop_inventory=in_shop_inventory,
        )

        inventory_search_response_data_inventory_sku_total_available_inventory_distribution.additional_properties = d
        return inventory_search_response_data_inventory_sku_total_available_inventory_distribution

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
