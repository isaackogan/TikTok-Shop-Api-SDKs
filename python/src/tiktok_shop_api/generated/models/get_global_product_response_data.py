from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.category import Category
  from ..models.get_global_product_response_data_brand import GetGlobalProductResponseDataBrand
  from ..models.get_global_product_response_data_certification import GetGlobalProductResponseDataCertification
  from ..models.get_global_product_response_data_main_image import GetGlobalProductResponseDataMainImage
  from ..models.get_global_product_response_data_package_dimension import GetGlobalProductResponseDataPackageDimension
  from ..models.get_global_product_response_data_package_weight import GetGlobalProductResponseDataPackageWeight
  from ..models.get_global_product_response_data_product import GetGlobalProductResponseDataProduct
  from ..models.get_global_product_response_data_product_attribute import GetGlobalProductResponseDataProductAttribute
  from ..models.get_global_product_response_data_size_chart import GetGlobalProductResponseDataSizeChart
  from ..models.get_global_product_response_data_sku import GetGlobalProductResponseDataSku
  from ..models.get_global_product_response_data_video import GetGlobalProductResponseDataVideo
  from ..models.manufacturer import Manufacturer





T = TypeVar("T", bound="GetGlobalProductResponseData")



@_attrs_define
class GetGlobalProductResponseData:
    """ 
        Attributes:
            id (str | Unset): The global product ID in TikTok Shop.
            title (str | Unset): The product title.
            main_images (list[GetGlobalProductResponseDataMainImage] | Unset): A list of images to display in the product
                image gallery.
            video (GetGlobalProductResponseDataVideo | Unset):
            description (str | Unset): The product description in HTML format.
            package_dimensions (GetGlobalProductResponseDataPackageDimension | Unset):
            package_weight (GetGlobalProductResponseDataPackageWeight | Unset):
            certifications (list[GetGlobalProductResponseDataCertification] | Unset): The list of certifications for your
                product.
            skus (list[GetGlobalProductResponseDataSku] | Unset): A list of global Stock Keeping Units (SKUs) used to
                identify distinct variants of the product.
            update_time (int | Unset): The time when the product is last updated.
                Unix timestamp in seconds.
            create_time (int | Unset): The time when the product is created.
                Unix timestamp in seconds.
            product_attributes (list[GetGlobalProductResponseDataProductAttribute] | Unset): A list of general attributes
                (e.g. manufacturer, country of origin, materials used) that describe the product as a whole, regardless of
                variant.
            size_chart (GetGlobalProductResponseDataSizeChart | Unset):
            products (list[GetGlobalProductResponseDataProduct] | Unset): The local products associated through global
                product publishing or manual binding.
            global_seller_id (str | Unset): The cross-border seller ID.
            brand (GetGlobalProductResponseDataBrand | Unset):
            category (Category | Unset):
            manufacturer (Manufacturer | Unset):
            responsible_person_ids (list[str] | Unset): A list of responsible person IDs. Retrieve the IDs from the [Search
                Responsible Persons API](67066a55f17b7d02f95d2fb1).
                **Note**: Applicable only for the EU market in certain categories.
            manufacturer_ids (list[str] | Unset): A list of manufacturer IDs. Retrieve the IDs from the [Search
                Manufacturers API](67066a580dcee902fa03ccf9).
                **Note**: Applicable only for the EU market in certain categories.
            source_locale (str | Unset): The BCP-47 locale codes for displaying category information.
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
            external_global_product_id (str | Unset): An external identifier used in an external ecommerce platform. This is
                used to associate the product between TikTok Shop and the external ecommerce platform.
     """

    id: str | Unset = UNSET
    title: str | Unset = UNSET
    main_images: list[GetGlobalProductResponseDataMainImage] | Unset = UNSET
    video: GetGlobalProductResponseDataVideo | Unset = UNSET
    description: str | Unset = UNSET
    package_dimensions: GetGlobalProductResponseDataPackageDimension | Unset = UNSET
    package_weight: GetGlobalProductResponseDataPackageWeight | Unset = UNSET
    certifications: list[GetGlobalProductResponseDataCertification] | Unset = UNSET
    skus: list[GetGlobalProductResponseDataSku] | Unset = UNSET
    update_time: int | Unset = UNSET
    create_time: int | Unset = UNSET
    product_attributes: list[GetGlobalProductResponseDataProductAttribute] | Unset = UNSET
    size_chart: GetGlobalProductResponseDataSizeChart | Unset = UNSET
    products: list[GetGlobalProductResponseDataProduct] | Unset = UNSET
    global_seller_id: str | Unset = UNSET
    brand: GetGlobalProductResponseDataBrand | Unset = UNSET
    category: Category | Unset = UNSET
    manufacturer: Manufacturer | Unset = UNSET
    responsible_person_ids: list[str] | Unset = UNSET
    manufacturer_ids: list[str] | Unset = UNSET
    source_locale: str | Unset = UNSET
    external_global_product_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.category import Category # noqa: PLC0415
        from ..models.get_global_product_response_data_brand import GetGlobalProductResponseDataBrand # noqa: PLC0415
        from ..models.get_global_product_response_data_certification import GetGlobalProductResponseDataCertification # noqa: PLC0415
        from ..models.get_global_product_response_data_main_image import GetGlobalProductResponseDataMainImage # noqa: PLC0415
        from ..models.get_global_product_response_data_package_dimension import GetGlobalProductResponseDataPackageDimension # noqa: PLC0415
        from ..models.get_global_product_response_data_package_weight import GetGlobalProductResponseDataPackageWeight # noqa: PLC0415
        from ..models.get_global_product_response_data_product import GetGlobalProductResponseDataProduct # noqa: PLC0415
        from ..models.get_global_product_response_data_product_attribute import GetGlobalProductResponseDataProductAttribute # noqa: PLC0415
        from ..models.get_global_product_response_data_size_chart import GetGlobalProductResponseDataSizeChart # noqa: PLC0415
        from ..models.get_global_product_response_data_sku import GetGlobalProductResponseDataSku # noqa: PLC0415
        from ..models.get_global_product_response_data_video import GetGlobalProductResponseDataVideo # noqa: PLC0415
        from ..models.manufacturer import Manufacturer # noqa: PLC0415
        id = self.id

        title = self.title

        main_images: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.main_images, Unset):
            main_images = []
            for main_images_item_data in self.main_images:
                main_images_item = main_images_item_data.to_dict()
                main_images.append(main_images_item)



        video: dict[str, Any] | Unset = UNSET
        if not isinstance(self.video, Unset):
            video = self.video.to_dict()

        description = self.description

        package_dimensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.package_dimensions, Unset):
            package_dimensions = self.package_dimensions.to_dict()

        package_weight: dict[str, Any] | Unset = UNSET
        if not isinstance(self.package_weight, Unset):
            package_weight = self.package_weight.to_dict()

        certifications: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.certifications, Unset):
            certifications = []
            for certifications_item_data in self.certifications:
                certifications_item = certifications_item_data.to_dict()
                certifications.append(certifications_item)



        skus: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.skus, Unset):
            skus = []
            for skus_item_data in self.skus:
                skus_item = skus_item_data.to_dict()
                skus.append(skus_item)



        update_time = self.update_time

        create_time = self.create_time

        product_attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.product_attributes, Unset):
            product_attributes = []
            for product_attributes_item_data in self.product_attributes:
                product_attributes_item = product_attributes_item_data.to_dict()
                product_attributes.append(product_attributes_item)



        size_chart: dict[str, Any] | Unset = UNSET
        if not isinstance(self.size_chart, Unset):
            size_chart = self.size_chart.to_dict()

        products: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.products, Unset):
            products = []
            for products_item_data in self.products:
                products_item = products_item_data.to_dict()
                products.append(products_item)



        global_seller_id = self.global_seller_id

        brand: dict[str, Any] | Unset = UNSET
        if not isinstance(self.brand, Unset):
            brand = self.brand.to_dict()

        category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        manufacturer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.manufacturer, Unset):
            manufacturer = self.manufacturer.to_dict()

        responsible_person_ids: list[str] | Unset = UNSET
        if not isinstance(self.responsible_person_ids, Unset):
            responsible_person_ids = self.responsible_person_ids



        manufacturer_ids: list[str] | Unset = UNSET
        if not isinstance(self.manufacturer_ids, Unset):
            manufacturer_ids = self.manufacturer_ids



        source_locale = self.source_locale

        external_global_product_id = self.external_global_product_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if main_images is not UNSET:
            field_dict["main_images"] = main_images
        if video is not UNSET:
            field_dict["video"] = video
        if description is not UNSET:
            field_dict["description"] = description
        if package_dimensions is not UNSET:
            field_dict["package_dimensions"] = package_dimensions
        if package_weight is not UNSET:
            field_dict["package_weight"] = package_weight
        if certifications is not UNSET:
            field_dict["certifications"] = certifications
        if skus is not UNSET:
            field_dict["skus"] = skus
        if update_time is not UNSET:
            field_dict["update_time"] = update_time
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if product_attributes is not UNSET:
            field_dict["product_attributes"] = product_attributes
        if size_chart is not UNSET:
            field_dict["size_chart"] = size_chart
        if products is not UNSET:
            field_dict["products"] = products
        if global_seller_id is not UNSET:
            field_dict["global_seller_id"] = global_seller_id
        if brand is not UNSET:
            field_dict["brand"] = brand
        if category is not UNSET:
            field_dict["category"] = category
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer
        if responsible_person_ids is not UNSET:
            field_dict["responsible_person_ids"] = responsible_person_ids
        if manufacturer_ids is not UNSET:
            field_dict["manufacturer_ids"] = manufacturer_ids
        if source_locale is not UNSET:
            field_dict["source_locale"] = source_locale
        if external_global_product_id is not UNSET:
            field_dict["external_global_product_id"] = external_global_product_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.category import Category # noqa: PLC0415
        from ..models.get_global_product_response_data_brand import GetGlobalProductResponseDataBrand # noqa: PLC0415
        from ..models.get_global_product_response_data_certification import GetGlobalProductResponseDataCertification # noqa: PLC0415
        from ..models.get_global_product_response_data_main_image import GetGlobalProductResponseDataMainImage # noqa: PLC0415
        from ..models.get_global_product_response_data_package_dimension import GetGlobalProductResponseDataPackageDimension # noqa: PLC0415
        from ..models.get_global_product_response_data_package_weight import GetGlobalProductResponseDataPackageWeight # noqa: PLC0415
        from ..models.get_global_product_response_data_product import GetGlobalProductResponseDataProduct # noqa: PLC0415
        from ..models.get_global_product_response_data_product_attribute import GetGlobalProductResponseDataProductAttribute # noqa: PLC0415
        from ..models.get_global_product_response_data_size_chart import GetGlobalProductResponseDataSizeChart # noqa: PLC0415
        from ..models.get_global_product_response_data_sku import GetGlobalProductResponseDataSku # noqa: PLC0415
        from ..models.get_global_product_response_data_video import GetGlobalProductResponseDataVideo # noqa: PLC0415
        from ..models.manufacturer import Manufacturer # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        _main_images = d.pop("main_images", UNSET)
        main_images: list[GetGlobalProductResponseDataMainImage] | Unset = UNSET
        if _main_images is not UNSET:
            main_images = []
            for main_images_item_data in _main_images:
                main_images_item = GetGlobalProductResponseDataMainImage.from_dict(main_images_item_data)



                main_images.append(main_images_item)


        _video = d.pop("video", UNSET)
        video: GetGlobalProductResponseDataVideo | Unset
        if isinstance(_video,  Unset):
            video = UNSET
        else:
            video = GetGlobalProductResponseDataVideo.from_dict(_video)




        description = d.pop("description", UNSET)

        _package_dimensions = d.pop("package_dimensions", UNSET)
        package_dimensions: GetGlobalProductResponseDataPackageDimension | Unset
        if isinstance(_package_dimensions,  Unset):
            package_dimensions = UNSET
        else:
            package_dimensions = GetGlobalProductResponseDataPackageDimension.from_dict(_package_dimensions)




        _package_weight = d.pop("package_weight", UNSET)
        package_weight: GetGlobalProductResponseDataPackageWeight | Unset
        if isinstance(_package_weight,  Unset):
            package_weight = UNSET
        else:
            package_weight = GetGlobalProductResponseDataPackageWeight.from_dict(_package_weight)




        _certifications = d.pop("certifications", UNSET)
        certifications: list[GetGlobalProductResponseDataCertification] | Unset = UNSET
        if _certifications is not UNSET:
            certifications = []
            for certifications_item_data in _certifications:
                certifications_item = GetGlobalProductResponseDataCertification.from_dict(certifications_item_data)



                certifications.append(certifications_item)


        _skus = d.pop("skus", UNSET)
        skus: list[GetGlobalProductResponseDataSku] | Unset = UNSET
        if _skus is not UNSET:
            skus = []
            for skus_item_data in _skus:
                skus_item = GetGlobalProductResponseDataSku.from_dict(skus_item_data)



                skus.append(skus_item)


        update_time = d.pop("update_time", UNSET)

        create_time = d.pop("create_time", UNSET)

        _product_attributes = d.pop("product_attributes", UNSET)
        product_attributes: list[GetGlobalProductResponseDataProductAttribute] | Unset = UNSET
        if _product_attributes is not UNSET:
            product_attributes = []
            for product_attributes_item_data in _product_attributes:
                product_attributes_item = GetGlobalProductResponseDataProductAttribute.from_dict(product_attributes_item_data)



                product_attributes.append(product_attributes_item)


        _size_chart = d.pop("size_chart", UNSET)
        size_chart: GetGlobalProductResponseDataSizeChart | Unset
        if isinstance(_size_chart,  Unset):
            size_chart = UNSET
        else:
            size_chart = GetGlobalProductResponseDataSizeChart.from_dict(_size_chart)




        _products = d.pop("products", UNSET)
        products: list[GetGlobalProductResponseDataProduct] | Unset = UNSET
        if _products is not UNSET:
            products = []
            for products_item_data in _products:
                products_item = GetGlobalProductResponseDataProduct.from_dict(products_item_data)



                products.append(products_item)


        global_seller_id = d.pop("global_seller_id", UNSET)

        _brand = d.pop("brand", UNSET)
        brand: GetGlobalProductResponseDataBrand | Unset
        if isinstance(_brand,  Unset):
            brand = UNSET
        else:
            brand = GetGlobalProductResponseDataBrand.from_dict(_brand)




        _category = d.pop("category", UNSET)
        category: Category | Unset
        if isinstance(_category,  Unset):
            category = UNSET
        else:
            category = Category.from_dict(_category)




        _manufacturer = d.pop("manufacturer", UNSET)
        manufacturer: Manufacturer | Unset
        if isinstance(_manufacturer,  Unset):
            manufacturer = UNSET
        else:
            manufacturer = Manufacturer.from_dict(_manufacturer)




        responsible_person_ids = cast(list[str], d.pop("responsible_person_ids", UNSET))


        manufacturer_ids = cast(list[str], d.pop("manufacturer_ids", UNSET))


        source_locale = d.pop("source_locale", UNSET)

        external_global_product_id = d.pop("external_global_product_id", UNSET)

        get_global_product_response_data = cls(
            id=id,
            title=title,
            main_images=main_images,
            video=video,
            description=description,
            package_dimensions=package_dimensions,
            package_weight=package_weight,
            certifications=certifications,
            skus=skus,
            update_time=update_time,
            create_time=create_time,
            product_attributes=product_attributes,
            size_chart=size_chart,
            products=products,
            global_seller_id=global_seller_id,
            brand=brand,
            category=category,
            manufacturer=manufacturer,
            responsible_person_ids=responsible_person_ids,
            manufacturer_ids=manufacturer_ids,
            source_locale=source_locale,
            external_global_product_id=external_global_product_id,
        )


        get_global_product_response_data.additional_properties = d
        return get_global_product_response_data

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
