from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetOpportunityDetailResponseDataOpportunityBasicInfo")


@_attrs_define
class GetOpportunityDetailResponseDataOpportunityBasicInfo:
    """
    Attributes:
        opportunity_type (str | Unset): The opportunity type.
            Possible values:
            - PRODUCT: A product opportunity.
            - KEYWORD: A keyword opportunity.
            - CATEGORY: A category opportunity.
        status (str | Unset): Opportunity status: ACTIVE / EXPIRED / FULFILLED(已提报)
        create_time (int | Unset): The opportunity creation time as a Unix timestamp in seconds (UTC).
        expire_time (int | Unset): Opportunity expiry date, second-level timestamp
        title (str | Unset): Opportunity title.
        category_id_level_1 (str | Unset): TikTok Shop L1 category ID.
        category_id_level_2 (str | Unset): TikTok Shop L2 category ID.
        category_id_level_3 (str | Unset): TikTok Shop L3 category ID.
        category_name_level_1 (str | Unset): Category name of 1st level category.
        category_name_level_2 (str | Unset): Category name of 2nd level category.
        category_name_level_3 (str | Unset): Category name of 3rd level category.
        reference_price (str | Unset): The reference price for the product to list, formatted with the applicable
            currency symbol and three decimal places. If both price boundaries are available, the value is returned as a
            range; if one is available, a single price is returned; if neither is available, an empty string is returned.
        reference_images (list[str] | Unset): Reference product images of the product to list.
        brand_info (str | Unset): Brand requirements for products specified by the opportunity.
        reward_info (str | Unset): Comma-separated descriptions of rewards that sellers can gain by listing products as
            required. Values are localized when a translation is available; otherwise, the configured reward description is
            returned.
        recom_info (str | Unset): Recommendation reason why this is an opportunity.
        tags (str | Unset): Comma-separated display values for the opportunity tags. Each value is localized when a
            translation is available; otherwise, the configured tag description or tag code is returned.
        tag_codes (list[str] | Unset): Tag codes for the opportunity. The available codes depend on seller and market
            configuration. Examples for Latam include `core_product` and `top_product`.
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

    opportunity_type: str | Unset = UNSET
    status: str | Unset = UNSET
    create_time: int | Unset = UNSET
    expire_time: int | Unset = UNSET
    title: str | Unset = UNSET
    category_id_level_1: str | Unset = UNSET
    category_id_level_2: str | Unset = UNSET
    category_id_level_3: str | Unset = UNSET
    category_name_level_1: str | Unset = UNSET
    category_name_level_2: str | Unset = UNSET
    category_name_level_3: str | Unset = UNSET
    reference_price: str | Unset = UNSET
    reference_images: list[str] | Unset = UNSET
    brand_info: str | Unset = UNSET
    reward_info: str | Unset = UNSET
    recom_info: str | Unset = UNSET
    tags: str | Unset = UNSET
    tag_codes: list[str] | Unset = UNSET
    external_product_id: str | Unset = UNSET
    reference_source: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        opportunity_type = self.opportunity_type

        status = self.status

        create_time = self.create_time

        expire_time = self.expire_time

        title = self.title

        category_id_level_1 = self.category_id_level_1

        category_id_level_2 = self.category_id_level_2

        category_id_level_3 = self.category_id_level_3

        category_name_level_1 = self.category_name_level_1

        category_name_level_2 = self.category_name_level_2

        category_name_level_3 = self.category_name_level_3

        reference_price = self.reference_price

        reference_images: list[str] | Unset = UNSET
        if not isinstance(self.reference_images, Unset):
            reference_images = self.reference_images

        brand_info = self.brand_info

        reward_info = self.reward_info

        recom_info = self.recom_info

        tags = self.tags

        tag_codes: list[str] | Unset = UNSET
        if not isinstance(self.tag_codes, Unset):
            tag_codes = self.tag_codes

        external_product_id = self.external_product_id

        reference_source = self.reference_source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if opportunity_type is not UNSET:
            field_dict["opportunity_type"] = opportunity_type
        if status is not UNSET:
            field_dict["status"] = status
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if expire_time is not UNSET:
            field_dict["expire_time"] = expire_time
        if title is not UNSET:
            field_dict["title"] = title
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
        if reference_price is not UNSET:
            field_dict["reference_price"] = reference_price
        if reference_images is not UNSET:
            field_dict["reference_images"] = reference_images
        if brand_info is not UNSET:
            field_dict["brand_info"] = brand_info
        if reward_info is not UNSET:
            field_dict["reward_info"] = reward_info
        if recom_info is not UNSET:
            field_dict["recom_info"] = recom_info
        if tags is not UNSET:
            field_dict["tags"] = tags
        if tag_codes is not UNSET:
            field_dict["tag_codes"] = tag_codes
        if external_product_id is not UNSET:
            field_dict["external_product_id"] = external_product_id
        if reference_source is not UNSET:
            field_dict["reference_source"] = reference_source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        opportunity_type = d.pop("opportunity_type", UNSET)

        status = d.pop("status", UNSET)

        create_time = d.pop("create_time", UNSET)

        expire_time = d.pop("expire_time", UNSET)

        title = d.pop("title", UNSET)

        category_id_level_1 = d.pop("category_id_level_1", UNSET)

        category_id_level_2 = d.pop("category_id_level_2", UNSET)

        category_id_level_3 = d.pop("category_id_level_3", UNSET)

        category_name_level_1 = d.pop("category_name_level_1", UNSET)

        category_name_level_2 = d.pop("category_name_level_2", UNSET)

        category_name_level_3 = d.pop("category_name_level_3", UNSET)

        reference_price = d.pop("reference_price", UNSET)

        reference_images = cast(list[str], d.pop("reference_images", UNSET))

        brand_info = d.pop("brand_info", UNSET)

        reward_info = d.pop("reward_info", UNSET)

        recom_info = d.pop("recom_info", UNSET)

        tags = d.pop("tags", UNSET)

        tag_codes = cast(list[str], d.pop("tag_codes", UNSET))

        external_product_id = d.pop("external_product_id", UNSET)

        reference_source = d.pop("reference_source", UNSET)

        get_opportunity_detail_response_data_opportunity_basic_info = cls(
            opportunity_type=opportunity_type,
            status=status,
            create_time=create_time,
            expire_time=expire_time,
            title=title,
            category_id_level_1=category_id_level_1,
            category_id_level_2=category_id_level_2,
            category_id_level_3=category_id_level_3,
            category_name_level_1=category_name_level_1,
            category_name_level_2=category_name_level_2,
            category_name_level_3=category_name_level_3,
            reference_price=reference_price,
            reference_images=reference_images,
            brand_info=brand_info,
            reward_info=reward_info,
            recom_info=recom_info,
            tags=tags,
            tag_codes=tag_codes,
            external_product_id=external_product_id,
            reference_source=reference_source,
        )

        get_opportunity_detail_response_data_opportunity_basic_info.additional_properties = d
        return get_opportunity_detail_response_data_opportunity_basic_info

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
