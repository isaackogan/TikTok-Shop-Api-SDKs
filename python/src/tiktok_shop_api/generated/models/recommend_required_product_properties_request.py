from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image import Image
    from ..models.recommend_required_product_properties_request_sales_property import (
        RecommendRequiredProductPropertiesRequestSalesProperty,
    )


T = TypeVar("T", bound="RecommendRequiredProductPropertiesRequest")


@_attrs_define
class RecommendRequiredProductPropertiesRequest:
    """
    Attributes:
        category_id (str): The ID of the leaf category selected for the product.
        product_title (str): Product title used to predict required properties. Do not include personal data.
        description (str | Unset): Product description used to improve prediction accuracy. Do not include personal
            data.
        images (list[Image] | Unset): Ordered product images used to improve prediction accuracy. Do not include images
            containing personal data.
        sales_properties (list[RecommendRequiredProductPropertiesRequestSalesProperty] | Unset): Existing standard sales
            properties that define the product variants and provide additional prediction context.
        target_property_ids (list[str] | Unset): Optional property IDs that limit prediction to specific properties.
            When omitted, no property ID filter is applied.
    """

    category_id: str
    product_title: str
    description: str | Unset = UNSET
    images: list[Image] | Unset = UNSET
    sales_properties: list[RecommendRequiredProductPropertiesRequestSalesProperty] | Unset = UNSET
    target_property_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category_id = self.category_id

        product_title = self.product_title

        description = self.description

        images: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)

        sales_properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sales_properties, Unset):
            sales_properties = []
            for sales_properties_item_data in self.sales_properties:
                sales_properties_item = sales_properties_item_data.to_dict()
                sales_properties.append(sales_properties_item)

        target_property_ids: list[str] | Unset = UNSET
        if not isinstance(self.target_property_ids, Unset):
            target_property_ids = self.target_property_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category_id": category_id,
                "product_title": product_title,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if images is not UNSET:
            field_dict["images"] = images
        if sales_properties is not UNSET:
            field_dict["sales_properties"] = sales_properties
        if target_property_ids is not UNSET:
            field_dict["target_property_ids"] = target_property_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image import Image  # noqa: PLC0415
        from ..models.recommend_required_product_properties_request_sales_property import (
            RecommendRequiredProductPropertiesRequestSalesProperty,  # noqa: PLC0415
        )

        d = dict(src_dict)
        category_id = d.pop("category_id")

        product_title = d.pop("product_title")

        description = d.pop("description", UNSET)

        _images = d.pop("images", UNSET)
        images: list[Image] | Unset = UNSET
        if _images is not UNSET:
            images = []
            for images_item_data in _images:
                images_item = Image.from_dict(images_item_data)

                images.append(images_item)

        _sales_properties = d.pop("sales_properties", UNSET)
        sales_properties: list[RecommendRequiredProductPropertiesRequestSalesProperty] | Unset = UNSET
        if _sales_properties is not UNSET:
            sales_properties = []
            for sales_properties_item_data in _sales_properties:
                sales_properties_item = RecommendRequiredProductPropertiesRequestSalesProperty.from_dict(
                    sales_properties_item_data
                )

                sales_properties.append(sales_properties_item)

        target_property_ids = cast(list[str], d.pop("target_property_ids", UNSET))

        recommend_required_product_properties_request = cls(
            category_id=category_id,
            product_title=product_title,
            description=description,
            images=images,
            sales_properties=sales_properties,
            target_property_ids=target_property_ids,
        )

        recommend_required_product_properties_request.additional_properties = d
        return recommend_required_product_properties_request

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
