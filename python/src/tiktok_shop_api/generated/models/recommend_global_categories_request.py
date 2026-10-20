from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.recommend_global_categories_request_category_version import RecommendGlobalCategoriesRequestCategoryVersion
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.diagnose_and_optimize_product_request_size_chart_image import DiagnoseAndOptimizeProductRequestSizeChartImage





T = TypeVar("T", bound="RecommendGlobalCategoriesRequest")



@_attrs_define
class RecommendGlobalCategoriesRequest:
    """ 
        Attributes:
            product_title (str): The product title.
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
            images (list[DiagnoseAndOptimizeProductRequestSizeChartImage] | Unset): Product images, including gallery
                images, images that appear in the description, product variant images.
            category_version (RecommendGlobalCategoriesRequestCategoryVersion | Unset): The category tree version to use for
                this product.
                Possible values based on region:
                - US: `v2`, represents the 7-level category tree.
                  **Important**: If the seller account contains an active US shop, you must pass `v2` when using this API.
                - Other regions: `v1`, represents the 3-level category tree.
                Default: `v1`
     """

    product_title: str
    description: str | Unset = UNSET
    images: list[DiagnoseAndOptimizeProductRequestSizeChartImage] | Unset = UNSET
    category_version: RecommendGlobalCategoriesRequestCategoryVersion | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.diagnose_and_optimize_product_request_size_chart_image import DiagnoseAndOptimizeProductRequestSizeChartImage # noqa: PLC0415
        product_title = self.product_title

        description = self.description

        images: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)



        category_version: str | Unset = UNSET
        if not isinstance(self.category_version, Unset):
            category_version = self.category_version.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "product_title": product_title,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if images is not UNSET:
            field_dict["images"] = images
        if category_version is not UNSET:
            field_dict["category_version"] = category_version

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.diagnose_and_optimize_product_request_size_chart_image import DiagnoseAndOptimizeProductRequestSizeChartImage # noqa: PLC0415
        d = dict(src_dict)
        product_title = d.pop("product_title")

        description = d.pop("description", UNSET)

        _images = d.pop("images", UNSET)
        images: list[DiagnoseAndOptimizeProductRequestSizeChartImage] | Unset = UNSET
        if _images is not UNSET:
            images = []
            for images_item_data in _images:
                images_item = DiagnoseAndOptimizeProductRequestSizeChartImage.from_dict(images_item_data)



                images.append(images_item)


        _category_version = d.pop("category_version", UNSET)
        category_version: RecommendGlobalCategoriesRequestCategoryVersion | Unset
        if isinstance(_category_version,  Unset):
            category_version = UNSET
        else:
            category_version = RecommendGlobalCategoriesRequestCategoryVersion(_category_version)




        recommend_global_categories_request = cls(
            product_title=product_title,
            description=description,
            images=images,
            category_version=category_version,
        )


        recommend_global_categories_request.additional_properties = d
        return recommend_global_categories_request

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
