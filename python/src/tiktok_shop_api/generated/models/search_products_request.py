from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.search_products_request_audit_status_item import SearchProductsRequestAuditStatusItem
from ..models.search_products_request_category_version import SearchProductsRequestCategoryVersion
from ..models.search_products_request_listing_platforms_item import SearchProductsRequestListingPlatformsItem
from ..models.search_products_request_listing_quality_tiers_item import SearchProductsRequestListingQualityTiersItem
from ..models.search_products_request_locale import SearchProductsRequestLocale
from ..models.search_products_request_sns_filter import SearchProductsRequestSnsFilter
from ..models.search_products_request_status import SearchProductsRequestStatus
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SearchProductsRequest")



@_attrs_define
class SearchProductsRequest:
    """ 
        Attributes:
            status (SearchProductsRequestStatus | Unset): Filter products based on the product's base version. In other
                words, this filter does not apply to post-live drafts or edits. For example, `status=DRAFT` returns only
                unpublished products in the DRAFT state, not live products with an active draft.

                Possible values:
                - ALL
                - DRAFT
                - PENDING
                - FAILED
                - ACTIVATE
                - SELLER_DEACTIVATED
                - PLATFORM_DEACTIVATED
                - FREEZE
                - DELETED
                Default: ALL
            seller_skus (list[str] | Unset): Filter products by these seller SKU codes.
            create_time_ge (int | Unset): Filter products to show only those that are created on or after the specified date
                and time. Unix timestamp in seconds.

                **Note**:
                `create_time_ge` and `create_time_le` together constitute the creation time filter condition.
                - If `create_time_ge` is filled but `create_time_le` is empty, `create_time_le` will default to the current
                time.
                - If `create_time_le` is filled but `create_time_ge` is empty, `create_time_ge` will default to the earliest
                shop time.
            create_time_le (int | Unset): Filter products to show only those that are created on or before the specified
                date and time. Unix timestamp in seconds.
                Refer to notes in `create_time_ge` for more usage information.
            update_time_ge (int | Unset): Filter products to show only those that are updated on or after the specified date
                and time. Unix timestamp in seconds.

                **Note**:
                `update_time_ge` and `update_time_le` together define the update time filter condition.
                - If `update_time_ge` is filled but `update_time_le` is empty, `update_time_le` will default to the current
                time.
                - If `update_time_le` is filled but `update_time_ge` is empty, `update_time_ge` will default to the earliest
                shop time.
            update_time_le (int | Unset): Filter products to show only those that are updated on or before the specified
                date and time. Unix timestamp in seconds.
                Refer to notes in `update_time_ge` for more usage information.
            category_version (SearchProductsRequestCategoryVersion | Unset): Filter products by the category tree version.
                Possible values based on region:
                - US: `v2`, represents the 7-level category tree.
                - Other regions: `v1`, represents the 3-level category tree.
                Default: Return all products from both `v1` and `v2` category trees.
            listing_quality_tiers (list[SearchProductsRequestListingQualityTiersItem] | Unset): Filter products by their
                listing quality tier.
                Possible values:
                - POOR
                - FAIR
                - GOOD
                - EXCELLENT
                Default: Returns all
                **Note**: Available only for the US market.
            listing_platforms (list[SearchProductsRequestListingPlatformsItem] | Unset): Filter products by the listing
                platforms.
                Possible values:
                - TOKOPEDIA
                - TIKTOK_SHOP
                Default: Return all products regardless of their listing platform.

                Applicable only for sellers that migrated from Tokopedia.
                **Note**:
                - You must also specify a `status` value other than `ALL` when filtering by listing platforms. Returning all
                statuses is not supported.
                - If you pass in one platform, the search will return products that are listed on that platform, including those
                that are listed on both platforms.
                - If you pass in `["TIKTOK_SHOP", "TOKOPEDIA"]`, only products listed on both platforms will be returned, not
                those listed on just one.
            audit_status (list[SearchProductsRequestAuditStatusItem] | Unset): Filter products by their audit status for
                TikTok Shop.
                Possible values:
                - AUDITING: Returns products where the base version or a post-live edit is currently being audited.
                - FAILED: Returns products where the base version or a post-live edit has failed audit, or had the audit
                cancelled.
                - APPROVED: Returns products that passed the audit and has been listed on the platform.
            sku_ids (list[str] | Unset): Filter products by SKU IDs.
                Max count: 10
            sns_filter (SearchProductsRequestSnsFilter | Unset): Filter products by their Subscribe and Save (SNS) status.
                Possible values:
                - CONFIGURED
                - ELIGIBLE
            return_draft_version (bool | Unset): Filter products to show only those that have a draft.
                - true: Returns products in their draft version only. Excludes those without a draft.
                - false: Returns all products regardless of whether they have a draft.
                Default: false

                **Note**: Applicable only if the product status filter is `ALL`, `DRAFT`, `ACTIVATE`, `SELLER_DEACTIVATED`, or
                `PLATFORM_DEACTIVATED`.
            locale (SearchProductsRequestLocale | Unset): The BCP-47 locale codes for displaying category information.
                Default: The default locale of your shop.
                Possible values:
                - cs-CZ
                - de-AT
                - de-BE
                - de-DE
                - el-GR
                - en-GB
                - en-IE
                - en-US
                - es-ES
                - es-MX
                - fr-FR
                - fr-BE
                - hu-HU
                - id-ID
                - it-IT
                - ja-JP
                - ms-MY
                - nl-NL
                - nl-BE
                - pl-PL
                - pt-BR
                - pt-PT
                - th-TH
                - vi-VN
                - zh-CN
            include_live_quick_products (bool | Unset): Whether to include LIVE_QUICK products in the query results.
                true — Returns LIVE_QUICK products and normal product.
                false —only return normal product.

                Default: false
     """

    status: SearchProductsRequestStatus | Unset = UNSET
    seller_skus: list[str] | Unset = UNSET
    create_time_ge: int | Unset = UNSET
    create_time_le: int | Unset = UNSET
    update_time_ge: int | Unset = UNSET
    update_time_le: int | Unset = UNSET
    category_version: SearchProductsRequestCategoryVersion | Unset = UNSET
    listing_quality_tiers: list[SearchProductsRequestListingQualityTiersItem] | Unset = UNSET
    listing_platforms: list[SearchProductsRequestListingPlatformsItem] | Unset = UNSET
    audit_status: list[SearchProductsRequestAuditStatusItem] | Unset = UNSET
    sku_ids: list[str] | Unset = UNSET
    sns_filter: SearchProductsRequestSnsFilter | Unset = UNSET
    return_draft_version: bool | Unset = UNSET
    locale: SearchProductsRequestLocale | Unset = UNSET
    include_live_quick_products: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        seller_skus: list[str] | Unset = UNSET
        if not isinstance(self.seller_skus, Unset):
            seller_skus = self.seller_skus



        create_time_ge = self.create_time_ge

        create_time_le = self.create_time_le

        update_time_ge = self.update_time_ge

        update_time_le = self.update_time_le

        category_version: str | Unset = UNSET
        if not isinstance(self.category_version, Unset):
            category_version = self.category_version.value


        listing_quality_tiers: list[str] | Unset = UNSET
        if not isinstance(self.listing_quality_tiers, Unset):
            listing_quality_tiers = []
            for listing_quality_tiers_item_data in self.listing_quality_tiers:
                listing_quality_tiers_item = listing_quality_tiers_item_data.value
                listing_quality_tiers.append(listing_quality_tiers_item)



        listing_platforms: list[str] | Unset = UNSET
        if not isinstance(self.listing_platforms, Unset):
            listing_platforms = []
            for listing_platforms_item_data in self.listing_platforms:
                listing_platforms_item = listing_platforms_item_data.value
                listing_platforms.append(listing_platforms_item)



        audit_status: list[str] | Unset = UNSET
        if not isinstance(self.audit_status, Unset):
            audit_status = []
            for audit_status_item_data in self.audit_status:
                audit_status_item = audit_status_item_data.value
                audit_status.append(audit_status_item)



        sku_ids: list[str] | Unset = UNSET
        if not isinstance(self.sku_ids, Unset):
            sku_ids = self.sku_ids



        sns_filter: str | Unset = UNSET
        if not isinstance(self.sns_filter, Unset):
            sns_filter = self.sns_filter.value


        return_draft_version = self.return_draft_version

        locale: str | Unset = UNSET
        if not isinstance(self.locale, Unset):
            locale = self.locale.value


        include_live_quick_products = self.include_live_quick_products


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if status is not UNSET:
            field_dict["status"] = status
        if seller_skus is not UNSET:
            field_dict["seller_skus"] = seller_skus
        if create_time_ge is not UNSET:
            field_dict["create_time_ge"] = create_time_ge
        if create_time_le is not UNSET:
            field_dict["create_time_le"] = create_time_le
        if update_time_ge is not UNSET:
            field_dict["update_time_ge"] = update_time_ge
        if update_time_le is not UNSET:
            field_dict["update_time_le"] = update_time_le
        if category_version is not UNSET:
            field_dict["category_version"] = category_version
        if listing_quality_tiers is not UNSET:
            field_dict["listing_quality_tiers"] = listing_quality_tiers
        if listing_platforms is not UNSET:
            field_dict["listing_platforms"] = listing_platforms
        if audit_status is not UNSET:
            field_dict["audit_status"] = audit_status
        if sku_ids is not UNSET:
            field_dict["sku_ids"] = sku_ids
        if sns_filter is not UNSET:
            field_dict["sns_filter"] = sns_filter
        if return_draft_version is not UNSET:
            field_dict["return_draft_version"] = return_draft_version
        if locale is not UNSET:
            field_dict["locale"] = locale
        if include_live_quick_products is not UNSET:
            field_dict["include_live_quick_products"] = include_live_quick_products

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: SearchProductsRequestStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = SearchProductsRequestStatus(_status)




        seller_skus = cast(list[str], d.pop("seller_skus", UNSET))


        create_time_ge = d.pop("create_time_ge", UNSET)

        create_time_le = d.pop("create_time_le", UNSET)

        update_time_ge = d.pop("update_time_ge", UNSET)

        update_time_le = d.pop("update_time_le", UNSET)

        _category_version = d.pop("category_version", UNSET)
        category_version: SearchProductsRequestCategoryVersion | Unset
        if isinstance(_category_version,  Unset):
            category_version = UNSET
        else:
            category_version = SearchProductsRequestCategoryVersion(_category_version)




        _listing_quality_tiers = d.pop("listing_quality_tiers", UNSET)
        listing_quality_tiers: list[SearchProductsRequestListingQualityTiersItem] | Unset = UNSET
        if _listing_quality_tiers is not UNSET:
            listing_quality_tiers = []
            for listing_quality_tiers_item_data in _listing_quality_tiers:
                listing_quality_tiers_item = SearchProductsRequestListingQualityTiersItem(listing_quality_tiers_item_data)



                listing_quality_tiers.append(listing_quality_tiers_item)


        _listing_platforms = d.pop("listing_platforms", UNSET)
        listing_platforms: list[SearchProductsRequestListingPlatformsItem] | Unset = UNSET
        if _listing_platforms is not UNSET:
            listing_platforms = []
            for listing_platforms_item_data in _listing_platforms:
                listing_platforms_item = SearchProductsRequestListingPlatformsItem(listing_platforms_item_data)



                listing_platforms.append(listing_platforms_item)


        _audit_status = d.pop("audit_status", UNSET)
        audit_status: list[SearchProductsRequestAuditStatusItem] | Unset = UNSET
        if _audit_status is not UNSET:
            audit_status = []
            for audit_status_item_data in _audit_status:
                audit_status_item = SearchProductsRequestAuditStatusItem(audit_status_item_data)



                audit_status.append(audit_status_item)


        sku_ids = cast(list[str], d.pop("sku_ids", UNSET))


        _sns_filter = d.pop("sns_filter", UNSET)
        sns_filter: SearchProductsRequestSnsFilter | Unset
        if isinstance(_sns_filter,  Unset):
            sns_filter = UNSET
        else:
            sns_filter = SearchProductsRequestSnsFilter(_sns_filter)




        return_draft_version = d.pop("return_draft_version", UNSET)

        _locale = d.pop("locale", UNSET)
        locale: SearchProductsRequestLocale | Unset
        if isinstance(_locale,  Unset):
            locale = UNSET
        else:
            locale = SearchProductsRequestLocale(_locale)




        include_live_quick_products = d.pop("include_live_quick_products", UNSET)

        search_products_request = cls(
            status=status,
            seller_skus=seller_skus,
            create_time_ge=create_time_ge,
            create_time_le=create_time_le,
            update_time_ge=update_time_ge,
            update_time_le=update_time_le,
            category_version=category_version,
            listing_quality_tiers=listing_quality_tiers,
            listing_platforms=listing_platforms,
            audit_status=audit_status,
            sku_ids=sku_ids,
            sns_filter=sns_filter,
            return_draft_version=return_draft_version,
            locale=locale,
            include_live_quick_products=include_live_quick_products,
        )


        search_products_request.additional_properties = d
        return search_products_request

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
