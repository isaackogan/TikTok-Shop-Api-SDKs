from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.recommend_category_request_listing_platform import RecommendCategoryRequestListingPlatform
from ..models.recommend_category_request_locale import RecommendCategoryRequestLocale
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.diagnose_and_optimize_product_request_size_chart_image import DiagnoseAndOptimizeProductRequestSizeChartImage
  from ..models.recommend_category_request_origin_platform_category import RecommendCategoryRequestOriginPlatformCategory
  from ..models.recommend_category_request_origin_platform_product_meta_data import RecommendCategoryRequestOriginPlatformProductMetaData





T = TypeVar("T", bound="RecommendCategoryRequest")



@_attrs_define
class RecommendCategoryRequest:
    """ 
        Attributes:
            product_title (str): The product title.
                Title length:
                - DE, ES, FR, IE, IT, JP, UK, US: [1, 255]
                - BR, MX: [1, 300]
                - Other regions: [25, 255]
            category_version (str | Unset): Filter categories by the category tree version.Possible values based on region:
                - US, EU and SEA: v2, represents the 7-level category tree.
                Important: For US, EU and SEA shops, you must pass v2 when using this API.
                - Other regions: v1, represents the 3-level category tree.Default: v1
            description (str | Unset): The product description in HTML format.

                **Note**:
                - The content must conform to the [HTML syntax](https://html.spec.whatwg.org/). All HTML tags are accepted but
                to optimize display on the TikTok Shop product detail page, the system will automatically convert certain tags
                into alternative formats, such as rendering `<table>` tags as images.
                - Max length: 10,000 characters.
                - Image guidelines: You must use [TikTok Shop image URLs](6509df95defece02be598a22). Max 30 `<img>` tags, each
                under 4000px with `src`, `width`, and `height` attributes.

                **Recommendations**:
                - If you are syncing a pre-existing description from another platform, include the full HTML source description
                here.
                - Provide a detailed description, ideally over 300 characters.
                - Include 3-5 key selling points, each under 250 characters, with supporting images.
                - Use 1600x1600 px for the image dimensions.
            images (list[DiagnoseAndOptimizeProductRequestSizeChartImage] | Unset): Product images, including gallery
                images, images that appear in the description, product variant images.
            include_prohibited_categories (bool | Unset): A flag to indicate whether to include matching categories that are
                prohibited on TikTok Shop. Set this to `true` to identify if the product falls under a category that you can't
                list on TikTok Shop in any circumstances.
                **Note**:
                - Applicable only for BR and MX markets.
                - Default: `false`
            listing_platform (RecommendCategoryRequestListingPlatform | Unset): Recommend categories that belong to the
                specified platform.
                Possible values:
                - TIKTOK_SHOP
                - TOKOPEDIA
                Default: TIKTOK_SHOP

                Applicable only for sellers that migrated from Tokopedia.
            locale (RecommendCategoryRequestLocale | Unset): The BCP-47 locale codes for displaying category information.
                Default: The default locale of your shop.
                Possible values:
                - `cs-CZ`
                - `de-AT`
                - `de-BE`
                - `de-DE`
                - `el-GR`
                - `en-GB`
                - `en-IE`
                - `en-US`
                - `es-ES`
                - `es-MX`
                - `fr-FR`
                - `fr-BE`
                - `hu-HU`
                - `id-ID`
                - `it-IT`
                - `ja-JP`
                - `ms-MY`
                - `nl-NL`
                - `nl-BE`
                - `pl-PL`
                - `pt-BR`
                - `pt-PT`
                - `th-TH`
                - `vi-VN`
                - `zh-CN`
            origin_platform_product_type (str | Unset): The product type defined on the source platform.
            origin_platform_vendor (str | Unset): The product vendor or brand name on the source platform.
            origin_platform_tags (list[str] | Unset): Tags associated with the product on the source platform.
            origin_platform_category (RecommendCategoryRequestOriginPlatformCategory | Unset):
            origin_platform_product_meta_data (RecommendCategoryRequestOriginPlatformProductMetaData | Unset):
            is_live_quick (bool | Unset): false — NORMAL products
                true — LIVE_QUICK products. Only seller with the required permissions can creat LIVE_QUICK products.
                Default: false
     """

    product_title: str
    category_version: str | Unset = UNSET
    description: str | Unset = UNSET
    images: list[DiagnoseAndOptimizeProductRequestSizeChartImage] | Unset = UNSET
    include_prohibited_categories: bool | Unset = UNSET
    listing_platform: RecommendCategoryRequestListingPlatform | Unset = UNSET
    locale: RecommendCategoryRequestLocale | Unset = UNSET
    origin_platform_product_type: str | Unset = UNSET
    origin_platform_vendor: str | Unset = UNSET
    origin_platform_tags: list[str] | Unset = UNSET
    origin_platform_category: RecommendCategoryRequestOriginPlatformCategory | Unset = UNSET
    origin_platform_product_meta_data: RecommendCategoryRequestOriginPlatformProductMetaData | Unset = UNSET
    is_live_quick: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.diagnose_and_optimize_product_request_size_chart_image import DiagnoseAndOptimizeProductRequestSizeChartImage # noqa: PLC0415
        from ..models.recommend_category_request_origin_platform_category import RecommendCategoryRequestOriginPlatformCategory # noqa: PLC0415
        from ..models.recommend_category_request_origin_platform_product_meta_data import RecommendCategoryRequestOriginPlatformProductMetaData # noqa: PLC0415
        product_title = self.product_title

        category_version = self.category_version

        description = self.description

        images: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)



        include_prohibited_categories = self.include_prohibited_categories

        listing_platform: str | Unset = UNSET
        if not isinstance(self.listing_platform, Unset):
            listing_platform = self.listing_platform.value


        locale: str | Unset = UNSET
        if not isinstance(self.locale, Unset):
            locale = self.locale.value


        origin_platform_product_type = self.origin_platform_product_type

        origin_platform_vendor = self.origin_platform_vendor

        origin_platform_tags: list[str] | Unset = UNSET
        if not isinstance(self.origin_platform_tags, Unset):
            origin_platform_tags = self.origin_platform_tags



        origin_platform_category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.origin_platform_category, Unset):
            origin_platform_category = self.origin_platform_category.to_dict()

        origin_platform_product_meta_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.origin_platform_product_meta_data, Unset):
            origin_platform_product_meta_data = self.origin_platform_product_meta_data.to_dict()

        is_live_quick = self.is_live_quick


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "product_title": product_title,
        })
        if category_version is not UNSET:
            field_dict["category_version"] = category_version
        if description is not UNSET:
            field_dict["description"] = description
        if images is not UNSET:
            field_dict["images"] = images
        if include_prohibited_categories is not UNSET:
            field_dict["include_prohibited_categories"] = include_prohibited_categories
        if listing_platform is not UNSET:
            field_dict["listing_platform"] = listing_platform
        if locale is not UNSET:
            field_dict["locale"] = locale
        if origin_platform_product_type is not UNSET:
            field_dict["origin_platform_product_type"] = origin_platform_product_type
        if origin_platform_vendor is not UNSET:
            field_dict["origin_platform_vendor"] = origin_platform_vendor
        if origin_platform_tags is not UNSET:
            field_dict["origin_platform_tags"] = origin_platform_tags
        if origin_platform_category is not UNSET:
            field_dict["origin_platform_category"] = origin_platform_category
        if origin_platform_product_meta_data is not UNSET:
            field_dict["origin_platform_product_meta_data"] = origin_platform_product_meta_data
        if is_live_quick is not UNSET:
            field_dict["is_live_quick"] = is_live_quick

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.diagnose_and_optimize_product_request_size_chart_image import DiagnoseAndOptimizeProductRequestSizeChartImage # noqa: PLC0415
        from ..models.recommend_category_request_origin_platform_category import RecommendCategoryRequestOriginPlatformCategory # noqa: PLC0415
        from ..models.recommend_category_request_origin_platform_product_meta_data import RecommendCategoryRequestOriginPlatformProductMetaData # noqa: PLC0415
        d = dict(src_dict)
        product_title = d.pop("product_title")

        category_version = d.pop("category_version", UNSET)

        description = d.pop("description", UNSET)

        _images = d.pop("images", UNSET)
        images: list[DiagnoseAndOptimizeProductRequestSizeChartImage] | Unset = UNSET
        if _images is not UNSET:
            images = []
            for images_item_data in _images:
                images_item = DiagnoseAndOptimizeProductRequestSizeChartImage.from_dict(images_item_data)



                images.append(images_item)


        include_prohibited_categories = d.pop("include_prohibited_categories", UNSET)

        _listing_platform = d.pop("listing_platform", UNSET)
        listing_platform: RecommendCategoryRequestListingPlatform | Unset
        if isinstance(_listing_platform,  Unset):
            listing_platform = UNSET
        else:
            listing_platform = RecommendCategoryRequestListingPlatform(_listing_platform)




        _locale = d.pop("locale", UNSET)
        locale: RecommendCategoryRequestLocale | Unset
        if isinstance(_locale,  Unset):
            locale = UNSET
        else:
            locale = RecommendCategoryRequestLocale(_locale)




        origin_platform_product_type = d.pop("origin_platform_product_type", UNSET)

        origin_platform_vendor = d.pop("origin_platform_vendor", UNSET)

        origin_platform_tags = cast(list[str], d.pop("origin_platform_tags", UNSET))


        _origin_platform_category = d.pop("origin_platform_category", UNSET)
        origin_platform_category: RecommendCategoryRequestOriginPlatformCategory | Unset
        if isinstance(_origin_platform_category,  Unset):
            origin_platform_category = UNSET
        else:
            origin_platform_category = RecommendCategoryRequestOriginPlatformCategory.from_dict(_origin_platform_category)




        _origin_platform_product_meta_data = d.pop("origin_platform_product_meta_data", UNSET)
        origin_platform_product_meta_data: RecommendCategoryRequestOriginPlatformProductMetaData | Unset
        if isinstance(_origin_platform_product_meta_data,  Unset):
            origin_platform_product_meta_data = UNSET
        else:
            origin_platform_product_meta_data = RecommendCategoryRequestOriginPlatformProductMetaData.from_dict(_origin_platform_product_meta_data)




        is_live_quick = d.pop("is_live_quick", UNSET)

        recommend_category_request = cls(
            product_title=product_title,
            category_version=category_version,
            description=description,
            images=images,
            include_prohibited_categories=include_prohibited_categories,
            listing_platform=listing_platform,
            locale=locale,
            origin_platform_product_type=origin_platform_product_type,
            origin_platform_vendor=origin_platform_vendor,
            origin_platform_tags=origin_platform_tags,
            origin_platform_category=origin_platform_category,
            origin_platform_product_meta_data=origin_platform_product_meta_data,
            is_live_quick=is_live_quick,
        )


        recommend_category_request.additional_properties = d
        return recommend_category_request

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
