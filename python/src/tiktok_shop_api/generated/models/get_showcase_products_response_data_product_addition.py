from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_showcase_products_response_data_product_addition_customized_main_image import (
        GetShowcaseProductsResponseDataProductAdditionCustomizedMainImage,
    )


T = TypeVar("T", bound="GetShowcaseProductsResponseDataProductAddition")


@_attrs_define
class GetShowcaseProductsResponseDataProductAddition:
    """
    Attributes:
        customized_main_images (list[GetShowcaseProductsResponseDataProductAdditionCustomizedMainImage] | Unset): A list
            of product images.
    """

    customized_main_images: list[GetShowcaseProductsResponseDataProductAdditionCustomizedMainImage] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        customized_main_images: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.customized_main_images, Unset):
            customized_main_images = []
            for customized_main_images_item_data in self.customized_main_images:
                customized_main_images_item = customized_main_images_item_data.to_dict()
                customized_main_images.append(customized_main_images_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if customized_main_images is not UNSET:
            field_dict["customized_main_images"] = customized_main_images

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_showcase_products_response_data_product_addition_customized_main_image import (
            GetShowcaseProductsResponseDataProductAdditionCustomizedMainImage,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _customized_main_images = d.pop("customized_main_images", UNSET)
        customized_main_images: list[GetShowcaseProductsResponseDataProductAdditionCustomizedMainImage] | Unset = UNSET
        if _customized_main_images is not UNSET:
            customized_main_images = []
            for customized_main_images_item_data in _customized_main_images:
                customized_main_images_item = (
                    GetShowcaseProductsResponseDataProductAdditionCustomizedMainImage.from_dict(
                        customized_main_images_item_data
                    )
                )

                customized_main_images.append(customized_main_images_item)

        get_showcase_products_response_data_product_addition = cls(
            customized_main_images=customized_main_images,
        )

        get_showcase_products_response_data_product_addition.additional_properties = d
        return get_showcase_products_response_data_product_addition

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
