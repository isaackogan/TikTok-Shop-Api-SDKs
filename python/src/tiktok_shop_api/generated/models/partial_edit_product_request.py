from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.partial_edit_product_request_listing_platforms_item import PartialEditProductRequestListingPlatformsItem
from ..models.partial_edit_product_request_locale import PartialEditProductRequestLocale
from ..models.partial_edit_product_request_save_mode import PartialEditProductRequestSaveMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_product_request_product_attribute import CreateProductRequestProductAttribute
    from ..models.main_image import MainImage
    from ..models.partial_edit_product_request_certification import PartialEditProductRequestCertification
    from ..models.partial_edit_product_request_package_dimension import PartialEditProductRequestPackageDimension
    from ..models.partial_edit_product_request_package_weight import PartialEditProductRequestPackageWeight
    from ..models.partial_edit_product_request_pod_info import PartialEditProductRequestPodInfo
    from ..models.partial_edit_product_request_replicated_product import PartialEditProductRequestReplicatedProduct
    from ..models.partial_edit_product_request_sku import PartialEditProductRequestSku
    from ..models.partial_edit_product_request_subscribe_info_edit import PartialEditProductRequestSubscribeInfoEdit
    from ..models.scheduled_sale import ScheduledSale
    from ..models.size_chart import SizeChart
    from ..models.video import Video


T = TypeVar("T", bound="PartialEditProductRequest")


@_attrs_define
class PartialEditProductRequest:
    """
    Attributes:
        auto_translate_enabled (bool | Unset): Whether to automatically translate the product content when listing the
            product in a market where multiple languages are needed. Omit this field when automatic translation is not
            needed.
        brand_id (str | Unset): The ID of the brand of this product.
            Use the [Get Brands API](https://partner.tiktokshop.com/docv2/page/6503075656e2bb0289dd5d01) to get the list of
            available brands for a shop.

            **Note**: Unauthorized brands won't be displayed on TikTok Shop.
        category_version (str | Unset): Filter categories by the category tree version.Possible values based on region:
            - US, EU and SEA: v2, represents the 7-level category tree.
            Important: For US, EU and SEA shops, you must pass v2 when using this API.
            - Other regions: v1, represents the 3-level category tree.Default: v1
        certifications (list[PartialEditProductRequestCertification] | Unset): The list of certifications for your
            product.
            Max count: 10

            As per TikTok Shop guidelines, certifications are required for certain restricted product categories. Retrieve
            the certification requirements for your product from the  [Get Category Rules
            API](https://partner.tiktokshop.com/docv2/page/6509c0febace3e02b74594a9). Refer to [TikTok Shop Restricted
            Products Policy](https://seller-
            us.tiktok.com/university/essay?identity=1&role=1&knowledge_id=3238037484275457&from=policy) for information on
            product category restrictions.
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
        external_product_id (str | Unset): An external identifier used in an external ecommerce platform. This is used
            to associate the product between TikTok Shop and the external ecommerce platform.
            Max length: 999 characters
        inventory_mode (str | Unset): Defines the inventory mode for the duplicated source product. This parameter
            supports two modes: SHARED and EXCLUSIVE.

            - SHARED: In this mode, the inventory of all interconnected (shared) products must be strictly consistent;
            otherwise, an error will be returned.
            - EXCLUSIVE: In this mode, the inventory for each product can be set independently without affecting others.

            Applicability:
            This feature is applicable ONLY for the EU market.

            Default Value:
            If left empty, the system defaults to the EXCLUSIVE mode.
        is_cod_allowed (bool | Unset): A flag indicating whether to show the Cash On Delivery (COD) payment option
            during checkout. Use the [Get Category Rules
            API](https://partner.tiktokshop.com/docv2/page/6509c0febace3e02b74594a9) to check if COD is supported for your
            product category.

            Applicable only for the following markets:
            - Global sellers: MY, PH, SA, TH, VN
            - Local sellers: ID, MY, PH, SA, TH, VN

            **Note**: If COD is not supported, the listing will fail if you set this to `true`.
        key_product_features (list[str] | Unset): Key Product Features. They will be displayed in the Product highlight
            module on the product detail page and will be used by search engines to increase your search weight for more
            traffic. The total number of items should not exceed 5, and the total character count should not exceed 1500.
        listing_platforms (list[PartialEditProductRequestListingPlatformsItem] | Unset): The platforms for listing the
            product.
            Possible values:
            - TOKOPEDIA
            - TIKTOK_SHOP
            Applicable only for sellers that migrated from Tokopedia.

            **IMPORTANT**: This field controls the product's visibility on the listing platforms.
            - If the product is live on both platforms but the request contains only 1 platform, the product will be
            deactivated and hidden from the omitted platform.
            - If the product is live on 1 platform but the request contains a different platform, the product will be
            deactivated and hidden from the omitted platform.
            - If you want to deactivate the product on both platforms, use the Deactivate Product API.
        locale (PartialEditProductRequestLocale | Unset): The BCP-47 locale code used when retrieving the existing
            product information for this edit.
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
        main_images (list[MainImage] | Unset): A list of images to display in the product image gallery.
            -  Max count: 9
            - Arrange your image URIs in the sequence that they should appear on TikTok Shop.
            - Image dimensions: [300x300 px, 4000x4000 px]

            **Recommendations**:
            - Use a minimum of 5 images.
            - The first image should have a white background. Use the [Optimize Images
            API](https://partner.tiktokshop.com/docv2/page/665692b35d39dc02deb49a97) to change the background to white.
        manufacturer_ids (list[str] | Unset): A list of manufacturer IDs. Retrieve the IDs from the [Search
            Manufacturers API](67066a580dcee902fa03ccf9).

            **Note**: Applicable only for the EU market in certain categories. Use the [Get Category Rules
            API](6509c0febace3e02b74594a9) to check the requirements.
        package_dimensions (PartialEditProductRequestPackageDimension | Unset):
        package_weight (PartialEditProductRequestPackageWeight | Unset):
        pod_info (PartialEditProductRequestPodInfo | Unset):
        product_attributes (list[CreateProductRequestProductAttribute] | Unset): A list of general attributes (e.g.
            manufacturer, country of origin, materials used) that describe the product as a whole, regardless of variant.

            **Important**: The attributes available for use are determined by the system based on the product's assigned
            category, with some being mandatory. You must provide the product attributes marked as `is_required` in the
            response of the [Get Attributes API](6509c5784a0bb702c0561cc8) to avoid listing failure.
        replicated_products (list[PartialEditProductRequestReplicatedProduct] | Unset): The list of local market
            replicas to which updates should be synced. As this is a partial edit endpoint, only updated fields will be
            synced.
            **Compulsory sync**
            - **Sales attribute changes** (in sales attribute id/name) must be synced to other markets. Therefore, you must
            provide the `seller_sku` above and complete the details in this object. The API call will fail if you don't
            provide these details.
            **Optional sync**
            - **New SKUs** (new sales attribute value id/name) are optional to sync to other markets. To sync, please
            provide the `seller_sku` above and complete the details in this object.
            - **General changes** are optional to sync to other markets. To sync, you only need to provide
            `replicated_products.region`.
        responsible_person_ids (list[str] | Unset): A list of responsible person IDs. Retrieve the IDs from the [Search
            Responsible Persons API](67066a55f17b7d02f95d2fb1).

            **Note**: Applicable only for the EU market in certain categories. Use the [Get Category Rules
            API](6509c0febace3e02b74594a9) to check the requirements.
        save_mode (PartialEditProductRequestSaveMode | Unset): Indicates how the product should be saved.
            Possible values:
            - AS_DRAFT: Save the product as a draft for future editing.
            - LISTING: Submit the edits for listing. Changes that require review are published after approval; changes to
            the `price` or `inventory` fields are published immediately.
            Default: LISTING

            **Note**:
            - Saving as draft is not supported when the product status is `DELETED`, or when the product is `PENDING` or
            `FREEZE` on any listing platform.
            - When saving a post-live draft with `save_mode=AS_DRAFT`, SKU `inventory` fields are not supported and will not
            be saved.
        scheduled_sale (ScheduledSale | Unset):
        search_terms (list[str] | Unset): Search terms (ST words). ST words will not be displayed to consumers; they are
            only used in search engines to increase your search weight and gain more traffic. Please ensure that ST words
            are consistent with the product description, with a maximum of 15 terms and a total of no more than 250
            characters.
        size_chart (SizeChart | Unset):
        skus (list[PartialEditProductRequestSku] | Unset): A list of Stock Keeping Units (SKUs) used to identify
            distinct variants of the product.

            **Note**:
            - Max SKUs for BR, EU, JP, MX, UK, US: 300
            - Max SKUs for other regions: 100

            **Recommendations**: Place the most important variant at the beginning of the array.
        subscribe_info_edit (PartialEditProductRequestSubscribeInfoEdit | Unset):
        title (str | Unset): The product title.
            Title length:
            - DE, ES, FR, IE, IT, JP, UK, US: [1, 255]
            - BR, MX: [1, 300]
            - Other regions: [25, 255]
        video (Video | Unset):
        is_blind_box (bool | Unset): Whether the product is a blind box of lucky bag. For example: PopMart
    """

    auto_translate_enabled: bool | Unset = UNSET
    brand_id: str | Unset = UNSET
    category_version: str | Unset = UNSET
    certifications: list[PartialEditProductRequestCertification] | Unset = UNSET
    description: str | Unset = UNSET
    external_product_id: str | Unset = UNSET
    inventory_mode: str | Unset = UNSET
    is_cod_allowed: bool | Unset = UNSET
    key_product_features: list[str] | Unset = UNSET
    listing_platforms: list[PartialEditProductRequestListingPlatformsItem] | Unset = UNSET
    locale: PartialEditProductRequestLocale | Unset = UNSET
    main_images: list[MainImage] | Unset = UNSET
    manufacturer_ids: list[str] | Unset = UNSET
    package_dimensions: PartialEditProductRequestPackageDimension | Unset = UNSET
    package_weight: PartialEditProductRequestPackageWeight | Unset = UNSET
    pod_info: PartialEditProductRequestPodInfo | Unset = UNSET
    product_attributes: list[CreateProductRequestProductAttribute] | Unset = UNSET
    replicated_products: list[PartialEditProductRequestReplicatedProduct] | Unset = UNSET
    responsible_person_ids: list[str] | Unset = UNSET
    save_mode: PartialEditProductRequestSaveMode | Unset = UNSET
    scheduled_sale: ScheduledSale | Unset = UNSET
    search_terms: list[str] | Unset = UNSET
    size_chart: SizeChart | Unset = UNSET
    skus: list[PartialEditProductRequestSku] | Unset = UNSET
    subscribe_info_edit: PartialEditProductRequestSubscribeInfoEdit | Unset = UNSET
    title: str | Unset = UNSET
    video: Video | Unset = UNSET
    is_blind_box: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_translate_enabled = self.auto_translate_enabled

        brand_id = self.brand_id

        category_version = self.category_version

        certifications: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.certifications, Unset):
            certifications = []
            for certifications_item_data in self.certifications:
                certifications_item = certifications_item_data.to_dict()
                certifications.append(certifications_item)

        description = self.description

        external_product_id = self.external_product_id

        inventory_mode = self.inventory_mode

        is_cod_allowed = self.is_cod_allowed

        key_product_features: list[str] | Unset = UNSET
        if not isinstance(self.key_product_features, Unset):
            key_product_features = self.key_product_features

        listing_platforms: list[str] | Unset = UNSET
        if not isinstance(self.listing_platforms, Unset):
            listing_platforms = []
            for listing_platforms_item_data in self.listing_platforms:
                listing_platforms_item = listing_platforms_item_data.value
                listing_platforms.append(listing_platforms_item)

        locale: str | Unset = UNSET
        if not isinstance(self.locale, Unset):
            locale = self.locale.value

        main_images: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.main_images, Unset):
            main_images = []
            for main_images_item_data in self.main_images:
                main_images_item = main_images_item_data.to_dict()
                main_images.append(main_images_item)

        manufacturer_ids: list[str] | Unset = UNSET
        if not isinstance(self.manufacturer_ids, Unset):
            manufacturer_ids = self.manufacturer_ids

        package_dimensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.package_dimensions, Unset):
            package_dimensions = self.package_dimensions.to_dict()

        package_weight: dict[str, Any] | Unset = UNSET
        if not isinstance(self.package_weight, Unset):
            package_weight = self.package_weight.to_dict()

        pod_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pod_info, Unset):
            pod_info = self.pod_info.to_dict()

        product_attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.product_attributes, Unset):
            product_attributes = []
            for product_attributes_item_data in self.product_attributes:
                product_attributes_item = product_attributes_item_data.to_dict()
                product_attributes.append(product_attributes_item)

        replicated_products: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.replicated_products, Unset):
            replicated_products = []
            for replicated_products_item_data in self.replicated_products:
                replicated_products_item = replicated_products_item_data.to_dict()
                replicated_products.append(replicated_products_item)

        responsible_person_ids: list[str] | Unset = UNSET
        if not isinstance(self.responsible_person_ids, Unset):
            responsible_person_ids = self.responsible_person_ids

        save_mode: str | Unset = UNSET
        if not isinstance(self.save_mode, Unset):
            save_mode = self.save_mode.value

        scheduled_sale: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scheduled_sale, Unset):
            scheduled_sale = self.scheduled_sale.to_dict()

        search_terms: list[str] | Unset = UNSET
        if not isinstance(self.search_terms, Unset):
            search_terms = self.search_terms

        size_chart: dict[str, Any] | Unset = UNSET
        if not isinstance(self.size_chart, Unset):
            size_chart = self.size_chart.to_dict()

        skus: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.skus, Unset):
            skus = []
            for skus_item_data in self.skus:
                skus_item = skus_item_data.to_dict()
                skus.append(skus_item)

        subscribe_info_edit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subscribe_info_edit, Unset):
            subscribe_info_edit = self.subscribe_info_edit.to_dict()

        title = self.title

        video: dict[str, Any] | Unset = UNSET
        if not isinstance(self.video, Unset):
            video = self.video.to_dict()

        is_blind_box = self.is_blind_box

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_translate_enabled is not UNSET:
            field_dict["auto_translate_enabled"] = auto_translate_enabled
        if brand_id is not UNSET:
            field_dict["brand_id"] = brand_id
        if category_version is not UNSET:
            field_dict["category_version"] = category_version
        if certifications is not UNSET:
            field_dict["certifications"] = certifications
        if description is not UNSET:
            field_dict["description"] = description
        if external_product_id is not UNSET:
            field_dict["external_product_id"] = external_product_id
        if inventory_mode is not UNSET:
            field_dict["inventory_mode"] = inventory_mode
        if is_cod_allowed is not UNSET:
            field_dict["is_cod_allowed"] = is_cod_allowed
        if key_product_features is not UNSET:
            field_dict["key_product_features"] = key_product_features
        if listing_platforms is not UNSET:
            field_dict["listing_platforms"] = listing_platforms
        if locale is not UNSET:
            field_dict["locale"] = locale
        if main_images is not UNSET:
            field_dict["main_images"] = main_images
        if manufacturer_ids is not UNSET:
            field_dict["manufacturer_ids"] = manufacturer_ids
        if package_dimensions is not UNSET:
            field_dict["package_dimensions"] = package_dimensions
        if package_weight is not UNSET:
            field_dict["package_weight"] = package_weight
        if pod_info is not UNSET:
            field_dict["pod_info"] = pod_info
        if product_attributes is not UNSET:
            field_dict["product_attributes"] = product_attributes
        if replicated_products is not UNSET:
            field_dict["replicated_products"] = replicated_products
        if responsible_person_ids is not UNSET:
            field_dict["responsible_person_ids"] = responsible_person_ids
        if save_mode is not UNSET:
            field_dict["save_mode"] = save_mode
        if scheduled_sale is not UNSET:
            field_dict["scheduled_sale"] = scheduled_sale
        if search_terms is not UNSET:
            field_dict["search_terms"] = search_terms
        if size_chart is not UNSET:
            field_dict["size_chart"] = size_chart
        if skus is not UNSET:
            field_dict["skus"] = skus
        if subscribe_info_edit is not UNSET:
            field_dict["subscribe_info_edit"] = subscribe_info_edit
        if title is not UNSET:
            field_dict["title"] = title
        if video is not UNSET:
            field_dict["video"] = video
        if is_blind_box is not UNSET:
            field_dict["is_blind_box"] = is_blind_box

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_product_request_product_attribute import (
            CreateProductRequestProductAttribute,  # noqa: PLC0415
        )
        from ..models.main_image import MainImage  # noqa: PLC0415
        from ..models.partial_edit_product_request_certification import (
            PartialEditProductRequestCertification,  # noqa: PLC0415
        )
        from ..models.partial_edit_product_request_package_dimension import (
            PartialEditProductRequestPackageDimension,  # noqa: PLC0415
        )
        from ..models.partial_edit_product_request_package_weight import (
            PartialEditProductRequestPackageWeight,  # noqa: PLC0415
        )
        from ..models.partial_edit_product_request_pod_info import PartialEditProductRequestPodInfo  # noqa: PLC0415
        from ..models.partial_edit_product_request_replicated_product import (
            PartialEditProductRequestReplicatedProduct,  # noqa: PLC0415
        )
        from ..models.partial_edit_product_request_sku import PartialEditProductRequestSku  # noqa: PLC0415
        from ..models.partial_edit_product_request_subscribe_info_edit import (
            PartialEditProductRequestSubscribeInfoEdit,  # noqa: PLC0415
        )
        from ..models.scheduled_sale import ScheduledSale  # noqa: PLC0415
        from ..models.size_chart import SizeChart  # noqa: PLC0415
        from ..models.video import Video  # noqa: PLC0415

        d = dict(src_dict)
        auto_translate_enabled = d.pop("auto_translate_enabled", UNSET)

        brand_id = d.pop("brand_id", UNSET)

        category_version = d.pop("category_version", UNSET)

        _certifications = d.pop("certifications", UNSET)
        certifications: list[PartialEditProductRequestCertification] | Unset = UNSET
        if _certifications is not UNSET:
            certifications = []
            for certifications_item_data in _certifications:
                certifications_item = PartialEditProductRequestCertification.from_dict(certifications_item_data)

                certifications.append(certifications_item)

        description = d.pop("description", UNSET)

        external_product_id = d.pop("external_product_id", UNSET)

        inventory_mode = d.pop("inventory_mode", UNSET)

        is_cod_allowed = d.pop("is_cod_allowed", UNSET)

        key_product_features = cast(list[str], d.pop("key_product_features", UNSET))

        _listing_platforms = d.pop("listing_platforms", UNSET)
        listing_platforms: list[PartialEditProductRequestListingPlatformsItem] | Unset = UNSET
        if _listing_platforms is not UNSET:
            listing_platforms = []
            for listing_platforms_item_data in _listing_platforms:
                listing_platforms_item = PartialEditProductRequestListingPlatformsItem(listing_platforms_item_data)

                listing_platforms.append(listing_platforms_item)

        _locale = d.pop("locale", UNSET)
        locale: PartialEditProductRequestLocale | Unset
        if isinstance(_locale, Unset):
            locale = UNSET
        else:
            locale = PartialEditProductRequestLocale(_locale)

        _main_images = d.pop("main_images", UNSET)
        main_images: list[MainImage] | Unset = UNSET
        if _main_images is not UNSET:
            main_images = []
            for main_images_item_data in _main_images:
                main_images_item = MainImage.from_dict(main_images_item_data)

                main_images.append(main_images_item)

        manufacturer_ids = cast(list[str], d.pop("manufacturer_ids", UNSET))

        _package_dimensions = d.pop("package_dimensions", UNSET)
        package_dimensions: PartialEditProductRequestPackageDimension | Unset
        if isinstance(_package_dimensions, Unset):
            package_dimensions = UNSET
        else:
            package_dimensions = PartialEditProductRequestPackageDimension.from_dict(_package_dimensions)

        _package_weight = d.pop("package_weight", UNSET)
        package_weight: PartialEditProductRequestPackageWeight | Unset
        if isinstance(_package_weight, Unset):
            package_weight = UNSET
        else:
            package_weight = PartialEditProductRequestPackageWeight.from_dict(_package_weight)

        _pod_info = d.pop("pod_info", UNSET)
        pod_info: PartialEditProductRequestPodInfo | Unset
        if isinstance(_pod_info, Unset):
            pod_info = UNSET
        else:
            pod_info = PartialEditProductRequestPodInfo.from_dict(_pod_info)

        _product_attributes = d.pop("product_attributes", UNSET)
        product_attributes: list[CreateProductRequestProductAttribute] | Unset = UNSET
        if _product_attributes is not UNSET:
            product_attributes = []
            for product_attributes_item_data in _product_attributes:
                product_attributes_item = CreateProductRequestProductAttribute.from_dict(product_attributes_item_data)

                product_attributes.append(product_attributes_item)

        _replicated_products = d.pop("replicated_products", UNSET)
        replicated_products: list[PartialEditProductRequestReplicatedProduct] | Unset = UNSET
        if _replicated_products is not UNSET:
            replicated_products = []
            for replicated_products_item_data in _replicated_products:
                replicated_products_item = PartialEditProductRequestReplicatedProduct.from_dict(
                    replicated_products_item_data
                )

                replicated_products.append(replicated_products_item)

        responsible_person_ids = cast(list[str], d.pop("responsible_person_ids", UNSET))

        _save_mode = d.pop("save_mode", UNSET)
        save_mode: PartialEditProductRequestSaveMode | Unset
        if isinstance(_save_mode, Unset):
            save_mode = UNSET
        else:
            save_mode = PartialEditProductRequestSaveMode(_save_mode)

        _scheduled_sale = d.pop("scheduled_sale", UNSET)
        scheduled_sale: ScheduledSale | Unset
        if isinstance(_scheduled_sale, Unset):
            scheduled_sale = UNSET
        else:
            scheduled_sale = ScheduledSale.from_dict(_scheduled_sale)

        search_terms = cast(list[str], d.pop("search_terms", UNSET))

        _size_chart = d.pop("size_chart", UNSET)
        size_chart: SizeChart | Unset
        if isinstance(_size_chart, Unset):
            size_chart = UNSET
        else:
            size_chart = SizeChart.from_dict(_size_chart)

        _skus = d.pop("skus", UNSET)
        skus: list[PartialEditProductRequestSku] | Unset = UNSET
        if _skus is not UNSET:
            skus = []
            for skus_item_data in _skus:
                skus_item = PartialEditProductRequestSku.from_dict(skus_item_data)

                skus.append(skus_item)

        _subscribe_info_edit = d.pop("subscribe_info_edit", UNSET)
        subscribe_info_edit: PartialEditProductRequestSubscribeInfoEdit | Unset
        if isinstance(_subscribe_info_edit, Unset):
            subscribe_info_edit = UNSET
        else:
            subscribe_info_edit = PartialEditProductRequestSubscribeInfoEdit.from_dict(_subscribe_info_edit)

        title = d.pop("title", UNSET)

        _video = d.pop("video", UNSET)
        video: Video | Unset
        if isinstance(_video, Unset):
            video = UNSET
        else:
            video = Video.from_dict(_video)

        is_blind_box = d.pop("is_blind_box", UNSET)

        partial_edit_product_request = cls(
            auto_translate_enabled=auto_translate_enabled,
            brand_id=brand_id,
            category_version=category_version,
            certifications=certifications,
            description=description,
            external_product_id=external_product_id,
            inventory_mode=inventory_mode,
            is_cod_allowed=is_cod_allowed,
            key_product_features=key_product_features,
            listing_platforms=listing_platforms,
            locale=locale,
            main_images=main_images,
            manufacturer_ids=manufacturer_ids,
            package_dimensions=package_dimensions,
            package_weight=package_weight,
            pod_info=pod_info,
            product_attributes=product_attributes,
            replicated_products=replicated_products,
            responsible_person_ids=responsible_person_ids,
            save_mode=save_mode,
            scheduled_sale=scheduled_sale,
            search_terms=search_terms,
            size_chart=size_chart,
            skus=skus,
            subscribe_info_edit=subscribe_info_edit,
            title=title,
            video=video,
            is_blind_box=is_blind_box,
        )

        partial_edit_product_request.additional_properties = d
        return partial_edit_product_request

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
