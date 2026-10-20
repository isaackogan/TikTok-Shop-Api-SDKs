from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.check_product_listing_request_listing_platforms_item import CheckProductListingRequestListingPlatformsItem
from ..models.check_product_listing_request_locale import CheckProductListingRequestLocale
from ..models.check_product_listing_request_selling_format import CheckProductListingRequestSellingFormat
from ..models.check_product_listing_request_shipping_insurance_requirement import (
    CheckProductListingRequestShippingInsuranceRequirement,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.certification import Certification
    from ..models.check_product_listing_request_option import CheckProductListingRequestOption
    from ..models.check_product_listing_request_sku import CheckProductListingRequestSku
    from ..models.main_image import MainImage
    from ..models.package_dimension import PackageDimension
    from ..models.package_weight import PackageWeight
    from ..models.product_attribute import ProductAttribute
    from ..models.product_tag_operation import ProductTagOperation
    from ..models.scheduled_sale import ScheduledSale
    from ..models.size_chart import SizeChart
    from ..models.video import Video


T = TypeVar("T", bound="CheckProductListingRequest")


@_attrs_define
class CheckProductListingRequest:
    """
    Attributes:
        description (str): The product description in HTML format.

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
        category_id (str): The ID of a leaf category for this product. Use the [Get Categories
            API](https://partner.tiktokshop.com/docv2/page/6509c89d0fcef602bf1acd9b) to obtain the available categories.

            **Note**:
            - Refer to TikTok Shop Academy for information on product category restrictions.
            - For the US market, if you are creating products in `INVITE_ONLY` categories, you must submit a separate
            application through the Qualification Center on TikTok Shop Seller Center to gain access. Otherwise, even if the
            product audit is passed, the product will not be listed and made available to buyers. (The product status will
            be `PENDING` and the audit status will be `PRE_APPROVED`)
            - For the Indonesia market, to list a product on both TikTok Shop and Tokopedia, you must use only categories
            that are available on both platforms.
        main_images (list[MainImage]): A list of images to display in the product image gallery.
            - Max count: 9
            - Arrange your image URIs in the sequence that they should appear on TikTok Shop.
            - Image dimensions: [300x300 px, 4000x4000 px]

            **Recommendations**:
            - Use a minimum of 5 images.
            - The first image should have a white background. Use the [Optimize Images
            API](https://partner.tiktokshop.com/docv2/page/665692b35d39dc02deb49a97) to change the background to white.
        skus (list[CheckProductListingRequestSku]): A list of Stock Keeping Units (SKUs) used to identify distinct
            variants of the product.

            **Note**:
            - Max SKUs for BR, EU, JP, MX, UK, US: 300
            - Max SKUs for other regions: 100

            **Recommendations**: Place the most important variant at the beginning of the array.
        title (str): The product title.
            Title length:
            - DE, ES, FR, IE, IT, JP, UK, US: [1, 255]
            - BR, MX: [1, 300]
            - Other regions: [25, 255]
        brand_id (str | Unset): The ID of the brand of this product.
            Use the [Get Brands API](https://partner.tiktokshop.com/docv2/page/6503075656e2bb0289dd5d01) to get the list of
            available brands for a shop.
            **Note**: Unauthorized brands won't be displayed on TikTok Shop.
        is_cod_allowed (bool | Unset): A flag indicating whether to show the Cash On Delivery (COD) payment option
            during checkout. Use the [Get Category Rules
            API](https://partner.tiktokshop.com/docv2/page/6509c0febace3e02b74594a9) to check if COD is supported for your
            product category.

            Applicable only for the following markets:
            - Global sellers: MY, PH, SA, TH, VN
            - Local sellers: ID, MY, PH, SA, TH, VN

            **Note**: If COD is not supported, the listing will fail if you set this to `true`.
        certifications (list[Certification] | Unset): The list of certifications for your product.
            Max count: 10

            As per TikTok Shop guidelines, certifications are required for certain restricted product categories. Retrieve
            the certification requirements for your product from the  [Get Category Rules
            API](https://partner.tiktokshop.com/docv2/page/6509c0febace3e02b74594a9). Refer to [TikTok Shop Restricted
            Products Policy](https://seller-
            us.tiktok.com/university/essay?identity=1&role=1&knowledge_id=3238037484275457&from=policy) for information on
            product category restrictions.
        package_weight (PackageWeight | Unset):
        product_attributes (list[ProductAttribute] | Unset): A list of general attributes (e.g. manufacturer, country of
            origin, materials used) that describe the product as a whole, regardless of variant.

            **Important**: The attributes available for use are determined by the system based on the product's assigned
            category, with some being mandatory. You must provide the product attributes marked as `is_required` in the
            response of the [Get Attributes API](6509c5784a0bb702c0561cc8) to avoid listing failure.
        size_chart (SizeChart | Unset):
        package_dimensions (PackageDimension | Unset):
        external_product_id (str | Unset): An external identifier used in an external ecommerce platform. This is used
            to associate the product between TikTok Shop and the external ecommerce platform.
            Max length: 999 characters
        delivery_option_ids (list[str] | Unset): This field is supported for seller accounts in the following regions
            only:
            - ID
            - MX
            - MY
            - PH
            - SG
            - TH
            - VN

            The custom delivery option IDs to apply to this product if you want to override the default warehouse delivery
            options. To retrieve the available option IDs, call [Get Warehouse Delivery Options](650aa46ebace3e02b75d9afa)
            with `scope=PRODUCT`.

            **Note**: Leave this field blank to inherit the default delivery options configured for the warehouse.
        video (Video | Unset):
        primary_combined_product_id (str | Unset): If this product is associated with a virtual bundle, this value is
            the ID of the primary product in the bundle.

            **Note**: Required only for virtual bundle products.
        manufacturer_ids (list[str] | Unset): A list of manufacturer IDs. Retrieve the IDs from the [Search
            Manufacturers API](67066a580dcee902fa03ccf9).

            **Note**: Applicable only for the EU market in certain categories. Use the [Get Category Rules
            API](6509c0febace3e02b74594a9) to check the requirements.
        responsible_person_ids (list[str] | Unset): A list of responsible person IDs. Retrieve the IDs from the [Search
            Responsible Persons API](67066a55f17b7d02f95d2fb1).

            **Note**: Applicable only for the EU market in certain categories. Use the [Get Category Rules
            API](6509c0febace3e02b74594a9) to check the requirements.
        listing_platforms (list[CheckProductListingRequestListingPlatformsItem] | Unset): The platforms for listing the
            product.
            Possible values:
            - TOKOPEDIA
            - TIKTOK_SHOP
            Default: TIKTOK_SHOP

            Applicable only for sellers that migrated from Tokopedia.
        shipping_insurance_requirement (CheckProductListingRequestShippingInsuranceRequirement | Unset): The shipping
            insurance purchase requirement imposed on buyers for the product.

            Possible values:
            - REQUIRED: Shipping insurance is mandatory and buyers can't opt out.
            - OPTIONAL: Buyers can choose to purchase shipping insurance through the platform.
            - NOT_SUPPORTED: Shipping insurance is not supported for the product.
            Default: OPTIONAL

            Applicable only if the listing platforms include TOKOPEDIA.
        is_pre_owned (bool | Unset): A flag to indicate if the product is pre-owned.

            Applicable only if TOKOPEDIA is the sole listing platform.
            **Note**: To list pre-owned products on the TikTok Shop platform, please specify the ID of one of the designated
            pre-owned product categories (e.g. pre-owned luxury bags, luggage, and accessories) in `category_id`.
        minimum_order_quantity (int | Unset): The minimum order quantity for the product.
            Valid range: [1, 20]

            Applicable only for the Indonesia market and selected sellers in other SEA markets. Contact your account manager
            for more information about gaining access to this field.
        shipping_template_id (str | Unset): Identifier of the shipping template that will be bound to the product
        option (CheckProductListingRequestOption | Unset):
        scheduled_sale (ScheduledSale | Unset):
        search_terms (list[str] | Unset): Search terms (ST words). ST words will not be displayed to consumers; they are
            only used in search engines to increase your search weight and gain more traffic. Please ensure that ST words
            are consistent with the product description, with a maximum of 15 terms and a total of no more than 250
            characters.
        key_product_features (list[str] | Unset): Key Product Features. They will be displayed in the Product highlight
            module on the product detail page and will be used by search engines to increase your search weight for more
            traffic. The total number of items should not exceed 5, and the total character count should not exceed 1500.
        product_tag_operations (list[ProductTagOperation] | Unset): Legacy operations for enabling or disabling the
            `AUCTION` product tag. If `selling_format` is provided, it takes precedence over this field.
        locale (CheckProductListingRequestLocale | Unset): The BCP-47 locale codes for displaying category information.
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
        selling_format (CheckProductListingRequestSellingFormat | Unset): Choose either Fixed price or Fixed price and
            LIVE auction. Fixed price is selected by default. LIVE auction require a starting bid price. Possible values:
            FIXED_PRICE, FIXED_PRICE_AND_LIVE_AUCTION.
        is_live_quick (bool | Unset): false — NORMAL products
            true — LIVE_QUICK products. Only seller with the required permissions can creat LIVE_QUICK products.
            Default: false
    """

    description: str
    category_id: str
    main_images: list[MainImage]
    skus: list[CheckProductListingRequestSku]
    title: str
    brand_id: str | Unset = UNSET
    is_cod_allowed: bool | Unset = UNSET
    certifications: list[Certification] | Unset = UNSET
    package_weight: PackageWeight | Unset = UNSET
    product_attributes: list[ProductAttribute] | Unset = UNSET
    size_chart: SizeChart | Unset = UNSET
    package_dimensions: PackageDimension | Unset = UNSET
    external_product_id: str | Unset = UNSET
    delivery_option_ids: list[str] | Unset = UNSET
    video: Video | Unset = UNSET
    primary_combined_product_id: str | Unset = UNSET
    manufacturer_ids: list[str] | Unset = UNSET
    responsible_person_ids: list[str] | Unset = UNSET
    listing_platforms: list[CheckProductListingRequestListingPlatformsItem] | Unset = UNSET
    shipping_insurance_requirement: CheckProductListingRequestShippingInsuranceRequirement | Unset = UNSET
    is_pre_owned: bool | Unset = UNSET
    minimum_order_quantity: int | Unset = UNSET
    shipping_template_id: str | Unset = UNSET
    option: CheckProductListingRequestOption | Unset = UNSET
    scheduled_sale: ScheduledSale | Unset = UNSET
    search_terms: list[str] | Unset = UNSET
    key_product_features: list[str] | Unset = UNSET
    product_tag_operations: list[ProductTagOperation] | Unset = UNSET
    locale: CheckProductListingRequestLocale | Unset = UNSET
    selling_format: CheckProductListingRequestSellingFormat | Unset = UNSET
    is_live_quick: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        category_id = self.category_id

        main_images = []
        for main_images_item_data in self.main_images:
            main_images_item = main_images_item_data.to_dict()
            main_images.append(main_images_item)

        skus = []
        for skus_item_data in self.skus:
            skus_item = skus_item_data.to_dict()
            skus.append(skus_item)

        title = self.title

        brand_id = self.brand_id

        is_cod_allowed = self.is_cod_allowed

        certifications: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.certifications, Unset):
            certifications = []
            for certifications_item_data in self.certifications:
                certifications_item = certifications_item_data.to_dict()
                certifications.append(certifications_item)

        package_weight: dict[str, Any] | Unset = UNSET
        if not isinstance(self.package_weight, Unset):
            package_weight = self.package_weight.to_dict()

        product_attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.product_attributes, Unset):
            product_attributes = []
            for product_attributes_item_data in self.product_attributes:
                product_attributes_item = product_attributes_item_data.to_dict()
                product_attributes.append(product_attributes_item)

        size_chart: dict[str, Any] | Unset = UNSET
        if not isinstance(self.size_chart, Unset):
            size_chart = self.size_chart.to_dict()

        package_dimensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.package_dimensions, Unset):
            package_dimensions = self.package_dimensions.to_dict()

        external_product_id = self.external_product_id

        delivery_option_ids: list[str] | Unset = UNSET
        if not isinstance(self.delivery_option_ids, Unset):
            delivery_option_ids = self.delivery_option_ids

        video: dict[str, Any] | Unset = UNSET
        if not isinstance(self.video, Unset):
            video = self.video.to_dict()

        primary_combined_product_id = self.primary_combined_product_id

        manufacturer_ids: list[str] | Unset = UNSET
        if not isinstance(self.manufacturer_ids, Unset):
            manufacturer_ids = self.manufacturer_ids

        responsible_person_ids: list[str] | Unset = UNSET
        if not isinstance(self.responsible_person_ids, Unset):
            responsible_person_ids = self.responsible_person_ids

        listing_platforms: list[str] | Unset = UNSET
        if not isinstance(self.listing_platforms, Unset):
            listing_platforms = []
            for listing_platforms_item_data in self.listing_platforms:
                listing_platforms_item = listing_platforms_item_data.value
                listing_platforms.append(listing_platforms_item)

        shipping_insurance_requirement: str | Unset = UNSET
        if not isinstance(self.shipping_insurance_requirement, Unset):
            shipping_insurance_requirement = self.shipping_insurance_requirement.value

        is_pre_owned = self.is_pre_owned

        minimum_order_quantity = self.minimum_order_quantity

        shipping_template_id = self.shipping_template_id

        option: dict[str, Any] | Unset = UNSET
        if not isinstance(self.option, Unset):
            option = self.option.to_dict()

        scheduled_sale: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scheduled_sale, Unset):
            scheduled_sale = self.scheduled_sale.to_dict()

        search_terms: list[str] | Unset = UNSET
        if not isinstance(self.search_terms, Unset):
            search_terms = self.search_terms

        key_product_features: list[str] | Unset = UNSET
        if not isinstance(self.key_product_features, Unset):
            key_product_features = self.key_product_features

        product_tag_operations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.product_tag_operations, Unset):
            product_tag_operations = []
            for product_tag_operations_item_data in self.product_tag_operations:
                product_tag_operations_item = product_tag_operations_item_data.to_dict()
                product_tag_operations.append(product_tag_operations_item)

        locale: str | Unset = UNSET
        if not isinstance(self.locale, Unset):
            locale = self.locale.value

        selling_format: str | Unset = UNSET
        if not isinstance(self.selling_format, Unset):
            selling_format = self.selling_format.value

        is_live_quick = self.is_live_quick

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "category_id": category_id,
                "main_images": main_images,
                "skus": skus,
                "title": title,
            }
        )
        if brand_id is not UNSET:
            field_dict["brand_id"] = brand_id
        if is_cod_allowed is not UNSET:
            field_dict["is_cod_allowed"] = is_cod_allowed
        if certifications is not UNSET:
            field_dict["certifications"] = certifications
        if package_weight is not UNSET:
            field_dict["package_weight"] = package_weight
        if product_attributes is not UNSET:
            field_dict["product_attributes"] = product_attributes
        if size_chart is not UNSET:
            field_dict["size_chart"] = size_chart
        if package_dimensions is not UNSET:
            field_dict["package_dimensions"] = package_dimensions
        if external_product_id is not UNSET:
            field_dict["external_product_id"] = external_product_id
        if delivery_option_ids is not UNSET:
            field_dict["delivery_option_ids"] = delivery_option_ids
        if video is not UNSET:
            field_dict["video"] = video
        if primary_combined_product_id is not UNSET:
            field_dict["primary_combined_product_id"] = primary_combined_product_id
        if manufacturer_ids is not UNSET:
            field_dict["manufacturer_ids"] = manufacturer_ids
        if responsible_person_ids is not UNSET:
            field_dict["responsible_person_ids"] = responsible_person_ids
        if listing_platforms is not UNSET:
            field_dict["listing_platforms"] = listing_platforms
        if shipping_insurance_requirement is not UNSET:
            field_dict["shipping_insurance_requirement"] = shipping_insurance_requirement
        if is_pre_owned is not UNSET:
            field_dict["is_pre_owned"] = is_pre_owned
        if minimum_order_quantity is not UNSET:
            field_dict["minimum_order_quantity"] = minimum_order_quantity
        if shipping_template_id is not UNSET:
            field_dict["shipping_template_id"] = shipping_template_id
        if option is not UNSET:
            field_dict["option"] = option
        if scheduled_sale is not UNSET:
            field_dict["scheduled_sale"] = scheduled_sale
        if search_terms is not UNSET:
            field_dict["search_terms"] = search_terms
        if key_product_features is not UNSET:
            field_dict["key_product_features"] = key_product_features
        if product_tag_operations is not UNSET:
            field_dict["product_tag_operations"] = product_tag_operations
        if locale is not UNSET:
            field_dict["locale"] = locale
        if selling_format is not UNSET:
            field_dict["selling_format"] = selling_format
        if is_live_quick is not UNSET:
            field_dict["is_live_quick"] = is_live_quick

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.certification import Certification  # noqa: PLC0415
        from ..models.check_product_listing_request_option import CheckProductListingRequestOption  # noqa: PLC0415
        from ..models.check_product_listing_request_sku import CheckProductListingRequestSku  # noqa: PLC0415
        from ..models.main_image import MainImage  # noqa: PLC0415
        from ..models.package_dimension import PackageDimension  # noqa: PLC0415
        from ..models.package_weight import PackageWeight  # noqa: PLC0415
        from ..models.product_attribute import ProductAttribute  # noqa: PLC0415
        from ..models.product_tag_operation import ProductTagOperation  # noqa: PLC0415
        from ..models.scheduled_sale import ScheduledSale  # noqa: PLC0415
        from ..models.size_chart import SizeChart  # noqa: PLC0415
        from ..models.video import Video  # noqa: PLC0415

        d = dict(src_dict)
        description = d.pop("description")

        category_id = d.pop("category_id")

        main_images = []
        _main_images = d.pop("main_images")
        for main_images_item_data in _main_images:
            main_images_item = MainImage.from_dict(main_images_item_data)

            main_images.append(main_images_item)

        skus = []
        _skus = d.pop("skus")
        for skus_item_data in _skus:
            skus_item = CheckProductListingRequestSku.from_dict(skus_item_data)

            skus.append(skus_item)

        title = d.pop("title")

        brand_id = d.pop("brand_id", UNSET)

        is_cod_allowed = d.pop("is_cod_allowed", UNSET)

        _certifications = d.pop("certifications", UNSET)
        certifications: list[Certification] | Unset = UNSET
        if _certifications is not UNSET:
            certifications = []
            for certifications_item_data in _certifications:
                certifications_item = Certification.from_dict(certifications_item_data)

                certifications.append(certifications_item)

        _package_weight = d.pop("package_weight", UNSET)
        package_weight: PackageWeight | Unset
        if isinstance(_package_weight, Unset):
            package_weight = UNSET
        else:
            package_weight = PackageWeight.from_dict(_package_weight)

        _product_attributes = d.pop("product_attributes", UNSET)
        product_attributes: list[ProductAttribute] | Unset = UNSET
        if _product_attributes is not UNSET:
            product_attributes = []
            for product_attributes_item_data in _product_attributes:
                product_attributes_item = ProductAttribute.from_dict(product_attributes_item_data)

                product_attributes.append(product_attributes_item)

        _size_chart = d.pop("size_chart", UNSET)
        size_chart: SizeChart | Unset
        if isinstance(_size_chart, Unset):
            size_chart = UNSET
        else:
            size_chart = SizeChart.from_dict(_size_chart)

        _package_dimensions = d.pop("package_dimensions", UNSET)
        package_dimensions: PackageDimension | Unset
        if isinstance(_package_dimensions, Unset):
            package_dimensions = UNSET
        else:
            package_dimensions = PackageDimension.from_dict(_package_dimensions)

        external_product_id = d.pop("external_product_id", UNSET)

        delivery_option_ids = cast(list[str], d.pop("delivery_option_ids", UNSET))

        _video = d.pop("video", UNSET)
        video: Video | Unset
        if isinstance(_video, Unset):
            video = UNSET
        else:
            video = Video.from_dict(_video)

        primary_combined_product_id = d.pop("primary_combined_product_id", UNSET)

        manufacturer_ids = cast(list[str], d.pop("manufacturer_ids", UNSET))

        responsible_person_ids = cast(list[str], d.pop("responsible_person_ids", UNSET))

        _listing_platforms = d.pop("listing_platforms", UNSET)
        listing_platforms: list[CheckProductListingRequestListingPlatformsItem] | Unset = UNSET
        if _listing_platforms is not UNSET:
            listing_platforms = []
            for listing_platforms_item_data in _listing_platforms:
                listing_platforms_item = CheckProductListingRequestListingPlatformsItem(listing_platforms_item_data)

                listing_platforms.append(listing_platforms_item)

        _shipping_insurance_requirement = d.pop("shipping_insurance_requirement", UNSET)
        shipping_insurance_requirement: CheckProductListingRequestShippingInsuranceRequirement | Unset
        if isinstance(_shipping_insurance_requirement, Unset):
            shipping_insurance_requirement = UNSET
        else:
            shipping_insurance_requirement = CheckProductListingRequestShippingInsuranceRequirement(
                _shipping_insurance_requirement
            )

        is_pre_owned = d.pop("is_pre_owned", UNSET)

        minimum_order_quantity = d.pop("minimum_order_quantity", UNSET)

        shipping_template_id = d.pop("shipping_template_id", UNSET)

        _option = d.pop("option", UNSET)
        option: CheckProductListingRequestOption | Unset
        if isinstance(_option, Unset):
            option = UNSET
        else:
            option = CheckProductListingRequestOption.from_dict(_option)

        _scheduled_sale = d.pop("scheduled_sale", UNSET)
        scheduled_sale: ScheduledSale | Unset
        if isinstance(_scheduled_sale, Unset):
            scheduled_sale = UNSET
        else:
            scheduled_sale = ScheduledSale.from_dict(_scheduled_sale)

        search_terms = cast(list[str], d.pop("search_terms", UNSET))

        key_product_features = cast(list[str], d.pop("key_product_features", UNSET))

        _product_tag_operations = d.pop("product_tag_operations", UNSET)
        product_tag_operations: list[ProductTagOperation] | Unset = UNSET
        if _product_tag_operations is not UNSET:
            product_tag_operations = []
            for product_tag_operations_item_data in _product_tag_operations:
                product_tag_operations_item = ProductTagOperation.from_dict(product_tag_operations_item_data)

                product_tag_operations.append(product_tag_operations_item)

        _locale = d.pop("locale", UNSET)
        locale: CheckProductListingRequestLocale | Unset
        if isinstance(_locale, Unset):
            locale = UNSET
        else:
            locale = CheckProductListingRequestLocale(_locale)

        _selling_format = d.pop("selling_format", UNSET)
        selling_format: CheckProductListingRequestSellingFormat | Unset
        if isinstance(_selling_format, Unset):
            selling_format = UNSET
        else:
            selling_format = CheckProductListingRequestSellingFormat(_selling_format)

        is_live_quick = d.pop("is_live_quick", UNSET)

        check_product_listing_request = cls(
            description=description,
            category_id=category_id,
            main_images=main_images,
            skus=skus,
            title=title,
            brand_id=brand_id,
            is_cod_allowed=is_cod_allowed,
            certifications=certifications,
            package_weight=package_weight,
            product_attributes=product_attributes,
            size_chart=size_chart,
            package_dimensions=package_dimensions,
            external_product_id=external_product_id,
            delivery_option_ids=delivery_option_ids,
            video=video,
            primary_combined_product_id=primary_combined_product_id,
            manufacturer_ids=manufacturer_ids,
            responsible_person_ids=responsible_person_ids,
            listing_platforms=listing_platforms,
            shipping_insurance_requirement=shipping_insurance_requirement,
            is_pre_owned=is_pre_owned,
            minimum_order_quantity=minimum_order_quantity,
            shipping_template_id=shipping_template_id,
            option=option,
            scheduled_sale=scheduled_sale,
            search_terms=search_terms,
            key_product_features=key_product_features,
            product_tag_operations=product_tag_operations,
            locale=locale,
            selling_format=selling_format,
            is_live_quick=is_live_quick,
        )

        check_product_listing_request.additional_properties = d
        return check_product_listing_request

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
