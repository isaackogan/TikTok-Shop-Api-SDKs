from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.diagnose_and_optimize_product_request_optimization_fields_item import (
    DiagnoseAndOptimizeProductRequestOptimizationFieldsItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.diagnose_and_optimize_product_request_main_image import DiagnoseAndOptimizeProductRequestMainImage
    from ..models.diagnose_and_optimize_product_request_product_attribute import (
        DiagnoseAndOptimizeProductRequestProductAttribute,
    )
    from ..models.diagnose_and_optimize_product_request_size_chart import DiagnoseAndOptimizeProductRequestSizeChart


T = TypeVar("T", bound="DiagnoseAndOptimizeProductRequest")


@_attrs_define
class DiagnoseAndOptimizeProductRequest:
    """
    Attributes:
        category_id (str): The ID of the category of this product. It must be a leaf category. Use the [Get Categories
            API](https://partner.tiktokshop.com/docv2/page/6509c89d0fcef602bf1acd9b) to find a leaf category.
            **Note**:
            - For the US market, refer to [TikTok Shop Restricted Products Policy](https://seller-
            us.tiktok.com/university/essay?identity=1&role=1&knowledge_id=3238037484275457&from=policy) for information on
            product category restrictions.
            - For the Indonesia market, to list a product on both TikTok Shop and Tokopedia, you must use only categories
            that are available on both platforms.
        product_id (str | Unset): The product ID of an existing product in TikTok Shop.
            - Omit this if you are diagnosing a brand-new product not yet listed in TikTok Shop.
            - Provide this ID if the product is similar to an existing one, and you want the diagnosis to consider both the
            existing product's details and the new information in this request.
        description (str | Unset): The product description in HTML format.
            **Note**:
            - The content must conform to the [HTML syntax](https://html.spec.whatwg.org/). All HTML tags are accepted but
            to optimize display on the TikTok Shop product detail page, the system will automatically convert certain tags
            into alternative formats, such as rendering `<table>` tags as images.
            - Max length: 10,000 characters.
            - Images must use TikTok Shop image URLs, not exceed 4000px, and include `src`, `width`, and `height`
            attributes.
            **Recommendations**:
            - If you are syncing a pre-existing description from another platform, include the full HTML source description
            here.
            - Provide a detailed description, ideally over 300 characters.
            - Include 3-5 key selling points, each under 250 characters, with supporting images.
            - Use 1600x1600 px for the image dimensions.
        brand_id (str | Unset): The ID of the brand of this product.
            Use the [Get Brands API](https://partner.tiktokshop.com/docv2/page/6503075656e2bb0289dd5d01) to get the list of
            available brands for a shop.
            **Note**: Unauthorized brands won't be displayed on TikTok Shop.
        main_images (list[DiagnoseAndOptimizeProductRequestMainImage] | Unset): A list of images to display in the
            product image gallery.
            Use the [Upload Product Image API](https://partner.tiktokshop.com/docv2/page/6509df95defece02be598a22) to upload
            the images first and obtain the corresponding image URI.
            **Note**:
            - Max number of image URIs: 9
            - Arrange your image URIs in the sequence that they should appear on TikTok Shop.
            - Image dimensions: [300x300 px, 4000x4000 px]
            **Recommendations**:
            - Use a minimum of 5 images.
            - The first image should have a white background. Use the [Optimize Images
            API](https://partner.tiktokshop.com/docv2/page/665692b35d39dc02deb49a97) to change the background to white.
        title (str | Unset): The product title.
            Title length:
            - DE, ES, FR, IE, IT, JP, UK, US: [1, 255]
            - BR, MX: [1, 300]
            - Other regions: [25, 255]
        product_attributes (list[DiagnoseAndOptimizeProductRequestProductAttribute] | Unset): A list of general
            attributes (e.g. manufacturer, country of origin, materials used) that describe the product as a whole,
            regardless of variant.
            **Note**: The attributes available for use are determined by the system based on the product's assigned
            category, with some being mandatory. Retrieve the product attributes by using the [Get Attributes
            API](https://partner.tiktokshop.com/docv2/page/6509c5784a0bb702c0561cc8).
        size_chart (DiagnoseAndOptimizeProductRequestSizeChart | Unset):
        optimization_fields (list[DiagnoseAndOptimizeProductRequestOptimizationFieldsItem] | Unset): The fields for
            which you want to generate specific optimization suggestions.
            Possible values:
            - TITLE: Product title
            - DESCRIPTION: Product description (suggestions for this may take more than 10 seconds to generate)
            - IMAGE: Product image displayed in the image gallery
            - ALL: Suggestions are generated for all the above fields
            - NONE: No suggestions will be provided.
            Default: NONE
    """

    category_id: str
    product_id: str | Unset = UNSET
    description: str | Unset = UNSET
    brand_id: str | Unset = UNSET
    main_images: list[DiagnoseAndOptimizeProductRequestMainImage] | Unset = UNSET
    title: str | Unset = UNSET
    product_attributes: list[DiagnoseAndOptimizeProductRequestProductAttribute] | Unset = UNSET
    size_chart: DiagnoseAndOptimizeProductRequestSizeChart | Unset = UNSET
    optimization_fields: list[DiagnoseAndOptimizeProductRequestOptimizationFieldsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category_id = self.category_id

        product_id = self.product_id

        description = self.description

        brand_id = self.brand_id

        main_images: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.main_images, Unset):
            main_images = []
            for main_images_item_data in self.main_images:
                main_images_item = main_images_item_data.to_dict()
                main_images.append(main_images_item)

        title = self.title

        product_attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.product_attributes, Unset):
            product_attributes = []
            for product_attributes_item_data in self.product_attributes:
                product_attributes_item = product_attributes_item_data.to_dict()
                product_attributes.append(product_attributes_item)

        size_chart: dict[str, Any] | Unset = UNSET
        if not isinstance(self.size_chart, Unset):
            size_chart = self.size_chart.to_dict()

        optimization_fields: list[str] | Unset = UNSET
        if not isinstance(self.optimization_fields, Unset):
            optimization_fields = []
            for optimization_fields_item_data in self.optimization_fields:
                optimization_fields_item = optimization_fields_item_data.value
                optimization_fields.append(optimization_fields_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category_id": category_id,
            }
        )
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if description is not UNSET:
            field_dict["description"] = description
        if brand_id is not UNSET:
            field_dict["brand_id"] = brand_id
        if main_images is not UNSET:
            field_dict["main_images"] = main_images
        if title is not UNSET:
            field_dict["title"] = title
        if product_attributes is not UNSET:
            field_dict["product_attributes"] = product_attributes
        if size_chart is not UNSET:
            field_dict["size_chart"] = size_chart
        if optimization_fields is not UNSET:
            field_dict["optimization_fields"] = optimization_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.diagnose_and_optimize_product_request_main_image import (
            DiagnoseAndOptimizeProductRequestMainImage,  # noqa: PLC0415
        )
        from ..models.diagnose_and_optimize_product_request_product_attribute import (
            DiagnoseAndOptimizeProductRequestProductAttribute,  # noqa: PLC0415
        )
        from ..models.diagnose_and_optimize_product_request_size_chart import (
            DiagnoseAndOptimizeProductRequestSizeChart,  # noqa: PLC0415
        )

        d = dict(src_dict)
        category_id = d.pop("category_id")

        product_id = d.pop("product_id", UNSET)

        description = d.pop("description", UNSET)

        brand_id = d.pop("brand_id", UNSET)

        _main_images = d.pop("main_images", UNSET)
        main_images: list[DiagnoseAndOptimizeProductRequestMainImage] | Unset = UNSET
        if _main_images is not UNSET:
            main_images = []
            for main_images_item_data in _main_images:
                main_images_item = DiagnoseAndOptimizeProductRequestMainImage.from_dict(main_images_item_data)

                main_images.append(main_images_item)

        title = d.pop("title", UNSET)

        _product_attributes = d.pop("product_attributes", UNSET)
        product_attributes: list[DiagnoseAndOptimizeProductRequestProductAttribute] | Unset = UNSET
        if _product_attributes is not UNSET:
            product_attributes = []
            for product_attributes_item_data in _product_attributes:
                product_attributes_item = DiagnoseAndOptimizeProductRequestProductAttribute.from_dict(
                    product_attributes_item_data
                )

                product_attributes.append(product_attributes_item)

        _size_chart = d.pop("size_chart", UNSET)
        size_chart: DiagnoseAndOptimizeProductRequestSizeChart | Unset
        if isinstance(_size_chart, Unset):
            size_chart = UNSET
        else:
            size_chart = DiagnoseAndOptimizeProductRequestSizeChart.from_dict(_size_chart)

        _optimization_fields = d.pop("optimization_fields", UNSET)
        optimization_fields: list[DiagnoseAndOptimizeProductRequestOptimizationFieldsItem] | Unset = UNSET
        if _optimization_fields is not UNSET:
            optimization_fields = []
            for optimization_fields_item_data in _optimization_fields:
                optimization_fields_item = DiagnoseAndOptimizeProductRequestOptimizationFieldsItem(
                    optimization_fields_item_data
                )

                optimization_fields.append(optimization_fields_item)

        diagnose_and_optimize_product_request = cls(
            category_id=category_id,
            product_id=product_id,
            description=description,
            brand_id=brand_id,
            main_images=main_images,
            title=title,
            product_attributes=product_attributes,
            size_chart=size_chart,
            optimization_fields=optimization_fields,
        )

        diagnose_and_optimize_product_request.additional_properties = d
        return diagnose_and_optimize_product_request

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
