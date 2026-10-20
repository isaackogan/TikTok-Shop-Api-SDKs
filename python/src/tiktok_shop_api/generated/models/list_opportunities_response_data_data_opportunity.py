from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListOpportunitiesResponseDataDataOpportunity")


@_attrs_define
class ListOpportunitiesResponseDataDataOpportunity:
    """
    Attributes:
        id (str | Unset): Unique ID of the opportunity
        title (str | Unset): Opportunity title.
        reference_images (list[str] | Unset): Reference product images of the product to list.
        category_id_level_1 (str | Unset): TikTok Shop L1 category ID.
        category_id_level_2 (str | Unset): TikTok Shop L2 category ID.
        category_id_level_3 (str | Unset): TikTok Shop L3 category ID.
        category_name_level_1 (str | Unset): Category name of 1st level category.
        category_name_level_2 (str | Unset): Category name of 2nd level category.
        category_name_level_3 (str | Unset): Category name of 3rd level category.
        is_collected (bool | Unset): Whether the authorized seller has saved this opportunity to their collection.
        query_words (str | Unset): Comma-separated TikTok Shop in-site search keywords associated with the opportunity.
        opportunity_type (str | Unset): Type of opportunity: PRODUCT（品线索）/ KEYWORD（词线索）/ CATEGORY（类目线索）
            Empty return for a specific opportunity type indicates the business team has not enabled merchant submission for
            this lead type in the corresponding market.
        brand_name (str | Unset): The brand name for products specified by the opportunity.
        create_time (int | Unset): The opportunity creation time as a Unix timestamp in seconds (UTC).
        expire_time (int | Unset): Opportunity expiry date, second-level timestamp
        est_market_sales_volume (str | Unset): Estimated market sales volume for the last 30 days, returned as an
            approximate bucket: `<100`, a value rounded down to a hundreds bucket ending in `00+`, a `k+` or `M+` value, or
            `100M+`.
        est_market_gmv (str | Unset): Estimated market sales GMV in USD for the last 30 days, returned as an approximate
            bucket: `<100`, a value rounded down to a hundreds bucket ending in `00+`, a `k+` or `M+` value, or `100M+`.
        search_volume (str | Unset): TikTok Shop in-site search volume, rounded to the nearest whole number and returned
            as a decimal string.
        competitor_product_count (str | Unset): Approximate number of competing products listed in the last 30 days,
            returned as one of `< 10`, `< 50`, `< 100`, or `100+`.
        video_view_pv (str | Unset): The cumulative short video view count of all videos associated with this product
            opportunity.
        tags (str | Unset): Comma-separated display values for the opportunity tags. Each value is localized when a
            translation is available; otherwise, the configured tag description or tag code is returned.
        tag_codes (list[str] | Unset): Tag codes for the opportunity. The available codes depend on seller and market
            configuration. Examples for Latam include `core_product` and `top_product`.
        reward_info (str | Unset): Comma-separated descriptions of rewards that sellers can gain by listing products as
            required. Values are localized when a translation is available; otherwise, the configured reward description is
            returned.
        external_product_id (str | Unset): Product ID on the reference source.
        reference_source (str | Unset): The reference platform code, returned only when `external_product_id` is
            present.
            Possible values:
            - `1`: SHOPEE
            - `2`: AMAZON
            - `3`: LOOKFANTASTIC
            - `4`: WALMART
            - `5`: TTS
            - `6`: ASOS
            - `7`: UNIVERSAL_PRODUCT
            - `8`: DTCNEXUS
            - `9`: TEMU
            - `10`: SHOPIFY
            - `11`: NEXUS_SHOPIFY
            - `12`: SHEIN
            - `13`: PIXEL
            - `14`: SHOPIFY_NON_1P
            - `15`: MIRAVIA
            - `16`: RAKUTEN
            - `17`: EBAY
            - `18`: ONBUY
            - `19`: MERCADO_LIBRE
            - `20`: ALLEGRO
            - `21`: BOL
            - `22`: DTC
    """

    id: str | Unset = UNSET
    title: str | Unset = UNSET
    reference_images: list[str] | Unset = UNSET
    category_id_level_1: str | Unset = UNSET
    category_id_level_2: str | Unset = UNSET
    category_id_level_3: str | Unset = UNSET
    category_name_level_1: str | Unset = UNSET
    category_name_level_2: str | Unset = UNSET
    category_name_level_3: str | Unset = UNSET
    is_collected: bool | Unset = UNSET
    query_words: str | Unset = UNSET
    opportunity_type: str | Unset = UNSET
    brand_name: str | Unset = UNSET
    create_time: int | Unset = UNSET
    expire_time: int | Unset = UNSET
    est_market_sales_volume: str | Unset = UNSET
    est_market_gmv: str | Unset = UNSET
    search_volume: str | Unset = UNSET
    competitor_product_count: str | Unset = UNSET
    video_view_pv: str | Unset = UNSET
    tags: str | Unset = UNSET
    tag_codes: list[str] | Unset = UNSET
    reward_info: str | Unset = UNSET
    external_product_id: str | Unset = UNSET
    reference_source: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        reference_images: list[str] | Unset = UNSET
        if not isinstance(self.reference_images, Unset):
            reference_images = self.reference_images

        category_id_level_1 = self.category_id_level_1

        category_id_level_2 = self.category_id_level_2

        category_id_level_3 = self.category_id_level_3

        category_name_level_1 = self.category_name_level_1

        category_name_level_2 = self.category_name_level_2

        category_name_level_3 = self.category_name_level_3

        is_collected = self.is_collected

        query_words = self.query_words

        opportunity_type = self.opportunity_type

        brand_name = self.brand_name

        create_time = self.create_time

        expire_time = self.expire_time

        est_market_sales_volume = self.est_market_sales_volume

        est_market_gmv = self.est_market_gmv

        search_volume = self.search_volume

        competitor_product_count = self.competitor_product_count

        video_view_pv = self.video_view_pv

        tags = self.tags

        tag_codes: list[str] | Unset = UNSET
        if not isinstance(self.tag_codes, Unset):
            tag_codes = self.tag_codes

        reward_info = self.reward_info

        external_product_id = self.external_product_id

        reference_source = self.reference_source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if reference_images is not UNSET:
            field_dict["reference_images"] = reference_images
        if category_id_level_1 is not UNSET:
            field_dict["category_id_level_1"] = category_id_level_1
        if category_id_level_2 is not UNSET:
            field_dict["category_id_level_2"] = category_id_level_2
        if category_id_level_3 is not UNSET:
            field_dict["category_id_level_3"] = category_id_level_3
        if category_name_level_1 is not UNSET:
            field_dict["category_name_level_1"] = category_name_level_1
        if category_name_level_2 is not UNSET:
            field_dict["category_name_level_2"] = category_name_level_2
        if category_name_level_3 is not UNSET:
            field_dict["category_name_level_3"] = category_name_level_3
        if is_collected is not UNSET:
            field_dict["is_collected"] = is_collected
        if query_words is not UNSET:
            field_dict["query_words"] = query_words
        if opportunity_type is not UNSET:
            field_dict["opportunity_type"] = opportunity_type
        if brand_name is not UNSET:
            field_dict["brand_name"] = brand_name
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if expire_time is not UNSET:
            field_dict["expire_time"] = expire_time
        if est_market_sales_volume is not UNSET:
            field_dict["est_market_sales_volume"] = est_market_sales_volume
        if est_market_gmv is not UNSET:
            field_dict["est_market_gmv"] = est_market_gmv
        if search_volume is not UNSET:
            field_dict["search_volume"] = search_volume
        if competitor_product_count is not UNSET:
            field_dict["competitor_product_count"] = competitor_product_count
        if video_view_pv is not UNSET:
            field_dict["video_view_pv"] = video_view_pv
        if tags is not UNSET:
            field_dict["tags"] = tags
        if tag_codes is not UNSET:
            field_dict["tag_codes"] = tag_codes
        if reward_info is not UNSET:
            field_dict["reward_info"] = reward_info
        if external_product_id is not UNSET:
            field_dict["external_product_id"] = external_product_id
        if reference_source is not UNSET:
            field_dict["reference_source"] = reference_source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        reference_images = cast(list[str], d.pop("reference_images", UNSET))

        category_id_level_1 = d.pop("category_id_level_1", UNSET)

        category_id_level_2 = d.pop("category_id_level_2", UNSET)

        category_id_level_3 = d.pop("category_id_level_3", UNSET)

        category_name_level_1 = d.pop("category_name_level_1", UNSET)

        category_name_level_2 = d.pop("category_name_level_2", UNSET)

        category_name_level_3 = d.pop("category_name_level_3", UNSET)

        is_collected = d.pop("is_collected", UNSET)

        query_words = d.pop("query_words", UNSET)

        opportunity_type = d.pop("opportunity_type", UNSET)

        brand_name = d.pop("brand_name", UNSET)

        create_time = d.pop("create_time", UNSET)

        expire_time = d.pop("expire_time", UNSET)

        est_market_sales_volume = d.pop("est_market_sales_volume", UNSET)

        est_market_gmv = d.pop("est_market_gmv", UNSET)

        search_volume = d.pop("search_volume", UNSET)

        competitor_product_count = d.pop("competitor_product_count", UNSET)

        video_view_pv = d.pop("video_view_pv", UNSET)

        tags = d.pop("tags", UNSET)

        tag_codes = cast(list[str], d.pop("tag_codes", UNSET))

        reward_info = d.pop("reward_info", UNSET)

        external_product_id = d.pop("external_product_id", UNSET)

        reference_source = d.pop("reference_source", UNSET)

        list_opportunities_response_data_data_opportunity = cls(
            id=id,
            title=title,
            reference_images=reference_images,
            category_id_level_1=category_id_level_1,
            category_id_level_2=category_id_level_2,
            category_id_level_3=category_id_level_3,
            category_name_level_1=category_name_level_1,
            category_name_level_2=category_name_level_2,
            category_name_level_3=category_name_level_3,
            is_collected=is_collected,
            query_words=query_words,
            opportunity_type=opportunity_type,
            brand_name=brand_name,
            create_time=create_time,
            expire_time=expire_time,
            est_market_sales_volume=est_market_sales_volume,
            est_market_gmv=est_market_gmv,
            search_volume=search_volume,
            competitor_product_count=competitor_product_count,
            video_view_pv=video_view_pv,
            tags=tags,
            tag_codes=tag_codes,
            reward_info=reward_info,
            external_product_id=external_product_id,
            reference_source=reference_source,
        )

        list_opportunities_response_data_data_opportunity.additional_properties = d
        return list_opportunities_response_data_data_opportunity

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
