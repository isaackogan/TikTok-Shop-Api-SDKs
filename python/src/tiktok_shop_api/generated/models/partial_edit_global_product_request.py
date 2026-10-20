from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.partial_edit_global_product_request_category_version import PartialEditGlobalProductRequestCategoryVersion
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.create_global_product_request_certification import CreateGlobalProductRequestCertification
  from ..models.main_image import MainImage
  from ..models.manufacturer import Manufacturer
  from ..models.package_dimension import PackageDimension
  from ..models.package_weight import PackageWeight
  from ..models.partial_edit_global_product_request_sku import PartialEditGlobalProductRequestSku
  from ..models.product_attribute import ProductAttribute
  from ..models.size_chart import SizeChart
  from ..models.video import Video





T = TypeVar("T", bound="PartialEditGlobalProductRequest")



@_attrs_define
class PartialEditGlobalProductRequest:
    """ 
        Attributes:
            title (str | Unset): The product title.
                Title length:
                - DE, ES, FR, IE, IT, JP, UK, US: [1, 255]
                - MX:[1,300]
                - Other regions: [25, 255]
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
            category_id (str | Unset): The product's current category ID. If provided, it must match the existing category;
                this API cannot change the product category.
                - It must be a leaf category that corresponds to the category tree type specified in the `category_version`
                property.
                - It must be a main category (`categories.permission_statuses=AVAILABLE` in [Get Global Categories
                API](650a03f8f1fd3102b91b338a)).

                **Note**: Refer to TikTok Shop Academy for information on product category restrictions.
            brand_id (str | Unset): The ID of the brand of this product.

                **Note**: Unauthorized brands won't be displayed on TikTok Shop.
            main_images (list[MainImage] | Unset): A list of images to display in the product image gallery.
                - Max count: 9
                - Arrange your image URIs in the sequence that they should appear on TikTok Shop.
                - Image dimensions: [300x300 px, 4000x4000 px]

                **Recommendations**:
                - Use a minimum of 5 images.
                - The first image should have a white background. Use the [Optimize Images
                API](https://partner.tiktokshop.com/docv2/page/665692b35d39dc02deb49a97) to change the background to white.
            skus (list[PartialEditGlobalProductRequestSku] | Unset): A list of global Stock Keeping Units (SKUs) used to
                identify distinct variants of the product.

                **Note**:
                - Max SKUs for EU, JP, UK, US: 300
                - Max SKUs for other regions: 100

                **Recommendations**: Place the most important variant at the beginning of the array.
            package_weight (PackageWeight | Unset):
            certifications (list[CreateGlobalProductRequestCertification] | Unset): The list of certifications for your
                product. If a non-empty list is provided, it replaces the existing certifications. If omitted or passed as an
                empty array, the existing certifications are retained.
                Max count: 10

                As per TikTok Shop guidelines, certifications are required for certain restricted product categories. Retrieve
                the certification requirements for your product from the [Get Global Category Rules
                API](https://partner.tiktokshop.com/docv2/page/650a056df1fd3102b91b5b8e). Refer to [TikTok Shop Restricted
                Products Policy](https://seller-
                us.tiktok.com/university/essay?identity=1&role=1&knowledge_id=3238037484275457&from=policy) for information on
                product category restrictions.
            package_dimensions (PackageDimension | Unset):
            product_attributes (list[ProductAttribute] | Unset): A list of general attributes (e.g. manufacturer, country of
                origin, materials used) that describe the product as a whole, regardless of variant. If a non-empty list is
                provided, it replaces the existing product attributes. If omitted or passed as an empty array, the existing
                product attributes are retained.

                **Important**: The attributes available for use are determined by the system based on the product's assigned
                category, with some being mandatory. You must provide the product attributes marked as `is_required` in the
                response of the [Get Global Attributes API](650a0483c16ffe02b8dfc80a).
            size_chart (SizeChart | Unset):
            video (Video | Unset):
            manufacturer (Manufacturer | Unset):
            manufacturer_ids (list[str] | Unset): A list of manufacturer IDs. Retrieve the IDs from the [Search
                Manufacturers API](67066a580dcee902fa03ccf9).
                If omitted, the manufacturer IDs already associated with the global product are retained. Pass an empty array to
                remove all existing manufacturer IDs.

                **Note**: Applicable only for the EU market in certain categories. Use the [Get Global Category Rules
                API](650a056df1fd3102b91b5b8e) to check the requirements.
            responsible_person_ids (list[str] | Unset): A list of responsible person IDs. Retrieve the IDs from the [Search
                Responsible Persons API](67066a55f17b7d02f95d2fb1).
                If omitted, the responsible person IDs already associated with the global product are retained. Pass an empty
                array to remove all existing responsible person IDs.

                **Note**: Applicable only for the EU market in certain categories. Use the [Get Global Category Rules
                API](650a056df1fd3102b91b5b8e) to check the requirements.
            category_version (PartialEditGlobalProductRequestCategoryVersion | Unset): The category tree version used by
                `category_id`.
                Possible values based on region:
                - US: `v2`, represents the 7-level category tree.
                  **Important**: If the seller account contains an active US shop, you must pass `v2` when using this API.
                - Other regions: `v1`, represents the 3-level category tree.
                Default: `v1`
            external_global_product_id (str | Unset): An external identifier used in an external ecommerce platform. This is
                used to associate the global product between TikTok Shop and the external ecommerce platform.
                Max length: 999 characters
     """

    title: str | Unset = UNSET
    description: str | Unset = UNSET
    category_id: str | Unset = UNSET
    brand_id: str | Unset = UNSET
    main_images: list[MainImage] | Unset = UNSET
    skus: list[PartialEditGlobalProductRequestSku] | Unset = UNSET
    package_weight: PackageWeight | Unset = UNSET
    certifications: list[CreateGlobalProductRequestCertification] | Unset = UNSET
    package_dimensions: PackageDimension | Unset = UNSET
    product_attributes: list[ProductAttribute] | Unset = UNSET
    size_chart: SizeChart | Unset = UNSET
    video: Video | Unset = UNSET
    manufacturer: Manufacturer | Unset = UNSET
    manufacturer_ids: list[str] | Unset = UNSET
    responsible_person_ids: list[str] | Unset = UNSET
    category_version: PartialEditGlobalProductRequestCategoryVersion | Unset = UNSET
    external_global_product_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_global_product_request_certification import CreateGlobalProductRequestCertification # noqa: PLC0415
        from ..models.main_image import MainImage # noqa: PLC0415
        from ..models.manufacturer import Manufacturer # noqa: PLC0415
        from ..models.package_dimension import PackageDimension # noqa: PLC0415
        from ..models.package_weight import PackageWeight # noqa: PLC0415
        from ..models.partial_edit_global_product_request_sku import PartialEditGlobalProductRequestSku # noqa: PLC0415
        from ..models.product_attribute import ProductAttribute # noqa: PLC0415
        from ..models.size_chart import SizeChart # noqa: PLC0415
        from ..models.video import Video # noqa: PLC0415
        title = self.title

        description = self.description

        category_id = self.category_id

        brand_id = self.brand_id

        main_images: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.main_images, Unset):
            main_images = []
            for main_images_item_data in self.main_images:
                main_images_item = main_images_item_data.to_dict()
                main_images.append(main_images_item)



        skus: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.skus, Unset):
            skus = []
            for skus_item_data in self.skus:
                skus_item = skus_item_data.to_dict()
                skus.append(skus_item)



        package_weight: dict[str, Any] | Unset = UNSET
        if not isinstance(self.package_weight, Unset):
            package_weight = self.package_weight.to_dict()

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



        size_chart: dict[str, Any] | Unset = UNSET
        if not isinstance(self.size_chart, Unset):
            size_chart = self.size_chart.to_dict()

        video: dict[str, Any] | Unset = UNSET
        if not isinstance(self.video, Unset):
            video = self.video.to_dict()

        manufacturer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.manufacturer, Unset):
            manufacturer = self.manufacturer.to_dict()

        manufacturer_ids: list[str] | Unset = UNSET
        if not isinstance(self.manufacturer_ids, Unset):
            manufacturer_ids = self.manufacturer_ids



        responsible_person_ids: list[str] | Unset = UNSET
        if not isinstance(self.responsible_person_ids, Unset):
            responsible_person_ids = self.responsible_person_ids



        category_version: str | Unset = UNSET
        if not isinstance(self.category_version, Unset):
            category_version = self.category_version.value


        external_global_product_id = self.external_global_product_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if category_id is not UNSET:
            field_dict["category_id"] = category_id
        if brand_id is not UNSET:
            field_dict["brand_id"] = brand_id
        if main_images is not UNSET:
            field_dict["main_images"] = main_images
        if skus is not UNSET:
            field_dict["skus"] = skus
        if package_weight is not UNSET:
            field_dict["package_weight"] = package_weight
        if certifications is not UNSET:
            field_dict["certifications"] = certifications
        if package_dimensions is not UNSET:
            field_dict["package_dimensions"] = package_dimensions
        if product_attributes is not UNSET:
            field_dict["product_attributes"] = product_attributes
        if size_chart is not UNSET:
            field_dict["size_chart"] = size_chart
        if video is not UNSET:
            field_dict["video"] = video
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer
        if manufacturer_ids is not UNSET:
            field_dict["manufacturer_ids"] = manufacturer_ids
        if responsible_person_ids is not UNSET:
            field_dict["responsible_person_ids"] = responsible_person_ids
        if category_version is not UNSET:
            field_dict["category_version"] = category_version
        if external_global_product_id is not UNSET:
            field_dict["external_global_product_id"] = external_global_product_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_global_product_request_certification import CreateGlobalProductRequestCertification # noqa: PLC0415
        from ..models.main_image import MainImage # noqa: PLC0415
        from ..models.manufacturer import Manufacturer # noqa: PLC0415
        from ..models.package_dimension import PackageDimension # noqa: PLC0415
        from ..models.package_weight import PackageWeight # noqa: PLC0415
        from ..models.partial_edit_global_product_request_sku import PartialEditGlobalProductRequestSku # noqa: PLC0415
        from ..models.product_attribute import ProductAttribute # noqa: PLC0415
        from ..models.size_chart import SizeChart # noqa: PLC0415
        from ..models.video import Video # noqa: PLC0415
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        category_id = d.pop("category_id", UNSET)

        brand_id = d.pop("brand_id", UNSET)

        _main_images = d.pop("main_images", UNSET)
        main_images: list[MainImage] | Unset = UNSET
        if _main_images is not UNSET:
            main_images = []
            for main_images_item_data in _main_images:
                main_images_item = MainImage.from_dict(main_images_item_data)



                main_images.append(main_images_item)


        _skus = d.pop("skus", UNSET)
        skus: list[PartialEditGlobalProductRequestSku] | Unset = UNSET
        if _skus is not UNSET:
            skus = []
            for skus_item_data in _skus:
                skus_item = PartialEditGlobalProductRequestSku.from_dict(skus_item_data)



                skus.append(skus_item)


        _package_weight = d.pop("package_weight", UNSET)
        package_weight: PackageWeight | Unset
        if isinstance(_package_weight,  Unset):
            package_weight = UNSET
        else:
            package_weight = PackageWeight.from_dict(_package_weight)




        _certifications = d.pop("certifications", UNSET)
        certifications: list[CreateGlobalProductRequestCertification] | Unset = UNSET
        if _certifications is not UNSET:
            certifications = []
            for certifications_item_data in _certifications:
                certifications_item = CreateGlobalProductRequestCertification.from_dict(certifications_item_data)



                certifications.append(certifications_item)


        _package_dimensions = d.pop("package_dimensions", UNSET)
        package_dimensions: PackageDimension | Unset
        if isinstance(_package_dimensions,  Unset):
            package_dimensions = UNSET
        else:
            package_dimensions = PackageDimension.from_dict(_package_dimensions)




        _product_attributes = d.pop("product_attributes", UNSET)
        product_attributes: list[ProductAttribute] | Unset = UNSET
        if _product_attributes is not UNSET:
            product_attributes = []
            for product_attributes_item_data in _product_attributes:
                product_attributes_item = ProductAttribute.from_dict(product_attributes_item_data)



                product_attributes.append(product_attributes_item)


        _size_chart = d.pop("size_chart", UNSET)
        size_chart: SizeChart | Unset
        if isinstance(_size_chart,  Unset):
            size_chart = UNSET
        else:
            size_chart = SizeChart.from_dict(_size_chart)




        _video = d.pop("video", UNSET)
        video: Video | Unset
        if isinstance(_video,  Unset):
            video = UNSET
        else:
            video = Video.from_dict(_video)




        _manufacturer = d.pop("manufacturer", UNSET)
        manufacturer: Manufacturer | Unset
        if isinstance(_manufacturer,  Unset):
            manufacturer = UNSET
        else:
            manufacturer = Manufacturer.from_dict(_manufacturer)




        manufacturer_ids = cast(list[str], d.pop("manufacturer_ids", UNSET))


        responsible_person_ids = cast(list[str], d.pop("responsible_person_ids", UNSET))


        _category_version = d.pop("category_version", UNSET)
        category_version: PartialEditGlobalProductRequestCategoryVersion | Unset
        if isinstance(_category_version,  Unset):
            category_version = UNSET
        else:
            category_version = PartialEditGlobalProductRequestCategoryVersion(_category_version)




        external_global_product_id = d.pop("external_global_product_id", UNSET)

        partial_edit_global_product_request = cls(
            title=title,
            description=description,
            category_id=category_id,
            brand_id=brand_id,
            main_images=main_images,
            skus=skus,
            package_weight=package_weight,
            certifications=certifications,
            package_dimensions=package_dimensions,
            product_attributes=product_attributes,
            size_chart=size_chart,
            video=video,
            manufacturer=manufacturer,
            manufacturer_ids=manufacturer_ids,
            responsible_person_ids=responsible_person_ids,
            category_version=category_version,
            external_global_product_id=external_global_product_id,
        )


        partial_edit_global_product_request.additional_properties = d
        return partial_edit_global_product_request

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
