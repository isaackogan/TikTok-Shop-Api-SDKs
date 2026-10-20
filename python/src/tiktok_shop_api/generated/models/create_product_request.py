from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_product_request_listing_platforms_item import CreateProductRequestListingPlatformsItem
from ..models.create_product_request_locale import CreateProductRequestLocale
from ..models.create_product_request_save_mode import CreateProductRequestSaveMode
from ..models.create_product_request_selling_format import CreateProductRequestSellingFormat
from ..models.create_product_request_shipping_insurance_requirement import (
    CreateProductRequestShippingInsuranceRequirement,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.certification import Certification
    from ..models.create_product_request_product_attribute import CreateProductRequestProductAttribute
    from ..models.create_product_request_sku import CreateProductRequestSku
    from ..models.main_image import MainImage
    from ..models.package_dimension import PackageDimension
    from ..models.package_weight import PackageWeight
    from ..models.product_tag_operation import ProductTagOperation
    from ..models.purchase_order_quantity_limit import PurchaseOrderQuantityLimit
    from ..models.scheduled_sale import ScheduledSale
    from ..models.size_chart import SizeChart
    from ..models.video import Video


T = TypeVar("T", bound="CreateProductRequest")


@_attrs_define
class CreateProductRequest:
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
        category_id (str): The ID of the category of this product. It must be a leaf category that corresponds to the
            category tree type specified in the `category_version` property. Use the [Get Categories
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
            - The first image should have a white background. Use the [Optimize Images API](665692b35d39dc02deb49a97) to
            change the background to white.
        skus (list[CreateProductRequestSku]): A list of Stock Keeping Units (SKUs) used to identify distinct variants of
            the product.

            **Note**:
            - Max SKUs for BR, EU, JP, MX, UK, US: 300
            - Max SKUs for other regions: 100

            **Recommendations**: Place the most important variant at the beginning of the array.
        title (str): The product title.
            Title length:
            - DE, ES, FR, IE, IT, JP, UK, US: [1, 255]
            - BR, MX: [1, 300]
            - Other regions: [25, 255]
        save_mode (CreateProductRequestSaveMode | Unset): Indicates how the product should be saved.
            Possible values:
            - AS_DRAFT: Save the product as a draft for future editing.
            - LISTING: Immediately list the product in the shop.
            Default: LISTING
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
        package_dimensions (PackageDimension | Unset):
        product_attributes (list[CreateProductRequestProductAttribute] | Unset): A list of general attributes (e.g.
            manufacturer, country of origin, materials used) that describe the product as a whole, regardless of variant.

            **Important**: The attributes available for use are determined by the system based on the product's assigned
            category, with some being mandatory. You must provide the product attributes marked as `is_required` in the
            response of the [Get Attributes API](6509c5784a0bb702c0561cc8) to avoid listing failure.
        package_weight (PackageWeight | Unset):
        video (Video | Unset):
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

            For all other regions, this field is NOT used and will NOT be processed if passed for create, edit, or partial
            edit operations.

            The custom delivery option IDs to apply to this product if you want to override the default warehouse delivery
            options. To retrieve the available option IDs, call [Get Warehouse Delivery Options](650aa46ebace3e02b75d9afa)
            with `scope=PRODUCT`.

            **Note**: Leave this field blank to inherit the default delivery options configured for the warehouse.
        size_chart (SizeChart | Unset):
        primary_combined_product_id (str | Unset): If this product is associated with a virtual bundle, this value is
            the ID of the primary product in the bundle.

            **Note**: Required only for virtual bundle products.
        is_not_for_sale (bool | Unset): A flag indicating whether the product is not for sale and only available through
            Gift with Purchase (GWP) promotions. Such products won't appear in searches or recommendations
            True: Not for sale
            False: For sale
        category_version (str | Unset): The category tree version to assign this product to.
            Possible values based on region:
            - US and SEA regions: `v2`, represents the 7-level category tree.
              **Important**: For US and SEA shops, you must pass `v2` when using this API.
            - Other regions: `v1`, represents the 3-level category tree.
            Default: `v1`
        manufacturer_ids (list[str] | Unset): A list of manufacturer IDs. Retrieve the IDs from the [Search
            Manufacturers API](67066a580dcee902fa03ccf9).

            **Note**: Applicable only for the EU market in certain categories. Use the [Get Category Rules
            API](6509c0febace3e02b74594a9) to check the requirements.
        responsible_person_ids (list[str] | Unset): A list of responsible person IDs. Retrieve the IDs from the [Search
            Responsible Persons API](67066a55f17b7d02f95d2fb1).

            **Note**: Applicable only for the EU market in certain categories. Use the [Get Category Rules
            API](6509c0febace3e02b74594a9) to check the requirements.
        listing_platforms (list[CreateProductRequestListingPlatformsItem] | Unset): The platforms for listing the
            product.
            Possible values:
            - TOKOPEDIA
            - TIKTOK_SHOP
            Default: TIKTOK_SHOP

            Applicable only for sellers that migrated from Tokopedia.
        shipping_insurance_requirement (CreateProductRequestShippingInsuranceRequirement | Unset): The shipping
            insurance purchase requirement imposed on buyers for the product.

            Possible values:
            - REQUIRED: Shipping insurance is mandatory and buyers can't opt out.
            - OPTIONAL: Buyers can choose to purchase shipping insurance through the platform.
            - NOT_SUPPORTED: Shipping insurance is not supported for the product.
            Default: OPTIONAL

            Applicable only if the listing platforms include TOKOPEDIA.
        minimum_order_quantity (int | Unset): The minimum order quantity for the product.
            Valid range: [1, 20]

            Applicable only for the Indonesia market and selected sellers in other SEA markets. Contact your account manager
            for more information about gaining access to this field.
        is_pre_owned (bool | Unset): A flag to indicate if the product is pre-owned.

            Applicable only if TOKOPEDIA is the sole listing platform.
            **Note**: To list pre-owned products on the TikTok Shop platform, please specify the ID of one of the designated
            pre-owned product categories (e.g. pre-owned luxury bags, luggage, and accessories) in `category_id`.
        idempotency_key (str | Unset): A unique key to recognize a request and prevent duplicate processing of the same
            request, especially in cases of connection issues. Ensure this key is unique within the shop for each request to
            avoid accidental duplicates. It can be used to track requests across the shop.
            Max length: 128 characters

            **Note**: We recommend that you generate v4 UUIDs for use as keys.
        shipping_template_id (str | Unset): Identifier of the shipping template that will be bound to the product
        scheduled_sale (ScheduledSale | Unset):
        locale (CreateProductRequestLocale | Unset): The BCP-47 locale codes for displaying category information.
            Default: The default locale of your shop. Possible values:
            - `de-DE`
            - `en-GB`
            - `en-IE`
            - `en-US`
            - `es-ES`
            - `es-MX`
            - `fr-FR`
            - `id-ID`
            - `it-IT`
            - `ja-JP`
            - `ms-MY`
            - `pt-BR`
            - `th-TH`
            - `vi-VN`
            - `zh-CN`
        auto_translate_enabled (bool | Unset): The field works only if products need to list with more than one
            languages in determined country, otherwise it does not need to fill in.
        search_terms (list[str] | Unset): Search terms (ST words). ST words will not be displayed to consumers; they are
            only used in search engines to increase your search weight and gain more traffic. Please ensure that ST words
            are consistent with the product description, with a maximum of 15 terms and a total of no more than 250
            characters.
        key_product_features (list[str] | Unset): Key Product Features. They will be displayed in the Product highlight
            module on the product detail page and will be used by search engines to increase your search weight for more
            traffic. The total number of items should not exceed 5, and the total character count should not exceed 1500.
        product_tag_operations (list[ProductTagOperation] | Unset): product tag to identity special type
            product.Possible values: AUCTION
        purchase_order_quantity_limit (PurchaseOrderQuantityLimit | Unset):
        selling_format (CreateProductRequestSellingFormat | Unset): Choose either Fixed price or Fixed price and LIVE
            auction. Fixed price is selected by default. LIVE auction requires a starting bid price. Possible values:
            FIXED_PRICE, FIXED_PRICE_AND_LIVE_AUCTION. If `selling_format` is provided, it takes priority over the legacy
            `product_tag_operations` field; `product_tag_operations` is used only when `selling_format` is not provided.
        is_live_quick (bool | Unset): false — NORMAL products
            true — LIVE_QUICK products. Only seller with the required permissions can creat LIVE_QUICK products.
            Default: false
        is_blind_box (bool | Unset): Whether the product is a blind box of lucky bag. For example: PopMart
    """

    description: str
    category_id: str
    main_images: list[MainImage]
    skus: list[CreateProductRequestSku]
    title: str
    save_mode: CreateProductRequestSaveMode | Unset = UNSET
    brand_id: str | Unset = UNSET
    is_cod_allowed: bool | Unset = UNSET
    certifications: list[Certification] | Unset = UNSET
    package_dimensions: PackageDimension | Unset = UNSET
    product_attributes: list[CreateProductRequestProductAttribute] | Unset = UNSET
    package_weight: PackageWeight | Unset = UNSET
    video: Video | Unset = UNSET
    external_product_id: str | Unset = UNSET
    delivery_option_ids: list[str] | Unset = UNSET
    size_chart: SizeChart | Unset = UNSET
    primary_combined_product_id: str | Unset = UNSET
    is_not_for_sale: bool | Unset = UNSET
    category_version: str | Unset = UNSET
    manufacturer_ids: list[str] | Unset = UNSET
    responsible_person_ids: list[str] | Unset = UNSET
    listing_platforms: list[CreateProductRequestListingPlatformsItem] | Unset = UNSET
    shipping_insurance_requirement: CreateProductRequestShippingInsuranceRequirement | Unset = UNSET
    minimum_order_quantity: int | Unset = UNSET
    is_pre_owned: bool | Unset = UNSET
    idempotency_key: str | Unset = UNSET
    shipping_template_id: str | Unset = UNSET
    scheduled_sale: ScheduledSale | Unset = UNSET
    locale: CreateProductRequestLocale | Unset = UNSET
    auto_translate_enabled: bool | Unset = UNSET
    search_terms: list[str] | Unset = UNSET
    key_product_features: list[str] | Unset = UNSET
    product_tag_operations: list[ProductTagOperation] | Unset = UNSET
    purchase_order_quantity_limit: PurchaseOrderQuantityLimit | Unset = UNSET
    selling_format: CreateProductRequestSellingFormat | Unset = UNSET
    is_live_quick: bool | Unset = UNSET
    is_blind_box: bool | Unset = UNSET
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

        save_mode: str | Unset = UNSET
        if not isinstance(self.save_mode, Unset):
            save_mode = self.save_mode.value

        brand_id = self.brand_id

        is_cod_allowed = self.is_cod_allowed

        certifications: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.certifications, Unset):
            certifications = []
            for certifications_item_data in self.certifications:
                certifications_item = certifications_item_data.to_dict()
                certifications.append(certifications_item)

        package_dimensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.package_dimensions, Unset):
            package_dimensions = self.package_dimensions.to_dict()

        product_attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.product_attributes, Unset):
            product_attributes = []
            for product_attributes_item_data in self.product_attributes:
                product_attributes_item = product_attributes_item_data.to_dict()
                product_attributes.append(product_attributes_item)

        package_weight: dict[str, Any] | Unset = UNSET
        if not isinstance(self.package_weight, Unset):
            package_weight = self.package_weight.to_dict()

        video: dict[str, Any] | Unset = UNSET
        if not isinstance(self.video, Unset):
            video = self.video.to_dict()

        external_product_id = self.external_product_id

        delivery_option_ids: list[str] | Unset = UNSET
        if not isinstance(self.delivery_option_ids, Unset):
            delivery_option_ids = self.delivery_option_ids

        size_chart: dict[str, Any] | Unset = UNSET
        if not isinstance(self.size_chart, Unset):
            size_chart = self.size_chart.to_dict()

        primary_combined_product_id = self.primary_combined_product_id

        is_not_for_sale = self.is_not_for_sale

        category_version = self.category_version

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

        minimum_order_quantity = self.minimum_order_quantity

        is_pre_owned = self.is_pre_owned

        idempotency_key = self.idempotency_key

        shipping_template_id = self.shipping_template_id

        scheduled_sale: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scheduled_sale, Unset):
            scheduled_sale = self.scheduled_sale.to_dict()

        locale: str | Unset = UNSET
        if not isinstance(self.locale, Unset):
            locale = self.locale.value

        auto_translate_enabled = self.auto_translate_enabled

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

        purchase_order_quantity_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.purchase_order_quantity_limit, Unset):
            purchase_order_quantity_limit = self.purchase_order_quantity_limit.to_dict()

        selling_format: str | Unset = UNSET
        if not isinstance(self.selling_format, Unset):
            selling_format = self.selling_format.value

        is_live_quick = self.is_live_quick

        is_blind_box = self.is_blind_box

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
        if save_mode is not UNSET:
            field_dict["save_mode"] = save_mode
        if brand_id is not UNSET:
            field_dict["brand_id"] = brand_id
        if is_cod_allowed is not UNSET:
            field_dict["is_cod_allowed"] = is_cod_allowed
        if certifications is not UNSET:
            field_dict["certifications"] = certifications
        if package_dimensions is not UNSET:
            field_dict["package_dimensions"] = package_dimensions
        if product_attributes is not UNSET:
            field_dict["product_attributes"] = product_attributes
        if package_weight is not UNSET:
            field_dict["package_weight"] = package_weight
        if video is not UNSET:
            field_dict["video"] = video
        if external_product_id is not UNSET:
            field_dict["external_product_id"] = external_product_id
        if delivery_option_ids is not UNSET:
            field_dict["delivery_option_ids"] = delivery_option_ids
        if size_chart is not UNSET:
            field_dict["size_chart"] = size_chart
        if primary_combined_product_id is not UNSET:
            field_dict["primary_combined_product_id"] = primary_combined_product_id
        if is_not_for_sale is not UNSET:
            field_dict["is_not_for_sale"] = is_not_for_sale
        if category_version is not UNSET:
            field_dict["category_version"] = category_version
        if manufacturer_ids is not UNSET:
            field_dict["manufacturer_ids"] = manufacturer_ids
        if responsible_person_ids is not UNSET:
            field_dict["responsible_person_ids"] = responsible_person_ids
        if listing_platforms is not UNSET:
            field_dict["listing_platforms"] = listing_platforms
        if shipping_insurance_requirement is not UNSET:
            field_dict["shipping_insurance_requirement"] = shipping_insurance_requirement
        if minimum_order_quantity is not UNSET:
            field_dict["minimum_order_quantity"] = minimum_order_quantity
        if is_pre_owned is not UNSET:
            field_dict["is_pre_owned"] = is_pre_owned
        if idempotency_key is not UNSET:
            field_dict["idempotency_key"] = idempotency_key
        if shipping_template_id is not UNSET:
            field_dict["shipping_template_id"] = shipping_template_id
        if scheduled_sale is not UNSET:
            field_dict["scheduled_sale"] = scheduled_sale
        if locale is not UNSET:
            field_dict["locale"] = locale
        if auto_translate_enabled is not UNSET:
            field_dict["auto_translate_enabled"] = auto_translate_enabled
        if search_terms is not UNSET:
            field_dict["search_terms"] = search_terms
        if key_product_features is not UNSET:
            field_dict["key_product_features"] = key_product_features
        if product_tag_operations is not UNSET:
            field_dict["product_tag_operations"] = product_tag_operations
        if purchase_order_quantity_limit is not UNSET:
            field_dict["purchase_order_quantity_limit"] = purchase_order_quantity_limit
        if selling_format is not UNSET:
            field_dict["selling_format"] = selling_format
        if is_live_quick is not UNSET:
            field_dict["is_live_quick"] = is_live_quick
        if is_blind_box is not UNSET:
            field_dict["is_blind_box"] = is_blind_box

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.certification import Certification  # noqa: PLC0415
        from ..models.create_product_request_product_attribute import (
            CreateProductRequestProductAttribute,  # noqa: PLC0415
        )
        from ..models.create_product_request_sku import CreateProductRequestSku  # noqa: PLC0415
        from ..models.main_image import MainImage  # noqa: PLC0415
        from ..models.package_dimension import PackageDimension  # noqa: PLC0415
        from ..models.package_weight import PackageWeight  # noqa: PLC0415
        from ..models.product_tag_operation import ProductTagOperation  # noqa: PLC0415
        from ..models.purchase_order_quantity_limit import PurchaseOrderQuantityLimit  # noqa: PLC0415
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
            skus_item = CreateProductRequestSku.from_dict(skus_item_data)

            skus.append(skus_item)

        title = d.pop("title")

        _save_mode = d.pop("save_mode", UNSET)
        save_mode: CreateProductRequestSaveMode | Unset
        if isinstance(_save_mode, Unset):
            save_mode = UNSET
        else:
            save_mode = CreateProductRequestSaveMode(_save_mode)

        brand_id = d.pop("brand_id", UNSET)

        is_cod_allowed = d.pop("is_cod_allowed", UNSET)

        _certifications = d.pop("certifications", UNSET)
        certifications: list[Certification] | Unset = UNSET
        if _certifications is not UNSET:
            certifications = []
            for certifications_item_data in _certifications:
                certifications_item = Certification.from_dict(certifications_item_data)

                certifications.append(certifications_item)

        _package_dimensions = d.pop("package_dimensions", UNSET)
        package_dimensions: PackageDimension | Unset
        if isinstance(_package_dimensions, Unset):
            package_dimensions = UNSET
        else:
            package_dimensions = PackageDimension.from_dict(_package_dimensions)

        _product_attributes = d.pop("product_attributes", UNSET)
        product_attributes: list[CreateProductRequestProductAttribute] | Unset = UNSET
        if _product_attributes is not UNSET:
            product_attributes = []
            for product_attributes_item_data in _product_attributes:
                product_attributes_item = CreateProductRequestProductAttribute.from_dict(product_attributes_item_data)

                product_attributes.append(product_attributes_item)

        _package_weight = d.pop("package_weight", UNSET)
        package_weight: PackageWeight | Unset
        if isinstance(_package_weight, Unset):
            package_weight = UNSET
        else:
            package_weight = PackageWeight.from_dict(_package_weight)

        _video = d.pop("video", UNSET)
        video: Video | Unset
        if isinstance(_video, Unset):
            video = UNSET
        else:
            video = Video.from_dict(_video)

        external_product_id = d.pop("external_product_id", UNSET)

        delivery_option_ids = cast(list[str], d.pop("delivery_option_ids", UNSET))

        _size_chart = d.pop("size_chart", UNSET)
        size_chart: SizeChart | Unset
        if isinstance(_size_chart, Unset):
            size_chart = UNSET
        else:
            size_chart = SizeChart.from_dict(_size_chart)

        primary_combined_product_id = d.pop("primary_combined_product_id", UNSET)

        is_not_for_sale = d.pop("is_not_for_sale", UNSET)

        category_version = d.pop("category_version", UNSET)

        manufacturer_ids = cast(list[str], d.pop("manufacturer_ids", UNSET))

        responsible_person_ids = cast(list[str], d.pop("responsible_person_ids", UNSET))

        _listing_platforms = d.pop("listing_platforms", UNSET)
        listing_platforms: list[CreateProductRequestListingPlatformsItem] | Unset = UNSET
        if _listing_platforms is not UNSET:
            listing_platforms = []
            for listing_platforms_item_data in _listing_platforms:
                listing_platforms_item = CreateProductRequestListingPlatformsItem(listing_platforms_item_data)

                listing_platforms.append(listing_platforms_item)

        _shipping_insurance_requirement = d.pop("shipping_insurance_requirement", UNSET)
        shipping_insurance_requirement: CreateProductRequestShippingInsuranceRequirement | Unset
        if isinstance(_shipping_insurance_requirement, Unset):
            shipping_insurance_requirement = UNSET
        else:
            shipping_insurance_requirement = CreateProductRequestShippingInsuranceRequirement(
                _shipping_insurance_requirement
            )

        minimum_order_quantity = d.pop("minimum_order_quantity", UNSET)

        is_pre_owned = d.pop("is_pre_owned", UNSET)

        idempotency_key = d.pop("idempotency_key", UNSET)

        shipping_template_id = d.pop("shipping_template_id", UNSET)

        _scheduled_sale = d.pop("scheduled_sale", UNSET)
        scheduled_sale: ScheduledSale | Unset
        if isinstance(_scheduled_sale, Unset):
            scheduled_sale = UNSET
        else:
            scheduled_sale = ScheduledSale.from_dict(_scheduled_sale)

        _locale = d.pop("locale", UNSET)
        locale: CreateProductRequestLocale | Unset
        if isinstance(_locale, Unset):
            locale = UNSET
        else:
            locale = CreateProductRequestLocale(_locale)

        auto_translate_enabled = d.pop("auto_translate_enabled", UNSET)

        search_terms = cast(list[str], d.pop("search_terms", UNSET))

        key_product_features = cast(list[str], d.pop("key_product_features", UNSET))

        _product_tag_operations = d.pop("product_tag_operations", UNSET)
        product_tag_operations: list[ProductTagOperation] | Unset = UNSET
        if _product_tag_operations is not UNSET:
            product_tag_operations = []
            for product_tag_operations_item_data in _product_tag_operations:
                product_tag_operations_item = ProductTagOperation.from_dict(product_tag_operations_item_data)

                product_tag_operations.append(product_tag_operations_item)

        _purchase_order_quantity_limit = d.pop("purchase_order_quantity_limit", UNSET)
        purchase_order_quantity_limit: PurchaseOrderQuantityLimit | Unset
        if isinstance(_purchase_order_quantity_limit, Unset):
            purchase_order_quantity_limit = UNSET
        else:
            purchase_order_quantity_limit = PurchaseOrderQuantityLimit.from_dict(_purchase_order_quantity_limit)

        _selling_format = d.pop("selling_format", UNSET)
        selling_format: CreateProductRequestSellingFormat | Unset
        if isinstance(_selling_format, Unset):
            selling_format = UNSET
        else:
            selling_format = CreateProductRequestSellingFormat(_selling_format)

        is_live_quick = d.pop("is_live_quick", UNSET)

        is_blind_box = d.pop("is_blind_box", UNSET)

        create_product_request = cls(
            description=description,
            category_id=category_id,
            main_images=main_images,
            skus=skus,
            title=title,
            save_mode=save_mode,
            brand_id=brand_id,
            is_cod_allowed=is_cod_allowed,
            certifications=certifications,
            package_dimensions=package_dimensions,
            product_attributes=product_attributes,
            package_weight=package_weight,
            video=video,
            external_product_id=external_product_id,
            delivery_option_ids=delivery_option_ids,
            size_chart=size_chart,
            primary_combined_product_id=primary_combined_product_id,
            is_not_for_sale=is_not_for_sale,
            category_version=category_version,
            manufacturer_ids=manufacturer_ids,
            responsible_person_ids=responsible_person_ids,
            listing_platforms=listing_platforms,
            shipping_insurance_requirement=shipping_insurance_requirement,
            minimum_order_quantity=minimum_order_quantity,
            is_pre_owned=is_pre_owned,
            idempotency_key=idempotency_key,
            shipping_template_id=shipping_template_id,
            scheduled_sale=scheduled_sale,
            locale=locale,
            auto_translate_enabled=auto_translate_enabled,
            search_terms=search_terms,
            key_product_features=key_product_features,
            product_tag_operations=product_tag_operations,
            purchase_order_quantity_limit=purchase_order_quantity_limit,
            selling_format=selling_format,
            is_live_quick=is_live_quick,
            is_blind_box=is_blind_box,
        )

        create_product_request.additional_properties = d
        return create_product_request

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
