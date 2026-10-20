from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_affiliate_partner_campaign_product_list_response_data_product_category import (
        GetAffiliatePartnerCampaignProductListResponseDataProductCategory,
    )
    from ..models.get_affiliate_partner_campaign_product_list_response_data_product_highest_price import (
        GetAffiliatePartnerCampaignProductListResponseDataProductHighestPrice,
    )
    from ..models.get_affiliate_partner_campaign_product_list_response_data_product_lowest_price import (
        GetAffiliatePartnerCampaignProductListResponseDataProductLowestPrice,
    )
    from ..models.get_affiliate_partner_campaign_product_list_response_data_product_sku_information_list import (
        GetAffiliatePartnerCampaignProductListResponseDataProductSkuInformationList,
    )


T = TypeVar("T", bound="GetAffiliatePartnerCampaignProductListResponseDataProduct")


@_attrs_define
class GetAffiliatePartnerCampaignProductListResponseDataProduct:
    """
    Attributes:
        id (str | Unset): The product identifier.
        review_status (str | Unset): The product review status. This an enumerated type with values:
            - PENDING
            - APPROVED
            - REJECTED
            - PENDING_CLOSED
            - CLOSED
        name (str | Unset): The product name.
        main_image_url (str | Unset): The product image URL.
        lowest_price (GetAffiliatePartnerCampaignProductListResponseDataProductLowestPrice | Unset):
        highest_price (GetAffiliatePartnerCampaignProductListResponseDataProductHighestPrice | Unset):
        inventory (int | Unset): The number of in-stock units of all SKUs for this product.
        shop_name (str | Unset): The TikTok Shop name.
        total_commission_rate (int | Unset): The total commission rate in hundredths of a percent (0.01%) units.
        creator_commission_rate (int | Unset): The creator commission rate in hundredths of a percent (0.01%) units.
        partner_commission_rate (int | Unset): The partner commission rate in hundredths of a percent (0.01%) units.
        open_collaboration_commission_rate (int | Unset): The product open collaboration commission rate in hundredths
            of a percent (0.01%) units.
        is_available (bool | Unset): Set to `true` if a product URL is available. Set to `false` if no product URL is
            available.
        product_sales (int | Unset): The total number of units sold of this product for this campaign.
        category (GetAffiliatePartnerCampaignProductListResponseDataProductCategory | Unset):
        sample_quota (int | Unset): The total amount of sample inventory available for allocation to creators by the
            seller.
        sku_information_list (list[GetAffiliatePartnerCampaignProductListResponseDataProductSkuInformationList] |
            Unset): A list of Stock Keeping Units (SKUs) used to identify distinct variants of the product.
        product_description (str | Unset): Return product description
    """

    id: str | Unset = UNSET
    review_status: str | Unset = UNSET
    name: str | Unset = UNSET
    main_image_url: str | Unset = UNSET
    lowest_price: GetAffiliatePartnerCampaignProductListResponseDataProductLowestPrice | Unset = UNSET
    highest_price: GetAffiliatePartnerCampaignProductListResponseDataProductHighestPrice | Unset = UNSET
    inventory: int | Unset = UNSET
    shop_name: str | Unset = UNSET
    total_commission_rate: int | Unset = UNSET
    creator_commission_rate: int | Unset = UNSET
    partner_commission_rate: int | Unset = UNSET
    open_collaboration_commission_rate: int | Unset = UNSET
    is_available: bool | Unset = UNSET
    product_sales: int | Unset = UNSET
    category: GetAffiliatePartnerCampaignProductListResponseDataProductCategory | Unset = UNSET
    sample_quota: int | Unset = UNSET
    sku_information_list: list[GetAffiliatePartnerCampaignProductListResponseDataProductSkuInformationList] | Unset = (
        UNSET
    )
    product_description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        review_status = self.review_status

        name = self.name

        main_image_url = self.main_image_url

        lowest_price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lowest_price, Unset):
            lowest_price = self.lowest_price.to_dict()

        highest_price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.highest_price, Unset):
            highest_price = self.highest_price.to_dict()

        inventory = self.inventory

        shop_name = self.shop_name

        total_commission_rate = self.total_commission_rate

        creator_commission_rate = self.creator_commission_rate

        partner_commission_rate = self.partner_commission_rate

        open_collaboration_commission_rate = self.open_collaboration_commission_rate

        is_available = self.is_available

        product_sales = self.product_sales

        category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        sample_quota = self.sample_quota

        sku_information_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sku_information_list, Unset):
            sku_information_list = []
            for sku_information_list_item_data in self.sku_information_list:
                sku_information_list_item = sku_information_list_item_data.to_dict()
                sku_information_list.append(sku_information_list_item)

        product_description = self.product_description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if review_status is not UNSET:
            field_dict["review_status"] = review_status
        if name is not UNSET:
            field_dict["name"] = name
        if main_image_url is not UNSET:
            field_dict["main_image_url"] = main_image_url
        if lowest_price is not UNSET:
            field_dict["lowest_price"] = lowest_price
        if highest_price is not UNSET:
            field_dict["highest_price"] = highest_price
        if inventory is not UNSET:
            field_dict["inventory"] = inventory
        if shop_name is not UNSET:
            field_dict["shop_name"] = shop_name
        if total_commission_rate is not UNSET:
            field_dict["total_commission_rate"] = total_commission_rate
        if creator_commission_rate is not UNSET:
            field_dict["creator_commission_rate"] = creator_commission_rate
        if partner_commission_rate is not UNSET:
            field_dict["partner_commission_rate"] = partner_commission_rate
        if open_collaboration_commission_rate is not UNSET:
            field_dict["open_collaboration_commission_rate"] = open_collaboration_commission_rate
        if is_available is not UNSET:
            field_dict["is_available"] = is_available
        if product_sales is not UNSET:
            field_dict["product_sales"] = product_sales
        if category is not UNSET:
            field_dict["category"] = category
        if sample_quota is not UNSET:
            field_dict["sample_quota"] = sample_quota
        if sku_information_list is not UNSET:
            field_dict["sku_information_list"] = sku_information_list
        if product_description is not UNSET:
            field_dict["product_description"] = product_description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_affiliate_partner_campaign_product_list_response_data_product_category import (
            GetAffiliatePartnerCampaignProductListResponseDataProductCategory,  # noqa: PLC0415
        )
        from ..models.get_affiliate_partner_campaign_product_list_response_data_product_highest_price import (
            GetAffiliatePartnerCampaignProductListResponseDataProductHighestPrice,  # noqa: PLC0415
        )
        from ..models.get_affiliate_partner_campaign_product_list_response_data_product_lowest_price import (
            GetAffiliatePartnerCampaignProductListResponseDataProductLowestPrice,  # noqa: PLC0415
        )
        from ..models.get_affiliate_partner_campaign_product_list_response_data_product_sku_information_list import (
            GetAffiliatePartnerCampaignProductListResponseDataProductSkuInformationList,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        review_status = d.pop("review_status", UNSET)

        name = d.pop("name", UNSET)

        main_image_url = d.pop("main_image_url", UNSET)

        _lowest_price = d.pop("lowest_price", UNSET)
        lowest_price: GetAffiliatePartnerCampaignProductListResponseDataProductLowestPrice | Unset
        if isinstance(_lowest_price, Unset):
            lowest_price = UNSET
        else:
            lowest_price = GetAffiliatePartnerCampaignProductListResponseDataProductLowestPrice.from_dict(_lowest_price)

        _highest_price = d.pop("highest_price", UNSET)
        highest_price: GetAffiliatePartnerCampaignProductListResponseDataProductHighestPrice | Unset
        if isinstance(_highest_price, Unset):
            highest_price = UNSET
        else:
            highest_price = GetAffiliatePartnerCampaignProductListResponseDataProductHighestPrice.from_dict(
                _highest_price
            )

        inventory = d.pop("inventory", UNSET)

        shop_name = d.pop("shop_name", UNSET)

        total_commission_rate = d.pop("total_commission_rate", UNSET)

        creator_commission_rate = d.pop("creator_commission_rate", UNSET)

        partner_commission_rate = d.pop("partner_commission_rate", UNSET)

        open_collaboration_commission_rate = d.pop("open_collaboration_commission_rate", UNSET)

        is_available = d.pop("is_available", UNSET)

        product_sales = d.pop("product_sales", UNSET)

        _category = d.pop("category", UNSET)
        category: GetAffiliatePartnerCampaignProductListResponseDataProductCategory | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = GetAffiliatePartnerCampaignProductListResponseDataProductCategory.from_dict(_category)

        sample_quota = d.pop("sample_quota", UNSET)

        _sku_information_list = d.pop("sku_information_list", UNSET)
        sku_information_list: (
            list[GetAffiliatePartnerCampaignProductListResponseDataProductSkuInformationList] | Unset
        ) = UNSET
        if _sku_information_list is not UNSET:
            sku_information_list = []
            for sku_information_list_item_data in _sku_information_list:
                sku_information_list_item = (
                    GetAffiliatePartnerCampaignProductListResponseDataProductSkuInformationList.from_dict(
                        sku_information_list_item_data
                    )
                )

                sku_information_list.append(sku_information_list_item)

        product_description = d.pop("product_description", UNSET)

        get_affiliate_partner_campaign_product_list_response_data_product = cls(
            id=id,
            review_status=review_status,
            name=name,
            main_image_url=main_image_url,
            lowest_price=lowest_price,
            highest_price=highest_price,
            inventory=inventory,
            shop_name=shop_name,
            total_commission_rate=total_commission_rate,
            creator_commission_rate=creator_commission_rate,
            partner_commission_rate=partner_commission_rate,
            open_collaboration_commission_rate=open_collaboration_commission_rate,
            is_available=is_available,
            product_sales=product_sales,
            category=category,
            sample_quota=sample_quota,
            sku_information_list=sku_information_list,
            product_description=product_description,
        )

        get_affiliate_partner_campaign_product_list_response_data_product.additional_properties = d
        return get_affiliate_partner_campaign_product_list_response_data_product

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
